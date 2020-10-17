import json
from google.cloud import firestore

def list(request):
    db = firestore.Client()
    doc_ref = db.collection('collection')
    docs = doc_ref.stream()
    items = []
    for doc in docs:
        items.append(doc.to_dict())
    return json.dumps(items)