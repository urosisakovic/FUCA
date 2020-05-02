from flask_wtf import FlaskForm
from wtforms import SelectField, StringField, SubmitField
from wtforms.validators import DataRequired

from fuca.models import News


class AdminAddNewsForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    content = StringField('Content', validators=[DataRequired()])
    submit = SubmitField('Add News')

    def populate_dd(self):
        pass


class AdminUpdateNewsForm(FlaskForm):
    news_dd = SelectField('News', choices=[])
    title = StringField('Title', validators=[DataRequired()])
    content = StringField('Content', validators=[DataRequired()])
    submit = SubmitField('Update News')

    def populate_dd(self):
        news_db = News.query.all()
        news_list = [news.jinja_dict() for news in news_db]
        news_choices = [(news['id'], news['title'] + ' ' + news['date']) for news in news_list]
        self.news_dd.choices = news_choices


class AdminDeleteNewsForm(FlaskForm):
    news_dd = SelectField('News', choices=[])
    submit = SubmitField('Delete News')

    def populate_dd(self):
        news_db = News.query.all()
        news_list = [news.jinja_dict() for news in news_db]
        news_choices = [(news['id'], news['title'] + ' ' + news['date']) for news in news_list]
        self.news_dd.choices = news_choices
