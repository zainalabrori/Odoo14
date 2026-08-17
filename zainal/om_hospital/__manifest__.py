# File Manifest berisi metadata (informasi utama) tentang modul Odoo kamu
{
    # Nama modul yang akan tampil di halaman Apps Odoo
    'name': 'Hospital Management',

    # Versi modul (biasanya diawali versi Odoo, misal: 14.0.1.0.0)
    'version': '1.0.0',

    # Ringkasan singkat fungsi modul
    'summary': 'Hospital Management Software',

    # Penjelasan lebih rinci mengenai modul
    'description': """Modul ini digunakan untuk mengelola data dan operasional rumah sakit.""",

    # Kategori modul di dalam Odoo Apps (misal: Productivity, Sales, Extra Tools)
    'category': 'Productivity',

    # Nama pembuat atau nama perusahaan pengembang
    'author': 'Zainal Abrori',

    # Situs web pengembang
    'website': 'https://www.odoomates.tech',

    # Lisensi modul (LGPL-3 adalah lisensi open-source standar Odoo)
    'license': 'LGPL-3',

    # Modul lain yang wajib ter-install sebelum modul ini bisa di-install
    # Biarkan kosong jika tidak bergantung pada modul lain
    'depends': [],

    # Tempat mendaftarkan file XML/CSV (View, Data, Security)
    'data': [
        'views/patient_view.xml',
    ],

    # Tempat mendaftarkan file demo data
    'demo': [],

    # Menentukan urutan tampil modul di daftar Apps (makin kecil nilainya, makin atas posisinya)
    'sequence': -100,

    # Menandakan apakah folder ini dianggap sebagai Aplikasi Utama di menu Apps
    'application': True,

    # Menandakan apakah modul ini dapat di-install secara manual
    'installable': True,

    # Jika True, modul akan ter-install otomatis jika semua dependensinya ter-install
    'auto_install': False,
}
