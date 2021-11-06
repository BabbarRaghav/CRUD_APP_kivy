from kivy.lang import Builder
from kivy.core.window import Window
from kivymd.app import MDApp
import MySQLdb
from kivymd.toast import toast

#set size of Window
Window.size=(400,600)

#connect MySQL
conn = MySQLdb.connect(host="localhost", port=3306, user="root", passwd="", database="crud")
#create database
def db_create_db(conn):
    mycursor = conn.cursor()
    mycursor.execute("CREATE DATABASE IF NOT EXISTS crud")

#create table
def db_create_table(conn):
    db_create_db(conn)
    mycursor = conn.cursor()
    query = "CREATE TABLE IF NOT EXISTS crud_table (" \
          "ID INT AUTO_INCREMENT PRIMARY KEY, " \
          "Name VARCHAR(255) NOT NULL, " \
          "Age INT NOT NULL)"
    mycursor.execute(query)
    
# invoking the function
db_create_table(conn)

#main app
class MainApp(MDApp):
    def __init__(self, **kwargs):
        super(MainApp, self).__init__(**kwargs)

    def build(self):
        self.screen=Builder.load_file('crud.kv')
        #mycursor = conn.cursor()
        #query = "SELECT * FROM crud_table"
        #mycursor.execute(query)
        #row={}
        #row = mycursor.fetchall()
        #print(row)
        #self.data_tables = MDDataTable(
        #    size_hint=(0.8, 0.3),
        #    pos_hint={'center_x': 0.5, 'center_y': 0.3},
        #    column_data=[
        #        ("No.", dp(30)),
        #        ("Name", dp(30)),
        #        ("Age", dp(30)),
        #    ],
        #    row_data=row
        #)
        #self.screen.add_widget(self.data_tables)
        return self.screen

    #insert data
    def insert_data(self):
        name=self.screen.ids.name.text
        age=self.screen.ids.age.text
        mycursor = conn.cursor()
        query = "INSERT INTO crud_table (name, age) VALUES (%s, %s)"
        val = (name, age)
        mycursor.execute(query, val)
        conn.commit()
        toast("Created")
        return mycursor.lastrowid

    #read data
    def read_data(self):
        mycursor = conn.cursor()
        query = "SELECT * FROM crud_table"
        mycursor.execute(query)
        row={}
        row = mycursor.fetchall()
        print(row)

    #update data
    def update_data(self):
        name=self.screen.ids.name.text
        age=self.screen.ids.age.text
        mycursor = conn.cursor()
        query = "UPDATE crud_table set name=%s, age=%s where name=%s"
        val = (name, age, name)
        mycursor.execute(query, val)
        conn.commit()
        toast("Updated")

    #delete data
    def delete_data(self):
        name=self.screen.ids.name.text
        age=self.screen.ids.age.text
        mycursor = conn.cursor()
        query = "DELETE from crud_table where name=%s and age=%s"
        val= (name, age)
        mycursor.execute(query, val)
        conn.commit()
        toast("Deleted")

#run the app    
MainApp().run()