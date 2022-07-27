import json

# Read the json file.
res = json.load(open("sample.json"))

# Get user input of the keys to search.
key_array = [str(x) for x in input("Enter the keys separated by / :").split("/")]
value="res"
for key in key_array:
    value=value+"['"+key+"']"

# Print output
print(eval(value))
