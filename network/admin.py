from django.contrib import admin

from network.models import NetworkLink, Product, Contact


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = (
        "country",
        "city",
    )


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        "product_name",
        "product_model",
    )


@admin.register(NetworkLink)
class NetworkLinkAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "type",
        "contact",
        "supplier",
        "debt",
    )
    list_display_links = (
        "supplier",
        "name",
    )
    list_filter = ("contact__city",)
    actions = ["clear_debt"]

    @admin.action(description="Очистить задолженность")
    def clear_debt(self, request, queryset):
        default_value = NetworkLink._meta.get_field("debt").default
        queryset.update(debt=default_value)
