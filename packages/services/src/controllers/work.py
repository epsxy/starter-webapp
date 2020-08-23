from flask import Blueprint, make_response
from src.worker.worker import Worker

work_api = Blueprint('work_api', __name__)

@work_api.route('')
def works():
    worker = Worker('work', 10)
    return worker.work()
