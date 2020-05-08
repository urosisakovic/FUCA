from datetime import datetime

from flask import Blueprint, redirect, render_template, request, url_for

from flask_login import current_user, login_required
from fuca import app, data_utils
from fuca.admin.news.forms import (AdminAddNewsForm, AdminDeleteNewsForm,
                                    AdminUpdateNewsForm)
from fuca.models import News

news = Blueprint('news', __name__)

@news.route("/admin/news", methods=['GET', 'POST'])
@login_required
def admin_news():
    if not current_user.is_admin:
        return "Access forbiden"

    return render_template('admin/news/layout.html',
                           title='Admin News')


@news.route("/admin/news/add", methods=['GET', 'POST'])
@login_required
def admin_news_add():
    if not current_user.is_admin:
        return "Access forbiden"

    form = AdminAddNewsForm()
    form.populate_dd()

    if form.validate_on_submit():
        data_utils.add_news(title=form.title.data,
                            content=form.content.data)

        return redirect(url_for('news.admin_news_add'))

    return render_template('admin/news/add.html',
                           form=form,
                           title='Admin Add News')


@news.route("/admin/news/update", methods=['GET', 'POST'])
@login_required
def admin_news_update():
    if not current_user.is_admin:
        return "Access forbiden"

    form = AdminUpdateNewsForm()
    form.populate_dd()
    
    if request.method == 'POST':
        data_utils.update_news(id=form.news_dd.data, 
                               new_title=form.title.data,
                               new_content=form.content.data)
        return redirect(url_for('news.admin_news_update'))

    return render_template('admin/news/update.html',
                           form=form,
                           title='Admin Update News')


@news.route("/admin/news/delete", methods=['GET', 'POST'])
@login_required
def admin_news_delete():
    if not current_user.is_admin:
        return "Access forbiden"

    form = AdminDeleteNewsForm()
    form.populate_dd()

    if request.method == 'POST':
        data_utils.delete_news(id=form.news_dd.data)
        return redirect(url_for('news.admin_news_delete'))

    return render_template('admin/news/delete.html',
                           form=form,
                           title='Admin Delete News')
