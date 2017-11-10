from django.contrib import admin

# Register your models here.

from .models import Case

class CaseAdmin(admin.ModelAdmin):

    class Meta:
        model = Case

admin.site.register(Case, CaseAdmin)
