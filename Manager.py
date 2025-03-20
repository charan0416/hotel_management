from os import remove

from Guest import *
from utility import *
from Room import *

class Manager :
    def __init__(self):
        self.guests = []
        self.rooms = 10

    def add_guest(self):
        name = input("enter the name")
        phone_number = int(input("enter phone number"))
        self.guests.append(name)

        print(f"new guest added :{name},{phone_number}")

    def list_guests(self):
        if len(self.guests) == 0:
            print("\nguest list is empty !")
            return
        else:
            for guests in self.guests:
                print(guests)

    def check_rooms(self):
        available_rooms = self.rooms - len(self.guests)
        # if len(self.guests) != 0:
        #     print("Rooms are available")
        if available_rooms == 0:
            print("Rooms are full")
        else:
            print(f"Only {len(self.guests)} is filled out of 10")

    def remove_guest(self):
        name = input("enter the name")
        for guests in self.guests:
            if guests == name:
                self.guests.remove(guests)
            print("guest removed successfully")

    def price(self):
        print("price of room is 5000")

    def food(self):
        food = input("enter the food name")
        print("food will be delivered in 15 min")













