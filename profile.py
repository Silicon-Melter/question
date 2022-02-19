from unicodedata import name
import firebase_admin
from firebase_admin import credentials, firestore

# init
cred = credentials.Certificate("serviceAccount.json")
firebase_admin.initialize_app(cred)

db = firestore.client()

ref = db.collection('userData')

# 1.1add
id = input('ปร:')
teacher = input('ครูประจำชั้น:')
name = input('ชื่อ:')
surname = input('นามสกุล:')
classs = input('ห้อง:')
ref.document(id).set({
    u'ครูประจำชั้น': teacher,
    u'ชื่อ': name,
    u'นามสกุล': surname,
    u'ห้อง': classs,
})