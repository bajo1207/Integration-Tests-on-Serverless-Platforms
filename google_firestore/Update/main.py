import json
from google.cloud import firestore

def update(request):
    data = request.get_json(force=True)
    if 'text' not in data:
        print("Validation Failed")
        raise Exception("Couldn't create the todo item.")   
    path = request.path.strip("/")
    print(path)
    if not path:
        print("Validation Failed")
        raise Exception("Couldn't get the todo item.")   
    db = firestore.Client()
    doc_ref = db.collection('collection').document(path)
    doc = doc_ref.get()
    if doc.exists:
        item = doc.to_dict()
        item.update(data)
        doc_ref.update(item)
        return json.dumps(item)
    else:
        return ('', 404)
 
    