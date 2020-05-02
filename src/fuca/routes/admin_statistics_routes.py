from flask import redirect, render_template, request, url_for

from fuca import app, data_utils
from fuca.forms import (AdminAddStatisticsForm, AdminDeleteStatisticsForm,
                        AdminUpdateStatisticsForm)
from fuca.models import Statistics


@app.route("/admin/statistics", methods=['GET', 'POST'])
def admin_statistics():
    return render_template('admin/statistics/layout.html', title='Admin Statistics')


@app.route("/admin/statistics/add", methods=['GET', 'POST'])
def admin_statistics_add():
    form = AdminAddStatisticsForm()
    form.populate_dd()
    
    if request.method == 'POST':
        data_utils.add_statistics()

    return render_template('admin/statistics/add.html', form=form, title='Admin Add Statistics')


@app.route("/admin/statistics/update", methods=['GET', 'POST'])
def admin_statistics_update():
    form = AdminUpdateStatisticsForm()
    form.populate_dd()
    
    if request.method == 'POST':
        data_utils.update_statistics()

    return render_template('admin/statistics/update.html', form=form, title='Admin Update Statistics')


@app.route("/admin/statistics/remove", methods=['GET', 'POST'])
def admin_statistics_delete():
    form = AdminDeleteStatisticsForm()
    form.populate_dd()
    
    if request.method == 'POST':
        data_utils.delete_statistics()

    return render_template('admin/statistics/delete.html', form=form, title='Admin Delete Statistics')
