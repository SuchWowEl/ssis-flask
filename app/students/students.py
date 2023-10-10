from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for, jsonify
)
from werkzeug.exceptions import abort

# from flaskr.auth import login_required
# from flaskr.db import get_db

from app.models import student_interface

bp = Blueprint('students', __name__)

@bp.route('/students/', methods=['GET', 'POST'])
def students():
    if request.method == 'GET':
        student_table = student_interface.all()
        student_table.insert(0, student_interface.headers())
        print("students retrieved")
        # student_table = json.loads(student_table)
        return jsonify({'table': render_template("table.html", content=student_table)})
        # return jsonify({'students': student_table})