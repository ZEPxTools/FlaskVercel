from flask import Flask , render_template, redirect, Blueprint

def create_app():   
    app = Flask(__name__)
    app.config['SECRET_KEY'] = "tirumalamatrix@2023"

    from .views import views

    app.register_blueprint(views, url_prefix="/")

    return app