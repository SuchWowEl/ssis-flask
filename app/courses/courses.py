from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for, jsonify
)
from werkzeug.exceptions import abort
import json

# from flaskr.auth import login_required
# from flaskr.db import get_db

from app.models import ofcourse

bp = Blueprint('courses', __name__)

@bp.route('/courses/', methods=['GET', 'POST'])
def courses():
    if request.method == 'GET':
        course_table = ofcourse.all()
        course_table.insert(0, ofcourse.headers())
        print("courses retrieved")
        # course_table = json.loads(course_table)
        return jsonify({'table': render_template("table.html", content=course_table)})
        # return jsonify({'courses': course_table})