from flask import Flask, make_response
from src.controllers.work import work_api
from src.controllers.pony import pony_api

server = Flask(__name__)

server.register_blueprint(pony_api, url_prefix='/ponies')
server.register_blueprint(work_api, url_prefix='/works')

@server.route('/')
def root():
    return 'Server started'
