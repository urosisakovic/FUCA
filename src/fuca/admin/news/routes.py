from datetime import datetime

from flask import Blueprint, redirect, render_template, request, url_for

from flask_login import current_user, login_required
from fuca import data_utils
from fuca.admin.news.forms import (AdminAddNewsForm, AdminDeleteNewsForm,
                                    AdminUpdateNewsForm)
from fuca.models import News

news = Blueprint('news', __name__)

@news.route("/", methods=['GET', 'POST'])
@login_required
def admin_news():
    if not current_user.is_admin:
        abort(403)

    return render_template('admin/news/layout.html',
                           title='Admin News')


@news.route("/add", methods=['GET', 'POST'])
@login_required
def admin_news_add():
    if not current_user.is_admin:
        abort(403)

    form = AdminAddNewsForm()
    form.populate_dd()

    if form.validate_on_submit():
        data_utils.add_news(title=form.title.data,
                            content=form.content.data)

        return redirect(url_for('news.admin_news_add'))

    return render_template('admin/news/add.html',
                           form=form,
                           title='Admin Add News')


@news.route("/update", methods=['GET', 'POST'])
@login_required
def admin_news_update():
    if not current_user.is_admin:
        abort(403)

    form = AdminUpdateNewsForm()
    form.populate_dd()

    page = request.args.get('id', type=int)
    if page:
        news = News.query.get(page)
        form.news_dd.default = page
        form.process()
        form.title.data = news.title
        form.content.data = news.content
    
    if request.method == 'POST':
        data_utils.update_news(id=form.news_dd.data, 
                               new_title=form.title.data,
                               new_content=form.content.data)
        return redirect(url_for('news.admin_news_update'))

    return render_template('admin/news/update.html',
                           form=form,
                           title='Admin Update News')


@news.route("/delete", methods=['GET', 'POST'])
@login_required
def admin_news_delete():
    if not current_user.is_admin:
        abort(403)

    form = AdminDeleteNewsForm()
    form.populate_dd()

    if request.method == 'POST':
        data_utils.delete_news(id=form.news_dd.data)
        return redirect(url_for('news.admin_news_delete'))

    return render_template('admin/news/delete.html',
                           form=form,
                           title='Admin Delete News')
