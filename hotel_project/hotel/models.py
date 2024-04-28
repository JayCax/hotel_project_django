from django.db import models
from datetime import time

class Room(models.Model):
    room_number = models.IntegerField(unique=True)
    capacity = models.IntegerField()
    # Add more fields as needed
    room_designation = models.TextField(default="single")
    floor = models.IntegerField()

    def __str__(self):
        return (f"Room {self.room_number} on floor {self.floor} is a {self.room_designation} with a "
                f"capacity of {self.capacity} guests")


class Client(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    # Add more fields as needed
    start_of_stay = models.DateField()
    duration_of_stay = models.IntegerField(default=1)
    check_in_time = models.TimeField(default=time(4))


    def __str__(self):
        return f"{self.name} starts their stay at {self.start_of_stay} for {self.duration_of_stay} nights"
