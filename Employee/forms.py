from django import forms
from .models import Employee
from django.core.exceptions import ValidationError
class EmployeeForm(forms.ModelForm):
    # Define the choices for Designation and Course with an empty option
    DESIGNATION_CHOICES = [
        ('', 'Select Designation'),  # Empty option for default choice
        ('HR', 'HR'),
        ('Manager', 'Manager'),
        ('Sales', 'Sales'),
    ]

    COURSE_CHOICES = [
        ('MCA', 'MCA'),
        ('BCA', 'BCA'),
        ('BSC', 'BSC'),
    ]
    
    GENDER_CHOICES = [
        ('Male', 'Male'),
        ('Female', 'Female'),
    ]

    # Use the choices in the fields
    Designation = forms.ChoiceField(choices=DESIGNATION_CHOICES, required=True)
    Course = forms.ChoiceField(
        choices=COURSE_CHOICES,
        widget=forms.RadioSelect,  # This renders the choices as radio buttons
        required=True
    )
    Gender = forms.ChoiceField(
        choices=GENDER_CHOICES,
        widget=forms.RadioSelect,  # This renders the choices as radio buttons
        required=True
    )


    class Meta:
        model = Employee
        fields = ['Image', 'Name', 'Email', 'Mobile', 'Designation', 'Gender', 'Course']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # If the form is being used to edit an employee, disable the Email field
        if self.instance and self.instance.pk:
            self.fields['Email'].disabled = True  # Disable Email field for editing

    def clean_Email(self):
        email = self.cleaned_data['Email']
        
        # Skip email validation if it's an edit (since it's disabled and not changed)
        if self.instance.pk:
            return email  # Skip email validation for existing records (editing)
        
        # Validate unique email during creation
        if Employee.objects.filter(Email=email).exists():
            raise forms.ValidationError("This email is already in use.")
        
        return email

    def clean_Mobile(self):
        mobile = self.cleaned_data['Mobile']
        
        # Ensure that the mobile number is 10 digits and consists of only numbers
        if len(mobile) != 10 or not mobile.isdigit():
            raise forms.ValidationError("Please enter a valid 10-digit mobile number.")
        
        return mobile

    def clean_Designation(self):
        designation = self.cleaned_data['Designation']
        if designation == '':
            raise forms.ValidationError("Please select a valid designation.")
        return designation

    def clean_Course(self):
        course = self.cleaned_data['Course']
        if course == '':
            raise forms.ValidationError("Please select a valid course.")
        return course

    def clean_Gender(self):
        gender = self.cleaned_data['Gender']
        if gender == '':
            raise forms.ValidationError("Please select a valid gender.")
        return gender
    


