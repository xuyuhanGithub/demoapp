
from flask import Flask

from app.models.ontologyLibray import db


def create_app():
    app=Flask(__name__)
    app.config.from_object('app.config.setting')
    app.config.from_object('app.config.secure')


    db.init_app(app)
    db.create_all(app=app)

    return app