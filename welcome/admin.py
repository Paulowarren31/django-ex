from django.contrib import admin

from .models import PageView, ExpenseAccount, ExpenseItem, ExpenseCategory

# Register your models here.


class PageViewAdmin(admin.ModelAdmin):
    list_display = ['hostname', 'timestamp']

admin.site.register(PageView, PageViewAdmin)
admin.site.register(ExpenseItem)
admin.site.register(ExpenseAccount)
admin.site.register(ExpenseCategory)
