from datetime import datetime

from flask import redirect, render_template, request, url_for

from fuca import app, db
from fuca.forms import (AdminAddNewsForm, AdminDeleteNewsForm,
                        AdminUpdateNewsForm)
from fuca.models import News


@app.route("/admin/news", methods=['GET', 'POST'])
def admin_news():
    return render_template('admin/news/layout.html',
                           title='Admin News')


@app.route("/admin/news/add", methods=['GET', 'POST'])
def admin_news_add():
    form = AdminAddNewsForm()
    form.populate_dd()

    if form.validate_on_submit():
        print("add news")
        newNews = News(title=form.title.data,
                       content=form.content.data)
        db.session.add(newNews)
        db.session.commit()

        return redirect(url_for('admin_news_add'))

    return render_template('admin/news/add.html',
                           form=form,
                           title='Admin Add News')


@app.route("/admin/news/update", methods=['GET', 'POST'])
def admin_news_update():
    form = AdminUpdateNewsForm()
    form.populate_dd()
    
    if request.method == 'POST':
        update_news = News.query.filter_by(id=form.news_dd.data).all()[0]
        update_news.title = form.title.data
        update_news.content = form.content.data
        update_news.date = datetime.utcnow()
        db.session.commit()

        return redirect(url_for('admin_news_update'))

    return render_template('admin/news/update.html',
                           form=form,
                           title='Admin Update News')


@app.route("/admin/news/delete", methods=['GET', 'POST'])
def admin_news_delete():
    form = AdminDeleteNewsForm()
    form.populate_dd()

    if request.method == 'POST':
        News.query.filter_by(id=form.news_dd.data).delete()
        db.session.commit()

        return redirect(url_for('admin_news_delete'))

    return render_template('admin/news/delete.html',
                           form=form,
                           title='Admin Delete News')
