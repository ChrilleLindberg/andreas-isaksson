from celery import Celery
from dotenv import load_dotenv

load_dotenv()

celery_app = Celery(__name__)
celery_app.conf.broker_url = "redis://redis:6379/0"
celery_app.conf.result_backend = "redis://redis:6379/1"
