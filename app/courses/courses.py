from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for, jsonify
)
from werkzeug.exceptions import abort
import json

# from flaskr.auth import login_required
# from flaskr.db import get_db

from app.models import ofcourse, college_interface

bp = Blueprint('courses', __name__)

coursecode = ""
search_header = "Filter by..."
search_value = ""

@bp.route('/courses/')
def courses():
    global coursecode
    coursecode = ""
    course_table = courses_table()
    print("courses retrieved")
    return render_template("course/course.html", content=course_table, search_details=[search_header, search_value])
        
@bp.route('/courses/add/')
def courses_add_view():
    college_table = college_interface.collegecodes()
    print(college_table)
    colleges = [item[0] for item in college_table]
    return render_template("course/edit.html", content=colleges)

@bp.route('/courses/addcourse/', methods=['POST'])
def courses_add():
    print("courses_add called")
    data = request.get_json()
    print("form: " + str(data))
    ofcourse.add(data)
    return redirect(url_for("courses.courses"))

@bp.route('/courses/edit/', methods=['POST'])
def courses_edit_view():
    print("courses_edit called")
    data = request.get_json()
    courseInfo = ofcourse.retrieve_course(data["code"])
    global coursecode 
    coursecode = data["code"]
    college_table = college_interface.collegecodes()
    print(college_table)
    colleges = [item[0] for item in college_table]
    return render_template("course/edit.html", content=colleges, info=courseInfo)

@bp.route('/courses/editcourse/', methods=['POST'])
def students_edit():
    global coursecode 
    print("students_edit called")
    data = request.get_json()
    print("form: " + str(data))
    ofcourse.update(data, coursecode)
    coursecode = ""
    return redirect(url_for("courses.courses"))

@bp.route('/courses/delete/', methods=['POST'])
def courses_delete():
    data = request.get_json()
    print(data)
    list = data["list"]
    print("list is " + str(list))
    ofcourse.delete_rows(list)
    return redirect(url_for("courses.courses"))

@bp.route('/courses/search/', methods=['POST'])
def students_search():
    # data = request.get_json()
    data = request.get_json()
    print("data:")
    print(data)
    global search_header, search_value
    search_header, search_value = data["header"], data["search"]
    return redirect(url_for("courses.courses"))

def courses_table():
    courses_table = ""
    if(not search_header in ["Filter by...", ""]):
        courses_table = ofcourse.search(search_header, search_value)
        courses_table.insert(0, ofcourse.headers())
    else:
        courses_table = ofcourse.all()
        courses_table.insert(0, ofcourse.headers())
    return courses_table