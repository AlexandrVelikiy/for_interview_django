from django.db import models


class IngredientType(models.Model):
    name = models.CharField(max_length=250)

    class Meta:
        verbose_name = "Ingredient Type"
        verbose_name_plural = "Ingredients Type"

    def __str__(self):
        return self.name


class Ingredient(models.Model):
    name = models.CharField(max_length=100)
    ingredients_type = models.ForeignKey(IngredientType, related_name='type_of_ingredients', on_delete=models.CASCADE)
    price = models.FloatField()

    class Meta:
        verbose_name = "Ingredient"
        verbose_name_plural = "Ingredients"

    def __str__(self):
        return self.name


class Pizza(models.Model):
    name = models.CharField(max_length=100, null=True)
    ingredients = models.ManyToManyField(Ingredient, related_name='ingredients')
    amount = models.IntegerField()

    class Meta:
        verbose_name = "Pizza"
        verbose_name_plural = "Pizzas"

    def __str__(self):
        return f"{self.name} for {self.amount}$"
