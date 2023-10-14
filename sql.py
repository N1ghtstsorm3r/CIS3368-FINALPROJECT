"""  Christine Simon - 1840920
"""
import mysql.connector
from  mysql.connector import Error

#creating connection function
def create_con(hostname,uname,pwd,dbname):
    connection = None
    
    try:
        connection = mysql.connector.connect(
            host = hostname,
            user = uname,
            password = pwd,
            database = dbname #These are the four paramenters, it will be executed to connected to the 
            #Databse, this is your username and password
        )
        print("Connection is sucessful")
    except Error as e: #Throwing the try block and move passed the error
        print("connection failed with error: ", e)
    return connection

#We need an execution function  the top one is only connection
def execute_myquery(conn, query):
    cursor = conn.cursor()
    #Remember this is the handler so its going to get information from DB
    try:
        cursor.execute(query)
        conn.commit()
        #You need to comit because otherwise it doesnt work into the database
        print("Query successful")
    except Error as e:
        print("Error :", e)
        
    #We need the results back, so bring in your fetchall method
    
def execute_read_myquery(conn, query):
    cursor = conn.cursor(dictionary=True)
    row = None #tHIS Brings back the results
    try:
        cursor.execute(query)
        rows = cursor.fetchall()
        return rows
    #Now the information comes back in dictionary form
    except Error as e:
        print("Error is :",e)
#All information is accessed through class notes and prior homeworks
