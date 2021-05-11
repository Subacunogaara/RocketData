from django.contrib import admin
from .models import EmployeeModel


def clear_total_paid(modeladmin, request, queryset):
    queryset.update(total_paid=f'{0}')
clear_total_paid.short_description = "Удалить информацию о выплаченной заработной плате"



class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'patronymic', 'position', 'chief', 'salary', 'total_paid',)
    list_filter = ('position', 'level',)
    actions = [clear_total_paid]







admin.site.register(EmployeeModel, EmployeeAdmin)



