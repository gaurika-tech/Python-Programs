def add_entry(d):
    d["city"] = "Lucknow"

def reassign_dict(d):
    d={"name": "Gaurika", "age" : 18}

 my_dict = {"name" : "GS", "semester" : "II"}

print("Before Function Call : ", my_dict)

add_entry(my_dict)

print("After Function Call, (addinhg a new key-value pair): ", my_dict)

reassign_dict(my_dict)

print("After Function Call, (reassigning the dictionary variable): ", my_dict)