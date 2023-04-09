from tkinter import ttk
from random import randint, choice
import tkinter as tk
from tkinter import*
from PIL import Image, ImageTk



def hotel_list_screen(root): 
    hotelmain = {
        1: {"photo" : "panpacific.png", "name" : "Pan Pacific Singapore", "location" : "Marina Bay","price" : 282,"hotelclass" : 5,"guestreview" : 8.8,"shuttlebusservice" : 0,"spa" : 1,"freebreakfast" : 1},
        2: {"photo" : "parkroyal.png", "name" : "Parkroyal Collection Marina Bay","location" : "Marina Bay","price" : 320,"hotelclass" : 5,"guestreview" : 8.5,"shuttlebusservice" : 0,"spa" : 1,"freebreakfast" : 1},
        3: {"photo" : "ritzcarlton.png", "name" : "Ritz-Carlton, Millenia Singapore","location" : "Marina Bay","price" : 444,"hotelclass" : 5,"guestreview" : 9.1,"shuttlebusservice" : 1,"spa" : 1,"freebreakfast" : 1},
        4: {"photo" : "fullerton.png", "name" : "The Fullerton Hotel Singapore","location" : "Marina Bay","price" : 333,"hotelclass" : 5,"guestreview" : 9.0,"shuttlebusservice" : 0,"spa" : 1,"freebreakfast" : 1},
        5: {"photo" : "conrad.png", "name" : "Conrad Centennial Singapore","location" : "Marina Bay","price" : 294,"hotelclass" : 5,"guestreview" : 8.9,"shuttlebusservice" : 0,"spa" : 1,"freebreakfast" : 1},
        6: {"photo" : "fullertonbay.png", "name" : "Fullerton Bay Hotel Singapore","location" : "Marina Bay","price" : 570,"hotelclass" : 5,"guestreview" : 9.2,"shuttlebusservice" : 0,"spa" : 0,"freebreakfast" : 1},
        7: {"photo" : "goodwood.png", "name" : "Goodwood Park Hotel","location" : "Orchard Road","price" : 241,"hotelclass" : 5,"guestreview" : 8.3,"shuttlebusservice" : 0,"spa" : 0,"freebreakfast" : 0},
        8: {"photo" : "hilton.png", "name" : "Hilton Singapore Orchard","location" : "Orchard Road","price" : 255,"hotelclass" : 5,"guestreview" : 8.3,"shuttlebusservice" : 1,"spa" : 0,"freebreakfast" : 0},
        9: {"photo" : "marriott.png", "name" : "Singapore Marriott Tang Plaza Hotel","location" : "Orchard Road","price" : 294,"hotelclass" : 5,"guestreview" : 8.1,"shuttlebusservice" : 0,"spa" : 0,"freebreakfast" : 1},
        10: {"photo" : "orchard.png", "name" : "Orchard Hotel Singapore","location" : "Orchard Road","price" : 173,"hotelclass" : 4,"guestreview" : 7.6,"shuttlebusservice" : 1,"spa" : 0,"freebreakfast" : 1},
        11: {"photo" : "york.png", "name" : "York Hotel","location" : "Orchard Road","price" : 167,"hotelclass" : 4,"guestreview" : 7.8,"shuttlebusservice" : 0,"spa" : 0,"freebreakfast" : 1},
        12: {"photo" : "royalplaza.png", "name" : "Royal Plaza on Scotts Hotel","location" : "Orchard Road","price" : 211,"hotelclass" : 5,"guestreview" : 8.5,"shuttlebusservice" : 0,"spa" : 0,"freebreakfast" : 0},
        13: {"photo" : "furamacity.png", "name" : "Furama City Centre Hotel","location" : "Chinatown","price" : 143,"hotelclass" : 4,"guestreview" : 7.8,"shuttlebusservice" : 0,"spa" : 0,"freebreakfast" : 0},
        14: {"photo" : "dorsett.png", "name" : "Dorsett Singapore","location" : "Chinatown","price" : 120,"hotelclass" : 4,"guestreview" : 8.2,"shuttlebusservice" : 0,"spa" : 0,"freebreakfast" : 0},
        15: {"photo" : "butternut.png", "name" : "Butternut Tree Hotel","location" : "Chinatown","price" : 60,"hotelclass" : 2,"guestreview" : 7.8,"shuttlebusservice" : 0,"spa" : 0,"freebreakfast" : 0},
        16: {"photo" : "scarlet.png", "name" : "The Scarlet Singapore","location" : "Chinatown","price" : 197,"hotelclass" : 4,"guestreview" : 8.3,"shuttlebusservice" : 0,"spa" : 0,"freebreakfast" : 0},
        17: {"photo" : "capri.png", "name" : "Capri by Fraser, China Square","location" : "Chinatown","price" : 201,"hotelclass" : 4,"guestreview" : 8.6,"shuttlebusservice" : 0,"spa" : 0,"freebreakfast" : 1},
        18: {"photo" : "wsingapore.png", "name" : "W Singapore - Sentosa Cove","location" : "Sentosa","price" : 270,"hotelclass" : 5,"guestreview" : 8.6,"shuttlebusservice" : 1,"spa" : 1,"freebreakfast" : 1},
        19: {"photo" : "one15.png", "name" : "ONE°15 Marina","location" : "Sentosa","price" : 239,"hotelclass" : 5,"guestreview" : 8.1,"shuttlebusservice" : 1,"spa" : 0,"freebreakfast" : 1},
        20: {"photo" : "capella.png", "name" : "Capella Singapore","location" : "Sentosa","price" : 853,"hotelclass" : 5,"guestreview" : 9.0,"shuttlebusservice" : 1,"spa" : 1,"freebreakfast" : 1},
        21: {"photo" : "equarisvilla.png", "name" : "Resorts World Sentosa - Equarius Villas","location" : "Sentosa","price" : 330,"hotelclass" : 5,"guestreview" : 8.3,"shuttlebusservice" : 0,"spa" : 0,"freebreakfast" : 1},
        22: {"photo" : "shangrila.png", "name" : "Shangri-La Rasa, Sentosa","location" : "Sentosa","price" : 264,"hotelclass" : 5,"guestreview" : 8.9,"shuttlebusservice" : 1,"spa" : 0,"freebreakfast" : 1},
        23: {"photo" : "amara.png", "name" : "Amara Sanctuary Resort Sentosa","location" : "Sentosa","price" : 211,"hotelclass" : 5,"guestreview" : 7.6,"shuttlebusservice" : 1,"spa" : 1,"freebreakfast" : 1},
        24: {"photo" : "parkregis.png", "name" : "Park Regis Singapore","location" : "Clarke Quay","price" : 170,"hotelclass" : 4,"guestreview" : 8.2,"shuttlebusservice" : 0,"spa" : 0,"freebreakfast" : 1},
        25: {"photo" : "holidayinncq.png", "name" : "Holiday Inn Express Clarke Quay","location" : "Clarke Quay","price" : 168,"hotelclass" : 3,"guestreview" : 8.5,"shuttlebusservice" : 0,"spa" : 0,"freebreakfast" : 1},
        26: {"photo" : "paradox.png", "name" : "Paradox Singapore Merchant Court","location" : "Clarke Quay","price" : 192,"hotelclass" : 4,"guestreview" : 9.0,"shuttlebusservice" : 0,"spa" : 0,"freebreakfast" : 1},
        27: {"photo" : "studiom.png", "name" : "Studio M Hotel","location" : "Clarke Quay","price" : 128,"hotelclass" : 4,"guestreview" : 7.7,"shuttlebusservice" : 0,"spa" : 0,"freebreakfast" : 1},
        28: {"photo" : "peninsula.png", "name" : "Peninsula Excelsior Hotel","location" : "Clarke Quay","price" : 172,"hotelclass" : 4,"guestreview" : 7.7,"shuttlebusservice" : 0,"spa" : 0,"freebreakfast" : 0},
        29: {"photo" : "msocial.png", "name" : "M Social Singapore","location" : "Clarke Quay","price" : 128,"hotelclass" : 4,"guestreview" : 8.1,"shuttlebusservice" : 0,"spa" : 0,"freebreakfast" : 1},
        30: {"photo" : "dhotel.png", "name" : "D’Hotel Singapore","location" : "Tiong Bahru","price" : 121,"hotelclass" : 4,"guestreview" : 8.3,"shuttlebusservice" : 0,"spa" : 0,"freebreakfast" : 0},
        31: {"photo" : "newcape.png", "name" : "New Cape Inn","location" : "Tiong Bahru","price" : 75,"hotelclass" : 3,"guestreview" : 7.1,"shuttlebusservice" : 0,"spa" : 0,"freebreakfast" : 0},
        32: {"photo" : "nostalgia.png", "name" : "Nostalgia Hotel","location" : "Tiong Bahru","price" : 109,"hotelclass" : 4,"guestreview" : 8.1,"shuttlebusservice" : 0,"spa" : 0,"freebreakfast" : 0},
        33: {"photo" : "linkhotel.png", "name" : "Link Hotel Singapore","location" : "Tiong Bahru","price" : 118,"hotelclass" : 4,"guestreview" : 7.4,"shuttlebusservice" : 0,"spa" : 1,"freebreakfast" : 0},
        34: {"photo" : "coller.png", "name" : "Coller Boutique Hostel","location" : "Tiong Bahru","price" : 46,"hotelclass" : 5,"guestreview" : 8.1,"shuttlebusservice" : 0,"spa" : 0,"freebreakfast" : 1},
        35: {"photo" : "hotel81osaka.png", "name" : "Hotel 81 Osaka","location" : "Tiong Bahru","price" : 159,"hotelclass" : 2,"guestreview" : 7.2,"shuttlebusservice" : 0,"spa" : 0,"freebreakfast" : 0},
        36: {"photo" : "parkview.png", "name" : "Park View Hotel","location" : "Bugis","price" : 88,"hotelclass" : 3,"guestreview" : 7.5,"shuttlebusservice" : 0,"spa" : 0,"freebreakfast" : 0},
        37: {"photo" : "heritage.png", "name" : "Heritage Collection on Seah","location" : "Bugis","price" : 180,"hotelclass" : 3,"guestreview" : 9.0,"shuttlebusservice" : 0,"spa" : 0,"freebreakfast" : 0},
        38: {"photo" : "intercontinental.png", "name" : "InterContinental Singapore","location" : "Bugis","price" : 360,"hotelclass" : 5,"guestreview" : 8.8,"shuttlebusservice" : 0,"spa" : 0,"freebreakfast" : 0},
        39: {"photo" : "calmo.png", "name" : "Hotel Calmo Bugis","location" : "Bugis","price" : 96,"hotelclass" : 3,"guestreview" : 7.5,"shuttlebusservice" : 0,"spa" : 0,"freebreakfast" : 0},
        40: {"photo" : "nuveheritage.png", "name" : "Hotel Nuve Heritage","location" : "Bugis","price" : 164,"hotelclass" : 4,"guestreview" : 8.2,"shuttlebusservice" : 0,"spa" : 0,"freebreakfast" : 1},
        41: {"photo" : "panpacificserviced.png", "name" : "Pan Pacific Serviced Suites Beach Road","location" : "Bugis","price" : 313,"hotelclass" : 5,"guestreview" : 8.7,"shuttlebusservice" : 0,"spa" : 0,"freebreakfast" : 1},
        42: {"photo" : "wanderlust.png", "name" : "Wanderlust, Oakwood","location" : "Little India","price" : 156,"hotelclass" : 4,"guestreview" : 9.0,"shuttlebusservice" : 0,"spa" : 0,"freebreakfast" : 0},
        43: {"photo" : "daulut.png", "name" : "The Daulat by Hotel Calmo","location" : "Little India","price" : 92,"hotelclass" : 3,"guestreview" : 7.1,"shuttlebusservice" : 0,"spa" : 0,"freebreakfast" : 0},
        44: {"photo" : "greatmadras.png", "name" : "The Great Madras","location" : "Little India","price" : 66,"hotelclass" : 4,"guestreview" : 7.4,"shuttlebusservice" : 0,"spa" : 0,"freebreakfast" : 1},
        45: {"photo" : "stsignature.png", "name" : "ST Signature Jalan Besar","location" : "Little India","price" : 88,"hotelclass" : 3,"guestreview" : 8.1,"shuttlebusservice" : 0,"spa" : 0,"freebreakfast" : 0},
        46: {"photo" : "hotel81dickson.png", "name" : "Hotel 81 Dickson","location" : "Little India","price" : 63,"hotelclass" : 2,"guestreview" : 7.1,"shuttlebusservice" : 0,"spa" : 0,"freebreakfast" : 0},
        47: {"photo" : "hotel81rochor.png", "name" : "Hotel 81 Rochor","location" : "Little India","price" : 57,"hotelclass" : 2,"guestreview" : 7.0,"shuttlebusservice" : 0,"spa" : 0,"freebreakfast" : 0},
        }
    
    global screen

    screen = root
    screen.geometry("900x800")
    screen.configure(bg="#d7dae2")
    screen.title("Hotel List")

    framez = Frame(screen)
    framez.pack(fill=BOTH, expand=1)

    my_canvas = Canvas(framez)
    my_canvas.pack(side=LEFT, fill=BOTH, expand=1)

    my_scrollbar = Scrollbar(framez, orient=VERTICAL, command=my_canvas.yview)
    my_scrollbar.pack(side=RIGHT, fill=Y)
    my_canvas.configure(yscrollcommand=my_scrollbar.set, scrollregion=(0,0,0,14100))

    

    counter=28
    for x, hotel in hotelmain.items():
        hotelImage = hotel["photo"]
        hotelnamex = hotel["name"]
        price = hotel["price"]
        rating = hotel["hotelclass"]
        breakfast = hotel["freebreakfast"]
        if(breakfast):
            breakfast = 'Yes'
        else:
            breakfast = 'No'
        bus = hotel["shuttlebusservice"]
        if(bus):
            bus = 'Yes'
        else:
            bus = 'No'
        spa = hotel["spa"]
        if(spa):
            spa = 'Yes'
        else:
            spa = 'No'
        


        img = Image.open(hotelImage)
        img = img.resize((390, 227), Image.ANTIALIAS)  
        photo = ImageTk.PhotoImage(img)

        hotel["photo_obj"] = photo

        hotel1_frame=Frame(my_canvas,bd=5,relief=RIDGE)
        hotel1_frame.place(x=30,y=counter,width=600,height=4000)

        placement1=Label(hotel1_frame,image=photo,compound=LEFT)
        placement1.place(x=10,y=10)


        hotelname=Label(hotel1_frame,text=hotelnamex, font=('times new roman',18,'bold'),fg='darkblue')
        hotelname.grid(row=0,column=0,padx=(430, 0), pady=20, sticky=W)
        info=Label(hotel1_frame,text='Price: $' + str(price), font=('times new roman',12,'bold'))
        info.grid(row=1,column=0,padx=(430, 0),pady=5,sticky=W)
        info=Label(hotel1_frame,text='Hotel Rating: ' + str(rating), font=('times new roman',12,'bold'))
        info.grid(row=2,column=0,padx=(430, 310),pady=5,sticky=W)
        info=Label(hotel1_frame,text='Breakfast Availability: ' + breakfast, font=('times new roman',12,'bold'))
        info.grid(row=3,column=0,padx=(430, 0),pady=5,sticky=W)
        info=Label(hotel1_frame,text='Shuttle Service Availability: ' + bus, font=('times new roman',12,'bold'))
        info.grid(row=4,column=0,padx=(430, 0),pady=5,sticky=W)
        info=Label(hotel1_frame,text='Spa Availability: ' + spa, font=('times new roman',12,'bold'))
        info.grid(row=5,column=0,padx=(430, 0),pady=5,sticky=W)

        my_canvas.create_window(10, counter, anchor=NW, window=hotel1_frame)
        counter+=300

    back_frame = Frame(screen)
    back_frame.pack(side=TOP)

    back_button = Button(back_frame, text="Back",font=("times new roman",15,'bold'),width=500,height=2,cursor='hand2',bg='lightgrey',fg='black')
    back_button.pack(padx=0, pady=0)

    
    screen.mainloop()
    


root = Tk()
hotel_list_screen(root)

