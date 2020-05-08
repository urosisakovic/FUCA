from flask import render_template

from flask_login import current_user, login_required
from fuca import app


@app.route("/admin")
@login_required
def admin():
    if not current_user.is_admin:
        return "Access forbiden"

    return render_template('admin/layout.html', title='Admin')
        
