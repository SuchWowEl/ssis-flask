from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for, jsonify
)
from werkzeug.exceptions import abort

# from flaskr.auth import login_required
# from flaskr.db import get_db

from app.models import student_interface, ofcourse

bp = Blueprint('students', __name__)

studentid = ""
search_header = "Filter by..."
search_value = ""

@bp.route('/students/')
def students():
    global studentid
    studentid = ""
    student_table = students_table()
    print("students retrieved")
    return render_template("student/student.html", content=student_table, search_details=[search_header, search_value])
    
@bp.route('/students/add/')
def students_add_view():
    course_table = ofcourse.coursecodes()
    print(course_table)
    courses = [item[0] for item in course_table]
    return render_template("student/edit.html", content=courses)
    
@bp.route('/students/addstudent/', methods=['POST'])
def students_add():
    print("students_add called")
    data = request.get_json()
    print("form: " + str(data))
    try:
        student_interface.add(data)
        return jsonify({'response':True})
    except Exception as e:
        return jsonify({'response':str(e)})
    
@bp.route('/students/edit/', methods=['POST'])
def students_edit_view():
    print("students_add called")
    data = request.get_json()
    studentInfo = student_interface.retrieve_student(data["id"])
    global studentid 
    studentid = data["id"]
    course_table = ofcourse.coursecodes()
    print("studentInfo from controller:")
    print(studentInfo)
    print(course_table)
    courses = [item[0] for item in course_table]
    return render_template("student/edit.html", content=courses, info=studentInfo)
    
@bp.route('/students/editstudent/', methods=['POST'])
def students_edit():
    global studentid 
    print("students_edit called")
    data = request.get_json()
    print("form: " + str(data))
    response = student_interface.update(data, studentid)
    studentid = ""
    if response != True:
        response = str(response)
    print(response)
    return jsonify({'response': response})
    # student_table = student_interface.all()
    # student_table.insert(0, student_interface.headers())
    # print("students retrieved")
    # return render_template("student/student.html", content=student_table)
        # return jsonify({'courses': course_table})
        
@bp.route('/students/delete/', methods=['POST'])
def students_delete():
    data = request.get_json()
    print(data)
    list = data["list"]
    print("list is " + str(list))
    response = student_interface.delete_rows(list)
    if response != True:
        response = str(response)
    return response

# @bp.route('/students/search/', methods=['POST'])
# def students_search():
#     # data = request.get_json()
#     data = request.get_json()
#     print("data:")
#     print(data)
#     global search_header, search_value
#     search_header, search_value = data["header"], data["search"]
#     return redirect(url_for("students.students"))

@bp.route('/students/search/', methods=['GET'])
def students_search():
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

@bp.route('/students/verify/<id>', methods=["GET"])
def students_id_confirm(id):
    if student_interface.confirm_student(id):
        return jsonify({"response": str(id)+" already exists"})
    else:
        return jsonify({"response": True})
    
@bp.route('/students/toast/fail/<id>', methods=["GET"])
def students_toast_fail(id):
    return render_template("toast_delete.html", error=id+" already exists")

def students_table():
    student_table = ""
    if(not search_header in ["Filter by...", ""]):
        student_table = student_interface.search(search_header, search_value)
        student_table.insert(0, student_interface.headers())
    else:
        student_table = student_interface.all()
        student_table.insert(0, student_interface.headers())
    return student_table

@bp.route('/students/gender/retriever/')
def gender_retriever():
    genders = ["Male", "Female", "Others"]
    return render_template("filter_dropdown.html", content = genders)