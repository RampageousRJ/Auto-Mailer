import pandas as pd
import json
from mailer import app,mail,app_logger
from mailer.forms import *
from flask import render_template,request,redirect,flash
from flask_mail import Message
from werkzeug.utils import secure_filename
import os
import uuid
import re
import mimetypes

def validEmail(email_text):
    if re.match('([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+',email_text) is not None:
        return True
    return False

@app.route('/',methods=['GET','POST'])
@app.route('/home',methods=['GET','POST'])
def home():
    emails=[]
    form=UploadForm()
    if request.method=='POST':
        file_req = request.files['upload']
        attach = request.files['attachments']
        try:
            file = pd.read_excel(file_req)
            sanitized_filepath = secure_filename(attach.filename)
            attachment_filename = str(uuid.uuid1()) + "_" + sanitized_filepath
            if sanitized_filepath:
                file_path = os.path.join(app.config['UPLOAD_FOLDER'], attachment_filename)
                attach.save(file_path)
                if os.path.exists(file_path):
                    app_logger.info("Attachment uploaded successfully!")
                else:
                    app_logger.error("Unable to upload attachment!")
            for index,row in file.iterrows():
                for values in row:
                    if validEmail(values):
                        emails.append(values)
                        break
            users=[]
            for email in emails:
                if email not in users:
                    users.append(email)
            with mail.connect() as conn:
                # for user in users:
                msg = Message(form.title.data,body=form.body.data,sender=(form.name.data,app.config['MAIL_USERNAME']),  recipients=users)
                if sanitized_filepath:
                    with app.open_emailsource(os.path.join(os.getcwd(),'mailer','static','attachments',attachment_filename)) as fp:
                        mime_type, _ = mimetypes.guess_type(sanitized_filepath)
                        msg.attach(sanitized_filepath,mime_type,fp.read())     
                conn.send(msg)
            flash('Mail sent!')
            app_logger.info("Mail sent successfully!")
            if sanitized_filepath:
                os.remove(os.path.join(app.config['UPLOAD_FOLDER'],attachment_filename))
            return redirect('home') 
        except Exception as e:
            app_logger.exception("Error occurred while sending mail")
            flash('Invalid file format!') 
            return redirect('home')
    return render_template('home.html',form=form)