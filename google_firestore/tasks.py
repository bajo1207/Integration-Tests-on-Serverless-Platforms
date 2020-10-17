from invoke import task
from threading import Thread
import os
@task
def start(c):
    createtodo = c.run('functions-framework --target create --source Create/main.py --debug --port 8000', asynchronous=True)
    listtodo = c.run('functions-framework --target list --source List/main.py --debug --port 8001', asynchronous=True)
    gettodo = c.run('functions-framework --target get --source Get/main.py --debug --port 8002', asynchronous=True)
    deletetodo = c.run('functions-framework --target delete --source Delete/main.py --debug --port 8003', asynchronous=True)
    updatetodo = c.run('functions-framework --target update --source Update/main.py --debug --port 8004', asynchronous=True)
    createtodo.join()
    listtodo.join()
    gettodo.join()
    deletetodo.join()
    updatetodo.join()