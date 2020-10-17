import json
from google.cloud import firestore

def get(request):
    path = request.path.strip("/")
    print(path)
    if not path:
        print("Validation Failed")
        raise Exception("Couldn't get the todo item.")   
    db = firestore.Client()
    doc_ref = db.collection('collection').document(path)
    doc = doc_ref.get()
    if doc.exists:
        return json.dumps(doc.to_dict())
    else:
        return ('', 404)
 
    