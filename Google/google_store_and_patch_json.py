import json
import collections
# Very different problem than I expected and very broad, no help from the interviewer on what exactly to implement - Position: Senior SDE Google Cloud:

# You have a backend system that stores all versions of a JSON object. 
# You need to reduce the amount of data stored, how would you design the API.
# I assumed they wanted to write a function to do a JSON diff of current state vs new state 
# so we only store the diff. Had no feedback whatsoever from the interviewer while working on it, so I have no idea what they expected.

# Ended up creating a function that returns a diff give two json objects and that's all I managed to do with the time I had. Still waiting to hear back if its a pass or not.


database = collections.defaultdict(int)  #database stores 1-{json}
#so 1 version will store the original json
#all subsequent versions will be diffs
database[1] ='{"name": "John", "age": 30, "city": "New York"}'  #original json is stored here 

def obj_diff(org , cur):
    #this will calcuate the diif
    if org == cur:
        return {}
    
    if org is None and cur is None:
        return [org , cur]
    
    if not isinstance(org , (dict , list)) or not isinstance(org , (dict , list)):
        return [org , cur]
    
    if isinstance(org, list) != isinstance(cur, list):
        return [org, cur]
    
    ret_obj = {}
    
    for key in cur:
        if key not in org:
            #this is a newly added filed
            ret_obj[key]=cur[key]
        elif key in org:
            #this key is present 
            #caluclate the difference
            diff = obj_diff(org[key] , cur[key])
            if diff:
                ret_obj[key] = diff
    
    return ret_obj

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
            
            

json_str1 = '{"name": "John", "age": {"age1" : "33"}, "city": "New York"}'
json_str2 = '{"name": "John", "age": 35, "city": "Los Angeles", "pincode": "3405"}'

# Assuming you have the diff calculated somewhere
diff = obj_diff(json.loads(json_str1), json.loads(json_str2))

# Now, apply the diff to get the updated JSON
updated_json = apply_diff(json.loads(json_str1), diff)
print(json.dumps(updated_json, indent=4))