"""
Author: Uros Isakovic
"""
from flask_wtf import FlaskForm
from fuca.models import News
from wtforms import SelectField, StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, ValidationError


class AdminAddNewsForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    content = TextAreaField('Content', validators=[DataRequired()])
    submit = SubmitField('Add News')

    def populate_dd(self):
        pass


class AdminUpdateNewsForm(FlaskForm):
    news_dd = SelectField('News', choices=[], id='select_news', coerce=int)
    title = StringField('Title', validators=[DataRequired()])
    content = TextAreaField('Content', validators=[DataRequired()])
    submit = SubmitField('Update News')

    def populate_dd(self):
        news = News.query.order_by(News.date.desc()).all()
        news_choices = [(-1, '')] + [(n.id, n.title + ' ' + n.date.strftime('%B %d, %Y')) for n in news]
        self.news_dd.choices = news_choices

    def validate_news_dd(self, news_dd):
        if news_dd.data == -1:
            raise ValidationError('You must select a news.')


class AdminDeleteNewsForm(FlaskForm):
    news_dd = SelectField('News', choices=[])
    submit = SubmitField('Delete News')

    def populate_dd(self):
        news = News.query.order_by(News.date.desc()).all()
        news_choices = [(n.id, n.title + ' ' + n.date.strftime('%B %d, %Y')) for n in news]
        self.news_dd.choices = news_choices
