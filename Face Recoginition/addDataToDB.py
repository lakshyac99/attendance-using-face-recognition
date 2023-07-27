import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
from firebase_admin import storage

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred,{
    'databaseURL':"https://faceattendancerealtime-16863-default-rtdb.firebaseio.com/"
})


ref = db.reference('Students')
data = {
    "321654":
        {
            "id": 321654,
            "name": "Murtaza hassan",
            "major": "Robotics",
            "starting_year": 2017,
            "total_attendance": 6,
            "standing": "G",
            "year": 4,
            "last_attendance_time": "2023-07-27 00:54:34"
        },

    "852741":
        {
            "id": 852741,
            "name": "Emly Blend",
            "major": "Economics",
            "starting_year": 2018,
            "total_attendance": 12,
            "standing": "B",
            "year": 2,
            "last_attendance_time": "2023-07-27 00:54:34"
        },

    "956235":
        {
            "id": 956235,
            "name": "Lakshya Singh",
            "major": "Computer Science",
            "starting_year": 2023,
            "total_attendance": 7,
            "standing": "G",
            "year": 1,
            "last_attendance_time": "2023-07-27 00:54:34"
        },

    "963852":
        {
            "id": 963852,
            "name": "Elon Musk",
            "major": "Physics",
            "starting_year": 2020,
            "total_attendance": 7,
            "standing": "G",
            "year": 2,
            "last_attendance_time": "2023-07-27 00:54:34"
        },
}

for key,value in data.items():
    ref.child(key).set(value)