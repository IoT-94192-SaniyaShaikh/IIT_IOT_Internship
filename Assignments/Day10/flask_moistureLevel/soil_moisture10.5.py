from flask import Flask, request, jsonify
import pymysql
import datetime
import paho.mqtt.publish as publish

app = Flask(__name__)

db = pymysql.connect(
    host="localhost",
    user="root",
    password="root", 
    database="smart_agriculture"
)

mqtt_broker = "localhost"
mqtt_topic = "alert/soil_moisture"
threshold = 30

@app.route('/moisture', methods=['POST'])
def store_moisture():
    data = request.json

    sensor_id = data['sensor_id']
    moisture_level = data['moisture_level']
    reading_time = datetime.datetime.now()

    cursor = db.cursor()

    query = "insert into soil_moisture(sensor_id, moisture_level, reading_time) values (%s, %s, %s)"
    cursor.execute(query, (sensor_id, moisture_level, reading_time))
    db.commit()

    if moisture_level < threshold:
        alert_msg = f"ALERT! Soil moisture low: {moisture_level}"
        publish.single(mqtt_topic, alert_msg, hostname=mqtt_broker)

    return jsonify({"message": "moisture data is stored"})

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
