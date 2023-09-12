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
    "django-admin startproject shopping_list ."
6. Tambahkan * pada ALLOWED_HOSTS di berkas settings.py