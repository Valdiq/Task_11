import json
import jsonschema

with open("request_schema.json") as f:
    REQUEST_SCHEMA = json.load(f)

def validate_request(data: dict) -> tuple:
    """
    Validate incoming request using JSON Schema.
    Returns:
        (bool, str or None)
        - bool: True jeśli poprawne, False jeśli niepoprawne
        - str: opis błędu (lub None, jeśli brak błędu)
    """
    try:
        jsonschema.validate(instance=data, schema=REQUEST_SCHEMA)
        return True, None
    except jsonschema.ValidationError as e:
        return False, f"Validation error: {e.message}"
    except jsonschema.SchemaError as e:
        return False, f"Schema error: {e.message}"