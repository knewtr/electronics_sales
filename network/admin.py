from django.contrib import admin

from network.models import Entrepreneur, Plant, Retail, Supplier


@admin.register(Plant)
class PlantAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "country",
        "city",
        "product_name",
        "supplier",
    )
    list_display_links = ("supplier", "name")
    list_filter = ["city"]
    actions = ["clear_debt"]

    @admin.action(description="Очистить задолженность")
    def clear_debt(self, request, queryset):
        default_value = Plant._meta.get_field("debt").default
        queryset.update(debt=default_value)


@admin.register(Retail)
class RetailAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "country",
        "city",
        "product_name",
        "supplier",
    )
    list_display_links = ("supplier", "name")
    list_filter = ["city"]
    actions = ["clear_debt"]

    @admin.action(description="Очистить задолженность")
    def clear_debt(self, request, queryset):
        default_value = Retail._meta.get_field("debt").default
        queryset.update(debt=default_value)


@admin.register(Entrepreneur)
class EntrepreneurAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "country",
        "city",
        "product_name",
        "supplier",
    )
    list_display_links = ("supplier", "name")
    list_filter = ["city"]
    actions = ["clear_debt"]

    @admin.action(description="Очистить задолженность")
    def clear_debt(self, request, queryset):
        default_value = Entrepreneur._meta.get_field("debt").default
        queryset.update(debt=default_value)
