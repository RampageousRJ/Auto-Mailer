import pandas as pd
import json
from mailer import app,mail
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
    res=[]
    form=UploadForm()
    if request.method=='POST':
        file_req = request.files['upload']
        attach = request.files['attachments']
        try:
            file = pd.read_excel(file_req)
            attachment_name = secure_filename(attach.filename)
            attachment_names = str(uuid.uuid1()) + "_" + attachment_name
            for index,row in file.iterrows():
                for values in row:
                    if validEmail(values):
                        res.append(values)
                        break
            l1=[]
            for i in res:
                if i not in l1:
                    l1.append(i)
            if attachment_name:
                file_path = os.path.join(app.config['UPLOAD_FOLDER'], attachment_names)
                attach.save(file_path)
                print(f"File saved at: {file_path}")
            with mail.connect() as conn:
                msg = Message(form.title.data,body=form.body.data,sender=(form.name.data,'automailer.0123@gmail.com'),  recipients=l1)
                if attachment_name:
                    with app.open_resource(os.path.join(app.config['UPLOAD_FOLDER'], attachment_names)) as fp:
                        mime_type, encoding = mimetypes.guess_type(attachment_name)
                        msg.attach(attachment_name, mime_type or "application/octet-stream", fp.read())    
                conn.send(msg)
            flash('Mail sent!')
            if attachment_name:
                os.remove(os.path.join(app.config['UPLOAD_FOLDER'],attachment_names))
                print(f"File removed from: {os.path.join(app.config['UPLOAD_FOLDER'],attachment_names)}")
            return redirect('home') 
        except Exception as e:
            print(e)
            flash('Invalid file format!') 
            return redirect('home')
    return render_template('home.html',form=form)