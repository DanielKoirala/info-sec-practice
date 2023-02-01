# A very simple Bottle Hello World app for you to get started with...
import os
from bottle import default_app, route, run, redirect
@route('/')
def get_index():
    redirect('/different')

@route('/different')
def get_different():
    return 'This is different!'

@route('/newmessage')
def get_newmessage():
    return ("This is a new message")

if 'PYTHONANYWHERE_DOMAIN' in os.environ:
    application = default_app()
else:
    run(host='localhost', port=8080)