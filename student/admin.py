from django.contrib import admin
from .models import Candidate

# Register your models here.


# class CandidateAdmin(admin.ModelAdmin):
#     list_per_page = 5
#     search_fields = ('firstname', 'secondname',)
#     list_display = ('name', 'age', 'phone', 'email', 'salary',)
#     list_editable = ('age', 'phone', 'email', 'salary',)
#     readonly_fields = ('language', 'libraries', 'firstname', 'secondname', 'age', 'email', 'others', 'mobile', 'databases', 'frameworks', 'job', 'situation', 'experience', 'gender', 'smoker', 'salary', 'file', 'phone', 'personality', 'messag',)
#     exclude = ('situation',)

admin.site.register(Candidate)

