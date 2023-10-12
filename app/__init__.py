print('eyo')
from flask import Flask, render_template, jsonify, request
from flask_mysql_connector import MySQL
from flask_bootstrap import Bootstrap
from config import DB_USERNAME, DB_PASSWORD, DB_NAME, DB_HOST, SECRET_KEY, BOOTSTRAP_SERVE_LOCAL
from flask_wtf.csrf import CSRFProtect

mysql = MySQL()
bootstrap = Bootstrap()

def create_app(test_config=None):
    app = Flask(__name__, static_folder='static', static_url_path='/static', instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY=SECRET_KEY,
        MYSQL_USER=DB_USERNAME,
        MYSQL_PASSWORD=DB_PASSWORD,
        MYSQL_DATABASE=DB_NAME,
        MYSQL_HOST=DB_HOST,
        #BOOTSTRAP_SERVE_LOCAL=BOOTSTRAP_SERVE_LOCAL
    )
    bootstrap.init_app(app)
    mysql.init_app(app)
    CSRFProtect(app)

    # from .user import user_bp as user_blueprint
    # app.register_blueprint(user_blueprint)
    # from . import models
    # student_interface = models.Student(mysql)
    
    # @app.route('/', defaults={'path': ''})
    # @app.route('/<path:path>', methods=('GET', 'POST'))
    # def catch_all(path):
        # return app.send_static_file("base.html")
        
    @app.route('/')
    def home(content=None):
        return render_template("base.html", content=content)
    
    from .students import students
    app.register_blueprint(students.bp)
    
    from .courses import courses
    app.register_blueprint(courses.bp)
    
    from .colleges import colleges
    app.register_blueprint(colleges.bp)
    
    # from controller.student import user_bp as user_blueprint
    # app.register_blueprint(user_blueprint)
        

    print("hiya!")
    return app
