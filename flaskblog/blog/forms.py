from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, URL, Length
from flask_ckeditor import CKEditorField
from wtforms.widgets import TextArea

class PostForm(FlaskForm):
    title = StringField("Title", validators=[DataRequired()])
    content = CKEditorField("Content", validators=[DataRequired()])
    author = StringField("Author")
    image_url = StringField('Image URL')
    submit = SubmitField("Submit")

class CommentForm(FlaskForm):
    content = StringField("Content", validators=[DataRequired(), Length(max=200)], widget=TextArea())
    submit = SubmitField("Submit")

class SearchForm(FlaskForm):
    searched = StringField("Content", validators=[DataRequired()], widget=TextArea())
    submit = SubmitField("Submit")