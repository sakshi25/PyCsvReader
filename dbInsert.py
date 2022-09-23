import psycopg2
from uuid import uuid4

from psycopg2._psycopg import cursor
from psycopg2.extensions import AsIs

class PostgreSQlWrapper:

    def __init__(self):
        '''  '''
        self.cursor = None
        self.conn = None

    def createConnection(self):
        conn = psycopg2.connect(database="postgres",
                                user='postgres', password='25',
                                host='127.0.0.1', port='5432'
                                )
        conn.autocommit = True
        self.cursor = conn.cursor()


    def createTable(self):
        sql = '''CREATE TABLE DETAILS2(employee_id char(20) NOT NULL,\
        employee_name char(20),\
        employee_email varchar(30), employee_salary char(20));'''

        self.cursor.execute(sql)

    def copyTabletoDB(self,list_of_dict):

        sql2 = '''INSERT INTO DETAILS(employee_id,employee_name,\
        employee_email,employee_salary)
        FROM '"C:\\Users\\saabhatn\\AppData\\Local\\Temp\\EmployeeDetails.csv"' DELIMITER ',' CSV HEADER;'''
        values =[]
        for employee_dict in list_of_dict:
            values.append(tuple(employee_dict.values()))

        sql = """insert into DETAILS2 (employee_id,employee_name,employee_email,employee_salary) values (%s,%s,%s,%s)"""
        result = cursor.executemany(sql, values)
        print(cursor.rowcount, "Record inserted successfully into mobile table")

    def pritnAllDetailsFromDB(self):
        sql3 = '''select * from details;'''
        self.cursor.execute(sql3)
        for i in self.cursor.fetchall():
            print(i)

    def closeConnetion(self):
        self.conn.commit()
        self.conn.close()

