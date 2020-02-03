from django import forms

from eapp1.models import Employee

# class EmployeeForm(forms.ModelForm):
#     class Meta:
#         model =  Employee
#         fields ='__all__'

class EmployeeForm(forms.ModelForm):
    eno = forms.IntegerField(
        label='Eno',
        widget=forms.NumberInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'eno'
            }
        ), required=True )
    name = forms.CharField(
        label='Name',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Name'
            }
        ),required=True, max_length= 50)


    Pan_number = forms.CharField(
        label='Pan number',
        widget=forms.TextInput(
            attrs={
                 'class': 'form-control',
                'placeholder': 'Pan number'
            }
        ),required=True, max_length= 50)


    age = forms.IntegerField(
        label='Age',
        widget=forms.NumberInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Age'
            }
        ),required=True, max_value= 65)



    gender = forms.CharField(
        label='Gender',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Gender'
            }
        ),required=True,max_length=1
    )
    email = forms.EmailField(
        label='Enter Your Email ID',
        widget=forms.EmailInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Email ID'
            }
        ),required=True,max_length=50
    )

    city = forms.CharField(
        label='Enter Your City Name',
        widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'city'
        }
        ),required=True,max_length=50
    )
    class Meta():
        model = Employee
        fields =['eno','ename','age','pan_no','email','city_name']

    #class
