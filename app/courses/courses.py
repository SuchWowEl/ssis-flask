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
    try:
        ofcourse.add(data)
        return jsonify({'response':True})
    except Exception as e:
        return jsonify({'response':str(e)})
    
@bp.route('/courses/edit/', methods=['GET'])
def courses_edit_view():
    print("courses_edit called")
    code_to_edit = request.args.getlist('code')
    courseInfo = ofcourse.retrieve_course(code_to_edit[0])
    global coursecode 
    coursecode = code_to_edit[0]
    college_table = college_interface.collegecodes()
    print(college_table)
    colleges = [item[0] for item in college_table]
    return render_template("course/edit.html", content=colleges, info=courseInfo)

@bp.route('/courses/editcourse/', methods=['POST'])
def courses_edit():
    global coursecode 
    print("coursecode called")
    data = request.get_json()
    print("form: " + str(data))
    response = ofcourse.update(data, coursecode)
    coursecode = ""
    if response != True:
        response = str(response)
    print(response)
    return jsonify({'response': response})
        
@bp.route('/courses/delete/', methods=['POST'])
def courses_delete():
    data = request.get_json()
    print(data)
    list = data["list"]
    print("list is " + str(list))
    response = ofcourse.delete_rows(list)
    if response != True:
        response = str(response)
    return jsonify({"response": response})

@bp.route('/courses/search/', methods=['GET'])
def courses_search():
    # data = request.get_json()
    try:
        header = request.args.getlist('header')
        search = request.args.getlist('search')
        print(f"header: {header[0]}, search: {search[0]}")
        global search_header, search_value
        search_header, search_value = header[0], search[0]
        return jsonify({'response': True})
    except Exception as e:
        return jsonify({'response': e})

@bp.route('/courses/verify/<id>', methods=["GET"])
def courses_id_confirm(id):
    if ofcourse.confirm_course(id):
        return jsonify({"response": str(id)+" already exists"})
    else:
        return jsonify({"response": True})
    
@bp.route('/courses/toast/fail/<id>', methods=["GET"])
def courses_toast_fail(id):
    return render_template("toast_delete.html", error=id+" already exists")

def courses_table():
    courses_table = ""
    if(not search_header in ["Filter by...", ""]):
        courses_table = ofcourse.search(search_header, search_value)
        courses_table.insert(0, ofcourse.headers())
    else:
        courses_table = ofcourse.all()
        courses_table.insert(0, ofcourse.headers())
    return courses_table

@bp.route('/courses/retriever/')
def courses_retriever():
    course_table = ofcourse.coursecodes()
    print(course_table)
    courses = [item[0] for item in course_table]
    return render_template("filter_dropdown.html", content = courses)