Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
1. Membuat repository di github dan lokal bernama inventoria.
2. Menghubungkan repositori lokal dengan repositori di GitHub dengan command:
    "git branch -M main"
    "git remote add origin https://github.com/ArditheusIH/inventoria.git"
3. Membuat virtual environment pada directory inventoria dengan command:
    "python -m venv env"
    dan mengaktifkannya dengan command:
    "env\Scripts\activate"
4. membuat berkas requirements.txt dan menambahkan beberapa dependencies.Kemudian install dengan command
    "pip install -r requirements.txt"
5. Buat proyek Django baru bernama inventoria dengan command
    "django-admin startproject inventoria ."
6. Tambahkan * pada ALLOWED_HOSTS di berkas settings.py
7. Membuat berkas .gitignore dan melakukan add, commit, dan push ke github.
8. Membuat aplikasi dengan nama main dengan command
    "python manage.py startapp main"
9. menambahkan aplikasi main ke proyek inventoria
10. membuat template html main.html yang berisi
    "<h1>Inventory</h1>
    <h5>Name: </h5>
    <p>{{ name }}<p>
    <h5>Amount: </h5>
    <p>{{ amount }}<p>
    <h5>Price: </h5>
    <p>{{ price }}<p>
    <h5>Description: </h5>
    <p>{{ description }}<p>
    "
11. mengisi models.py dengan
    "class Product(models.Model):
    name = models.CharField(max_length=255)
    amount = models.IntegerField()
    price = models.IntegerField()
    description = models.TextField()"
12. memigrasi model dengan command
    "python manage.py makemigrations" lalu
    "python manage.py migrate"

13. Mengisi views.py dengan
    "
    from django.shortcuts import render

    
    def show_main(request):
        context = {
            'name': 'Minyak goreng',
            'amount': '100',
            'price': '20000',
            'description': 'Minyak untuk menggoreng makanan',
        }

        return render(request, "main.html", context)
        "
14.  membuat urls.py di dalam main
    "
    from django.urls import path
    from main.views import show_main

    app_name = 'main'

    urlpatterns = [
        path('', show_main, name='show_main'),
    ]
    "
15. mengisi menambahkan "path('main/', include('main.urls'))," pada urls.py di dalam inventoria
16. melakukan testing
17. melakukan add commit push ke github
18. mendeploy ke adaptable.io

