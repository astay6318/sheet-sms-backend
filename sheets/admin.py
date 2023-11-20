from django.contrib import admin
from .models import Response,Form,Question,Answer

admin.site.register(Form)
admin.site.register(Question)
admin.site.register(Answer)
admin.site.register(Response) 
