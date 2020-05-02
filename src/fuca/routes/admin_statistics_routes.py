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
        return redirect(url_for('admin_statistics_add'))

    return render_template('admin/statistics/add.html', form=form, title='Admin Add Statistics')


@app.route("/admin/statistics/update", methods=['GET', 'POST'])
def admin_statistics_update():
    form = AdminUpdateStatisticsForm()
    form.populate_dd()
    
    if request.method == 'POST':
        data_utils.update_statistics(match_id=form.match_dd.data,
                                     player_id=form.player_dd.data,
                                     goals=form.goals.data,
                                     assists=form.assists.data,
                                     yellow=form.yellow.data,
                                     red=form.red.data)
        return redirect(url_for('admin_statistics_update'))

    return render_template('admin/statistics/update.html', form=form, title='Admin Update Statistics')


@app.route("/admin/statistics/remove", methods=['GET', 'POST'])
def admin_statistics_delete():
    form = AdminDeleteStatisticsForm()
    form.populate_dd()
    
    if request.method == 'POST':
        data_utils.delete_statistics(match_id=form.match_dd.data,
                                     player_id=form.player_dd.data)
        return redirect(url_for('admin_statistics_delete'))

    return render_template('admin/statistics/delete.html', form=form, title='Admin Delete Statistics')
