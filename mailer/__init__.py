from flask import Flask
from flask_mail import Mail

app = Flask(__name__)
app.config['SECRET_KEY']='7dbb1be0d140bd8f205c8d07'
app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'automailer.0123@gmail.com'
app.config['MAIL_PASSWORD'] = 'whjq jjdo tfrv ksqy'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
app.config['RECAPTCHA_PUBLIC_KEY'] = "6LcyAbAnAAAAAGj1ZLz7ZqWVCqBuZAlvzLWS9pRK"
app.config['RECAPTCHA_PRIVATE_KEY'] = "6LcyAbAnAAAAAPXGV_OzjOXHWvxu6ocLeO3XR7VV"
mail = Mail(app)

from mailer.routes import *

