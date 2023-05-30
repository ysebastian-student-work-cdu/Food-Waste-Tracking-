from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse

from .models import Payment

@csrf_exempt
def initiate_payment(request):
    if request.method == 'POST':
        amount = float(request.POST.get('amount', 0))
        if amount <= 0:
            return JsonResponse({'error': 'Invalid amount.'})

        payment = Payment.objects.create(amount=amount)
        payment.save()

        return JsonResponse({'payment_id': payment.id, 'amount': payment.amount})
    else:
        return JsonResponse({'error': 'Invalid request method.'})

def complete_payment(request, payment_id):
    try:
        payment = Payment.objects.get(pk=payment_id)
    except Payment.DoesNotExist:
        return JsonResponse({'error': 'Payment not found.'})

    payment.status = 'completed'
    payment.save()

    return JsonResponse({'message': 'Payment completed successfully.'})
