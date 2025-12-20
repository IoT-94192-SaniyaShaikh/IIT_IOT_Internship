from flask import Flask, request
from datetime import datetime
from utils.executequery import executequery
from utils.executeselect import executeselectquery

server = Flask(__name__)

@server.get('/')
def homepage():
    return "<html><body><h1>This is home page</h1></body></html>"

@server.route('/soil_moisture', methods=['POST'])
def create_soil_moisture ():

    sensor_id= request.get_json().get('sensor_id')
    moisture_level= request.get_json().get('moisture_level')
    date_time= datetime.now()
    query = f"insert into soil_moisture  values({sensor_id}, '{moisture_level}', '{date_time }');"
 
    executequery(query=query)

    return "soil_moisture  is added successfully"

@server.route('/soil_moisture', methods=['GET'])
def retrieve_soil_moisture():
    query = "SELECT * FROM soil_moisture;"
    data = executeselectquery(query=query)

    formatted_data = []
    for row in data:
        sensor_id = row[0]
        moisture_level = row[1]
        date_time = row[2].strftime("%Y-%m-%d %H:%M:%S")

        formatted_data.append((sensor_id, moisture_level, date_time))

    return f"Soil moisture: {formatted_data}"


@server.route('/soil_moisture', methods=['PUT'])
def update_soil_moisture ():
   
    sensor_id = request.get_json().get('sensor_id')
    moisture_level = request.get_json().get('moisture_level')
    query = f"update soil_moisture  SET moisture_level  = '{moisture_level}' where sensor_id = '{sensor_id}';"

    executequery(query=query)

    return "moisture_level  is updated successfully"

@server.route('/soil_moisture', methods=['DELETE'])
def delete_soil_moisture ():
    
    sensor_id = request.get_json().get('sensor_id')

    query = f"delete from soil_moisture  where sensor_id = '{sensor_id}';"
    executequery(query=query)

    return "sensor id  is deleted successfully"


@server.post('/soil_moisture/high_moisture_level')
def get_high_moisture():

    data = request.get_json()

    if not data or 'moisture_level' not in data:
        return {"error": "moisture_level is required"}, 400

    moisture_level = data['moisture_level']

   
    query = f"""
        SELECT sensor_id, moisture_level, date_time
        FROM soil_moisture
        WHERE moisture_level > {moisture_level}
    """

    result = executeselectquery(query=query)

    formatted_data = []
    for row in result:
         sensor_id=row[0]
         moisture_level= row[1]
         date_time= row[2].strftime("%Y-%m-%d %H:%M:%S")
         formatted_data.append((sensor_id, moisture_level, date_time))
        

    return f"high_moisture_readings: {formatted_data}"
    

if __name__ == '__main__':
    server.run(host='0.0.0.0', port=4000, debug=True)