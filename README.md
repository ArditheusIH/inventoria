link app: https://inventori.adaptable.app/main/

Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
1. Membuat repository di github dan lokal bernama inventoria.
2. Menghubungkan repositori lokal dengan repositori di GitHub dengan command:
    `git branch -M main` dan
    `git remote add origin https://github.com/ArditheusIH/inventoria.git`
3. Membuat virtual environment pada directory inventoria dengan command:
    `python -m venv env`
    dan mengaktifkannya dengan command:
    `env\Scripts\activate`
4. membuat berkas requirements.txt dan menambahkan beberapa dependencies.Kemudian install dengan command
    `pip install -r requirements.txt`
5. Buat proyek Django baru bernama inventoria dengan command
    `django-admin startproject inventoria .`
6. Tambahkan * pada ALLOWED_HOSTS di berkas settings.py
7. Membuat berkas .gitignore dan melakukan add, commit, dan push ke github.
    ```
    # Django
    *.log
    *.pot
    *.pyc
    __pycache__
    db.sqlite3
    media

    # Backup files
    *.bak 

    # If you are using PyCharm
    # User-specific stuff
    .idea/**/workspace.xml
    .idea/**/tasks.xml
    .idea/**/usage.statistics.xml
    .idea/**/dictionaries
    .idea/**/shelf

    # AWS User-specific
    .idea/**/aws.xml

    # Generated files
    .idea/**/contentModel.xml

    # Sensitive or high-churn files
    .idea/**/dataSources/
    .idea/**/dataSources.ids
    .idea/**/dataSources.local.xml
    .idea/**/sqlDataSources.xml
    .idea/**/dynamic.xml
    .idea/**/uiDesigner.xml
    .idea/**/dbnavigator.xml

    # Gradle
    .idea/**/gradle.xml
    .idea/**/libraries

    # File-based project format
    *.iws

    # IntelliJ
    out/

    # JIRA plugin
    atlassian-ide-plugin.xml

    # Python
    *.py[cod] 
    *$py.class 

    # Distribution / packaging 
    .Python build/ 
    develop-eggs/ 
    dist/ 
    downloads/ 
    eggs/ 
    .eggs/ 
    lib/ 
    lib64/ 
    parts/ 
    sdist/ 
    var/ 
    wheels/ 
    *.egg-info/ 
    .installed.cfg 
    *.egg 
    *.manifest 
    *.spec 

    # Installer logs 
    pip-log.txt 
    pip-delete-this-directory.txt 

    # Unit test / coverage reports 
    htmlcov/ 
    .tox/ 
    .coverage 
    .coverage.* 
    .cache 
    .pytest_cache/ 
    nosetests.xml 
    coverage.xml 
    *.cover 
    .hypothesis/ 

    # Jupyter Notebook 
    .ipynb_checkpoints 

    # pyenv 
    .python-version 

    # celery 
    celerybeat-schedule.* 

    # SageMath parsed files 
    *.sage.py 

    # Environments 
    .env 
    .venv 
    env/ 
    venv/ 
    ENV/ 
    env.bak/ 
    venv.bak/ 

    # mkdocs documentation 
    /site 

    # mypy 
    .mypy_cache/ 

    # Sublime Text
    *.tmlanguage.cache 
    *.tmPreferences.cache 
    *.stTheme.cache 
    *.sublime-workspace 
    *.sublime-project 

    # sftp configuration file 
    sftp-config.json 

    # Package control specific files Package 
    Control.last-run 
    Control.ca-list 
    Control.ca-bundle 
    Control.system-ca-bundle 
    GitHub.sublime-settings 

    # Visual Studio Code
    .vscode/* 
    !.vscode/settings.json 
    !.vscode/tasks.json 
    !.vscode/launch.json 
    !.vscode/extensions.json 
    .history
    ```
8. Membuat aplikasi dengan nama main dengan command
    `python manage.py startapp main`
9. menambahkan aplikasi main ke proyek inventoria
10. membuat template html main.html yang berisi
    ```   
    <h1>Inventory</h1>
    <h5>Name: </h5>
    <p>{{ name }}<p>
    <h5>Amount: </h5>
    <p>{{ amount }}<p>
    <h5>Price: </h5>
    <p>{{ price }}<p>
    <h5>Description: </h5>
    <p>{{ description }}<p>
    ```
11. mengisi models.py dengan
    ```
    class Product(models.Model):
    name = models.CharField(max_length=255)
    amount = models.IntegerField()
    price = models.IntegerField()
    description = models.TextField()"
    ```
12. memigrasi model dengan command `python manage.py makemigrations` lalu `python manage.py migrate`

13. Mengisi views.py dengan
    ```
    from django.shortcuts import render
    def show_main(request):
        context = {
            'name': 'Minyak goreng',
            'amount': '100',
            'price': '20000',
            'description': 'Minyak untuk menggoreng makanan',
        }

        return render(request, "main.html", context)
    ```
14. membuat urls.py di dalam main
    ``` 
    from django.urls import path
    from main.views import show_main

    app_name = 'main'

    urlpatterns = [
        path('', show_main, name='show_main'),
    ]
    ```
    
15. mengisi menambahkan `path('main/', include('main.urls')),` pada urls.py di dalam inventoria
16. melakukan testing
    ```
    from django.test import TestCase
    from main.models import Product

    '''This test checks if the attributes are using the correct data type'''
    class mainTest(TestCase):
        def test_field_data_type(self):
            product = Product(name="minyak", amount=100, price=20000, description="goreng")
            
            self.assertIsInstance(product.name, str)
            self.assertIsInstance(product.amount, int)
            self.assertIsInstance(product.price, int)
            self.assertIsInstance(product.description, str)
    ```
17. melakukan add commit push ke github
18. mendeploy ke adaptable.io

Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html
![bagan](bagan.png)
    `urls.py` berfungsi untuk mengatur rute yang diinginkan (dalam kasus ini app main) sehingga web yang dibuka adalah main. `models.py` berfungsi untuk mengatur struktur database dan mengakses data. `views.py` berisi logic aplikasinya. Setelah menerima permintaan dari router(`urls.py`), `views.py` akan memproses permintaan tersebut, mengambil atau memanipulasi data dari `models.py`, dan kemudian merender template HTML. `main.html` untuk merancang tampilan yang  diisi dengan data dari `models.py` melalui `views.py`

Jelaskan mengapa kita menggunakan virtual environment? Apakah kita tetap dapat membuat aplikasi web berbasis Django tanpa menggunakan virtual environment?
    Ada beberapa alasan kita menggunakan virtual environment. Proyek kita menjadi lebih teratur dan bersih. Virtual environment memungkinkan kita untuk membuat lingkungan tertutup yang terpisah untuk setiap proyek yang berbeda. Kita juga bisa menginstall dependency yang berbeda-beda untuk setiap proyek.
    Kita bisa saja tidak menggunakan virtual environment, tetapi ini tidak bagus untuk mengerjakan lebih dari satu proyek karena hal ini membuat proyek-proyek berbagi sumber daya dan lingkungan yang sama padahal mungkin kebutuhannya berbeda-beda. 

Jelaskan apakah itu MVC, MVT, MVVM dan perbedaan dari ketiganya.
    MVC(Model-View-Controller) adalah suatu framework pola arsitektur yang membuat aplikasi terbagi ke dalam 3 komponen utama, yaitu model, view, serta controller. Controller berfungsi untuk menghubungkan dan mengontrol model serta view supaya bisa saling terkoneksi. Controller Bertanggung jawab untuk mengelola input pengguna, mengubah model sesuai dengan input tersebut, dan mengatur tampilan yang harus diperbarui.
    MVT(Model-View-Template) adalah sebuah konsep arsitektur yang diterapkan dalam pengembangan web dengan tujuan memisahkan elemen-elemen utama dari sebuah aplikasi. Konsep ini memungkinkan pengembang web untuk mengorganisasi dan mengelola kode dengan lebih terstruktur.
    MVVM(Model-View-ViewModel) mirip dengan MVC dan MVT. ViewModel berfungsi untuk mengelola tampilan dan logika tampilan. Ini berperan sebagai perantara antara model dan view, tetapi dengan lebih banyak kontrol terhadap tampilan. ViewModel biasanya mengikat data antara model dan view.

