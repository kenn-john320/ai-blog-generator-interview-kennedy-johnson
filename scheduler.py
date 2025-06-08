import datetime
import logging
import atexit

from apscheduler.schedulers.background import BackgroundScheduler
from seo_fetcher import random_metrics
from ai_generator import generate_blog
# from config import DAILY_KEYWORD, SCHEDULE_HOURS

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
DAILY_KEYWORD = "Wireless earbuds"


def daily_generate(): 
    """
    Generates the daily blog post using the configured keyword and writes it into a dated file!
    """ 
    try: 
        logging.info("Generating daily blog...")
        
        seo = random_metrics(DAILY_KEYWORD)
        blog = generate_blog(DAILY_KEYWORD, seo)
    
        filename = f"daily_blog_{datetime.now().strftime('%Y_%m_%d')}.md"
        with open(filename, 'w') as f: 
            f.write(blog)
            logging.info(f"Blog written to {filename}.")
    except Exception as e:
        logging.error(f"Error in daily_generate: {e}")
        

def start_scheduler():
    # create the scheduler
    scheduler = BackgroundScheduler()
    
    # Make job run every 6 hours
    scheduler.add_job(daily_generate, 'interval', hours=6)
    
    # Start the scheduler
    scheduler.start()
    atexit.register(lambda:scheduler.shutdown())