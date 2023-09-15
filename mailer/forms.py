from flask_wtf import FlaskForm
from wtforms import FileField,StringField,SubmitField,TextAreaField
from wtforms.validators import DataRequired,Length
from flask_wtf.file import FileRequired,FileAllowed

class UploadForm(FlaskForm):
    title = StringField("Enter Title ",validators=[DataRequired()])
    upload = FileField("Upload Excel File ",validators=[FileRequired(),FileAllowed(['xlsx'],'Excel Sheets Only!')])
    body = TextAreaField("Enter Body ",validators=[DataRequired()])
    submit = SubmitField("Send Mail")