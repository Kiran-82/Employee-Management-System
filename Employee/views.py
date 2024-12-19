from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login
from .models import Admin,Employee
from django.contrib import messages
from .forms import EmployeeForm
from django.core.exceptions import ValidationError
from django.contrib.auth.decorators import login_required
def admin_login(request):
    if request.method == 'POST':
        username = request.POST['userName']
        password = request.POST['Pwd']
        try:
            # Validate admin credentials
            admin = Admin.objects.get(userName=username, Pwd=password)
            # Save admin info in the session
            request.session['admin_id'] = admin.sno
            return redirect('admin_dashboard')  # Redirect to the admin dashboard
        except Admin.DoesNotExist:
            # Show an error message if credentials are invalid
            return render(request, 'admin_login.html', {'error': 'Invalid username or password.'})
    return render(request, 'admin_login.html')

def admin_dashboard(request):
    if 'admin_id' not in request.session:
        return redirect('admin_login')  # Redirect to login if not authenticated

    # Get the total number of employees
    total_employees = Employee.objects.count()

    return render(request, 'admin_dashboard.html', {'total_employees': total_employees})
def employee_list(request):
    search_query = request.GET.get('search', '')  # Get the search query from the URL
    employees = Employee.objects.all()  # Default to all employees

    if search_query:
        employees = employees.filter(
            Name__icontains=search_query
        ) | employees.filter(
            Designation__icontains=search_query
        )

    return render(request, 'employee_list.html', {'employees': employees})

def add_employee(request):
    if 'admin_id' not in request.session:
        return redirect('admin_login')  # Redirect to login if not authenticated
    
    if request.method == 'POST':
        # Extract form data
        name = request.POST['Name']
        email = request.POST['Email']
        mobile = request.POST['Mobile']
        designation = request.POST['Designation']
        gender = request.POST['Gender']
        course = request.POST['Course']
        image = request.FILES.get('Image')  # Handle image upload

        # Validate mobile number (10 digits)
        if len(mobile) != 10 or not mobile.isdigit():
            messages.error(request, 'Please enter a valid 10-digit mobile number.')
            form = EmployeeForm(request.POST, request.FILES)  # Reinitialize form with existing data
            return render(request, 'add_employee.html', {'form': form})  # Pass form with data back to template

        # Check if the email already exists in the database
        if Employee.objects.filter(Email=email).exists():
            messages.error(request, 'This email is already in use. Please use a different email.')
            form = EmployeeForm(request.POST, request.FILES)  # Reinitialize form with existing data
            return render(request, 'add_employee.html', {'form': form})  # Pass form with data back to template

        # Validate image file type
        if image:
            allowed_extensions = ['jpg', 'jpeg', 'png']
            extension = image.name.split('.')[-1].lower()
            if extension not in allowed_extensions:
                messages.error(request, "Invalid image format. Only jpg, jpeg, and png are allowed.")
                form = EmployeeForm(request.POST, request.FILES)
                return render(request, 'add_employee.html', {'form': form})

            # Check if the file is an image
            if not image.content_type.startswith('image/'):
                messages.error(request, "File is not a valid image.")
                form = EmployeeForm(request.POST, request.FILES)
                return render(request, 'add_employee.html', {'form': form})

        # If all validations pass, create and save the new employee
        employee = Employee(
            Name=name,
            Email=email,
            Mobile=mobile,
            Designation=designation,
            Gender=gender,
            Course=course,
            Image=image
        )
        employee.save()

        # Show success message
        messages.success(request, 'Employee added successfully!')

        # Redirect to employee list page
        return redirect('employee_list')

    # If it's a GET request, simply render an empty form
    form = EmployeeForm()
    return render(request, 'add_employee.html', {'form': form})
def edit_employee(request, id):
    employee = get_object_or_404(Employee, id=id)

    if request.method == 'POST':
        form = EmployeeForm(request.POST, request.FILES, instance=employee)

        # Validate the form first (this checks all the required fields)
        if form.is_valid():
            # Now validate mobile number explicitly
            mobile = request.POST.get('Mobile')
            if len(mobile) != 10 or not mobile.isdigit():
                form.add_error('Mobile', 'Please enter a valid 10-digit mobile number.')
                return render(request, 'edit_employee.html', {'form': form, 'employee': employee})

            # Validate image file type (if an image is uploaded)
            image = request.FILES.get('Image')
            if image:
                # Validate image file extension
                allowed_extensions = ['jpg', 'jpeg', 'png']
                extension = image.name.split('.')[-1].lower()
                if extension not in allowed_extensions:
                    form.add_error('Image', "Invalid image format. Only jpg, jpeg, and png are allowed.")
                    return render(request, 'edit_employee.html', {'form': form, 'employee': employee})

                # Check if the file is an actual image
                if not image.content_type.startswith('image/'):
                    form.add_error('Image', "The uploaded file is not a valid image.")
                    return render(request, 'edit_employee.html', {'form': form, 'employee': employee})

            # If everything is valid, save the form
            form.save()
            messages.success(request, 'Employee updated successfully!')
            return redirect('employee_list')

        else:
            messages.error(request, 'Please correct the errors below.')
            # Add a return to the edit page with the form showing the existing data and errors
            return render(request, 'edit_employee.html', {'form': form, 'employee': employee})

    else:
        # For GET request, just load the form with the existing employee data
        form = EmployeeForm(instance=employee)

    return render(request, 'edit_employee.html', {'form': form, 'employee': employee})

def delete_employee(request, id):
    if 'admin_id' not in request.session:
        return redirect('admin_login')  # Redirect to login if not authenticated

    employee = get_object_or_404(Employee, id=id)

    # Delete the employee
    employee.delete()

    # Redirect to employee list page with a success message
    return redirect('employee_list')