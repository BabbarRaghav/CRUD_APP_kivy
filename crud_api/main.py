from kivy.lang import Builder
from kivy.core.window import Window
from kivymd.app import MDApp
from kivymd.toast import toast
import pyrebase

#set firebase
FirebaseConfig={
    'apiKey': "AIzaSyDHD31roBM5N_03k4hTbqrq6t3EHm3RqxA",
    'authDomain': "crudapi-4de08.firebaseapp.com",
    'projectId': "crudapi-4de08",
    'storageBucket': "crudapi-4de08.appspot.com",
    'messagingSenderId': "448610712037",
    'appId': "1:448610712037:web:b61a5eacd481e8ea51d70c",
    'measurementId': "G-1VWVMGLBYK",
    'databaseURL': "https://crudapi-4de08-default-rtdb.firebaseio.com/"
}
firebase=pyrebase.initialize_app(FirebaseConfig)
db=firebase.database()

#set size of Window
Window.size=(400,600)

#main app
class MainApp(MDApp):
    def build(self):
        self.screen=Builder.load_file('crud.kv')
        return self.screen

    def insert(self):
        name=self.screen.ids.name.text
        age=self.screen.ids.age.text
        data={'name':name, 'age':age}
        db.child(name).set(data)
        toast("Created")

    def update(self):
        name=self.screen.ids.name.text
        age=self.screen.ids.age.text
        db.child(name).update({'age':age})
        toast("Updated")

    def read(self):
        user=db.get()
        for i in user.each():
            print(i.val())

    def delete(self):
        name=self.screen.ids.name.text
        db.child(name).remove()
        toast("Deleted")

#run the app    
MainApp().run()
