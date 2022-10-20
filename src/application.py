from flask import Flask, Response, request
from datetime import datetime
import json
from contact_resource import ContactResource
from flask_cors import CORS

# Create the Flask application object.
app = Flask(__name__,
            static_url_path='/',
            static_folder='static/class-ui/',
            template_folder='web/templates')

CORS(app)


@app.get("/api/health")
def get_health():
    t = str(datetime.now())
    msg = {
        "name": "Codeplay-Contact-Service",
        "health": "Good",
        "at time": t
    }

    # DFF TODO Explain status codes, content type, ... ...
    result = Response(json.dumps(msg), status=200, content_type="application/json")

    return result


@app.route("/contact/<id>/email", methods=["GET", "PUT", "POST", "DELETE"])
def get_email_by_id(id):
    if request.method == "GET":
        result = ContactResource.get_email_by_id(id)
        if result:
            return Response(json.dumps(result), status=200, content_type="application/json")
        else:
            return Response("Not found", status=404, content_type="application/json")
    elif request.method == "PUT":
        email = request.get_json()["email"]
        result = ContactResource.update_email_by_id(id, email)
        return Response("OK", status=200, content_type="application/json")
    elif request.method == "POST":
        email = request.get_json()["email"]
        try:
            result = ContactResource.insert_email_by_id(id, email)
            return Response("OK", status=200, content_type="application/json")
        except Exception as e:
            return Response("Error", status=500, content_type="application/json")
    elif request.method == "DELETE":
        result = ContactResource.delete_email_by_id(id)
        return Response("OK", status=200, content_type="application/json")
    
@app.route("/contact/<id>/address", methods=["GET", "PUT", "POST", "DELETE"])
def get_address_by_id(id):
    if request.method == "GET":
        result = ContactResource.get_address_by_id(id)
        if result:
            return Response(json.dumps(result), status=200, content_type="application/json")
        else:
            return Response("Not found", status=404, content_type="application/json")
    elif request.method == "PUT":
        address = request.get_json()["address"]
        result = ContactResource.update_address_by_id(id, address)
        return Response("OK", status=200, content_type="application/json")
    elif request.method == "POST":
        address = request.get_json()["address"]
        try:
            result = ContactResource.insert_address_by_id(id, address)
            return Response("OK", status=200, content_type="application/json")
        except Exception as e:
            return Response("Error", status=500, content_type="application/json")
    elif request.method == "DELETE":
        result = ContactResource.delete_address_by_id(id)
        return Response("OK", status=200, content_type="application/json")

@app.route("/contact/<id>/phone", methods=["GET", "PUT", "POST", "DELETE"])
def get_phone_by_id(id):
    if request.method == "GET":
        result = ContactResource.get_phone_by_id(id)
        if result:
            return Response(json.dumps(result), status=200, content_type="application/json")
        else:
            return Response("Not found", status=404, content_type="application/json")
    elif request.method == "PUT":
        phone = request.get_json()["phone"]
        result = ContactResource.update_phone_by_id(id, phone)
        return Response("OK", status=200, content_type="application/json")
    elif request.method == "POST":
        phone = request.get_json()["phone"]
        try:
            result = ContactResource.insert_phone_by_id(id, phone)
            return Response("OK", status=200, content_type="application/json")
        except Exception as e:
            return Response("Error", status=500, content_type="application/json")
    elif request.method == "DELETE":
        result = ContactResource.delete_phone_by_id(id)
        return Response("OK", status=200, content_type="application/json")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5011)

