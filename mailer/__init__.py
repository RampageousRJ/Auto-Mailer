from flask import Flask
from flask_mail import Mail
from dotenv import load_dotenv
import tempfile
import os
import logging
load_dotenv()

app = Flask(__name__)
app.config['SECRET_KEY']=os.getenv("AUTOMAILER_SECRET_KEY")
app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = os.getenv('MAIL_ID')
app.config['MAIL_PASSWORD'] = os.getenv('MAIL_PASSWORD')
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
app.config['RECAPTCHA_PUBLIC_KEY'] = os.getenv('AUTOMAILER_PUBLIC_KEY')
app.config['RECAPTCHA_PRIVATE_KEY'] = os.getenv('AUTOMAILER_PRIVATE_KEY')
app.config['UPLOAD_FOLDER'] = tempfile.gettempdir()

mail = Mail(app)

app_logger = logging.Logger('automailer')
app_logger.setLevel(logging.DEBUG)

if not app_logger.handlers:
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.DEBUG)
    formatter = logging.Formatter('[%(asctime)s] %(levelname)s: %(message)s')
    console_handler.setFormatter(formatter)
    app_logger.addHandler(console_handler)

from mailer.routes import *