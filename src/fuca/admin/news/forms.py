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
        news = News.query.order_by(News.date.desc()).all()
        news_choices = [(n.id, n.title + ' ' + n.date.strftime('%B %d, %Y')) for n in news]
        self.news_dd.choices = news_choices


class AdminDeleteNewsForm(FlaskForm):
    news_dd = SelectField('News', choices=[])
    submit = SubmitField('Delete News')

    def populate_dd(self):
        news = News.query.order_by(News.date.desc()).all()
        news_choices = [(n.id, n.title + ' ' + n.date.strftime('%B %d, %Y')) for n in news]
        self.news_dd.choices = news_choices
