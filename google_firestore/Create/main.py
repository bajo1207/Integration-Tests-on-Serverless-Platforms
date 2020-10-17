import time
import uuid
import json
from google.cloud import firestore

def create(request):
    data = request.get_json(force=True)
    if 'text' not in data:
        print("Validation Failed")
        raise Exception("Couldn't create the todo item.")   
    timestamp = str(time.time())
    item = {
        'id': str(uuid.uuid1()),
        'text': data['text'],
        'checked': False,
        'createdAt': timestamp,
        'updatedAt': timestamp,
    }
    db = firestore.Client()
    doc_ref = db.collection('collection').document(item['id'])
    doc_ref.set(item)
    return json.dumps(item)