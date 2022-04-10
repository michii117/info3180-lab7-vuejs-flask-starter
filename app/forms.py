# Add any form classes for Flask-WTF here
from flask_wtf import FlaskForm
from wtforms import TextAreaField,
from wtforms.validators import DataRequired, InputRequired
from flask_wtf.file import FileField, FileAllowed, FileRequired
from flask_wtf.csrf import CSRFProtect


class UploadForm(FlaskForm):
    description = TextAreaField("Description", validators=[DataRequired()])
    photo = FileField('Choose File: ', validators=[FileRequired(), FileAllowed(['jpg', 'png'],'Image Files Only!')])


