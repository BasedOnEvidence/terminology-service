from django.contrib import admin
from terminology_service.terminology_dbms.models import (
    Directory, DirectoryItem
)


admin.site.register(Directory)
admin.site.register(DirectoryItem)
