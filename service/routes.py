from flask import jsonify, request
from . import app
import json

@app.route('/', methods=['GET', 'POST', 'DELETE', 'PUT', 'HEAD', 'OPTIONS'])
@app.route('/<path:path>', methods=['GET', 'POST', 'DELETE', 'PUT', 'HEAD', 'OPTIONS'])
def index(path = None):
    rtn = {
        "path": path,
        "body": request.get_json(),
        "method": request.method,
        "form": None
    }
    if request.form:
        rtn["form"] = request.form
    if request.args:
        rtn["query"] = request.args

    rtn["headers"] = {}
    for k,v in request.headers.items():
        rtn["headers"][k] = v

    print(json.dumps(rtn, sort_keys=True, indent=2, separators=(',', ': ')))
    return jsonify(rtn)
