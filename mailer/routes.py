import pandas as pd
import json
from mailer import app,mail
from mailer.forms import *
from flask import render_template,request,redirect,flash
from flask_mail import Message
from werkzeug.utils import secure_filename
import os
import uuid
import mimetypes

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
            file_name = secure_filename(attach.filename)
            file_names = str(uuid.uuid1()) + "_" + file_name
            if file_name:
                attach.save(os.path.join(app.config['UPLOAD_FOLDER'], file_names))
            for index,row in file.iterrows():
                for values in row:
                    if str(values).__contains__("@") and ((str(values).__contains__("gmail.com") or str(values).__contains__(".edu"))):
                        res.append(values)
                        break
            l1=[]
            for i in res:
                if i not in l1:
                    l1.append(i)
            with mail.connect() as conn:
                for user in l1:
                    msg = Message(form.title.data,body=form.body.data,sender=('MIST','automailer.0123@gmail.com'),  recipients=[user])
                    if file_name:
                        with app.open_resource(os.getenv('ATTACHMENT_FOLDER')+file_names) as fp:
                            mime_type, encoding = mimetypes.guess_type(file_name)
                            msg.attach(file_name,mime_type,fp.read())     
                    conn.send(msg)
            flash('Mail sent!')
            if file_name:
                os.remove(os.path.join(app.config['UPLOAD_FOLDER'],file_names))
            return redirect('home') 
        except Exception:
            flash('Invalid file format!') 
            return redirect('home')
    return render_template('home.html',form=form)