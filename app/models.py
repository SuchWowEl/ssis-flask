# from app import mysql


class Student:

    def __init__(self, mysql, username=None, password=None, email=None):
        self.mysql = mysql
        self.username = username
        self.password = password
        self.email = email

    def add(self):
        cursor = self.mysql.connection.cursor()

        sql = f"INSERT INTO users(username,user_password,email) \
                VALUES('{self.username}',md5('{self.password}'),'{self.email}')" 

        cursor.execute(sql)
        self.mysql.connection.commit()
        
    def update(self, column, newvalue, id):
        cursor = self.mysql.connection.cursor()
        
        # UPDATE `ssis`.`student` SET `firstname` = 'asda' WHERE (`id` = '2021-0001');
        sql = f"UPDATE `ssis`.`student` SET `{column}` = '{newvalue}' \
                WHERE (`id` = '{id}')" 

        cursor.execute(sql)
        self.mysql.connection.commit()
        
        
        
        

    # @classmethod
    def all(self):
        cursor = self.mysql.connection.cursor()

        sql = "SELECT * from student"
        cursor.execute(sql)
        result = cursor.fetchall()
        return result

    # @classmethod
    def delete(self,id):    
        try:
            cursor = self.mysql.connection.cursor()
            sql = f"DELETE from users where id= {id}"
            cursor.execute(sql)
            self.mysql.connection.commit()
            return True
        except:
            return False

        
