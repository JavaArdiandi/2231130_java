from django.urls import path
from  . import views
urlpatterns = [
  path('' , views.getBandara , name='getbandara'),
  path('addbandara' , views.addBandara , name='addbandara'),
  path('storebandara' , views.storeBandara , name='storebandara'),
  path('editbandara/<int:id>'  , views.editBandara , name='editbandara'),
  path('updatebandara/<int:id>' , views.updateBandara , name='updatebandara'),
  path('deletebandara/<int:id>' ,  views.deleteBandara , name='deletebandara'),
  
  #  Path Maskapai
  path('maskapai/' , views.getMaskapai , name='getmaskapai'),
  path('maskapai/addmaskapai' , views.addMaskapai , name='addmaskapai'),
  path('maskapai/storemaskapai' , views.storeMaskapai , name='storemaskapai'),
  path('maskapai/editmaskapai/<int:id>'  , views.editMaskapai , name='editmaskapai'),
  path('maskapai/updatemaskapai/<int:id>' , views.updateMaskapai , name='updatemaskapai'),
  path('maskapai/deletemaskapai/<int:id>' ,  views.deleteMaskapai , name='deletemaskapai'),

  #  Path Pilot 
  path('pilot/' , views.getPilot , name='getpilot'),
  path('pilot/addpilot' , views.addPilot , name='addpilot'),
  path('pilot/storepilot' , views.storePilot , name='storepilot'),
  path('pilot/editpilot/<int:id>'  , views.editPilot , name='editpilot'),
  path('pilot/updatepilot/<int:id>' , views.updatePilot , name='updatepilot'),
  path('pilot/deletepilot/<int:id>' ,  views.deletePilot , name='deletepilot'),

  #  Path Pesawat 
  path('pesawat/' , views.getPesawat , name='getpesawat'),
  path('pesawat/addpesawat' , views.addPesawat , name='addpesawat'),
  path('pesawat/storepesawat' , views.storePesawat , name='storepesawat'),
  path('pesawat/editpesawat/<int:id>'  , views.editPesawat , name='editpesawat'),
  path('pesawat/updatepesawat/<int:id>' , views.updatePesawat , name='updatepesawat'),
  path('pesawat/deletepesawat/<int:id>' ,  views.deletePesawat , name='deletepesawat'),
]