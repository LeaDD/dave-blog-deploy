from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired, URL, Email
from flask_ckeditor import CKEditorField


# WTForm for creating a blog post
class CreatePostForm(FlaskForm):
    title = StringField("Blog Post Title", validators=[DataRequired()])
    subtitle = StringField("Subtitle", validators=[DataRequired()])
    img_url = StringField("Blog Image URL", validators=[DataRequired(), URL()])
    body = CKEditorField("Blog Content", validators=[DataRequired()])
    submit = SubmitField("Submit Post")

class CreateRegistrationForm(FlaskForm):
    name = StringField("Your Name", validators=[DataRequired()])
    email = StringField("Your E-mail", validators=[DataRequired(), Email()])
    password = PasswordField("Enter a Password", validators=[DataRequired()])
    submit = SubmitField("Register")

class LoginForm(FlaskForm):
    email = StringField("Enter your email", validators=[DataRequired()])
    password = PasswordField("Enter your password", validators=[DataRequired()])
    login = SubmitField("Login")

class CommentForm(FlaskForm):
    comment = CKEditorField("Blog Comment")
    submit = SubmitField("Submit Comment")
