from typing import Union
from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="mohib",
  database="attendance"
)
class ProductReview(BaseModel):
    id: int
    name: str
    attendance: int

app = FastAPI()

origins = [
    "http://localhost.tiangolo.com",
    "https://localhost.tiangolo.com",
    "http://localhost",
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Item(BaseModel):
    ID: int
    Name: str
    attendance: int
   


@app.post("/addattendance/")
async def create_item(item: Item):
    mycursor = mydb.cursor()
    sql = "Insert into attendance.students (ID,Nam,attendance) Values (%s,%s,%s)"
    val = (item.ID,item.Name,item.attendance)
    mycursor.execute(sql, val)
    mydb.commit()
    return item

@app.get("/showattendance/")
async def create_item()-> list[ProductReview]:
    mycursor = mydb.cursor()
    sql = "Select * from students;"
    mycursor.execute(sql)
    reviews = await ProductReview
    return reviews
    
    # mydb.commit()
    return 