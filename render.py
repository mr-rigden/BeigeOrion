import json
import os.path

from jinja2 import Environment, FileSystemLoader

import quality_control
from utils import *

file_loader = FileSystemLoader('templates')
env = Environment(loader=file_loader)


def save_index_page():
    file_path = os.path.join(CONFIG['OUTPUT_DIR'], "index.html")
    template = env.get_template('index.html')
    output = template.render(CONFIG=CONFIG)
    with open(file_path, 'w') as f:
        f.write(output)


def save_subject_page(subject):
    data = quality_control.get_full_quality_report(subject['SCREEN_NAME'])
    file_name = subject['SCREEN_NAME'] + ".html"
    file_path = os.path.join(CONFIG['OUTPUT_DIR'], file_name)
    template = env.get_template('subject.html')
    output = template.render(CONFIG=CONFIG, subject=subject, data=data)
    with open(file_path, 'w') as f:
        f.write(output)


def save_subject_all_pages():
    for subject in CONFIG['SUBJECTS']:
        save_subject_page(subject)
