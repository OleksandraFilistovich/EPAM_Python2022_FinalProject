from flask_wtf import FlaskForm
from wtforms import  SubmitField


class PurchaseForm(FlaskForm):
    submit = SubmitField(label='Purchase')
