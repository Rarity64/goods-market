from django.contrib import admin
from .models import Good, UserProfile, EmailDigest

admin.site.register(Good)
admin.site.register(UserProfile)
admin.site.register(EmailDigest)