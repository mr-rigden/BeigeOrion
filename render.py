import os.path

from jinja2 import Environment, FileSystemLoader

from config import CONFIG

file_loader = FileSystemLoader('templates')
env = Environment(loader=file_loader)
output_dir = os.path.join(os.getcwd(), 'output')


def save_index_page():
    template = env.get_template('index.html')
    output = template.render(CONFIG=CONFIG)
    with open('output/index.html', 'w') as f:
        f.write(output)


def save_subject_page(subject):
    print('fuck you')
    file_name = subject['SCREEN_NAME']
    file_path = os.path.join(output_dir, file_name)
    print(file_path)
    template = env.get_template('subject.html')
    output = template.render(CONFIG=CONFIG, subject=subject)
    with open(file_path, 'w') as f:
        f.write(output)


def save_subject_all_pages():
    for subject in CONFIG['SUBJECTS']:
        save_subject_page(subject)
