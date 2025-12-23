import paho.mqtt.client as mqtt
import mysql.connector
from datetime import datetime

# Database connection
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="iot_db"
)
cursor = db.cursor()

def on_message(client, userdata, msg):
    data = msg.payload.decode()
    appliance, status = data.split(",")

    time = datetime.now()

    query = """
    INSERT INTO appliance_status (appliance_name, status, updated_at)
    VALUES (%s, %s, %s)
    """
    cursor.execute(query, (appliance, status, time))
    db.commit()

    print(f"{appliance} turned {status}")

client = mqtt.Client()
client.on_message = on_message

client.connect("localhost", 1883, 60)
client.subscribe("home/appliance/control")

print("Subscriber running...")
client.loop_forever()
