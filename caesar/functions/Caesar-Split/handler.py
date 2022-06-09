import json

from .cloud_function import cloud_function


# Wrapper for OpenFaaS
def handle(event):
    req_json = json.loads(event)
    print("handler.py")
    print(req_json)
    return cloud_function(req_json)
