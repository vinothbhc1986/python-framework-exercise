from typing import Optional

from pydantic import BaseModel

# define custom validators using python's built-in assert statement
class Car(BaseModel):
    make: str
    year: int
    color: Optional[str] = None

car_data = {
    "make": "Ford",
    "year": 21,
}
car = Car(**car_data) # ** → unpacks a dictionary
#Take the keys in car_data and use them as the argument names when creating the Car object.
# car = Car(make="Ford", year=25)
# print(car)


numbers = [10, 20]  #* → unpacks a list/tuple
print(*numbers)
# print(10, 20)
