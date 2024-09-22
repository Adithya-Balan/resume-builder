from django.contrib import admin
from .models import skill, userinfo, education, others, working_info

# Register your models here.
admin.site.register(skill)
admin.site.register(userinfo)
admin.site.register(others)
admin.site.register(working_info)
admin.site.register(education)



