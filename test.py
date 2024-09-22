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

#values = ("E100", "Location 1", "09:09:09 2024-09-22", None, "0:00:00", None, None, 0)
#mycursor.execute("INSERT INTO " + setup.employee_table + " (EMPLOYEE_ID, STATION, START, STOP, DURATION, WARNINGS, CORRESPONDING_JOBS, BREAK_TIME) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)", values)
#mydb.commit()

#today_date = str(datetime.datetime.now().date())

mycursor.execute("SELECT * FROM employees")
e = mycursor.fetchall()
print(e)
'''
mycursor.execute("SELECT EMPLOYEE_ID FROM " + setup.employee_table + " WHERE STOP IS NULL AND STATION!=%s", ([setup.Location_name]))
employee_df = mycursor.fetchall()
print(employee_df)
'''
mycursor.close()
mydb.close()
