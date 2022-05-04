from email.policy import default
from django.db import models

# Create your models here.

"""
create table app_userinfo(
    id bigint auto_increment primary key
    PostalCode int,
    Segment = varchar(32)
    ...
)
"""

class Address(models.Model):
    PostalCode = models.ImageField(default=0)
    Segment = models.CharField(max_length=32, default="null")
    Country = models.CharField(max_length=32, default="null")
    City = models.CharField(max_length=32, default="null")
    State = models.CharField(max_length=32, default="null")
    Region = models.CharField(max_length=32, default="null")



