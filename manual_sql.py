from dash import dash_table, Dash, dcc, html, Input, Output, callback
import pandas as pd
import paho.mqtt.client as mqtt
import mysql.connector
import time, datetime
from datetime import date, timedelta
import threading
import plotly.graph_objects as go
import plotly_express as px
import setup

mydb = mysql.connector.connect(host=setup.host, user=setup.user, password=setup.password, database=setup.database, port=setup.port, buffered=True)
mycursor = mydb.cursor()

'''
mycursor.execute("DELETE FROM scan_event")
mycursor.execute("DELETE FROM employees")
mycursor.execute("DELETE FROM jobs")
mycursor.execute("TRUNCATE TABLE scan_event)
'''

'''
values = ("E1", "Location 2", "09:09:09 2024-09-22", None, "0:00:00", None, 0)
mycursor.execute("INSERT INTO " + setup.employee_table + " (EMPLOYEE_ID, STATION, START, STOP, DURATION, WARNINGS, BREAK_TIME) VALUES (%s, %s, %s, %s, %s, %s, %s)", values)
'''

'''
mycursor.execute("SELECT * FROM employees")
e = mycursor.fetchall()
print(e)
'''

mydb.commit()
mycursor.close()
mydb.close()
