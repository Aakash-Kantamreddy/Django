from django.shortcuts import render,redirect
from.models import data
from.models import ContactMessage
from django.contrib import messages
# from .forms import ContactForm  # Assuming you have a form defined in forms.py
# from django.http import JsonResponse



# Create your views here.


def Home(request):
    return render(request,"index.html")

def login(request):
    return render(request,"login.html")

def signup(request):
    
    if(request.method == "POST"):
        username = request.POST["username"]
        email = request.POST["email"]
        password =request.POST["password"]
        confirm_password = request.POST["confirm_password"]
        datas = data(username=username,email=email,password=password,confirm_password=confirm_password)
        messages.success(request, 'You have successfully registered!')  # Add success message
        datas.save()
        
        return redirect("login")
    return render(request,"signup.html")

    # if request.method == "POST":
    #     form = SignUpForm(request.POST)
    #     if form.is_valid():
    #         form.save()  # This assumes your form handles saving to the database
    #         username = form.cleaned_data.get('username')
    #         messages.success(request, f'Account created for {username}. You can now log in.')
    #         return redirect('login')  # Redirect to login page after successful signup
    # else:
    #     form = SignUpForm()  # Create a new form instance if not a POST request
    
    # return render(request, "signup.html", {'form': form})
    

def About(request):
    return render(request,"about.html")
 
def contact(request):

    # if request.method == 'POST':
    #     form = ContactForm(request.POST)
    #     if form.is_valid():
    #         # Process form data here
    #         name = form.cleaned_data['name']
    #         email = form.cleaned_data['email']
    #         subject = form.cleaned_data['subject']
    #         message = form.cleaned_data['message']

    #         # Save to database if using a model
    #         # contact_message = ContactMessage(name=name, email=email, subject=subject, message=message)
    #         # contact_message.save()

    #         # Simulate sending email (replace with actual email sending logic)
    #         # For demonstration, just print the message to console
    #         print(f'New Contact Form Submission:\nName: {name}\nEmail: {email}\nSubject: {subject}\nMessage: {message}')

    #         # Return success message
    #         return JsonResponse({'status': 'success'})

    #     else:
    #         # Return validation errors
    #         return JsonResponse({'status': 'error', 'errors': form.errors})

    # else:
    #     form = ContactForm()  # Create a new instance of the form
    #     return render(request, 'contact.html', {'form': form})
     return render(request,"contact.html")

def Team(request):
    return render(request,"team.html")
def Services(request):
    return render(request,"services.html")




