from django.db import models
from django.contrib.auth.models import User
import uuid
# Create your models here.
class BaseModel(models.Model):
    uid = models.UUIDField(default=uuid.uuid4,primary_key=True,editable=False)
    created_at = models.DateField(auto_now_add=True),
    updated_at = models.DateField(auto_now_add=True)

class Facility(BaseModel):
    facility_name = models.CharField(max_length=100)

    def __str__(self):
        return self.facility_name

class Hotel(BaseModel):
    hotel_name = models.CharField(max_length=100)
    description = models.TextField()
    hotel_price = models.IntegerField()
    facility = models.ManyToManyField(Facility)
    def __str__(self):
        return self.hotel_name

class HotelBooking(BaseModel):
    hotels = models.ForeignKey(Hotel,on_delete=models.CASCADE)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    booking_type=models.CharField(choices=(('Pre Paid','Pre Paid'),('Post Paid','Post Paid')), max_length=100)    


    