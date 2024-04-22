import json

def apply_diff(base_json, diff):
    """
    Apply the given diff to the base JSON object.
    
    Args:
    - base_json: The base JSON object to which the diff will be applied.
    - diff: The JSON diff to apply.
    
    Returns:
    - updated_json: The JSON object after applying the diff.
    """
    if not diff:
        return base_json
    
    if not base_json:
        base_json = {}
        
    for key, value in diff.items():
        if isinstance(value, dict):
            if key not in base_json or not isinstance(base_json[key], dict):
                base_json[key] = {}
            base_json[key] = apply_diff(base_json[key], value)
        elif isinstance(value, list):
            if key not in base_json or not isinstance(base_json[key], list):
                base_json[key] = []
            base_json[key] = apply_diff(base_json[key], value)
        else:
            base_json[key] = value
    
    return base_json

# Example usage
json_str1 = '{"name": "John", "age": 30, "city": "New York"}'
json_str2 = '{"name": "John", "age": 35, "city": "Los Angeles", "pincode": "3405"}'

# Assuming you have the diff calculated somewhere
diff = obj_diff(json.loads(json_str1), json.loads(json_str2))

# Now, apply the diff to get the updated JSON
updated_json = apply_diff(json.loads(json_str1), diff)
print(json.dumps(updated_json, indent=4))