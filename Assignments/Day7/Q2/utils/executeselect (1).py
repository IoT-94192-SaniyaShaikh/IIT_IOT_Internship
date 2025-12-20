from utils.dbconnection import getBDConnection

# to execute select query
def executeselectquery(query):
    # Change this line:
    connection = getBDConnection()  # <--- Added () here
    
    # Now connection is an object, and .cursor() will work
    cursor = connection.cursor()
    
    # execute query with cursor
    cursor.execute(query)
    
    # fetch data from cursor
    data = cursor.fetchall()
    
    # close the cursor and connection
    cursor.close()
    connection.close()
    
    return data