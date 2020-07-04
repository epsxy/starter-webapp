from flask import Flask
from src.worker import Worker

server = Flask(__name__)

@server.route('/')
def hello_world():
    worker = Worker('work', 10)
    return worker.work()