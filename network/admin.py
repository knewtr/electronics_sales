from django.contrib import admin

from network.models import Contact, NetworkLink, Product


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = (
        "email",
        "country",
        "city",
    )
    list_filter = (
        "country",
        "city",
    )


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        "product_name",
        "product_model",
    )
    list_filter = (
        "product_model",
        "product_date",
    )


@admin.register(NetworkLink)
class NetworkLinkAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "name",
        "type",
        "supplier",
        "debt",
    )
    list_display_links = (
        "supplier",
        "name",
    )
    list_filter = (
        "contact__city",
        "contact__country",
    )
    actions = ["clear_debt"]

    @admin.action(description="Очистить задолженность")
    def clear_debt(self, request, queryset):
        return queryset.update(debt=0.00)
