from app import mysql
import numpy


class Student:

    # def __init__(self, mysql, username=None, password=None, email=None):
    #     mysql = mysql
    #     self.username = username
    #     self.password = password
    #     self.email = email
    
    def retrieve_student(self, id):
        cursor = mysql.connection.cursor()
        print("a student triggered")

        sql = f"SELECT * from student where (`id` = '{id}')"
        cursor.execute(sql)
        result = cursor.fetchone() 
        print("retreived student from model:")
        print(result)
        values = []
        for inner_tuple in result:
            values.append(inner_tuple)
        print("retreived tuplevar from model:")
        print(values)
        return values
        
    
    # student_info is dict
    def add(self, student_info):
        cursor = mysql.connection.cursor()
        
        print(student_info)

        sql = f"INSERT INTO `student` (`id`, `firstname`, `lastname`, `course`, `year`, `gender`) \
       VALUES ('{student_info['id']}', '{student_info['firstname']}', '{student_info['lastname']}', '{student_info['course']}', \
               '{student_info['year']}', '{student_info['gender']}')"

        cursor.execute(sql)
        mysql.connection.commit()
        
    # student_info is dict
    def update(self, student_info, studentID):
        cursor = mysql.connection.cursor()
        
        sql = f"UPDATE `student` \
                SET `id` = '{student_info['id']}', `firstname` = '{student_info['firstname']}', `lastname` = '{student_info['lastname']}', \
                `course` = '{student_info['course']}', `year` = {student_info['year']}, `gender` = '{student_info['gender']}' \
                WHERE `id` = '{studentID}'"
                
        print(sql)

        cursor.execute(sql)
        mysql.connection.commit()
        
    # @classmethod
    def all(self):
        cursor = mysql.connection.cursor()
        print("students triggered")

        sql = "SELECT * from student"
        cursor.execute(sql)
        result = cursor.fetchall()
        return result
    
    def headers(self):
        cursor = mysql.connection.cursor()
        sql = "SELECT COLUMN_NAME \
        FROM INFORMATION_SCHEMA.COLUMNS \
        WHERE TABLE_NAME = 'student' \
        AND TABLE_SCHEMA = 'ssis' \
        ORDER BY ORDINAL_POSITION;"
        cursor.execute(sql)
        result = cursor.fetchall() 
        values = []
        for inner_tuple in result:
            values.append(inner_tuple[0])
        tuplevar = tuple(values)
        return tuplevar
        
    def delete_rows(self, id_to_delete):
        # id_to_delete = ["John Doe", "Jane Doe"]
        cursor = mysql.connection.cursor()
        if not isinstance(id_to_delete, (list, tuple, numpy.ndarray)):
            id_to_delete = [id_to_delete]
        placeholders = ",".join(["%s"] * len(id_to_delete))
        sql = "DELETE FROM student WHERE `id` IN ({})".format(
            placeholders)
        # sql2 = " IN ({})".format(placeholders)
        cursor.execute(sql, tuple(id_to_delete))
        mysql.connection.commit()

    # @classmethod
    def delete(self,id):    
        try:
            cursor = mysql.connection.cursor()
            sql = f"DELETE from student where id= {id}"
            cursor.execute(sql)
            mysql.connection.commit()
            return True
        except:
            return False

class Course:

    # def __init__(self, mysql, username=None, password=None, email=None):
    #     mysql = mysql
    #     self.username = username
    #     self.password = password
    #     self.email = email
    
    # student_info is list
    def add(self, course_info):
        cursor = mysql.connection.cursor()

        sql = f"INSERT INTO `student` (`code`, `name`, `college`) \
       VALUES ('{course_info[0]}', '{course_info[1]}', '{course_info[2]}')"

        cursor.execute(sql)
        mysql.connection.commit()
        
    def update(self, column, newvalue, id):
        cursor = mysql.connection.cursor()
        
        # UPDATE `ssis`.`student` SET `firstname` = 'asda' WHERE (`id` = '2021-0001');
        sql = f"UPDATE `course` SET `{column}` = '{newvalue}' \
                WHERE (`id` = '{id}')" 

        cursor.execute(sql)
        mysql.connection.commit()
    # @classmethod
    def all(self):
        cursor = mysql.connection.cursor()

        sql = "SELECT * from course"
        cursor.execute(sql)
        result = cursor.fetchall()
        return result
    
    # @classmethod
    def coursecodes(self):
        cursor = mysql.connection.cursor()

        sql = "SELECT code from course"
        cursor.execute(sql)
        result = cursor.fetchall()
        return result
    
    def headers(self):
        cursor = mysql.connection.cursor()
        sql = "SELECT COLUMN_NAME \
        FROM INFORMATION_SCHEMA.COLUMNS \
        WHERE TABLE_NAME = 'course' \
        AND TABLE_SCHEMA = 'ssis' \
        ORDER BY ORDINAL_POSITION;"
        cursor.execute(sql)
        result = cursor.fetchall()
        values = []
        for inner_tuple in result:
            values.append(inner_tuple[0])
        tuplevar = tuple(values)
        return tuplevar

    # @classmethod
    def delete(self,id):    
        try:
            cursor = mysql.connection.cursor()
            sql = f"DELETE from course where id= {id}"
            cursor.execute(sql)
            mysql.connection.commit()
            return True
        except:
            return False

class College:

    # def __init__(self, mysql, username=None, password=None, email=None):
    #     mysql = mysql
    #     self.username = username
    #     self.password = password
    #     self.email = email
    
    # student_info is list
    def add(self, college_info):
        cursor = mysql.connection.cursor()

        sql = f"INSERT INTO `college` (`code`, `name`) \
       VALUES ('{college_info[0]}', '{college_info[1]}')"

        cursor.execute(sql)
        mysql.connection.commit()
        
    def update(self, column, newvalue, code):
        cursor = mysql.connection.cursor()
        
        # UPDATE `ssis`.`student` SET `firstname` = 'asda' WHERE (`id` = '2021-0001');
        sql = f"UPDATE `college` SET `{column}` = '{newvalue}' \
                WHERE (`code` = '{code}')" 

        cursor.execute(sql)
        mysql.connection.commit()
    # @classmethod
    def all(self):
        cursor = mysql.connection.cursor()

        sql = "SELECT * from college"
        cursor.execute(sql)
        result = cursor.fetchall()
        return result
    
    def headers(self):
        cursor = mysql.connection.cursor()
        sql = "SELECT COLUMN_NAME \
        FROM INFORMATION_SCHEMA.COLUMNS \
        WHERE TABLE_NAME = 'college' \
        AND TABLE_SCHEMA = 'ssis' \
        ORDER BY ORDINAL_POSITION;"
        cursor.execute(sql)
        result = cursor.fetchall()
        values = []
        for inner_tuple in result:
            values.append(inner_tuple[0])
        tuplevar = tuple(values)
        return tuplevar

    # @classmethod
    def delete(self,code):    
        try:
            cursor = mysql.connection.cursor()
            sql = f"DELETE from college where code= {code}"
            cursor.execute(sql)
            mysql.connection.commit()
            return True
        except:
            return False


student_interface = Student()
ofcourse = Course()
college_interface = College()
