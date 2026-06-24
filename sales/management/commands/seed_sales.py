from django.core.management.base import BaseCommand
from django.utils import timezone
from sales.models import SaleRecord
import random
from datetime import timedelta
from decimal import Decimal

class Command(BaseCommand):
    help = 'Seed the database with a year of random data'

    def handle(self, *args, **kwargs):
        SaleRecord.objects.all().delete()  # Clear existing data

        start = timezone.now().date().replace(month=1, day=1)  # Start from the beginning of the year
        records = []

        for i in range(365):  # For each day of the year
            sales = random.randint(100, 1000)  # Random sales amount
            unit_price = Decimal(str(round(random.uniform(10, 50))))
            revenue = unit_price * sales  # Calculate revenue based on sales and unit price

            records.append(SaleRecord(
                date=start + timedelta(days=i),
                sales = sales,
                returns = random.randint(0, 100),
                revenue = revenue,
            ))

        SaleRecord.objects.bulk_create(records)  # Bulk create for efficiency
        self.stdout.write(self.style.SUCCESS(f'Created {len(records)} sale records for the year.'))