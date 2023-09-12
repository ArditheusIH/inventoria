from django.shortcuts import render


# Create your views here.
def show_main(request):
    context = {
        'name': 'Minyak goreng',
        'amount': '100',
        'price': '20000',
        'description': 'Minyak untuk menggoreng makanan',
    }

    return render(request, "main.html", context)