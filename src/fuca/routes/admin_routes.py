from flask import render_template
from fuca import app

@app.route("/admin")
def admin():
    return render_template('admin/layout.html',
                           title='Admin')
