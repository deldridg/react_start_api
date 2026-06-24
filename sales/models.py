from django.db import models

# Create your models here.
class SaleRecord(models.Model):
    date = models.DateField()
    sales = models.IntegerField()
    returns = models.IntegerField()
    revenue = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)

    class Meta:
        ordering = ['date']  # Order by date ascending

    def __str__(self):
        return f"Date: {self.date}, Sales: {self.sales}, Revenue: {self.revenue}"