from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for, jsonify
)
from werkzeug.exceptions import abort

# from flaskr.auth import login_required
# from flaskr.db import get_db

from app.models import student_interface, ofcourse

bp = Blueprint('students', __name__)

studentid = ""

@bp.route('/students/')
def students():
    global studentid
    studentid = ""
    student_table = student_interface.all()
    student_table.insert(0, student_interface.headers())
    print("students retrieved")
    return render_template("student/student.html", content=student_table)
    
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
    student_interface.add(data)
    return jsonify({"ok":True})
    
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
    student_interface.update(data, studentid)
    studentid = ""
    return redirect(url_for("students.students"))
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
    student_interface.delete_rows(list)
    return redirect(url_for("students.students"))

@bp.route('/students/search/', methods=['POST'])
def students_search():
    # data = request.get_json()
    data = request.get_json()
    print("data:")
    print(data)
    student_table = ""
    if(data["search"] != ""):
        student_table = student_interface.search(data["header"], data["search"])
        student_table.insert(0, student_interface.headers())
    else:
        student_table = student_interface.all()
        student_table.insert(0, student_interface.headers())
    print("students retrieved")
    return render_template("table.html", content=student_table)