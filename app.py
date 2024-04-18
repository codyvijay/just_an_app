from flask import Flask


app=Flask(__name__, template_folder="template", static_folder="static")
app.app_context().push()

from application.controllers import *

if __name__ == '__main__':
    app.run()