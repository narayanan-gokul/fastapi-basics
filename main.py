from fastapi import FastAPI
from enum import Enum
from pydantic import BaseModel


class Employee(BaseModel):
    name: str
    age: int
    department: str


class Coin(str, Enum):
    HEADS = "Heads"
    TAILS = "Tails"


class Rogue(BaseModel):
    name: str


app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/greeting/{name}")
async def greeting(name: str):
    return "Hello, {name}!".format(name=name)


@app.get("/coin/{toss}")
async def coin(toss: Coin, try_number: int = 0):
    if toss is Coin.HEADS:
        return "You win try {try_number}!".format(try_number=try_number)
    else:
        return "You lose :("


@app.post("/employee/create")
async def create_employee(employee: Employee, rogue: Rogue):
    return employee


@app.post("employee/check-age")
async def check_age_employee(employee: Employee, age: int, coin: Coin):
    return employee.age == age
