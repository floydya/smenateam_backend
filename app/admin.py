from django.contrib import admin

from .models import Printer, Check


@admin.register(Printer)
class PrinterAdmin(admin.ModelAdmin):
    pass


@admin.register(Check)
class CheckAdmin(admin.ModelAdmin):
    list_filter = ('printer', 'status', 'printer__check_type')
    list_display = ('id', 'printer', 'get_check_type', 'status',)
    readonly_fields = ('get_check_type',)

    def get_check_type(self, obj):
        return obj.printer.check_type
    get_check_type.short_description = "Check type"
