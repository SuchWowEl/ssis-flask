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

@bp.route('/courses/', methods=['GET', 'POST'])
def courses():
    if request.method == 'GET':
        course_table = ofcourse.all()
        course_table.insert(0, ofcourse.headers())
        print("courses retrieved")
        # course_table = json.loads(course_table)
        return render_template("course/course.html", content=course_table)
        # return jsonify({'courses': course_table})
        
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
    course_table = ""
    if(data["search"] != ""):
        course_table = ofcourse.search(data["header"], data["search"])
        course_table.insert(0, ofcourse.headers())
    else:
        course_table = ofcourse.all()
        course_table.insert(0, ofcourse.headers())
    print("students retrieved")
    return render_template("table.html", content=course_table)