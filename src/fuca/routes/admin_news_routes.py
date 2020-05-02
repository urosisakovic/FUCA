from datetime import datetime

from flask import redirect, render_template, request, url_for

from fuca import app, data_utils
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
        data_utils.add_news(title=form.title.data,
                            content=form.content.data)

        return redirect(url_for('admin_news_add'))

    return render_template('admin/news/add.html',
                           form=form,
                           title='Admin Add News')


@app.route("/admin/news/update", methods=['GET', 'POST'])
def admin_news_update():
    form = AdminUpdateNewsForm()
    form.populate_dd()
    
    if request.method == 'POST':
        data_utils.update_news(id=form.news_dd.data, 
                               new_title=form.title.data,
                               new_content=form.content.data)
        return redirect(url_for('admin_news_update'))

    return render_template('admin/news/update.html',
                           form=form,
                           title='Admin Update News')


@app.route("/admin/news/delete", methods=['GET', 'POST'])
def admin_news_delete():
    form = AdminDeleteNewsForm()
    form.populate_dd()

    if request.method == 'POST':
        data_utils.delete_news(id=form.news_dd.data)
        return redirect(url_for('admin_news_delete'))

    return render_template('admin/news/delete.html',
                           form=form,
                           title='Admin Delete News')
