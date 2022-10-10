import datetime
from dis import disco
import email
from unittest import mock
from urllib import request
from xml.dom.minidom import Document
from django import views
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from sqlalchemy import null
from .forms import *
from .models import FilmDetails
from .models import *
from django.core.mail import *
from django.contrib.auth.models import *
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User
import hashlib
import pymysql
import datetime

# Create a home page added by Radiela
def home(request):
    films = FilmDetails.objects.all()
    upcoming = UpcomingFilmDetails.objects.all()

    return render(request,'home_page.html', {'films':films, 'upcoming':upcoming})


# Create a home page for logged in users, added by Radiela
def auth_user(request):
    films = FilmDetails.objects.all()
    upcoming = UpcomingFilmDetails.objects.all()
    orders = OrderDetails.objects.all()

    return render(request, 'user_auth_page.html', {'films':films, 'upcoming':upcoming, 'orders':orders})


# Function for gathering data, added by Radiela
def get_database_login(column):

    # Change the database source, if using a database
    con = pymysql.connect(host="localhost", user="root", password="", database="uwe-flix")  # MySQL database
    data = []

    with con.cursor() as curs:
        # Get all items from ('table') - chosen Table to work with
        curs.execute("SELECT * FROM `user_page_student`")
        table = curs.fetchall()
        
        # Get all items from the chosen column in the Table
        num = len(table)
        for i in range(0, num):
            item = table[i][column]
            data.append(item)

    con.close()
    return data


# Function for gathering data, added by Radiela
def get_database_order(column):

    # Change the database source, if using a database
    con = pymysql.connect(host="localhost", user="root", password="", database="uwe-flix")  # MySQL database
    data = []

    with con.cursor() as curs:
        # Get all items from ('table') - chosen Table to work with
        curs.execute("SELECT * FROM `orders`")
        table = curs.fetchall()
        
        # Get all items from the chosen column in the Table
        num = len(table)
        for i in range(0, num):
            item = table[i][column]
            data.append(item)

    con.close()
    return data


# Delete fields from Student, added by Radiela
def delete_database_field(id):
    Student.objects.filter(id_number=id).delete()

# Delete an item from the order, added by Radiela
def delete_order_field(id):
    OrderDetails.objects.filter(id=id).delete()



# Function for extracting user object, added by Radiela
def find_user(index):
    
    # Get all user details from the database
    all_names = get_database_login(1)
    all_surnames = get_database_login(2)
    all_emails = get_database_login(3)
    usernames = get_database_login(4)
    passwords = get_database_login(5)
    credits = get_database_login(6)
    in_clubs = get_database_login(8)

    # Extract the chosen field details
    first_name = all_names[index]
    last_name = all_surnames[index]
    email = all_emails[index]
    id_number = usernames[index]
    hashed = passwords[index]
    credits = credits[index]
    in_club = in_clubs[index]

    # Update the user
    user = Student()
    user.first_name = first_name
    user.last_name = last_name
    user.email = email
    user.password = hashed
    user.id_number = id_number
    user.credits = credits
    user.in_club = in_club

    return user



# Function for login with generated ID and password, added by Radiela
def user_auth(user_id, user_pass):
    usernames = get_database_login(4)
    auth = False
    print("username: ", user_id)
    if user_id in usernames:
        ind = usernames.index(user_id)
        passwords = get_database_login(5)
        check = passwords[ind]

        password = str(hashlib.sha256(str.encode(user_pass)).hexdigest())
        if password == check:
            auth = True
                
            return auth


# Manager page, added by Radiela
def manager(request):
    movie_list = FilmDetails.objects.all()
    showings_list = ShowingDetails.objects.all()
    screen_list = ScreenDetails.objects.all()
    upcoming_list = UpcomingFilmDetails.objects.all()

    form = RemoveUpcomingForm(request.POST)
    if form.is_valid():
        selected = form.cleaned_data['choose_item']
        ind = selected.id
        UpcomingFilmDetails.objects.filter(id=ind).delete()

    form2 = RemoveScreenForm(request.POST)
    if form2.is_valid():
        selected = form2.cleaned_data['choose_screen']
        ind = selected.id
        ScreenDetails.objects.filter(id=ind).delete()

    form3 = RemoveShowingForm(request.POST)
    if form3.is_valid():
        selected = form3.cleaned_data['choose_showing']
        ind = selected.id
        ShowingDetails.objects.filter(id=ind).delete()

    form4 = RemoveMovieForm(request.POST)
    if form4.is_valid():
        selected = form4.cleaned_data['choose_movie']
        ind = selected.id
        FilmDetails.objects.filter(id=ind).delete()       

    return render (request, 'staff/manager.html', {'form':form, 'form2':form2, 'form3':form3, 'form4':form4,
        'movie_list':movie_list, 'showings_list':showings_list, 'screen_list':screen_list, 'upcoming_list':upcoming_list
        })



# A view for accounts' main page, added by Radiela
def accounts(request):
    club_list = Club.objects.all()
    stud_list = Student.objects.all()
    staff_list = User.objects.all()
    
    form = RemoveClubForm(request.POST)
    if form.is_valid():
        selected = form.cleaned_data['choose_club']
        ind = selected.id
        Club.objects.filter(id=ind).delete()

    form2 = RemoveUserForm(request.POST)
    if form2.is_valid():
        selected = form2.cleaned_data['choose_user']
        ind = selected.id
        users = Student.objects.all()

        for user in users:
            if user.id == ind:
                email = user.email
                form2.send(email)

        Student.objects.filter(id=ind).delete()


    form3 = RemoveStaffForm(request.POST)
    if form3.is_valid():
        selected = form3.cleaned_data['choose_member']
        ind = selected.id
        User.objects.filter(id=ind).delete()

    return render(request, 'staff/accounts.html', {'form':form, 'form2':form2, 'form3':form3, 'club_list':club_list, 'stud_list':stud_list, 'staff_list':staff_list})


def show_club(request, club_id):
    
    club = Club.objects.get(pk=club_id)
    
    return render (request, 'show/show_club.html', {'club':club})


def show_student(request, student_id):
    
    student = Student.objects.get(pk=student_id)
    
    return render (request, 'show/show_student.html', {'student':student})


def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            print("User, ", user)
            login(request,user)
            return redirect('manager')
        else:                  # Login with generated id and password, added by Radiela (until line 194)
            success = user_auth(username, password)
            print("USER AUTH success: ", success)
            if success == True:
                OrderDetails.objects.all().delete() 
                all_users = get_database_login(4)
                if username in all_users:
                    ind = all_users.index(username)
                    current_user = find_user(ind)

                user = authenticate(request)
                films = FilmDetails.objects.all()
                upcoming = UpcomingFilmDetails.objects.all()
                return render(request, 'user_page/user_auth_page.html', {'current_user':current_user, 'films':films, 'upcoming':upcoming})
            else:
                messages.success(request, ("There was error in login in"))
                return redirect('login')
    else:
        return render (request,'authenticate/login.html')


def logout_user(request):
	logout(request)
	messages.success(request, ("You were Logged Out"))
	return redirect('home')


# A function for generating unique 10-digit id added by Radiela
def generate_id():
        number = ""
        for i in range(0, 7):  # 7-digit number
            number += random.choice(string.digits)
        
        all_users = get_database_login(4)
        if number not in all_users:     # Ensure uniqueness of the generated ID
            return number
        else:
            generate_id()


# A function for generating unique 8-symbols password added by Radiela
def generate_password():
    password = ""
    for i in range(0, 10):  # 10-digit password
        password += random.choice(string.hexdigits).lower()

    return password


# Function for user registration through the webpage, added by Radiela
def user_registration(request):
    msg = ""
    submitted = False
    if request.method == "POST":
        form = UserForm(request.POST)

        if form.is_valid():
            # Get data from form 
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            email = form.cleaned_data['email']

            all_emails = get_database_login(3)
            if email in all_emails:
                msg = "Email already exists"
            else:
                # Generate unique id and password
                password = generate_password()
                hashed = str(hashlib.sha256(str.encode(password)).hexdigest())
                id_number = str(generate_id())

                 # Save to DB
                user = Student()
                user.first_name = first_name
                user.last_name = last_name
                user.email = email
                user.password = hashed
                user.id_number = id_number
                user.in_club = "no"
                user.save()

                form.send(id_number, password)
 
                return redirect(registration_successful)             
    else: 
        form = UserForm
        if 'submitted' in request.GET:
            submitted = True
    return render(request, 'registration/register_page.html', {'form':form, 'submitted':submitted, 'msg':msg})

def registration_successful(request):
    return render(request, 'registration/success_registration.html')



# Function for displaying forgotten password page, added by Radiela
def password_request(request):
    msg_uname = ""
    msg_email = ""
    if request.method == "POST":
        form = ForgottenPassword(request.POST)
        if form.is_valid():
            all_emails = get_database_login(3)
            all_users = get_database_login(4)

            email = form.cleaned_data['email']
            username = form.cleaned_data['username']

            password = generate_password()
            hashed = str(hashlib.sha256(str.encode(password)).hexdigest())
            
            if email in all_emails:
                ind = all_emails.index(email)
                check = all_users[ind]
                if check == username:
                    user = find_user(ind)
                    user.password = hashed
                    delete_database_field(username)
                    user.save()
                    form.send(password)

                    return redirect(password_changed)

                else:
                    msg_uname = "error"
            else:
                msg_email = "error"
    else:
        form = ForgottenPassword
    
    return render(request, 'password/forgotten_password.html', {'form' : form, 'msg_uname':msg_uname, 'msg_email':msg_email})


# The option for user to see their username by providing email and password, added by Radiela
def forgotten_username(request):
    msg_pass = ""
    msg_email = ""
    if request.method == "POST":
        form = ForgottenID(request.POST)

        if form.is_valid():
            all_passwords = get_database_login(5)
            all_emails = get_database_login(3)

            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            hashed = str(hashlib.sha256(str.encode(password)).hexdigest())

            if email in all_emails:
                ind = all_emails.index(email)
                check = all_passwords[ind]
                if check == hashed:
                    user = find_user(ind)
                    username = user.id_number
                    form.send(username)

                    return redirect(username_changed)
                else:
                    msg_pass = "error"
            else:
                msg_email = "error"
    else:
        form = ForgottenID
    
    return render(request, 'password/forgotten_id.html', {'form':form, 'msg_pass':msg_pass, 'msg_email':msg_email})

# Added by Radiela
def username_changed(request):
    return render(request, 'password/id_sent.html')


# Views for the success in changing password, added by Radiela
def password_changed(request):
    return render(request, 'password/password_changed.html')


def student_registration(request):
    submitted = False
    msg = ""
    if request.method == "POST":
        form = StudForm(request.POST)

        if form.is_valid():
            # Get data from form (added by Radiela)
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            email = form.cleaned_data['email']
            credits = form.cleaned_data['credits']
            club = form.cleaned_data['Club']
            in_club = form.cleaned_data['in_club']

            # Generate unique id and password added by Radiela
            password = generate_password()
            hashed = str(hashlib.sha256(str.encode(password)).hexdigest())
            id_number = str(generate_id())

            all_emails = get_database_login(3)
            if email in all_emails:
                msg = "message"
            else:
                # Save to DB added by Radiela
                student = Student()
                student.first_name = first_name
                student.last_name = last_name
                student.email = email
                student.id_number = id_number
                student.password = hashed
                student.credits = credits
                student.Club = club
                student.in_club = in_club
                student.save()

                form.send(id_number, password)
                return redirect(accounts)
    else: 
        form = StudForm
        if 'submitted' in request.GET:
            submitted = True
    return render(request, 'registration/student_registration.html', {'form':form, 'submitted':submitted, 'msg':msg})



def club_registration(request):
    msg = ""
    submitted = False
    form = ClubForm(request.POST)
    if form.is_valid():
        name = form.cleaned_data['name']
        clubs = Club.objects.all()
        print("ALL ", clubs)
        for club in clubs:
            if name == club.name:
                msg = "error"
            else:
                form.send()
                form.save()
                submitted = True
                return redirect(registration_successful)
    else:
        form = ClubForm()

    return render(request, 'registration/club_registration.html', {'form':form,'submitted':submitted, 'msg':msg})



def staff_registration(request):
    msg_email = ""
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            
            user = User.objects.create_superuser(       # Staff is registered as superuser, added by Radiela
            username = form.cleaned_data['username'],
            email = form.cleaned_data['email'],
            password = form.cleaned_data['password1'])

            user.save()
            return redirect(registration_successful) 
    else:
        form = RegisterForm() 
    return render(request, 'registration/staff_registration.html', {"form":form, 'msg_uname':msg_email})


# Upload page view - base for upload drop-down pages added by Radiela
def upload_details_page(request):

    return render(request, 'upload_page.html')



# Create a page for uploading movie details into db added by Radiela
def movie_details(request):

    form= MovieForm(request.POST, request.FILES)
    
    if form.is_valid():
        title = form.cleaned_data['title']
        title = title.replace(" ", "")
        img = form.cleaned_data['img']
        age_rating = form.cleaned_data['age_rating']
        duration = form.cleaned_data['duration']
        description = form.cleaned_data['description']

        movie = FilmDetails()
        movie.title = title
        movie.img = img
        movie.age_rating = age_rating
        movie.duration = duration
        movie.description = description

        movie.save()
        return redirect(upload_details_page)

    else:
        form = MovieForm()
        
    return render(request, 'upload_movie.html', {'form': form})


# Create a page for uploading Upcoming movie details into db added by Radiela
def upcoming_movie_details(request):

    form= UpcomingMovieForm(request.POST, request.FILES)
    
    if form.is_valid():
        title = form.cleaned_data['title']
        title = title.replace(" ", "")
        img = form.cleaned_data['img']
        age_rating = form.cleaned_data['age_rating']
        duration = form.cleaned_data['duration']
        description = form.cleaned_data['description']

        movie = UpcomingFilmDetails()
        movie.title = title
        movie.img = img
        movie.age_rating = age_rating
        movie.duration = duration
        movie.description = description

        movie.save()
        return redirect(upload_details_page)

    else:
        form = UpcomingMovieForm()
        
    return render(request, 'upload_upcoming.html', {'form': form})

    
# Views for displaying movie details from the database added by Radiela
def display_movie_details(request):

    movie_list = FilmDetails.objects.all()

    return render(request, 'show/show_movies.html', {'movie_list': movie_list})


def display_upcoming(request):
    upcoming_list = UpcomingFilmDetails.objects.all()

    return render(request, 'show/show_upcoming.html', {'upcoming_list':upcoming_list})


# Create a page for uploading showing details into db added by Radiela
def showing_details(request):

    form= ShowingsForm(request.POST)

    if form.is_valid():
        form.save()
        return redirect(upload_details_page)

    else:
        form = ShowingsForm()
        
    return render(request, 'upload_showings.html', {'form': form})


# Views for displaying showing details from the database added by Radiela
def display_showing_details(request):

    # get the details of all showings
    obj = ShowingDetails.objects.all()
    context={
        'show': obj
    }

    return render(request, "home_page.html", context)


# Create a page for uploading screen details into db added by Radiela
def screen_details(request):

    form= ScreenForm(request.POST)

    if form.is_valid():
        form.save()
        return redirect(upload_details_page)

    else:
        form = ScreenForm()
        
    return render(request, 'upload_screen.html', {'form': form})


# Views for displaying screen details from the database added by Radiela
def display_screen_details(request):

    # get the details of all screens 
    all_screens = ScreenDetails.objects.all()
    return render(request, "home_page.html", {'all_screens': all_screens })



# Function for users to buy credits, added by Radiela
def display_add_credits(request):
    form = CreditForm(request.POST)
    msg = ""
    msg2 = ""

    if form.is_valid():
        credits_added = form.cleaned_data['credits']
        username = form.cleaned_data['username']
        all_users = get_database_login(4)
        all_credits = get_database_login(6)
        
        if username in all_users:
            ind = all_users.index(username)
            credits_added = int(credits_added)
            print("Credits added: ", credits_added)
            if credits_added > 0:
                user = find_user(ind)
                credits_available = int(all_credits[ind])
                credits_available += credits_added
                print("Available: ", user.credits, "total: ", credits_available)
                user.credits = credits_available
                email = user.email

                delete_database_field(username)
                user.save()
                form.send(email)
                return render(request, 'payment/payment_page.html', {'user':user})
            else:
                msg2 = "error"
        else:
            msg = "error"
    else:
        form = CreditForm()
    
    return render(request, 'shopping_cart/add_credits.html', {'form' : form, 'msg':msg, 'msg2':msg2})



# Views for Contact form added by Radiela
def dislpay_contact_page(request):
    return render(request, 'contact/contact_page.html')


# Function for sending email to Admin/Manager from the Contact form added by Radiela
def contact_form(request):
    form = ContactForm(request.POST)

    if form.is_valid():
        form.send()
        
        return redirect(dislpay_contact_page)

    else:
        form = ContactForm()
        
    return render(request, 'contact/contact_form.html', {'form': form})



# Function that allows user to create an order, added by Radiela
def create_order(request):
    form = OrderForm(request.POST)
    screen_type = "2D"
    price = 3
    msg=""

    if form.is_valid():
        num_seats = form.cleaned_data['selected_seats']
        screen = str(form.cleaned_data['screen'])
        last = len(screen) - 1
        char = screen[last]
        screen_details = screen.split()

        if num_seats == 0:
            msg = "error"
        else:
            # Get screen type and price (2D = 3 credits; 3D = 5 credits)
            if char == "1":
                price = 3
            elif char == "2":
                price = 5
            else:
                price = 3
                screen_type = "3D"

            price = price * num_seats 

            order = OrderDetails()
            order.title = screen_details[0]
            order.date = screen_details[1]
            order.time = screen_details[2]
            order.screen_type = screen_type
            order.selected_seats = num_seats
            order.price = price
            order.save()
            return redirect(shopping_cart)
    else:
        form = OrderForm
     
    return render(request, 'shopping_cart/create_order.html', {'form':form, 'msg':msg})


# Shopping cart page view, added by Radiels
def shopping_cart(request):
    orders = OrderDetails.objects.all()
    form = RemoveItemForm(request.POST)

    if form.is_valid():
        choose_item = form.cleaned_data['choose_item']
        ind = choose_item.id
        print("ind", ind)
        delete_order_field(ind)

    return render(request, 'shopping_cart/shopping_cart.html', {'orders':orders, 'form':form})


# Views for displaying payment form added by Radiela
def display_payment(request):

    #form = CardForm(request.POST)
    form = ConfirmOrderForm(request.POST)
    orders = OrderDetails.objects.all()
    msg = ""
    msg2 = ""
    msg_uname = ""
    msg_pass = ""

    if form.is_valid():
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        all_users = get_database_login(4)
        all_passwords = get_database_login(5)

        if username in all_users:
            ind = all_users.index(username)
            check = all_passwords[ind]
            hashed = str(hashlib.sha256(str.encode(password)).hexdigest())
        
            if check == hashed:
                user = find_user(ind)
                email = user.email
                credits_available = user.credits
                credits = int(credits_available)

                all_tickets = get_database_order(6)  #cost
                total_price = 0
                for item in all_tickets:
                    total_price += item
                total_price = round(total_price, 2)

                club = str(user.in_club)
            
                if club != "no":  # Add discount if user in a club 20%
                    msg2 = "yes"
                    discount = total_price/5
                    total_price = total_price - discount

                if credits >= total_price:  # If credits are sufficient
                    credits -= total_price
                    credits = round(credits, 2)
                    user.credits = credits
                    delete_database_field(username)
                    user.save()

                    title = get_database_order(1)
                    date = get_database_order(2)
                    screen_type = get_database_order(4)
                    seats = get_database_order(5)
                    id = get_database_order(0)

                    form.send(email, title[0], screen_type[0], date[0], seats[0], credits)

                    order = PaidOrderDetails()
                    order.username = username
                    order.date = datetime.datetime.now()
                    order.price = total_price
                    order.save()

                    for item in id:
                        delete_order_field(item)

                    return render(request, 'payment/payment_page.html', {'user':user, 'msg2':msg2})
                else:
                    msg = "Not enough credits"
            else:
                msg_pass = "error"
        else:
            msg_uname = "error"
    else:
        form = ConfirmOrderForm()
        print("Invalid Form")
        print(form.errors)
        
    return render(request, 'confirm_payment.html', {'form': form, 'orders':orders, 'msg':msg, 'msg_uname':msg_uname, 'msg_pass':msg_pass})


# Views for payment page added by Radiela
def display_payment_page(request):
    orders = OrderDetails.objects.all()

    return render(request, 'payment_page.html', {'orders':orders})


def monthly_payments(request):
    msg = ""
    form = ConfirmOrderForm(request.POST)
    if form.is_valid():
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        success = user_auth(username, password)

        if success is True:
            order = PaidOrderDetails()
            order.username = username
            orders = PaidOrderDetails.objects.filter(username=username)
            return render(request, 'payment/payments.html', {'orders':orders})
        else:
            msg = "error"



    return render(request, 'payment/confirm.html', {'form':form, 'msg':msg})