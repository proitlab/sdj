from django.contrib import admin
from django.forms.widgets import SelectDateWidget
from data.models import *
from django.utils.translation import ugettext_lazy


from import_export import resources
from import_export.admin import ImportExportModelAdmin

class AnggotaResource(resources.ModelResource):
    class Meta:
        model = Anggota
        exclude = ('created_at', 'updated_at', )


class KeluargaResource(resources.ModelResource):
    class Meta:
        model = Keluarga
        exclude = ('created_at', 'updated_at', )

# Register your models here.
class WilayahAdmin(admin.ModelAdmin):
    list_display = ('id', 'nama_wilayah')
    actions = None
    #ordering = ['id_wilayah']
    icon_name = 'map'
    ordering = ['id']
    search_fields =  ['nama_wilayah']

    # This will help you to disbale add functionality
    def has_add_permission(self, request):
        return False

class KeluargaAdmin(ImportExportModelAdmin):
    resource_class = KeluargaResource
    list_display = ('id', 'kepala_keluarga',)
    icon_name = 'home'
    actions = None

    ordering = ['kepala_keluarga']
    search_fields = ['kepala_keluarga']

class AnggotaAdmin(ImportExportModelAdmin):
    #form = 'AnggotaForm'
    resource_class = AnggotaResource
    icon_name = 'person'
    formfield_overrides = {models.DateField: {"widget": SelectDateWidget(years=range(1950, 2020))}}
    list_display = ('nomor_anggota', 'nama_anggota', 'wilayah')
    list_filter = ('status_anggota', 'wilayah' )

    search_fields = ['nama_anggota']

    actions = None

    fieldsets = (
            ('Keanggotaan', {
                'fields' : (('nomor_anggota', 'status_anggota'),
                    'kepala_keluarga',
                    )
                }),
            ('Alasan Non Aktif', {
                'classes': ('collapse',),
                'fields' : ('alasan_non_aktif',
                    )
                }),
            ('Data Anggota', {
                'classes': ('wide','extrapretty',),
                'fields' : (
                    'foto_anggota',
                    ('nama_anggota', 'jenis_kelamin'),
                    ('tanggal_lahir', 'tempat_lahir'),
                    'alamat',
                    ('kelurahan', 'kecamatan', 'kota_kabupaten', 'kode_pos'),
                    'wilayah',
                    ('nomor_hp', 'alamat_email'), 
                    ('status_pernikahan', 'status_kehidupan'),
                    ('golongan_darah', 'golongan_darah_rhesus'),
                    ('etnik', 'pendidikan', 'pekerjaan'),
                )
                }),
            ('Baptis, Sidi dan Nikah', {
                'classes': ('collapse',),
                'fields': (
                    ('tanggal_baptis', 'gereja_baptis', 'pendeta_baptis'),
                    ('tanggal_sidi', 'gereja_sidi', 'pendeta_sidi'),
                    ('tanggal_nikah', 'gereja_nikah', 'pendeta_nikah'),
                )
                }),
            ('Keterangan Lain', {
                'classes': ('collapse',),
                'fields' : ('minat_pelayanan', 'nomor_kartu_parkir', 'keterangan'),
                }),
            )

    autocomplete_fields = ['kepala_keluarga', 'wilayah']

admin.site.register(Wilayah, WilayahAdmin)
admin.site.register(Keluarga, KeluargaAdmin)
admin.site.register(Anggota, AnggotaAdmin)

