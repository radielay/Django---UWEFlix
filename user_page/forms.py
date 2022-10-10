from dataclasses import fields
from email import message
import email
from email.policy import default
from django import forms
from .models import *
from creditcards.forms import *
from django.conf import settings
from django.core.mail import send_mail
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm



class ClubForm(forms.ModelForm):
    class Meta: 
        model = Club
        fields = ['name', 'address', 'address2', 'city', 'postcode' ,'contact_number', 'landline_number' , 'rep_name', 'rep_email']

    def get_info(self):    # Method that returns formatted information, added by Radiela
        
        # Cleaned data
        cl_data = super().clean()
        rep_name = cl_data.get('rep_name')
        club_name = cl_data.get('name')
        email = cl_data.get('rep_email')

        msg = "Dear " + rep_name + ", your club " + club_name + " has been added to UWEFlix!"
        msg += "\n"
        msg += "You and all other club members are eligible for a discount of 20%."

        return email, msg
        
    # Send email function, added by Radiela
    def send(self):

        email, msg = self.get_info()

        send_mail(                  # Sensitive credentials are handled in .env file
            subject='Welcome to UWEFlix',    
            message=msg,
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[email]
        )


# Remove club, added by Radiela
class RemoveClubForm(forms.ModelForm):
    class Meta:
        model = RemoveClubDetails
        fields=['choose_club']
        

# Remove staff form, added by Radiela
class RemoveStaffForm(forms.ModelForm):
    class Meta:
        model = RemoveStaffDetails
        fields = ['choose_member']


class StudForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ('first_name', 'last_name', 'email', 'Club', 'credits', 'in_club')

    def get_info(self, user_id, password):    # Method that returns formatted information, added by Radiela
        
        # Cleaned data
        cl_data = super().clean()

        f_name = cl_data.get('first_name').strip()
        l_name = cl_data.get('last_name').strip()

        credits_available = str(cl_data.get('credits'))

        email = cl_data.get('email')
        msg = "Dear " + f_name + " " + l_name + ", thank you for registering with UWEFlix!"
        msg2 = "\nYour user ID is: " + user_id + " and your password: " + password
        msg3 = "\n You now have " + credits_available + " credits to your account."
        msg += msg2
        msg += "\n"
        msg += msg3

        return email, msg
        

    # Send email function, added by Radiela
    def send(self, user_id, password):

        email, msg = self.get_info(user_id, password)

        send_mail(                  # Sensitive credentials are handled in .env file
            subject='Welcome to UWEFlix',    
            message=msg,
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[email]
        )


# Form for users making their own registration (no club), added by Radiela
class UserForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ('first_name', 'last_name', 'email')
    
    def get_info(self, user_id, password):    # Method that returns formatted information
        
        # Cleaned data
        cl_data = super().clean()

        f_name = cl_data.get('first_name').strip()
        l_name = cl_data.get('last_name').strip()

        email = cl_data.get('email')
        msg = "Dear " + f_name + " " + l_name + ", thank you for registering with UWEFlix!"
        msg2 = "\nYour user ID is: " + user_id + " and your password: " + password
        msg3 = "\n You now have 0 credits to your account."
        msg += msg2
        msg += "\n"
        msg += msg3

        return email, msg
        

    # Send email function
    def send(self, user_id, password):

        email, msg = self.get_info(user_id, password)

        send_mail(                  # Sensitive credentials are handled in .env file
            subject='Welcome to UWEFlix',    
            message=msg,
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[email]
        )


# Remove user, added by Radiela
class RemoveUserForm(forms.ModelForm):
    class Meta:
        model = RemoveUserDetails
        fields=['choose_user']

    def get_info(self):    # Method that returns formatted information
        
        msg = "\n Your UWEFlix account has been terminated."
        return msg

    # Send email function
    def send(self, email):

        msg = self.get_info()

        send_mail(                  # Sensitive credentials are handled in .env file
            subject='Your account has been removed',    
            message=msg,
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[email]
        )


# The option for user to request a new password, added by Radiela
class ForgottenPassword(forms.Form):
    username = forms.CharField(max_length=50)
    email = forms.EmailField()

    class Meta:
        fields = ['username', 'email']

    def get_info(self, password):    # Method that returns formatted information
        
        # Cleaned data
        cl_data = super().clean()
        
        username = cl_data.get('username')
        email = cl_data.get('email')

        msg = "You have requested a change of password."
        msg2 = "\nYour new password is " + password
        msg += msg2

        return email, msg
        

    # Send email function
    def send(self, password):

        email, msg = self.get_info(password)

        send_mail(                  # Sensitive credentials are handled in .env file
            subject='Forgotten password UWEFlix',    
            message=msg,
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[email]
        )



# User can request to see their username, added by Radiela
class ForgottenID(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        fields = ['email', 'password']

    def get_info(self, username):    # Method that returns formatted information
        
        # Cleaned data
        cl_data = super().clean()
        
        email = cl_data.get('email')
        password = cl_data.get('password')

        msg = "Your new username is " + username

        return email, password, msg
        

    # Send email function
    def send(self, username):

        email, password, msg = self.get_info(username)

        send_mail(                  # Sensitive credentials are handled in .env file
            subject='Forgotten username UWEFlix',    
            message=msg,
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[email]
        )


class RegisterForm(UserCreationForm):
    email = forms.EmailField()
    class Meta: 
        model = User
        fields = ["username", "email", "password1", "password2"]



# Create a form for uploading Film Details added by Radiela
class MovieForm(forms.ModelForm):
    class Meta:
        model = FilmDetails
        fields= ["title", "img", "age_rating", "duration", "description"]


# Remove movies, added by Radiela
class RemoveMovieForm(forms.ModelForm):
    class Meta:
        model = RemoveMovieDetails
        fields=['choose_movie']


# Create a form for uploading Upcoming Film Details added by Radiela
class UpcomingMovieForm(forms.ModelForm):
    class Meta:
        model = UpcomingFilmDetails
        fields= ["title", "img", "age_rating", "duration", "description"]


# Remove upcoming movie, added by Radiela
class RemoveUpcomingForm(forms.ModelForm):
    class Meta:
        model = RemoveUpcomingDetails
        fields=['choose_item']


# Create a form for uploading Showing Details added by Radiela
class ShowingsForm(forms.ModelForm):
    class Meta:
        model = ShowingDetails
        fields= ["Films", "date", "time", ]


# Remove showings, added by Radiela
class RemoveShowingForm(forms.ModelForm):
    class Meta:
        model = RemoveShowingDetails
        fields=['choose_showing']


# Create a form for uploading Screen Details added by Radiela
class ScreenForm(forms.ModelForm):
    class Meta:
        model = ScreenDetails
        fields= ["Showings", "seats_available", "screen_type"]


# Remove screen, added by Radiela
class RemoveScreenForm(forms.ModelForm):
    class Meta:
        model = RemoveScreenDetails
        fields=['choose_screen']


"""# Create a form for uploading Card Details added by Radiela
class CardForm(forms.Form):
    cc_number = CardNumberField(label='Card Number')
    cc_expiry = CardExpiryField(label='Expiration Date')
    cc_code = SecurityCodeField(label='CVV/CVC')"""


# Create a form for buying credits, added by Radiela
class CreditForm(forms.Form):
    username = forms.CharField(max_length=8)
    credits = forms.IntegerField()

    cc_number = CardNumberField(label='Card Number')
    cc_expiry = CardExpiryField(label='Expiration Date')
    cc_code = SecurityCodeField(label='CVV/CVC')


    def get_info(self):    # Method that returns formatted information 
        
        # Cleaned data
        cl_data = super().clean()
        credits = cl_data.get('credits')
        subject = "Credits Added"

        msg = f'You have just added {credits} credits to your account.'
        msg += f'\n'
        msg += f'\nThank you for choosing UWEFlix!'

        return subject, msg
        

    # Send email function, added by Radiela
    def send(self, email):

        subject, msg = self.get_info()

        send_mail(                  # Sensitive credentials are handled in .env file
            subject=subject,    
            message=msg,
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[email]
        )


# Orders, added by Radiela
class OrderForm(forms.ModelForm):
    class Meta:
        model = OrderDetails
        fields=['screen', 'selected_seats']


# Remove item from cart, added by Radiela
class RemoveItemForm(forms.ModelForm):
    class Meta:
        model = RemoveOrderDetails
        fields=['choose_item']


# Confirm order, added by Radiela
class ConfirmOrderForm(forms.Form):
    username = forms.CharField(max_length=8)
    password = forms.CharField(widget=forms.PasswordInput)
 
    def get_info(self, title, screen_type, date, seats, credits):    # Method that returns formatted information 
        
        # Cleaned data
        subject = "You have placed a new order"

        msg = f'Thank you for your recent order with UWEFlix!'
        msg += f'\n'
        msg += f'\nYou have purchased {seats} tickets for {title} {screen_type} on {date} '
        msg += f'\n'
        msg += f'\n Credits left in your account: {credits}'
        msg += f'\nThank you for choosing UWEFlix!'

        return subject, msg
        
    # Send email function, added by Radiela
    def send(self, email, title, screen_type, date, seats, credits):

        subject, msg = self.get_info(title, screen_type, date, seats, credits)

        send_mail(                  # Sensitive credentials are handled in .env file
            subject=subject,    
            message=msg,
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[email]
        )
    



# Create contact form for user to send queries added by Radiela
class ContactForm(forms.Form):

    name = forms.CharField(max_length=120)
    email = forms.EmailField()
    inquiry = forms.CharField(max_length=70)
    message = forms.CharField(widget=forms.Textarea)

    def get_info(self):    # Method that returns formatted information 
        
        # Cleaned data
        cl_data = super().clean()

        name = cl_data.get('name').strip()
        from_email = cl_data.get('email')
        subject = cl_data.get('inquiry')

        msg = f'{name} with email {from_email} said:'   # Email content
        msg += f'\n"{subject}"\n\n'
        msg += cl_data.get('message')

        return subject, msg
        

    # Send email function, added by Radiela
    def send(self):

        subject, msg = self.get_info()

        send_mail(                  # Sensitive credentials are handled in .env file
            subject=subject,    
            message=msg,
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[settings.RECIPIENT_ADDRESS]
        )


    
