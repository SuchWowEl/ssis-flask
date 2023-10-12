from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for, jsonify
)
from werkzeug.exceptions import abort
import json

# from flaskr.auth import login_required
# from flaskr.db import get_db

from app.models import college_interface

bp = Blueprint('colleges', __name__)

@bp.route('/colleges/', methods=['GET', 'POST'])
def colleges():
    if request.method == 'GET':
        college_table = college_interface.all()
        college_table.insert(0, college_interface.headers())
        print("colleges retrieved")
        # college_table = json.loads(college_table)
        return jsonify({'table': render_template("table.html", content=college_table)})
        # return jsonify({'colleges': college_table})