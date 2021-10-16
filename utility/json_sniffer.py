def sniffer(source: dict) -> dict:
    """
    Sniffs schema of given source dictionary corresponding to json

    The "source" is expected to have an attribute key of "message" and
    all attributes within this key are captured. All attributes are
    padded with "tag" and "description" keys, all properties set to
    "required":false and keys with values "string", "integer", "boolean"
    "array of strings" and "dict" mapped to "string", "integer", "boolean"
    "enum" and "array" respectively

    """
    # extracts the message attributes
    message = source["message"]

    properties = {}  # holds the sniffed schema

    for key in message.keys():
        item = message[key]
        data = {}
        if type(item) == int:
            data["type"] = "integer"
        elif type(item) == str:
            data["type"] = "string"
        elif type(item) == bool:
            data["type"] = "boolean"
        elif type(item) == dict:
            data["type"] = "array"
        else:
            data["type"] = "enum"

        # pad with tag and description key
        data["tag"] = ""
        data["description"] = ""

        # set property "required" false
        data["required"] = False

        properties[key] = data
    return properties
