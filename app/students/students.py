from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for, jsonify
)
from werkzeug.exceptions import abort
from cloudinary import uploader
from cloudinary.uploader import upload
from cloudinary.utils import cloudinary_url

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
    #print("form: " + str(data))
    try:
        pic_link = data['profile_pic']
        if pic_link != "static/default_pic.svg":
            upload_result = upload(pic_link, public_id = data['id'], 
            overwrite = True,folder="SSIS", resource_type='image')
            secure_url = upload_result['secure_url']
        else:
            secure_url = ""
        data['profile_pic'] = secure_url
        print(f"secure_url: {secure_url}")
        student_interface.add(data)
        return jsonify({'response':True})
    except Exception as e:
        print(str(e))
        return jsonify({'response':str(e)})
    
@bp.route('/students/edit/', methods=['GET'])
def students_edit_view():
    print("/students/edit/ called")
    id_to_edit = request.args.getlist('id')
    studentInfo = student_interface.retrieve_student(id_to_edit[0])
    global studentid 
    studentid = id_to_edit[0]
    course_table = ofcourse.coursecodes()
    print("studentInfo from controller:")
    print(studentInfo)
    print(course_table)
    courses = [item[0] for item in course_table]
    return render_template("student/edit.html", content=courses, info=studentInfo)
    
@bp.route('/students/editstudent/', methods=['POST'])
def students_edit():
    global studentid 
    data = request.get_json()
    new_pic = data['profile_pic']
    
    secure_url = ""
    old_info = student_interface.retrieve_student(studentid)
    if old_info[6] != new_pic: # if pic_changed
        # upload
        if new_pic != "static/default_pic.svg": # there's a new pic
            upload_result = upload(new_pic, public_id = data['id'], 
            overwrite = True, folder="SSIS", resource_type='image')
            secure_url = upload_result['secure_url']
        else:
            secure_url = ""
        data['profile_pic'] = secure_url
        if studentid != data['id'] or secure_url == "": # if id_changed or pic_delete
            print("delete old id")
            uploader.destroy("SSIS/"+studentid) # delete old pic
    if studentid != data['id'] and old_info[6] == new_pic: # if id_changed and not pic_changed
        uploader.rename("SSIS/"+studentid, "SSIS/"+data['id'])
    
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
    print(f"delete is {response}")
    if response != True:
        print("delete failed")
        response = str(response)
    else:
        for public_id in list:
            uploader.destroy("SSIS/"+public_id) # delete old pic
    return jsonify({'response': response})

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
    else:
        student_table = student_interface.all()
    result = student_interface.headers()
    to_insert = (result[0], result[1], result[2], result[3], result[4], result[5], "college")
    student_table.insert(0, to_insert)
    return student_table

@bp.route('/students/gender/retriever/')
def gender_retriever():
    genders = ["Male", "Female", "Others"]
    return render_template("filter_dropdown.html", content = genders)

@bp.route('/students/loading')
def spinner():
    return render_template("student/uploading.html")