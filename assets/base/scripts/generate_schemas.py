import json

INPUT_JSON  = "../lang/en_us/game.json"
OUTPUT_JSON = "game.schema.json"

PREDEFINED = {
    "$id": "https://raw.githubusercontent.com/FinalForEach/Cosmic-Reach-Localization/master/assets/base/lang/game.schema.json",
    "title": "Cosmic Reach language (game.json)",
    "description": "FinalForEach's Cosmic Reach game localization language schema for game.json",
    "additionalProperties": False
}

METADATA_OVERRIDE = {
    "type": "object",
    "description": "Special metadata property for the language",
    "additionalProperties": False,
    "properties": {
        "name": {
        "type": "string",
        "description": "The language's name shown in the language menu"
        },
        "fallbacks": {
        "type": "array",
        "items": {
            "type": "string"
        },
        "uniqueItems": True,
        "minItems": 0,
        "maxItems": 4,
        "description": "The language codes from which translations can be pulled from if missing keys in this file."
        }
    },
    "required": [
        "name"
    ]
}

def infer_schema(value):
    if isinstance(value, dict):
        props = {k: infer_schema(v) for k, v in value.items()}
        return {
            "type": "object",
            "properties": props,
            "minProperties": len(props)
        }
    if isinstance(value, list):
        return {
            "type": "array",
            "items": infer_schema(value[0]) if value else {}
        }
    if isinstance(value, bool):  return {"type": "boolean"}
    if isinstance(value, int):   return {"type": "integer"}
    if isinstance(value, float): return {"type": "number"}
    if value is None:            return {"type": "null"}
    return {"type": "string"}

def main():
    with open(INPUT_JSON) as f:
        data = json.load(f)

    schema = {
        "$schema": "https://json-schema.org/draft/2020-12/schema",
        **PREDEFINED,
        **infer_schema(data)
    }

    schema['properties']['metadata'] = METADATA_OVERRIDE

    with open(OUTPUT_JSON, "w") as f:
        json.dump(schema, f, indent=2)

if __name__ == "__main__":
    main()
