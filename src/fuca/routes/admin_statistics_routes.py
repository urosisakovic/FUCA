from flask import redirect, render_template, request, url_for

from fuca import app, db, forms


@app.route("/admin/statistics", methods=['GET', 'POST'])
def admin_statistics():
    form = AdminAddStatsForm()
    if form.validate_on_submit():
        print("Validated")
    else:
        print("Not Validated")

    return render_template('admin/statistics.html', form=form, title='Admin Statistics')
