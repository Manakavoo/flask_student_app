# # Define Flask-WTF forms here
# from flask_wtf import FlaskForm
# from wtforms import StringField, TextAreaField, SubmitField
# from wtforms.validators import DataRequired, Email

# class StudentApplicationForm(FlaskForm):
#     name = StringField('Full Name', validators=[DataRequired()])
#     email = StringField('Email', validators=[DataRequired(), Email()])
#     academic_background = TextAreaField('Academic Background', validators=[DataRequired()])
#     submit = SubmitField('Submit Application')

from wtforms import FileField
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, Email

class StudentApplicationForm(FlaskForm):
    name = StringField('Full Name', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    academic_background = TextAreaField('Academic Background', validators=[DataRequired()])
    degree_certificate = FileField('Degree Certificate (PDF)', validators=[DataRequired()])
    id_proof = FileField('ID Proof (PDF)', validators=[DataRequired()])
    submit = SubmitField('Submit Application')
