from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for, jsonify
)
from werkzeug.exceptions import abort

# from flaskr.auth import login_required
# from flaskr.db import get_db

from app.models import student_interface

bp = Blueprint('students', __name__)

@bp.route('/students')
def students():
    student_table = student_interface.all()
    return jsonify({'students': student_table})