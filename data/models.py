from django.db import models

# Jenis Kelamin
LAKILAKI = 'LK'
PEREMPUAN = 'PR'
JENIS_KELAMIN = [
    (LAKILAKI, 'Laki-Laki'),
    (PEREMPUAN, 'Perempuan'),
]

# Golongan Darah
GOLONGAN_DARAH = [
    ('A', 'A'),
    ('B', 'B'),
    ('AB', 'AB'),
    ('O', 'O'),
]

GOLONGAN_DARAH_RHESUS = [
    ('RP', 'Rhesus Positif'),
    ('RN', 'Rhesus Negatif'),
]

STATUS_PERNIKAHAN = [
    ('MENIKAH', 'Menikah'),
    ('BELUM_MENIKAH', 'Belum Menikah'),
    ('CERAI', 'Cerai'),
]

# https://en.wikipedia.org/wiki/Ethnic_groups_in_Indonesia
ETNIK = [
    ('ACEH', 'Aceh'),
    ('BALI', 'Bali'),
    ('BANTEN', 'Banten'),
    ('BANJAR', 'Banjar'),
    ('BATAK', 'Batak'),
    ('BETAWI', 'Betawi'),
    ('BUGIS', 'Bugis'),
    ('CIREBON', 'Cirebon'),
    ('DAYAK', 'Dayak'),
    ('GORONTALO', 'Gorontalo'),
    ('JAWA', 'Jawa'),
    ('LAMPUNG', 'Lampung'),
    ('MADURA', 'Madura'),
    ('MAKASAR', 'Makasar'),
    ('MELAYU', 'Melayu'),
    ('MINAHASA', 'Minahasa'),
    ('MINANGKABAU', 'Minangkabau'),
    ('NIAS', 'Nias'),
    ('PALEMBANG', 'Palembang'),
    ('TIONGHOA', 'Tionghoa'),
    ('SASAK', 'Sasak'),
    ('SUNDA', 'Sunda'),
    ('LAINNYA', 'Lainnya'),
]

# Pekerjaan
PEKERJAAN = [
    ('PNS', 'PNS'),
    ('TNI_POLRI', 'TNI/POLRI'),
    ('KARYAWAN_SWASTA', 'Karyawan Swasta'),
    ('WIRAUSAHA', 'Wirausaha'),
    ('PROF_MANDIRI_MEDIS', 'Profesional Mandiri Medis'),
    ('PROF_MANDIRI_HUKUM', 'Profesional Mandiri Hukum'),
    ('PROF_MANDIRI_PROYEK', 'Profesional Mandiri Tidak Tetap/Proyek/Konsultan'),
    ('PENSIUNAN', 'Pensiunan'),
    ('MAHASISWA', 'Mahasiswa'),
    ('PELAJAR', 'Pelajar'),
    ('RUMAH_TANGGA', 'Bapak/Ibu Rumah Tangga'),
    ('LAINNYA', 'Lainnya'),
]

# Pendidikan
PENDIDIKAN = [
    ('SD', 'SD'),
    ('SMP', 'SMP'),
    ('SMA', 'SMA/SPK'),
    ('D3', 'D3'),
    ('S1', 'S1'),
    ('S2', 'S2'),
    ('S3', 'S3'),
]

#Minat Pelayanan
MINAT_PELAYANAN = [
    ('PADUAN_SUARA', 'Paduan Suara'),
    ('PEMUSIK', 'Pemusik'),
    ('MULTIMEDIA', 'Multimedia'),
    ('FASILITATOR_PA', 'Fasilitator PA'),
    ('GURU_SEKOLAH_MINGGU', 'Guru Sekolah Minggu'),
    ('GURU_TUNAS_REMAJA', 'Guru Tunas Remaja'),
    ('PEMERHATI', 'Pemerhati'),
    ('KEDUKAAN', 'Kedukaan'),
    ('PARENTING', 'Parenting'),
    ('PASUTRI', 'Pasutri'),
    ('LEKTOR', 'Lektor'),
    ('PNJ', 'Pemandu Nyanyian Jemaat'),
    ('PEMAZMUR', 'Pemazmur'),
    ('DIAKONIA', 'Diakonia'),
    ('PEMELIHARA_BANGUNAN', 'Pemelihara Bangunan'),
]

# Status Keanggotaan
STATUS_KEANGGOTAAN = [
    ('ANGGOTA_SIDI', 'Anggota Sidi'),
    ('ANGGOTA_ANAK', 'Anggota Anak'),
    ('SIMPATISAN', 'Simpatisan'),
    ('NON_AKTIF', 'Non Aktif'),
]

# Status Keanggotaan
STATUS_KEHIDUPAN = [
    ('HIDUP', 'Hidup'),
    ('ALMARHUM', 'Almarhum'),
]

LOKASI_PEMAKAMAN = [
    ('N_SM', 'Bukan Sari Mulia'),
    ('Y_SM', 'Sari Mulia'),
]

ALASAN_NON_AKTIF = [
    ('NONE', 'Tidak Ada Alasan'),
    ('ATKE', 'Atestasi Keluar'),
    ('PIKK', 'Pindah Keluar Kota'),
    ('PIAG', 'Pindah Agama'),
]

# Model Wilayah
class Wilayah(models.Model):
    nama_wilayah = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, auto_now_add=False)

    class Meta:
        db_table = 'wilayah'
        verbose_name_plural = 'Wilayah'

    def __str__(self):
        return '%s' % self.nama_wilayah

    def clean(self):
        self.nama_wilayah = self.nama_wilayah.upper()

    def save(self):
        self.full_clean()
        return super(Wilayah, self).save(*args, **kwargs)

# Model Keluarga
class Keluarga(models.Model):
    kepala_keluarga = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, auto_now_add=False)

    class Meta:
        db_table = 'keluarga'
        verbose_name_plural = 'Keluarga'

    def __str__(self):
        return "%s" % (self.kepala_keluarga)

    def clean(self):
        self.kepala_keluarga = self.kepala_keluarga.title()

    def save(self, *args, **kwargs):
        self.full_clean()
        return super(Keluarga, self).save(*args, **kwargs)

# Model Anggota
class Anggota(models.Model):
    nomor_anggota = models.CharField(max_length=10, unique=True)
    status_anggota = models.CharField(max_length=20, choices=STATUS_KEANGGOTAAN, default='ANGGOTA')
    nama_anggota = models.CharField(max_length=100)
    tanggal_lahir = models.DateField()
    tempat_lahir = models.CharField(max_length=50)
    alamat = models.CharField(max_length=200, blank=True)
    kelurahan = models.CharField(max_length=50, blank=True)
    kecamatan = models.CharField(max_length=50, blank=True)
    kota_kabupaten = models.CharField(max_length=50, blank=True)
    kode_pos = models.CharField(max_length=10, blank=True)
    kepala_keluarga = models.ForeignKey(Keluarga, on_delete=models.PROTECT)
    wilayah = models.ForeignKey(Wilayah, on_delete=models.PROTECT)
    jenis_kelamin = models.CharField(max_length=2, choices=JENIS_KELAMIN, default=LAKILAKI)
    nomor_hp = models.CharField(max_length=30, blank=True)
    alamat_email = models.EmailField(blank=True)
    status_pernikahan = models.CharField(max_length=15, choices=STATUS_PERNIKAHAN, default='MENIKAH')
    status_kehidupan = models.CharField(max_length=15, choices=STATUS_KEHIDUPAN, default='HIDUP')
    lokasi_pemakaman = models.CharField(max_length=5, choices=LOKASI_PEMAKAMAN, default='N_SM')
    lokasi_sari_mulia = models.CharField(max_length=50, blank=True)
    golongan_darah = models.CharField(max_length=2, choices=GOLONGAN_DARAH, default='A')
    golongan_darah_rhesus = models.CharField(max_length=2, choices=GOLONGAN_DARAH_RHESUS, default='RP')
    etnik = models.CharField(max_length=15, choices=ETNIK, default='MELAYU')
    pendidikan = models.CharField(max_length=10, choices=PENDIDIKAN, default='S1')
    pekerjaan = models.CharField(max_length=30, choices=PEKERJAAN, default='PNS')
    tanggal_nikah = models.DateField(null=True, blank=True)
    gereja_nikah = models.CharField(max_length=100, blank=True)
    pendeta_nikah = models.CharField(max_length=100, blank=True)
    tanggal_baptis = models.DateField(null=True, blank=True)
    gereja_baptis = models.CharField(max_length=100, blank=True)
    pendeta_baptis = models.CharField(max_length=100, blank=True)
    tanggal_sidi = models.DateField(null=True, blank=True)
    gereja_sidi = models.CharField(max_length=100, blank=True)
    pendeta_sidi = models.CharField(max_length=100, blank=True)
    minat_pelayanan = models.CharField(max_length=30, choices=MINAT_PELAYANAN, default='PENATUA')
    foto_anggota = models.ImageField(upload_to='images/', blank=True)
    nomor_kartu_parkir = models.CharField(max_length=50, blank=True)
    alasan_non_aktif = models.CharField(max_length=50, choices=ALASAN_NON_AKTIF, default='NONE')
    keterangan = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, auto_now_add=False)

    def __str__(self):
        return "%s %s" % (self.nomor_anggota, self.nama_anggota)

    def clean(self):
        self.nama_anggota = self.nama_anggota.title()
        self.nomor_anggota = self.nomor_anggota.upper()

    def save(self, *args, **kwargs):
        self.full_clean()
        return super(Anggota, self).save(*args, **kwargs)

    class Meta:
        db_table = 'anggota'
        verbose_name_plural = 'Anggota'
    