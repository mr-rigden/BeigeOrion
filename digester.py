import botometer
import peewee
import tweepy

import api_keys
from config import CONFIG
import models
from utils import *

logger.info('Initializing Botometer')
twitter_app_auth = {
    'consumer_key': api_keys.TWITTER['CONSUMER_KEY'],
    'consumer_secret': api_keys.TWITTER['CONSUMER_SECRET'],
    'access_token': api_keys.TWITTER['ACCESS_TOKEN'],
    'access_token_secret': api_keys.TWITTER['ACCESS_TOKEN_SECRET'],
}

bom = botometer.Botometer(
    wait_on_ratelimit=True,
    mashape_key=api_keys.MASHAPE_KEY,
    **twitter_app_auth)

logger.info('Initializing Tweepy')
auth = tweepy.OAuthHandler(api_keys.TWITTER['CONSUMER_KEY'],
                           api_keys.TWITTER['CONSUMER_SECRET'])
auth.set_access_token(api_keys.TWITTER['ACCESS_TOKEN'],
                      api_keys.TWITTER['ACCESS_TOKEN_SECRET'])
api = tweepy.API(
    auth,
    wait_on_rate_limit=True,
    wait_on_rate_limit_notify=True,
    compression=True)


def add_all_subjects():
    for subject in CONFIG['SUBJECTS']:
        add_subject(subject['SCREEN_NAME'])


def add_subject(screen_name):
    logger.info('Creating subject: {}'.format(screen_name))

    twitter_data = user = api.get_user(screen_name)

    record, created = models.Subject.get_or_create(
        screen_name=user.screen_name, id_str=user.id_str)

    if not created:
        logger.info('    Record already exits')


def add_subject_followers(screen_name):
    subject = models.Subject.get(models.Subject.screen_name == screen_name)
    logger.info('Adding followers for {}'.format(screen_name))
    id_strs = get_follower_ids(screen_name)
    for id_str in id_strs:
        follower = get_or_add_follower(id_str)
        add_relationship(subject, follower)


def get_follower_ids(screen_name):
    logger.info('Getting follower ids for {}'.format(screen_name))
    id_strs = []
    for page in tweepy.Cursor(
            api.followers_ids, screen_name=screen_name).pages():
        id_strs.extend(page)
    return id_strs


def get_or_add_follower(id_str):
    logger.info('Adding follower: {}'.format(id_str))
    follower, created = models.Follower.get_or_create(id_str=id_str)
    if not created:
        logger.info('    already exists')
    follower.save()
    return follower


def update_all_followers():
    for subject in CONFIG['SUBJECTS']:
        delete_relationships(subject['SCREEN_NAME'])
        add_subject_followers(subject['SCREEN_NAME'])


def add_relationship(subject, follower):
    logger.info('    Adding relationship between {} and {}'.format(
        subject.screen_name, follower.id_str))
    relationship, created = models.Relationship.get_or_create(
        subject=subject, follower=follower)
    if not created:
        logger.info('    already exists')
    return relationship


def delete_relationships(screen_name):
    logger.info('Deleting all relationships for: {}'.format(screen_name))
    subject = models.Subject.get(models.Subject.screen_name == screen_name)
    models.Relationship().delete().where(
        models.Relationship.subject == subject).execute()


def set_missing_botometers():
    logger.info('Setting missing botometers')
    followers = models.Follower.select().where(
        models.Follower.botometer == None)
    for follower in followers:
        set_botometer(follower)
        left = models.Follower.select().where(
            models.Follower.botometer == None).count()
        total = models.Follower.select().count()
        logger.info('{} missing botometers left'.format(left))


def set_botometer(follower):
    logger.info('Setting botometer for {}'.format(follower.id_str))
    try:
        score = bom.check_account(follower.id_str)['scores']['universal']
    except botometer.NoTimelineError:
        logger.error('Botometer FAIL: Follower {} has no timeline'.format(
            follower.id_str))
        score = 1
    except tweepy.error.TweepError:
        logger.error('Botometer FAIL: Not authorized {}'.format(
            follower.id_str))
        score = 1
    follower.botometer = score
    logger.info('    Score of {}'.format(score))
    follower.save()
