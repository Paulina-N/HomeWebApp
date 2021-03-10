from django.shortcuts import render, redirect
from django.contrib import messages
from products.choices import lighting_choices, scents_candles, home_decor, electronics
from .models import Contact

def contact_us(request):
    context = {
        'lighting_choices': lighting_choices,
        'scents_candles': scents_candles,
        'home_decor': home_decor,
        'electronics': electronics,
    }

    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        message = request.POST['message']

        contact = Contact(name=name, email=email, message=message)

        contact.save()

        messages.success(request, 'Your request has been submitted, we will get back to you soon')
        return redirect('contact_us')

    return render(request, 'pages/contact_us.html', context)
