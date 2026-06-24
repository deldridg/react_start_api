from django.http import JsonResponse
from .models import SaleRecord

# Create your views here.
def sales_data(request):
    start = request.GET.get('start')
    end = request.GET.get('end')

    qs = SaleRecord.objects.all()

    if start:
        qs = qs.filter(date__gte=start)
    if end:
        qs = qs.filter(date__lte=end)

    data = list(qs.values('date', 'sales', 'returns', 'revenue'))

    # Convert date objects to string format for JSON serialization
    for row in data:
        row['date'] = str(row['date'])
        row['revenue'] = float(row['revenue'])  # Convert Decimal to float for JSON serialization

    return JsonResponse(data, safe=False)