import json
import os.path

from jinja2 import Environment, FileSystemLoader

from config import CONFIG
import quality_control

file_loader = FileSystemLoader('templates')
env = Environment(loader=file_loader)
output_dir = os.path.join(os.getcwd(), 'output')


def save_index_page():
    template = env.get_template('index.html')
    output = template.render(CONFIG=CONFIG)
    with open('output/index.html', 'w') as f:
        f.write(output)


def save_subject_page(subject):
    data = quality_control.get_full_quality_report(subject['SCREEN_NAME'])
    file_name = subject['SCREEN_NAME'] + ".html"
    file_path = os.path.join(output_dir, file_name)
    template = env.get_template('subject.html')
    output = template.render(CONFIG=CONFIG, subject=subject, data=data)
    with open(file_path, 'w') as f:
        f.write(output)


def save_subject_all_pages():
    for subject in CONFIG['SUBJECTS']:
        save_subject_page(subject)
