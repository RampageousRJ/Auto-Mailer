import pandas as pd
import json
from mailer import app,mail
from mailer.forms import *
from flask import render_template,request,redirect,flash
from flask_mail import Message

@app.route('/',methods=['GET','POST'])
@app.route('/home',methods=['GET','POST'])
def home():
    l1=[]
    form=UploadForm()
    if request.method=='POST':
        file_req = request.files['upload']
        try:
            file = pd.read_excel(file_req)
            json_file=file.to_json()
            d1=json.loads(json_file)
            for rows in d1.values():
                for values in rows.values():
                    if values.__contains__("@"):
                        l1.append(values)
            msg = Message(form.title.data,body=form.body.data,sender='sjrj0604@gmail.com',recipients=l1)
            print(l1)
            # mail.send(msg)
            flash('Mail sent!')
            return redirect('home') 
        except:
            flash('Invalid file format!') 
            return redirect('home')
    return render_template('home.html',form=form)