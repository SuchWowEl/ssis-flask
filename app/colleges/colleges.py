from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for, jsonify
)
from werkzeug.exceptions import abort
import json

# from flaskr.auth import login_required
# from flaskr.db import get_db

from app.models import college_interface

bp = Blueprint('colleges', __name__)

collegecode = ""

@bp.route('/colleges/', methods=['GET', 'POST'])
def colleges():
    if request.method == 'GET':
        college_table = college_interface.all()
        college_table.insert(0, college_interface.headers())
        print("colleges retrieved")
        # college_table = json.loads(college_table)
        return render_template("college/college.html", content=college_table)
        # return jsonify({'colleges': college_table})
        
@bp.route('/colleges/add/')
def colleges_add_view():
    return render_template("college/edit.html", content=colleges)

@bp.route('/colleges/addcollege/', methods=['POST'])
def colleges_add():
    print("colleges_add called")
    data = request.get_json()
    print("form: " + str(data))
    college_interface.add(data)
    return redirect(url_for("colleges.colleges"))

@bp.route('/colleges/edit/', methods=['POST'])
def colleges_edit_view():
    print("colleges_edit_view called")
    data = request.get_json()
    collegeInfo = college_interface.retrieve_college(data["code"])
    global collegecode 
    collegecode = data["code"]
    return render_template("college/edit.html", info=collegeInfo)

@bp.route('/colleges/editcollege/', methods=['POST'])
def colleges_edit():
    global collegecode 
    print("students_edit called")
    data = request.get_json()
    print("form: " + str(data))
    college_interface.update(data, collegecode)
    collegecode = ""
    return redirect(url_for("colleges.colleges"))

@bp.route('/colleges/delete/', methods=['POST'])
def colleges_delete():
    data = request.get_json()
    print(data)
    list = data["list"]
    print("list is " + str(list))
    college_interface.delete_rows(list)
    return redirect(url_for("colleges.colleges"))

@bp.route('/colleges/search/', methods=['POST'])
def students_search():
    # data = request.get_json()
    data = request.get_json()
    print("data:")
    print(data)
    college_table = ""
    if(data["search"] != ""):
        college_table = college_interface.search(data["header"], data["search"])
        college_table.insert(0, college_interface.headers())
    else:
        college_table = college_interface.all()
        college_table.insert(0, college_interface.headers())
    print("students retrieved")
    return render_template("table.html", content=college_table)