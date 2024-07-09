from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(User)
admin.site.register(Chat)
admin.site.register(DeleteRequest)
admin.site.register(Feedback)
admin.site.register(Book)