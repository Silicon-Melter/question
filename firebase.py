import firebase_admin
from firebase_admin import credentials, firestore

# init
cred = credentials.Certificate("serviceAccount.json")
firebase_admin.initialize_app(cred)

db = firestore.client()

ref = db.collection('historyBook').document(u'37815')

# 1.1add
ref.set({
    u'ชื่อหนังสือ': u'Harry Potter',
    u'รหัสหนังสือ': u'1234',
    u'วันที่ยืม': '19 Feb 2022 08:55:33 pm UTC+7',
    u'วันที่ต้องคืน': '20 Feb 2022 08:55:33 pm UTC+7',
    u'ระยะเวลาที่ยืม': 1,
    u'เรื่องย่อ': 'เป็นชุดนวนิยายแฟนตาซีจำนวนเจ็ดเล่ม',
})

# 1.2read
users_ref = db.collection(u'historyBook')
docs = users_ref.stream()

for doc in docs:
    print(f'{doc.id} => {doc.to_dict()}')

# 1.3update
field_updates = {
    u'วันที่ต้องคืน': '19 Feb 2022 08:55:33 pm UTC+7',
    u'ระยะเวลาที่ยืม': 0,
}
ref.update(field_updates)

# 1.4delete
field_updates = {
    u'เรื่องย่อ': firestore.DELETE_FIELD,
}
ref.update(field_updates)
