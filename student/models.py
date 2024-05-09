from django.db import models
from multiselectfield import MultiSelectField

# Create your models here.

GENDER = (
    ('Male', 'Male'),
    ('Female', 'Female'),
)

SMOKER = (
    ('Yes', 'Yes'),
    ('No', 'No'),
)

PERSONALITY = (
    ('', 'Enter your personality'),
    ('Am soo Quity', 'Am soo Quity'),
    ('Am talkative', 'Am talkative'),
    ('Am moderate', 'Am moderate')
)

SITUATION = (
    ('pending', 'pending'),
    ('approved', 'approved'),
    ('woooo', 'woooo'),
    ('zeeeee', 'zeeeee')
)

SALARY = (
    ('Less to 300,000', 'Less to 300,000'),
    ('Is between 300,000 and 700,000', 'Is between 300,000 and 700,000'),
    ('Is between 700,000 and 1,000,000', 'Is between 700,000 and 1,000,000'),
    ('It greater to 1,000,000', 'It greater to 1,000,000'),
)

EXPERIENCE = (
    ('programming', 'Programming'),
    ('Accounting', 'Accounting'),
    ('Developing', 'Developing'),
    ('Software Engineering', 'Software Engineering'),
    ('Fullstack Engineering', 'Fullstack Engineering'),
    ('Front-end Engineering', 'Front-end Engineering')
)

# These for multifield selections

LANGUAGE = (
    ('Python','Python'),
    ('Php','Php'),
    ('Javascript','Javascript'),
    ('Ruby','Ruby'),
    ('C++','C++'),
    ('Others','Others'),
)

FRAMEWORKS = (
    ('Django','Django'),
    ('Laravel','Laravel'),
    ('Flask','Flask'),
    ('Bootspring','Bootspring'),
    ('Vue','Vue'),
    ('Others','Others'),
)

DATABASES = (
    ('MySQL','MySQL'),
    ('SQLite','SQLite'),
    ('Postgre','Postgre'),
    ('MongoDB','MongoDB'),
    ('MariaDB','MariaDB'),
    ('Others','Others'),
)

LIBRARIES = (
    ('Ajax','MySQL'),
    ('Jquery','Jquery'),
    ('React','React'),
    ('Chart.js','Chart'),
    ('Gsap','Gsap'),
    ('Others','Others'),
)

MOBILE = (
    ('React native','React native'),
    ('Kivy','Kivy'),
    ('Flutter','Flutter'),
    ('Xamarin','Xamarin'),
    ('Ionic','Ionic'),
    ('Others','Others'),
)

OTHERS = (
    ('UML','React native'),
    ('SQL','SQL'),
    ('GIT','GIT'),
    ('Docker','Docker'),
    ('GraphQL','GraphQL'),
    ('Others','Others'),
)



class Candidate(models.Model):
    firstname = models.CharField(max_length=50)
    secondname = models.CharField(max_length=50)
    email = models.EmailField(max_length=60)
    phone = models.CharField(default=0)
    personality = models.CharField(max_length=50, null=False, choices=PERSONALITY)
    gender = models.CharField(max_length=7, null=False)
    experience = models.BooleanField(default=False)  # Change this line
    smoker = models.CharField(max_length=3, null=False, choices=SMOKER, default='Yes')
    situation = models.CharField(max_length=8, null=False, choices=SITUATION, default='pending')
    job = models.CharField(max_length=50, null=False, default='Developing')
    messag = models.TextField(max_length=200)
    salary = models.CharField(max_length=60, null=False, choices=SALARY)
    age = models.CharField(max_length=3)
    phone = models.CharField(max_length=13)
    file = models.FileField(upload_to='documents')
    created_at = models.DateTimeField(auto_now_add=True)
    
      #This is for multiple selection 
    # language = MultiSelectField(validators=[0], choices=LANGUAGE, default="")
    # frameworks = MultiSelectField(validators=[0], choices=FRAMEWORKS, default="")
    # databases = MultiSelectField(validators=[0], choices=DATABASES, default="")
    # libraries = MultiSelectField(validators=[0], choices=LIBRARIES, default="")
    # mobile = MultiSelectField(validators=[0], choices=MOBILE, default="")
    # others = MultiSelectField(validators=[0], choices=OTHERS, default="")


    def __str__(self):
        return self.firstname
    
    def name(unganisha):
        return "%s %s" % (unganisha.firstname, unganisha.secondname)
