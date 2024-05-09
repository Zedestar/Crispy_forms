from django import forms
from .models import Candidate,  GENDER, SMOKER
from django.core.validators import RegexValidator

# - Creatinng the forms here 

class AddStudent(forms.ModelForm):

    firstname = forms.CharField(
    label='First Name', min_length=3, max_length=50,
    required=True,
    validators=[
        RegexValidator(
            regex=r'^[a-zA-Z]*$',
            message='Only letters are allowed',
            code='invalid_letters',
        ),
    ],
    widget=forms.TextInput(
        attrs={
            'placeholder':'Enter your first name',
            'autocomplete':'off',
        }
    ),
    )


    secondname = forms.CharField(
        label='Second Name', min_length=3, max_length=50,
        required=True,
        validators=[
            RegexValidator(
                regex=r'^[a-zA-Z]*$',
                message='Only letters are allowed',
                code='invalid_letters',
            ),
        ],
        widget=forms.TextInput(
            attrs={
                'placeholder':'Enter your second name',
                'autocomplete':'off',
            }
        ),
    )

    job = forms.CharField(
        label='Your Job', min_length=3, max_length=50,
        required=True,
        validators=[
            RegexValidator(
                regex=r'^[a-zA-Z\s]*$',
                message='Only letters are allowed',
                code='invalid_letters',
            ),
        ],
        widget=forms.TextInput(
            attrs={
                'placeholder':'Enter your Job',
                'autocomplete':'off',
            }
        ),
    )

    age = forms.CharField(
        label='Your age', min_length=1, max_length=3,
        required=True,
        widget=forms.NumberInput(
            attrs={
                'placeholder':'Enter your age',
                'autocomplete':'off',
            }
        ),
    )

    phone = forms.CharField(
        label='Phone Number', min_length=12, max_length=12,
        required=True,
        widget=forms.NumberInput(
            attrs={
                'placeholder':'Enter your phone number',
                'autocomplete':'off',
            }
        ),
    )

    gender = forms.ChoiceField(
        label='Gender',
        required=True,
        choices=GENDER,
        widget=forms.RadioSelect(
            attrs={
                'placeholder':'What is your gender',
                'autocomplete':'off',
            }
        ),
    )

    smoker = forms.ChoiceField(
        label='Smoking',
        required=True,
        choices=SMOKER,
        widget=forms.RadioSelect(
            attrs={
                'placeholder':'Are you smoking',
                'autocomplete':'off',
            }
        ),
    )

    experience = forms.BooleanField(
        label='I have an experience',
        required=True,
        widget=forms.CheckboxInput(
            attrs={
                'placeholder':'Are you smoking',
                'autocomplete':'off',
            }
        ),
    )

    email = forms.CharField(
        label='Your email', min_length=3, max_length=50,
        required=True,
        validators=[
            RegexValidator(
                regex=r'^[\w\.-]+@[\w\.-]+\.\w+$',
                message='Enter valid email example zede@gmail.com',
                code='invalid email',
            ),
        ],
        widget=forms.TextInput(
            attrs={
                'placeholder':'Enter your email',
                'autocomplete':'off',
            }
        ),
    )

    class Uppercase(forms.CharField):
        def to_python(self, value):
            return value.upper()

    messag = Uppercase(
        label='About you', min_length=50, max_length=500,
        required=True,
        widget=forms.Textarea(
            attrs={
                'placeholder':'Talk about your self especially your school life',
                'autocomplete':'off',
                'row':10,
                'style':'text-transform : capitalize; font-size : 13px',
            }
        ),
    )

    file = forms.FileField(
        label='Certificate', 
        required=True,
        widget=forms.ClearableFileInput(
            attrs={
                'placeholder':'Enter any your academy certificate',
                'autocomplete':'off',
            }
        ),
    )
    ######################          IT WORK             #####################
    #THIS MAKE THE FIELDS READ ONLY WHERE YOU CAN'T WRITE ANYTHING
    # def __init__(self, *args, **kwargs):
    #     super(AddStudent, self).__init__(*args, **kwargs)
    #     read_only = ['firstname', 'secondname', 'phone', 'age']
    #     for field in read_only:
    #        self.fields[field].widget.attrs['readonly'] = 'true'
        #################          IT DIDN'T WORK         #####################
        #self.fields['personality'].choices = [('','Select your personality'),] + list(self.fields['personality'].widgets.choices)[1:]
        #['phone'].widget.attrs.update[
        #    {
        #        'placeholder':'Kindly enter your phone number',
        #        'style':'font-size:32px; background-color:blue;'
        #    }
        #]        DOESNOT WORK 

    def clean_email(self):
        email_ndugu = self.cleaned_data.get('email')
        for obj in Candidate.objects.all():
            if obj.email == email_ndugu:
                raise forms.ValidationError('The email ' + email_ndugu + ' is already exist. Try another email')
        return email_ndugu
    class Meta:
        model = Candidate
        fields = "__all__"

        