from django.contrib import admin
from signin.models import Register
from signin.models import UploadImage
# Register your models here.
admin.site.register(Register)
admin.site.register(UploadImage)