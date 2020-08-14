import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

# creamos la credencial desde la credencial default
credential = credentials.ApplicationDefault()
firebase_admin.initialize_app(credential)
# creamos la instancia de cliente de firestore
db = firestore.client()

def get_users():
    return db.collection('users').get()


def get_todos(user_id):
    return db.collection('users').document(user_id).collection('todos').get()