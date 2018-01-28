from flask import send_from_directory

def index_get():
    return send_from_directory('static/', 'index.html')

def app_get(path):
    return send_from_directory('static/', path )