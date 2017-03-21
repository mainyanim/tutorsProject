from django.contrib import admin
from accounts.models import UserProfile, Subject, Language
# Register your models here.
admin.site.register(UserProfile)
admin.site.register(Subject)
admin.site.register(Language)
