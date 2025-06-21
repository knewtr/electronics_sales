from django.db import models


class Supplier(models.Model):
    name = models.CharField(max_length=150, verbose_name="Наименование поставщика")

    class Meta:
        verbose_name = "Поставщик"
        verbose_name_plural = "Поставщики"


class Plant(models.Model):
    name = models.CharField(max_length=150, verbose_name="Наименование завода")
    email = models.CharField(max_length=100, verbose_name="Почта")
    country = models.CharField(max_length=100, verbose_name="Страна")
    city = models.CharField(max_length=150, verbose_name="Город")
    street = models.CharField(max_length=150, verbose_name="Улица")
    building = models.CharField(max_length=20, verbose_name="Номер дома")
    product_name = models.CharField(
        max_length=150, verbose_name="Наименование продукта"
    )
    product_model = models.CharField(max_length=100, verbose_name="Модель продукта")
    product_date = models.DateField(verbose_name="Дата выхода")
    supplier = models.ForeignKey(
        Supplier,
        on_delete=models.CASCADE,
        verbose_name="Поставщик",
        blank=True,
        null=True,
        related_name="plant",
    )
    debt = models.FloatField(default=0.0, verbose_name="Задолженность")
    creation_date = models.DateField(verbose_name="Дата создания")

    class Meta:
        verbose_name = "Завод"
        verbose_name_plural = "Заводы"

    def __str__(self):
        return f"{self.name} - {self.product_name}"


class Retail(models.Model):
    name = models.CharField(max_length=150, verbose_name="Наименование розничной сети")
    email = models.CharField(max_length=100, verbose_name="Почта")
    country = models.CharField(max_length=100, verbose_name="Страна")
    city = models.CharField(max_length=150, verbose_name="Город")
    street = models.CharField(max_length=150, verbose_name="Улица")
    building = models.CharField(max_length=20, verbose_name="Номер дома")
    product_name = models.CharField(
        max_length=150, verbose_name="Наименование продукта"
    )
    product_model = models.CharField(max_length=100, verbose_name="Модель продукта")
    product_date = models.DateField(verbose_name="Дата выхода")
    supplier = models.ForeignKey(
        Supplier,
        on_delete=models.CASCADE,
        verbose_name="Поставщик",
        blank=True,
        null=True,
        related_name="retail",
    )
    debt = models.FloatField(default=0.0, verbose_name="Задолженность")
    creation_date = models.DateField(verbose_name="Дата создания")

    class Meta:
        verbose_name = "Розничная сеть"
        verbose_name_plural = "Розничные сети"

    def __str__(self):
        return f"{self.name} - {self.product_name}"


class Entrepreneur(models.Model):
    name = models.CharField(max_length=150, verbose_name="Наименование ИП")
    email = models.CharField(max_length=100, verbose_name="Почта")
    country = models.CharField(max_length=100, verbose_name="Страна")
    city = models.CharField(max_length=150, verbose_name="Город")
    street = models.CharField(max_length=150, verbose_name="Улица")
    building = models.CharField(max_length=20, verbose_name="Номер дома")
    product_name = models.CharField(
        max_length=150, verbose_name="Наименование продукта"
    )
    product_model = models.CharField(max_length=100, verbose_name="Модель продукта")
    product_date = models.DateField(verbose_name="Дата выхода")
    supplier = models.ForeignKey(
        Supplier,
        on_delete=models.CASCADE,
        verbose_name="Поставщик",
        blank=True,
        null=True,
        related_name="entrepreneur",
    )
    debt = models.FloatField(default=0.00, verbose_name="Задолженность")
    creation_date = models.DateField(verbose_name="Дата создания")

    class Meta:
        verbose_name = "Индивидуальный предприниматель"
        verbose_name_plural = "Индивидуальные предприниматели"

    def __str__(self):
        return f"{self.name} - {self.product_name}"
