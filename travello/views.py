from django.shortcuts import render
from .models import Destination

# Create your views here.

def index(request):
    
    # # Destination 1
    # dest1 = Destination()
    # dest1.name = 'Bali'
    # dest1.desc = 'The country of diverse culture and tradition.'
    # dest1.img = 'destination_1.jpg'
    # dest1.price = 700
    # dest1.offer = True
    
    # # Destination 2
    # dest2 = Destination()
    # dest2.name = 'Indonesia'
    # dest2.desc = 'A beautiful archipelago with stunning landscapes.'
    # dest2.img = 'destination_2.jpg'
    # dest2.price = 650
    # dest2.offer = False
    
    # # Destination 3
    # dest3 = Destination()
    # dest3.name = 'San Francisco'
    # dest3.desc = 'The iconic city with the Golden Gate Bridge.'
    # dest3.img = 'destination_3.jpg'
    # dest3.price = 850
    # dest3.offer = True

    
    
    # # Destination 4
    # dest4 = Destination()
    # dest4.name = 'Paris'
    # dest4.desc = 'The city of love and the Eiffel Tower.'
    # dest4.img = 'destination_4.jpg'
    # dest4.price = 750
    # dest4.offer = False
    
    # # Destination 5
    # dest5 = Destination()
    # dest5.name = 'Phi Phi Island'
    # dest5.desc = 'Tropical paradise with crystal clear waters.'
    # dest5.img = 'destination_5.jpg'
    # dest5.price = 600
    # dest5.offer = True
    
    # # Destination 6
    # dest6 = Destination()
    # dest6.name = 'Mykonos'
    # dest6.desc = 'Greek island known for its vibrant nightlife.'
    # dest6.img = 'destination_6.jpg'
    # dest6.price = 800
    # dest6.offer = False

    
    # # Create a list of all destinations
    # dests = [dest1, dest2, dest3,dest4, dest5,dest6]
    
    
    dests = Destination.objects.all()
    return render(request, 'index.html', {'dests': dests})