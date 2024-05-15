from django.shortcuts import render , redirect
from .models import Pesawat , Pilot ,Maskapai, Bandara 

# Create your views here.
def getPesawat(request):
  pesawat = Pesawat.objects.all()
  return render(request=request, template_name='pesawat/index.html', context={'list_pesawat': pesawat})

def addPesawat(request):
  return render(request=request , template_name='pesawat/create.html' )

def storePesawat(request):
  nama_pesawat_field = request.POST['nama_pesawat_field']
  jenis_pesawat_field = request.POST['jenis_pesawat_field']
  pesawat = Pesawat(nama_pesawat = nama_pesawat_field , jenis_pesawat = jenis_pesawat_field)
  pesawat.save()
  return redirect('/pesawat')

def editPesawat(request , id):
  pesawat = Pesawat.objects.get(id=id)
  return render(request=request , template_name='pesawat/edit.html' , context={'pesawat' : pesawat})

def updatePesawat(request , id):
  nama_pesawat_field = request.POST['nama_pesawat_field']
  jenis_pesawat_field = request.POST['jenis_pesawat_field']
  pesawat = Pesawat.objects.get(id=id)
  pesawat.nama_pesawat = nama_pesawat_field 
  pesawat.jenis_pesawat = jenis_pesawat_field
  pesawat.save()
  return redirect('/pesawat')

def deletePesawat(request , id):
  pesawat = Pesawat.objects.get(id=id)
  pesawat.delete()
  return redirect('/pesawat')

#  View Pilot
def getPilot(request):
  pilot = Pilot.objects.all()
  return render(request=request, template_name='pilot/index.html', context={'list_pilot': pilot})

def addPilot(request):
  return render(request=request , template_name='pilot/create.html' )

def storePilot(request):
  nama_pilot_field = request.POST['nama_pilot_field']
  nomor_telepon_field = request.POST['nomor_telepon_field']
  pilot = Pilot(nama_pilot = nama_pilot_field  , nomor_telepon = nomor_telepon_field)
  pilot.save()
  return redirect('/pilot')

def editPilot(request , id):
  pilot = Pilot.objects.get(id=id)
  return render(request=request , template_name='pilot/edit.html' , context={'pilot' : pilot})

def updatePilot(request , id):
  nama_pilot_field = request.POST['nama_pilot_field']
  nomor_telepon_field = request.POST['nomor_telepon_field']
  pilot = Pilot.objects.get(id=id)
  pilot.nama_pilot = nama_pilot_field 
  pilot.nomor_telepon = nomor_telepon_field
  pilot.save()
  return redirect('/pilot')

def deletePilot(request , id):
  pilot = Pilot.objects.get(id=id)
  pilot.delete()
  return redirect('/pilot')


#  View Maskapai
def getMaskapai(request):
  maskapai = Maskapai.objects.all()
  return render(request=request, template_name='maskapai/index.html', context={'list_maskapai': maskapai})

def addMaskapai(request):
  return render(request=request , template_name='maskapai/create.html' )

def storeMaskapai(request):
  nama_maskapai_field = request.POST['nama_maskapai_field']
  lokasi_maskapai_field = request.POST['lokasi_maskapai_field']
  maskapai = Maskapai(nama_maskapai = nama_maskapai_field  , lokasi_maskapai = lokasi_maskapai_field)
  maskapai.save()
  return redirect('/maskapai')

def editMaskapai(request , id):
  maskapai = Maskapai.objects.get(id=id)
  return render(request=request , template_name='maskapai/edit.html' , context={'maskapai' : maskapai})

def updateMaskapai(request , id):
  nama_maskapai_field = request.POST['nama_maskapai_field']
  lokasi_maskapai_field = request.POST['lokasi_maskapai_field']
  maskapai = Maskapai.objects.get(id=id)
  maskapai.nama_maskapai = nama_maskapai_field 
  maskapai.lokasi_maskapai = lokasi_maskapai_field
  maskapai.save()
  return redirect('/maskapai')

def deleteMaskapai(request , id):
  maskapai = Maskapai.objects.get(id=id)
  maskapai.delete()
  return redirect('/maskapai')

# Views Bandara
def getBandara(request):
  bandara = Bandara.objects.select_related('pesawat' , 'maskapai' , 'pilot').all()
  return render(request=request , template_name='index.html' , context={'list_bandara' : bandara})

def addBandara(request):
  pilot = Pilot.objects.all()
  maskapai = Maskapai.objects.all()
  pesawat = Pesawat.objects.all()
  return render(request=request , template_name='create.html' , context={'list_pesawat' : pesawat  , 'list_maskapai' : maskapai , 'list_pilot' : pilot , })

def storeBandara(request):
  pesawat_field = request.POST['pesawat_field']
  maskapai_field = request.POST['maskapai_field']
  pilot_field = request.POST['pilot_field']
  nama_bandara_field = request.POST['nama_bandara_field']
  jalur_field = request.POST['jalur_field']
  lokasi_bandara_field = request.POST['lokasi_bandara_field']
  harga_tiket_field = request.POST['harga_tiket_field']
  
  try:
    pesawat_instance = Pesawat.objects.get(id=pesawat_field)
  except Pesawat.DoesNotExist:
    pesawat_instance = 0

  try:
    pilot_instance = Pilot.objects.get(id=pilot_field)
  except Pesawat.DoesNotExist:
    pilot_instance = 0

  try:
    maskapai_instance = Maskapai.objects.get(id=maskapai_field)
  except Maskapai.DoesNotExist:
    maskapai_instance = 0
  
  bandara = Bandara(nama_bandara = nama_bandara_field , lokasi_bandara = lokasi_bandara_field , maskapai= maskapai_instance , pilot = pilot_instance , pesawat =  pesawat_instance , harga_tiket = harga_tiket_field , jalur = jalur_field)
  bandara.save()
  return redirect('/')

def editBandara(request , id):
  bandara = Bandara.objects.get(id=id)
  return render(request=request  , template_name='edit.html' , context={'bandara' : bandara})

def updateBandara(request , id):
  nama_bandara_field = request.POST['nama_bandara_field']
  harga_tiket_field = request.POST['harga_tiket_field']
  lokasi_bandara_field = request.POST['lokasi_bandara_field']
  jalur_field = request.POST['jalur_field']
  bandara = Bandara.objects.get(id=id)
  bandara.nama_bandara = nama_bandara_field
  bandara.lokasi_bandara = lokasi_bandara_field
  bandara.harga_tiket = harga_tiket_field
  bandara.jalur = jalur_field
  bandara.save()
  return redirect('/')

def deleteBandara(request,id):
  bandara = Bandara.objects.get(id=id)
  bandara.delete()
  return redirect('/')  
 