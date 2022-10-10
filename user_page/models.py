from django.db import models
import random
import string
from django.contrib.auth.models import User
from sqlalchemy import ForeignKey, false

"""class Representatives(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    Club = models.ForeignKey('Club', null = True, blank = True, on_delete=models.CASCADE)
    

    def __str__(self):
        return self.first_name + ' ' + self.last_name"""


class Student(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    Club = models.ForeignKey('Club', null=True, blank=True, on_delete=models.CASCADE )

    # Unique password and ID added by Radiela
    id_number = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    credits = models.PositiveIntegerField(null=False, default=0)

    class Type(models.TextChoices):
        yes = 'yes'
        no = 'no'

    in_club = models.CharField(max_length=5, choices=Type.choices, default="no")

    def __str__(self):
        return self.first_name + ' ' + self.last_name


# Remove user details, added by Radiela
class RemoveUserDetails(models.Model):
    choose_user = models.ForeignKey(Student, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.choose_user)


# Remove staff details, added by Radiela
class RemoveStaffDetails(models.Model):
    choose_member = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.choose_member)


class Club(models.Model):
    name = models.CharField('Club name', max_length = 30)
    address = models.CharField('Address: ', max_length = 50)
    address2 = models.CharField('Address 2 (Optional): ', max_length = 50, default='', blank = True)
    city = models.CharField('City: ', max_length = 30, default='')
    postcode = models.CharField('Postcode: ', max_length = 7, default='')
    contact_number = models.CharField(max_length=20)
    landline_number = models.CharField(max_length=20, null = True, blank = True)
    description = models.TextField(blank = True)

    rep_name = models.CharField(max_length=20, default="none")  # rep details placed inside Club class, added by Radiela
    rep_email = models.EmailField(default="none")

    def __str__(self):
        return self.name


# Remove club details, added by Radiela
class RemoveClubDetails(models.Model):
    choose_club = models.ForeignKey(Club, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.choose_club)


# Create a model for uploading film details added by Radiela
class FilmDetails(models.Model):

    title = models.CharField(max_length=200)
    img = models.ImageField(upload_to="media")
    age_rating = models.CharField(max_length=10)
    duration = models.CharField(max_length=10)
    description = models.TextField()

    class Meta:
        db_table = "Movies"

    def __str__(self):
        return self.title


# Remove movie details, added by Radiela
class RemoveMovieDetails(models.Model):
    choose_movie = models.ForeignKey(FilmDetails, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.choose_movie)


# Create a model for uploading Upcoming film details added by Radiela
class UpcomingFilmDetails(models.Model):

    title = models.CharField(max_length=200)
    img = models.ImageField(upload_to="media")
    age_rating = models.CharField(max_length=10)
    duration = models.CharField(max_length=10)
    description = models.TextField()

    class Meta:
        db_table = "Upcoming_Movies"

    def __str__(self):
        return self.title


# Remove an upcoming movie, added by Radiela
class RemoveUpcomingDetails(models.Model):
    choose_item = models.ForeignKey(UpcomingFilmDetails, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.choose_item)


# Create a model for uploading showing details added by Radiela
class ShowingDetails(models.Model):

    date = models.DateField(help_text="Example: 2022-01-01")
    time = models.TimeField(auto_now=False, auto_now_add=False, help_text="Example: 10:30")
    Films = models.ForeignKey(FilmDetails, blank=False, null=True, on_delete=models.CASCADE)

    class Meta:
        db_table = "Showings"
    
    def __str__(self):
        return str(self.Films.title) + " " + str(self.date) + " " + str(self.time)


# Remove showing details, added by Radiela
class RemoveShowingDetails(models.Model):
    choose_showing = models.ForeignKey(ShowingDetails, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.choose_showing)


# Create a model for uploading screen details added by Radiela
class ScreenDetails(models.Model):

    seats_available = models.PositiveIntegerField()
    Showings =models.ForeignKey(ShowingDetails, blank=False, null=False, on_delete=models.CASCADE)

    class Type(models.TextChoices):
        screen1 = '1', '2D'
        screen2 = '2', '3D'
    
    screen_type = models.CharField(max_length=2, choices=Type.choices, default=Type.screen1)


    class Meta:
        db_table = "Screens"

    def __str__(self):
        return str(self.Showings) + " " + str(self.screen_type)


# Remove screen details, added by Radiela
class RemoveScreenDetails(models.Model):
    choose_screen = models.ForeignKey(ScreenDetails, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.choose_screen)


# Order details added by Radiela
class OrderDetails(models.Model):

    title = models.CharField(max_length=20, null=True)
    date = models.DateField(help_text="Example: 2022-01-01", null=True)
    time = models.TimeField(auto_now=False, auto_now_add=False, help_text="Example: 10:30", null=True)
    screen_type = models.CharField(max_length=5, default="2D")

    screen = models.ForeignKey(ScreenDetails, blank=False, null=True, on_delete=models.CASCADE)
    selected_seats = models.PositiveIntegerField(default=1, null=False)
    price = models.PositiveBigIntegerField(default=3)

    class Meta:
        db_table = "Orders"
    
    def __str__(self):
        return str(self.id)


# Remove an intem from the shopping cart, added by Radiela
class RemoveOrderDetails(models.Model):
    choose_item = models.ForeignKey(OrderDetails, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.id) + " " + str(self.choose_item)


# Model for showing passed payments, added by Radiela
class PaidOrderDetails(models.Model):
    username = models.CharField(max_length=8)
    date = models.DateField(null=True)
    price = models.FloatField(default=3)

    class Meta:
        db_table = "Payments"

    def __str__(self):
        return self.username 
        





    

        


