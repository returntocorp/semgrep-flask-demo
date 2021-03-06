from flask import Flask, request, jsonify
from marshmallow import Schema, fields, ValidationError

app = Flask(__name__)


# --- ERROR HANDLERS ---

@app.errorhandler(ValidationError)
def handle_validation_error(err: ValidationError):
    return jsonify({"errors": err.normalized_messages()}), 400


# --- SCHEMATA ---

class DataSchema(Schema):
    data = fields.Str(required=True)


data_schema = DataSchema()

# --- ROUTES ---


@app.route('/', methods=['POST'])
def reflect():
    data = data_schema.load(data=request.get_json())
    return jsonify(data["data"])
