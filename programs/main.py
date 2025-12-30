# CRUD - operation
# Data store - DB,FILE,LIST

# REST API - MVC
# Get- To display the records
# POST - THis is to create/add new record
# Put - This is to update hole records(Ex - Name,Email,Ph,Add)
# PATCH - This is to update a single entity (Ex- Name or Email or PH)
# DELETE - This is to delete the records

from fastapi import FastAPI
import json

app = FastAPI()

@app.get("/Home")
def Home():
    return {"Name":"FAst API"}

@app.get("/")
def dashboard():
    return{"Dashboard":" This is Dashboard of the API"}

DATA_FILE = "data.json"

# reading the file
def read_file():
    with open(DATA_FILE,'r') as f:
        return json.load(f)
    
# Writting into the file

def write_file(data):
    with open(DATA_FILE,'w') as f:
        return json.dump(data,f)
    
# display all records
@app.get("/records")
def get_all_records():
    print(read_file())
    return read_file()

# Create New Records
@app.post("/newuser")
def add_user(user_data:dict):
    data = read_file()
    
    data.append(user_data)
    print(data)
    write_file(data)

    return data

# display Individual record
@app.get("/records/{index}")
def single_record(index:int):
    data = read_file()
    print(data[index])
    return data[index]





# MVC -

# M - model
# V - View
# C - Controller
# DB - MongoDb


# Backend  
# UUID
# Session memory 
# cookies

# max_age = 
# Request, Respone,HTTPException



# JWT - JSon Web Token
from pymongo import MongoClient

client = MongoClient("mongodb+srv://krabhinit60_db_user:qR95NzF5qRw54bfB@cluster0.pnzoxlu.mongodb.net/")
db = client["auth_system"]

user_auth =db["Emp"]



user_auth.find_one({"email":email})
user_auth.insert(
    {
        "name":name,
        "email":email
    }
)