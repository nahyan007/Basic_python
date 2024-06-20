# dictionary = a changeable, unordered collection of unique key:value pairs Fast because they use hashing, allow us to access a value quickly

capitals = {
    "usa" : "Washington DC",
    "bangladesh" :"dhaka",
    "china" : "beijing",
    "russia" : "moscow"
}

capitals.update({"germany": "berlin"})

# print(capitals.get("germany"))
# print(capitals.keys())
# print(capitals.values())
# print(capitals.items())

for keys, values in capitals.items():
    print(keys + " capital is " + values)