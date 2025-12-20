import mysql.connector

def getBDConnection():
    connection=mysql.connector.connect(
        host="localhost",
        port=3306,
        user="root",
        password="root",
        database="iot_data",
        use_pure=True
    )
    return connection