from app import mysql


class Student:

    # def __init__(self, mysql, username=None, password=None, email=None):
    #     mysql = mysql
    #     self.username = username
    #     self.password = password
    #     self.email = email
    
    # student_info is list
    def add(self, student_info):
        cursor = mysql.connection.cursor()

        sql = f"INSERT INTO `student` (`id`, `firstname`, `lastname`, `course`, `year`, `gender`) \
       VALUES ('{student_info[0]}', '{student_info[1]}', '{student_info[2]}', '{student_info[3]}', \
               '{student_info[4]}', '{student_info[5]}')"

        cursor.execute(sql)
        mysql.connection.commit()
        
    def update(self, column, newvalue, id):
        cursor = mysql.connection.cursor()
        
        # UPDATE `ssis`.`student` SET `firstname` = 'asda' WHERE (`id` = '2021-0001');
        sql = f"UPDATE `ssis`.`student` SET `{column}` = '{newvalue}' \
                WHERE (`id` = '{id}')" 

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
