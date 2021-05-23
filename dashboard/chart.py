from data.models import *
from data_support.models import *


# Count Gender
def chart_gender():

    data_gender = {}
    all_gender = JENIS_KELAMIN

    for e in all_gender:
        count_gender = Anggota.objects.filter(jenis_kelamin=e[0]).count()
        data_gender[e[1]] = count_gender
    
    all_gender = list(data_gender.keys())
    return all_gender, data_gender


# Count Etnik
def chart_etnik():

    data_etnik = {}
    all_etnik = Etnik.objects.all()

    for e in all_etnik:
        count_etnik = Anggota.objects.filter(etnik=e).count()
        data_etnik[e.nama_etnik] = count_etnik
    
    all_etnik = list(data_etnik.keys())
    return all_etnik, data_etnik


# Count Profesi
def chart_profesi():

    data_profesi = {}
    all_profesi = Profesi.objects.all()

    for e in all_profesi:
        count_profesi = Anggota.objects.filter(profesi=e).count()
        data_profesi[e.nama_profesi] = count_profesi

    all_profesi = list(data_profesi.keys())
    return all_profesi, data_profesi



