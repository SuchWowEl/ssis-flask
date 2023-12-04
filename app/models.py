from app import mysql
import numpy


class Student:
    
    def retrieve_student(self, id):
        cursor = mysql.connection.cursor()
        print("a student triggered")

        sql = f"SELECT * from ssis.student where (`id` = '{id}')"
        cursor.execute(sql)
        result = cursor.fetchone() 
        print("retreived student from model:")
        print(result)
        values = []
        if result == None:
            return []
        for inner_tuple in result:
            values.append(inner_tuple)
        print("retreived tuplevar from model:")
        print(values)
        return values
    
    def confirm_student(self, id):
        result = self.retrieve_student(id)
        return len(result)!=0
        
    
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
        
        try:
            sql = f"UPDATE `ssis`.`student` \
                    SET `id` = '{student_info['id']}', `firstname` = '{student_info['firstname']}', `lastname` = '{student_info['lastname']}', \
                    `course` = '{student_info['course']}', `year` = {student_info['year']}, `gender` = '{student_info['gender']}' \
                    WHERE `id` = '{studentID}'"
                    
            print(sql)

            cursor.execute(sql)
            mysql.connection.commit()
            return True
        except Exception as e:
            return e
        
    # @classmethod
    def all(self):
        cursor = mysql.connection.cursor()
        print("students triggered")

        sql = f"SELECT student.id, student.firstname, student.lastname, student.course, student.`year`, student.gender, \
                college.`code` \
                FROM ssis.student \
                INNER JOIN ssis.course \
                ON student.course = course.`code` \
                INNER JOIN ssis.college \
                ON college.`code` = course.`college`"
        cursor.execute(sql)
        result = cursor.fetchall()
        return result
    
    # @classmethod
    def search(self, header, value):
        cursor = mysql.connection.cursor()
        print("students triggered")

        sql = ""
        if  (header == "code"):
            sql = f"SELECT student.id, student.firstname, student.lastname, student.course, student.`year`, student.gender, \
                    college.`code` \
                    FROM ssis.student \
                    INNER JOIN ssis.course \
                    ON student.course = course.`code` \
                    INNER JOIN ssis.college \
                    ON college.`code` = course.`college` \
                    WHERE college.`code` LIKE '%{value}%';"
        elif (not header in ["gender", "course"]):
            sql = f"SELECT student.id, student.firstname, student.lastname, student.course, student.`year`, student.gender, \
                    college.`code` \
                    FROM ssis.student \
                    INNER JOIN ssis.course \
                    ON student.course = course.`code` \
                    INNER JOIN ssis.college \
                    ON college.`code` = course.`college` \
                    WHERE `{header}` LIKE '%{value}%';"
        else:
            sql = f"SELECT student.id, student.firstname, student.lastname, student.course, student.`year`, student.gender, \
                    college.`code` \
                    FROM ssis.student \
                    INNER JOIN ssis.course \
                    ON student.course = course.`code` \
                    INNER JOIN ssis.college \
                    ON college.`code` = course.`college` \
                    WHERE `{header}` = '{value}';"
        cursor.execute(sql)
        result = cursor.fetchall()
        return result
    
    def studentids(self):
        cursor = mysql.connection.cursor()

        sql = "SELECT id from `ssis`.`student`"
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
        try:
            cursor = mysql.connection.cursor()
            if not isinstance(id_to_delete, (list, tuple, numpy.ndarray)):
                id_to_delete = [id_to_delete]
            placeholders = ",".join(["%s"] * len(id_to_delete))
            sql = "DELETE FROM `ssis`.`student` WHERE `id` IN ({})".format(
                placeholders)
            # sql2 = " IN ({})".format(placeholders)
            cursor.execute(sql, tuple(id_to_delete))
            mysql.connection.commit()
            return True
        except Exception as e:
            return e

    # @classmethod
    def delete(self,id):    
        try:
            cursor = mysql.connection.cursor()
            sql = f"DELETE from `ssis`.`student` where id= {id}"
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
    
    def retrieve_course(self, code):
        cursor = mysql.connection.cursor()
        print("a course triggered")

        sql = f"SELECT * from `ssis`.`course` where (`code` = '{code}')"
        print(sql)
        cursor.execute(sql)
        result = cursor.fetchone() 
        print("retreived course from model:")
        print(result)
        values = []
        if result == None:
            return []
        for inner_tuple in result:
            values.append(inner_tuple)
        print("retreived tuplevar from model:")
        print(values)
        return values
    
    def confirm_course(self, code):
        result = self.retrieve_course(code)
        return len(result)!=0
    
    def add(self, course_info):
        print(course_info)
        print()
        cursor = mysql.connection.cursor()

        sql = f"INSERT INTO `ssis`.`course` (`code`, `name`, `college`) \
       VALUES ('{course_info['code']}', '{course_info['name']}', '{course_info['college']}')"

        cursor.execute(sql)
        mysql.connection.commit()
        
    def update(self, course_info, courseCode):
        try:
            cursor = mysql.connection.cursor()
            
            # UPDATE `ssis`.`student` SET `firstname` = 'asda' WHERE (`id` = '2021-0001');
            sql = f"UPDATE `ssis`.`course` \
                    SET `code` = '{course_info['code']}', `name` = '{course_info['name']}', `college` = '{course_info['college']}' \
                    WHERE `code` = '{courseCode}'"

            cursor.execute(sql)
            mysql.connection.commit()
            return True
        except Exception as e:
            return e
    # @classmethod
    def all(self):
        cursor = mysql.connection.cursor()

        sql = "SELECT * from ssis.course"
        cursor.execute(sql)
        result = cursor.fetchall()
        return result
    
    # @classmethod
    def search(self, header, value):
        cursor = mysql.connection.cursor()
        print("courses search")

        sql = ""
        if(header != "gender"):
            sql = f"SELECT * \
                FROM `ssis`.`course` \
                WHERE `{header}` LIKE '%{value}%';"
        else:
            sql = f"SELECT * \
                FROM `ssis`.`course` \
                WHERE `{header}`  '{value}';"
        cursor.execute(sql)
        result = cursor.fetchall()
        return result
    
    # @classmethod
    def coursecodes(self):
        cursor = mysql.connection.cursor()

        sql = "SELECT code from `ssis`.`course`"
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

    def delete_rows(self, id_to_delete):
        # id_to_delete = ["John Doe", "Jane Doe"]
        try:
            cursor = mysql.connection.cursor()
            if not isinstance(id_to_delete, (list, tuple, numpy.ndarray)):
                id_to_delete = [id_to_delete]
            placeholders = ",".join(["%s"] * len(id_to_delete))
            sql = "DELETE FROM `ssis`.`course` WHERE `code` IN ({})".format(
                placeholders)
            # sql2 = " IN ({})".format(placeholders)
            cursor.execute(sql, tuple(id_to_delete))
            mysql.connection.commit()
            return True
        except Exception as e:
            return e

    # @classmethod
    def delete(self,id):    
        try:
            cursor = mysql.connection.cursor()
            sql = f"DELETE from `ssis`.`course` where id= {id}"
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
    
    def retrieve_college(self, code):
        cursor = mysql.connection.cursor()
        print("a college triggered")

        sql = f"SELECT * from `ssis`.`college` where (`code` = '{code}')"
        cursor.execute(sql)
        result = cursor.fetchone() 
        print("retreived college from model:")
        print(result)
        values = []
        if result == None:
            return []
        for inner_tuple in result:
            values.append(inner_tuple)
        print("retreived tuplevar from model:")
        print(values)
        return values
    
    def confirm_college(self, code):
        result = self.retrieve_college(code)
        return len(result)!=0
    
    # student_info is list
    def add(self, college_info):
        cursor = mysql.connection.cursor()

        sql = f"INSERT INTO `ssis`.`college` (`code`, `name`) \
       VALUES ('{college_info['code']}', '{college_info['name']}')"

        cursor.execute(sql)
        mysql.connection.commit()
        
    def update(self, college_info, collegeCode):
        try:
            cursor = mysql.connection.cursor()
            
            # UPDATE `ssis`.`student` SET `firstname` = 'asda' WHERE (`id` = '2021-0001');
            sql = f"UPDATE `ssis`.`college` \
            SET `code` = '{college_info['code']}', `name` = '{college_info['name']}' \
            WHERE `code` = '{collegeCode}'"

            cursor.execute(sql)
            mysql.connection.commit()
            return True
        except Exception as e:
            return e
    
    def collegecodes(self):
        cursor = mysql.connection.cursor()

        sql = "SELECT code from `ssis`.`college`"
        cursor.execute(sql)
        result = cursor.fetchall()
        return result
        
    
    # @classmethod
    def all(self):
        cursor = mysql.connection.cursor()

        sql = "SELECT * from `ssis`.`college`"
        cursor.execute(sql)
        result = cursor.fetchall()
        return result
    
    # @classmethod
    def search(self, header, value):
        cursor = mysql.connection.cursor()
        print("courses search")

        sql = f"SELECT * \
            FROM `ssis`.`college` \
            WHERE `{header}` LIKE '%{value}%';"
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

    def delete_rows(self, id_to_delete):
        try:
            # id_to_delete = ["John Doe", "Jane Doe"]
            cursor = mysql.connection.cursor()
            if not isinstance(id_to_delete, (list, tuple, numpy.ndarray)):
                id_to_delete = [id_to_delete]
            placeholders = ",".join(["%s"] * len(id_to_delete))
            sql = "DELETE FROM `ssis`.`college` WHERE `code` IN ({})".format(
                placeholders)
            # sql2 = " IN ({})".format(placeholders)
            cursor.execute(sql, tuple(id_to_delete))
            mysql.connection.commit()
            return True
        except Exception as e:
            return e
        
    # @classmethod
    def delete(self,code):    
        try:
            cursor = mysql.connection.cursor()
            sql = f"DELETE from `ssis`.`college` where code= {code}"
            cursor.execute(sql)
            mysql.connection.commit()
            return True
        except:
            return False


student_interface = Student()
ofcourse = Course()
college_interface = College()
