from django.shortcuts import render, redirect
from django.conf import settings
import moncashify
# Create your views here.
def index(request):
    return render(request,'home.html',{})

def donate(request):
    if request.method == 'POST':
        amount = int(request.POST['amount'])
        order_id = 'Donation'
        
        moncash = moncashify.API(settings.MONCASH_CLIENT_ID, settings.MONCASH_SECRET_KEY, True)
        payment = moncash.payment(order_id, amount)
    
        return redirect(payment.redirect_url)
    return render(request, 'donate.html', {})