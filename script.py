
import pyodbc

 Connection to SQL Server
conn = pyodbc.connect('DRIVER={SQL Server};'
                      'SERVER=your_server_name;'
                      'DATABASE=CupcakeDeliveryDB;'
                      'UID=your_username;'
                      'PWD=your_password')

cursor = conn.cursor()


