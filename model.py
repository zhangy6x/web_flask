from flask_wtf import FlaskForm
from wtforms import Form, FloatField, validators, StringField
from math import pi


class InputForm(Form):
    formula = StringField(
        label='Chemical formula', default='Ag',
        validators=[validators.InputRequired()])
    A = FloatField(
        label='amplitude (m)', default=1.0,
        validators=[validators.InputRequired()])
    b = FloatField(
        label='damping factor (kg/s)', default=0,
        validators=[validators.InputRequired()])
    w = FloatField(
        label='frequency (1/s)', default=2 * pi,
        validators=[validators.InputRequired()])
    T = FloatField(
        label='time interval (s)', default=18,
        validators=[validators.InputRequired()])
    thickness = FloatField(
        label='Thickness (mm)', default=18,
        validators=[validators.InputRequired()])
    density = FloatField(
        label='Density (g/cm3)', default=18,
        validators=[validators.InputRequired()])