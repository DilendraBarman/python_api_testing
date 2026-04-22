from jsonschema import validate, ValidationError

def validate_json_schema(data, schema):
    try:
        validate(instance=data, schema=schema)
        return True
    except ValidationError as e:
        raise AssertionError(f"JSON Schema validation error: {e}")
