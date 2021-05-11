from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html

from .models import EmployeeModel


def clear_total_paid(modeladmin, request, queryset):
    queryset.update(total_paid=f'{0}')


clear_total_paid.short_description = "Удалить информацию о выплаченной заработной плате"


class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'patronymic',
                    'position', 'link_to_chief', 'salary', 'total_paid',
                    )
    list_filter = ('position', 'level',)
    actions = [clear_total_paid]


    def link_to_chief(self, obj):
        link = reverse("admin:staff_employeemodel_change", args=[obj.chief_id])
        return format_html('<a href="{}">{}</a>', link, obj.chief)

    link_to_chief.short_description = 'Chief'

admin.site.register(EmployeeModel, EmployeeAdmin)



