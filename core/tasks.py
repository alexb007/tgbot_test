import asyncio
from celery.utils.log import get_task_logger

logger = get_task_logger(__name__)

from test_dj.celery import app
from .utils import update_websites_status, api_update_currencies


@app.task
def update_websites():
    loop = asyncio.get_event_loop()
    loop.run_until_complete(update_websites_status())

@app.task
def update_currencies():
    loop = asyncio.get_event_loop()
    loop.run_until_complete(api_update_currencies())
