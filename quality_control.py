import time

import models
from utils import *


def get_all_relationships(screen_name):
    subject = models.Subject.get(models.Subject.screen_name == screen_name)

    relationships = models.Relationship.select().where(
        models.Relationship.subject == subject)
    return relationships


def get_subject_follower_quality(screen_name):
    logger.info('Checking Quality for subject: {}'.format(screen_name))
    chunk = 1 / 6
    quality = {}
    quality['no_timeline'] = 0
    quality['protected'] = 0
    quality['very_good'] = 0
    quality['good'] = 0
    quality['neutral'] = 0
    quality['poor'] = 0
    quality['very_poor'] = 0
    quality['total'] = 0
    relationships = get_all_relationships(screen_name)
    for relationship in relationships:
        logger.info('   Checking Follower {}'.format(
            relationship.follower.id_str))
        quality['total'] += 1
        score = relationship.follower.botometer
        if score is None:
            logger.info('   Follower has no score')
            continue

        if score == -1:
            quality['no_timeline'] += 1
            logger.info('   No Timeline Account')
            continue

        if score == -2:
            quality['protected'] += 1
            logger.info('   Protected Account')
            continue


        if score < chunk:
            quality['very_good'] += 1
            logger.info('   Score of {} is Very Good'.format(score))
        elif score < (2 * chunk):
            quality['good'] += 1
            logger.info('   Score of {} is Good'.format(score))
        elif score < (3 * chunk):
            quality['neutral'] += 1
            logger.info('   Score of {} is Neutral'.format(score))
        elif score < (4 * chunk):
            quality['poor'] += 1
            logger.info('   Score of {} is Poor'.format(score))
        else:
            quality['very_poor'] += 1
            logger.info('   Score of {} is Very Poor'.format(score))
    return quality


def add_quality_report(screen_name):
    subject = models.Subject.get(models.Subject.screen_name == screen_name)
    quality = get_subject_follower_quality(screen_name)
    epoch_time = int(time.time())

    quality_report = models.Quality_Report()
    quality_report.subject = subject
    quality_report.epoch_time = epoch_time
    quality_report.very_good = quality['very_good']
    quality_report.good = quality['good']
    quality_report.neutral = quality['neutral']
    quality_report.poor = quality['poor']
    quality_report.very_poor = quality['very_poor']
    quality_report.total = quality['total']
    quality_report.no_timeline = quality['no_timeline']
    quality_report.protected = quality['protected']
    quality_report.save()


def get_full_quality_report(screen_name):
    data = {}
    data['epoch_time'] = []
    data['very_good'] = []
    data['good'] = []
    data['neutral'] = []
    data['poor'] = []
    data['very_poor'] = []
    data['no_timeline'] = []
    data['protected'] = []
    data['total'] = []
    subject = models.Subject.get(models.Subject.screen_name == screen_name)
    query = models.Quality_Report.select().where(
        models.Quality_Report.subject == subject).order_by(
            models.Quality_Report.epoch_time)
    for each in query:
        data['epoch_time'].append(each.epoch_time)
        data['very_good'].append(each.very_good)
        data['good'].append(each.good)
        data['neutral'].append(each.neutral)
        data['poor'].append(each.poor)
        data['very_poor'].append(each.very_poor)
        data['no_timeline'].append(each.no_timeline)
        data['protected'].append(each.protected)
        data['total'].append(each.total)
    data['bot_percent'] = round(
        (data['very_poor'][-1] / data['total'][-1] * 100))
    data['headline'] = get_headline(data['bot_percent'], screen_name)
    return data


def get_headline(bot_percent, screen_name):
    headline = "About {}% of the Twitter followers of @{} are probably bots"
    return headline.format(bot_percent, screen_name)


def run_all_quality_reports():
    for subject in CONFIG['SUBJECTS']:
        add_quality_report(subject['SCREEN_NAME'])
