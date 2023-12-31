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
search_header = "Filter by..."
search_value = ""

@bp.route('/colleges/')
def colleges():
    global collegecode
    collegecode = ""
    college_table = colleges_table()
    print("courses retrieved")
    # college_table = json.loads(college_table)
    return render_template("college/college.html", content=college_table, search_details=[search_header, search_value])
    # return jsonify({'colleges': college_table})
        
@bp.route('/colleges/add/')
def colleges_add_view():
    return render_template("college/edit.html", content=colleges)

@bp.route('/colleges/addcollege/', methods=['POST'])
def colleges_add():
    print("colleges_add called")
    data = request.get_json()
    print("form: " + str(data))
    try:
        college_interface.add(data)
        return jsonify({'response':True})
    except Exception as e:
        return jsonify({'response':str(e)})
    
@bp.route('/colleges/edit/', methods=['GET'])
def colleges_edit_view():
    print("colleges_edit_view called")
    code_to_edit = request.args.getlist('code')
    collegeInfo = college_interface.retrieve_college(code_to_edit[0])
    global collegecode 
    collegecode = code_to_edit[0]
    return render_template("college/edit.html", info=collegeInfo)

@bp.route('/colleges/editcollege/', methods=['POST'])
def colleges_edit():
    global collegecode 
    print("colleges_edit called")
    data = request.get_json()
    print("form: " + str(data))
    response = college_interface.update(data, collegecode)
    collegecode = ""
    if response != True:
        response = str(response)
    print(response)
    return jsonify({'response': response})

@bp.route('/colleges/delete/', methods=['POST'])
def colleges_delete():
    data = request.get_json()
    print(data)
    list = data["list"]
    print("list is " + str(list))
    response = college_interface.delete_rows(list)
    if response != True:
        response = str(response)
    return jsonify({"response": response})

@bp.route('/colleges/search/', methods=['GET'])
def colleges_search():
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

@bp.route('/colleges/verify/<id>', methods=["GET"])
def colleges_id_confirm(id):
    if college_interface.confirm_college(id):
        return jsonify({"response": str(id)+" already exists"})
    else:
        return jsonify({"response": True})
    
@bp.route('/colleges/toast/fail/<id>', methods=["GET"])
def colleges_toast_fail(id):
    return render_template("toast_delete.html", error=id+" already exists")

def colleges_table():
    colleges_table = ""
    if(not search_header in ["Filter by...", ""]):
        colleges_table = college_interface.search(search_header, search_value)
        colleges_table.insert(0, college_interface.headers())
    else:
        colleges_table = college_interface.all()
        colleges_table.insert(0, college_interface.headers())
    return colleges_table

@bp.route('/colleges/retriever/')
def colleges_retriever():
    college_table = college_interface.collegecodes()
    print(college_table)
    colleges = [item[0] for item in college_table]
    return render_template("filter_dropdown.html", content = colleges)