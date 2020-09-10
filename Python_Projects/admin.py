from django.contrib import admin
from .models import djangoClasses
from .models import graphicDesign
from .models import cyberSecurity
from .models import helpDesk
# Register your models here.


admin.site.register(djangoClasses)
admin.site.register(graphicDesign)
admin.site.register(cyberSecurity)
admin.site.register(helpDesk)