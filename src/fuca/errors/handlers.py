"""
Author: Nikola Barjaktarevic
"""
from flask import Blueprint, render_template

errors = Blueprint('errors', __name__)

@errors.app_errorhandler(404)
def error_404(error):
    """
    Route function which handles 404 error.

    Args:
        error: Flask-needed unused argument. 
    """
    return render_template('errors/404.html'), 404


@errors.app_errorhandler(403)
def error_403(error):
    """
    Route function which handles 403 error.

    Args:
        error: Flask-needed unused argument. 
    """
    return render_template('errors/403.html'), 403


@errors.app_errorhandler(500)
def error_500(error):
    """
    Route function which handles 500 error.

    Args:
        error: Flask-needed unused argument. 
    """
    return render_template('errors/500.html'), 500
