from flask_wtf import FlaskForm
from werkzeug.routing import ValidationError
from wtforms import SubmitField, StringField, PasswordField
from wtforms.validators import DataRequired, Email

from app.models import User


class SignupForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    email = StringField('Email address', validators=[DataRequired(), Email()])
    submit = SubmitField('Sign Up')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is not None:
            raise ValidationError('An account is already registered for that email address.')
