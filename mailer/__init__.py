from flask import Flask
from flask_mail import Mail
from dotenv import load_dotenv
import os
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
app.config['UPLOAD_FOLDER']=os.path.abspath(os.getcwd())+"\\mailer\\static\\attachments\\"
mail = Mail(app)

from mailer.routes import *