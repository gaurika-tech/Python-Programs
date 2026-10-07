import re
#using the string 
text = "Name: Gaurika! . Date : 07-10-2026. Course: B.Tech-M.tech CSE . Subject : python. @"

print("\n1. re.match() - Form Input & Username Validation")
if re.match(r"^\w+", text):
    print ("Valid Entry Start Found!")

username = "Gaurika" 
if re.match(r"[a-zA-Z_]{5,15}", username):
    print("Valid Username Format: ", username)   




print("\n2. re.search() - Specific Info Extraction")
date = re.search(r"\d{2}-\d{2}-\d{4}", text)
if date:
    print ("Date Found!", date.group())

if re.search(r"\.@", text):
    print("String correctly ends")  




print("\n3. re.findall() Examples")
courses = re.findall(r"(B\.Tech|M\.tech|CSE)", text)
print("Courses Found!", courses)

subjects = re.findall(r"python|Gaurika",text,re.IGNORECASE)
print("Matched Words: ", subjects)





print("\n4. re.sub() Replacing all matches")
replace = re.sub(r"[^a-zA-Z0-9\s]", "", text)
print("Replaced Text!", replace)

spaces = re.sub(r"\s+", "" , text)
print("Blank Spaces:", spaces)





print("\n5. re.split() Split the string")
symbols = re.split(r"[:!.\-\s]+", text)
print("Tokens:" ,symbols)

split_by_digits = re.split(r"\d+", text)
print("Split By Digits:" , split_by_digits)