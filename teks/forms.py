from django import forms
from .models import data  # Import your model
from .models import ContactMessage
class ContactForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    subject = forms.CharField(max_length=255)
    message = forms.CharField(widget=forms.Textarea)

# class SignUpForm(forms.ModelForm):
#     confirm_password = forms.CharField(widget=forms.PasswordInput())
    
#     class Meta:
#         model = data  # Replace with your actual model name
#         fields = ['username', 'email', 'password', 'confirm_password']
#         widgets = {
#             'password': forms.PasswordInput(),
#         }
    
#     def clean(self):
#         cleaned_data = super().clean()
#         password = cleaned_data.get("password")
#         confirm_password = cleaned_data.get("confirm_password")
        
#         if password != confirm_password:
#             raise forms.ValidationError(
#                 "Passwords do not match."
#             )
        
#         # You can add more validation as needed
    
#     def save(self, commit=True):
#         instance = super().save(commit=False)
#         instance.set_password(self.cleaned_data["password"])  # Ensure password is hashed
#         if commit:
#             instance.save()
#         return instance
