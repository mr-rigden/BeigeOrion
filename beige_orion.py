import digester
import quality_control
import render
from utils import *

if __name__ == "__main__":
    logger.info('Starting BeigeOrion')
    digester.add_all_subjects()
    digester.update_all_followers()
    digester.set_random_missing_botometers()
    quality_control.run_all_quality_reports()
    render.save_index_page()
    render.save_subject_all_pages()
