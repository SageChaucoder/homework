from django.contrib import admin

# Register your models here.

from .models import Member, Product, Employee
from import_export.admin import ImportExportModelAdmin

admin.site.register(Member, ImportExportModelAdmin)
admin.site.register(Product, ImportExportModelAdmin)
admin.site.register(Employee, ImportExportModelAdmin)