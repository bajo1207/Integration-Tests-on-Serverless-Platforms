from google.cloud import firestore

def delete(request):
    path = request.path.strip("/")
    print(path)
    if not path:
        print("Validation Failed")
        raise Exception("Couldn't get the todo item.")   
    db = firestore.Client()
    db.collection('collection').document(path).delete()
    return '',200
    
   
