"""
Author: Uros Isakovic
"""
from flask import render_template, abort

from flask_login import current_user, login_required
from flask import Blueprint

adminhome = Blueprint('adminhome', __name__)

@adminhome.route("/")
@login_required
def admin():
    """
    Route reserved for admin access only.
    Used for administration of the whole website.
    """
    if not current_user.is_admin:
        abort(403)

    return render_template('admin/layout.html', title='Admin')
        
