from django.db import models
from django.urls import reverse

#creating our product model, this maps a product object to the database that stores our inventory of products
class Product(models.Model):
	name = models.CharField(max_length = 60, default="Item")
	quantity = models.IntegerField(default=0)
	price = models.DecimalField(decimal_places=2, max_digits=100)
	status = models.CharField(max_length= 100, default="available")

	def get_absolute_url(self):
		return reverse("products:product-detail",kwargs={"id": self.id})#f"/products/{self.id}"