from utils.dbconnection import getBDConnection
#to execute create,update,and delete query

def executequery(query):
    # create connection with mysql server
    connection=getBDConnection()
    #create cursor to execute a query
    cursor=connection.cursor()
    # execute query eith cursor
    cursor.execute(query)
    #commite your change to mysql server
    connection.commit()
    #close cursor
    cursor.close()
    #connection close
    connection.close()