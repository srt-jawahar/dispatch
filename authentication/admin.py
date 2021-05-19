from django.contrib import admin

from .models import User, Role

# Register your models here.

admin.site.register(User)
admin.site.register(Role)
admin.site.site_header = "Dispatch Planner Administration"
admin.site.site_title = "Manange Master Data"
admin.site.index_title = "Responsibilities"
