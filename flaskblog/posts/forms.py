from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Email


class PostForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    content = TextAreaField('Content', validators=[DataRequired()])
    submit = SubmitField('Post')

class CommentForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    content = TextAreaField('Content', validators=[DataRequired()])
    submit = SubmitField('Comment')
