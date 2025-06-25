from django.db import models


class Contact(models.Model):
    email = models.CharField(max_length=100, verbose_name="Почта")
    country = models.CharField(max_length=100, verbose_name="Страна")
    city = models.CharField(max_length=150, verbose_name="Город")
    street = models.CharField(max_length=150, verbose_name="Улица")
    building = models.CharField(max_length=20, verbose_name="Номер дома")
    network_link = models.ForeignKey(
        "NetworkLink",
        verbose_name="Звено",
        on_delete=models.CASCADE,
        related_name="NetworkLink",
        blank=True,
        null=True,
    )

    class Mete:
        verbose_name = "Контакт"
        verbose_name_plural = "Контакты"

    def __str__(self):
        return (
            f"{self.email}; {self.country}, {self.city}, {self.street}, {self.building}"
        )


class Product(models.Model):
    product_name = models.CharField(
        max_length=150, verbose_name="Наименование продукта"
    )
    product_model = models.CharField(max_length=100, verbose_name="Модель продукта")
    product_date = models.DateField(verbose_name="Дата выхода")

    class Mete:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"

    def __str__(self):
        return f"{self.product_name} - {self.product_model}"


class NetworkLink(models.Model):
    PLANT = "plant"
    RETAIL = "retail"
    ENTREPRENEUR = "entrepreneur"

    LINK_TYPE = (
        (PLANT, "завод"),
        (RETAIL, "розница"),
        (ENTREPRENEUR, "ип"),
    )
    name = models.CharField(max_length=150, verbose_name="Наименование")
    type = models.CharField(max_length=15, choices=LINK_TYPE, verbose_name="Тип")
    contact = models.OneToOneField(
        Contact,
        verbose_name="Контакты",
        on_delete=models.CASCADE,
        related_name="contact",
        blank=True,
        null=True,
    )
    product = models.ManyToManyField(
        Product,
        verbose_name="Продукт",
    )
    supplier = models.ForeignKey(
        "self",
        on_delete=models.CASCADE,
        verbose_name="Поставщик",
        blank=True,
        null=True,
        related_name="material_supplier",
    )
    debt = models.DecimalField(
        max_digits=10, decimal_places=2, verbose_name="Задолженность"
    )
    creation_date = models.DateField(verbose_name="Дата создания")

    class Meta:
        verbose_name = "Звено"
        verbose_name_plural = "Звенья"

    def __str__(self):
        return f"{self.type} {self.name}"
