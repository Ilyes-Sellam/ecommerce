from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from flask_login import current_user
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from shop.models import Customer



class RegistrationFrom(FlaskForm):
    username = StringField('Username',
                           validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    address = StringField('Address',
                           validators=[DataRequired(), Length(min=2, max=200)])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password',
                                     validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')

    def validate_username(self, username):

        costomer = Customer.query.filter_by(username=username.data).first()
        if costomer:
            raise ValidationError(
                'That username is taken. Please choose a difrent one.')

    def validate_email(self, email):

        costomer = Customer.query.filter_by(email=email.data).first()
        if costomer:
            raise ValidationError(
                'That email is taken. Please choose a difrent one.')


class LoginFrom(FlaskForm):
    email = StringField('Email',
                        validators=[DataRequired(), Email()])

    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')


class UpdateAccountFrom(FlaskForm):
    username = StringField('Username',
                           validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    
    submit = SubmitField('Update')

    def validate_username(self, username):
        if username.data != current_user.username:
            customer = Customer.query.filter_by(username=username.data).first()
            if customer:
                raise ValidationError(
                    'That username is taken. Please choose a difrent one.')

    def validate_email(self, email):
        if email.data != current_user.email:
            customer = Customer.query.filter_by(email=email.data).first()
            if customer:
                raise ValidationError(
                    'That email is taken. Please choose a difrent one.')


