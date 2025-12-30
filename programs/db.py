# from pymongo import MongoClient

# client = MongoClient("mongodb+srv://krabhinit60_db_user:qR95NzF5qRw54bfB@cluster0.pnzoxlu.mongodb.net/") # connection to DB
# db = client["auth_system"] # DB - Schema 

# user_auth =db["Emp"] # DB Collection (Table)

# user_auth.insert_one(   
#     {
#         "name":"alex",
#         "email":"alex@gmail.com",
#         "Phone":1111
#     }
# )

# print(user_auth.find_one({"name":'Abhinit'}))

# # Protect Routes
# # JWT
# # Cookies


# name = [
#     {"name":"Abhinit"},
#     {"name":"Alex"}
# ]

# name=(
#     {"name":"Abhinit"},
#     {"name":"Alex"}
# )

# name={

#     {"name":"Abhinit"},
    
# }

# class User:
  
#     def __init__(self,id,name,email,phone):
#         self.name:str = name
#         self.id: int=id
#         self.email:str = email
#         self.phone :int= phone

#     def printtt():
#         print
        


# {"id":1}: {"name":"monit", "hobby": {"cricket", "vollyball"}, "email": "m@gmail.com"}

# {
#     "id":1

# }
# name = {"ID":{"name":"monit", "hobby": {"cricket", "vollyball"}, "email": "m@gmail.com"}}
# print(dict(name["ID"].get))



name=[
  {"001": {
    "name": "John smith",
    "email": "js@gmail.com",
    "married": False,
    "weight": 80.0,
    "allergy": [
      "nuts",1
    ], # this can be accessed only via List Index/array
    "phone": "1234567890",
    "dob": "1992-12-21",
    "linkedin_url": "https://linkedin.com/js",
    "emergency_contact": 0,
    "calculated_age": 33,

    "add":{"India": "Pune"} # this can be found via Keys and Values
    
        },},
  {"002": {
    "name": "Merry john",
    "email": "merry@hdfc.com",
    "married": True,
    "weight": 60.0,
    "allergy": [
      "dogs"
    ],
    "phone": "9876543210",
    "dob": "1992-12-21",
    "linkedin_url": "https://linkedin.com/merry_me",
    "emergency_contact": 911,
    "calculated_age": 33
  }}


]

# name=[
#   {"id":1},{"id":2}
# ]


print(name[0]) # this will print the values of 1st index =
print(name["001"]) # 
print(name[0].keys())
print(name[0].values())
print(name[0]["email"])
print(name[0]["allergy"])
print(name[0]["allergy"][0]) 
print(len(name[0]["allergy"]))
print(name[0]["001"]["add"]["India"])