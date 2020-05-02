from flask import redirect, render_template, request, url_for

from fuca import app, db
from fuca.forms import AdminResultForm
from fuca.models import Match


@app.route("/admin/results", methods=['GET', 'POST'])
def admin_results():
    form = AdminResultForm()

    matches_db = Match.query.all()
    matches = [match.jinja_dict() for match in matches_db]
    match_choices = [(match['id'], match['team1_name'] + ' - ' + match['team2_name']) for match in matches]
    form.match_dd.choices = match_choices

    if form.validate_on_submit():
        print("Validated")
    else:
        print("Not Validated")

    return render_template('admin/results.html', form=form, title='Admin Results')