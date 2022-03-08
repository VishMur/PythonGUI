import tkinter as tk
from tkinter import *
import AttractionGUI

import data
import sorting
import CompareAttractions

root = Tk()
root.geometry("1000x500")  # width x height
root.title('AttractionsFinder')
canvas=Canvas(root, width=1000, height=500)
canvas.pack()



#----------------------------------------------------------------------------

#Inital Frame: Title
greeting = Label(text="Attractions App", font = ("Arial", 40))

#locationList = Listbox(root, selectmode ="single")
#locationList.pack(expand = YES, fill = "both")
#options = ["Northern Utah", "Salt Lake Area", "Western Utah", "Southwestern Utah", "Eastern Utah"]
#for each_item in range(len(options)):
#    locationList.insert(END, options[each_item])

def show_TitleFrameWidget():
    greeting.place(x = 200,y = 200)


def hide_TitleFrameWidget():
    greeting.place_forget()

#----------------------------------------------------------------------------

#Finding Attractions Frame: App
location = Label(text = "Location:", font = ("Arial",20))
attractionType = Label(text = "Type of Attraction:", font = ("Arial",20))
price = Label(text = "Price:", font = ("Arial",20))
rating = Label(text = "Rating:", font = ("Arial",20))
busyness = Label(text = "Traffic:", font = ("Arial",20))

def show_AppFrameWidget():
    location.place(x=15, y=15)
    attractionType.place(x=15, y=105)
    price.place(x=15, y=195)
    rating.place(x=15, y=285)
    busyness.place(x=15, y=375)

    canvas.create_line(275, 10, 275, 480)
    
def hide_AppFrameWidget():
    location.place_forget()
    attractionType.place_forget()
    price.place_forget()
    rating.place_forget()
    busyness.place_forget()

def show():
    myLabel = Label(root, text=locationClicked.get()).pack()

locationClicked = StringVar()
locationClicked.set("Select a Location")
locationField = OptionMenu(root, locationClicked, "Northern Utah", "Salt Lake Area", "Western Utah", "Southwestern Utah", "Eastern Utah")
locationField.place(x=15,y=55)

attractionTypeClicked = StringVar()
attractionTypeClicked.set("Select a Type of Attraction")
attractionTypeField = OptionMenu(root, attractionTypeClicked, "Sports", "Food", "Nature / Outdoor", "Cultural / Historical", "Entertainment")
attractionTypeField.place(x=15,y=145)

attractionPriceClicked = StringVar()
attractionPriceClicked.set("Select a Price")
attractionPriceField = OptionMenu(root, attractionPriceClicked, "$", "$$", "$$$")
attractionPriceField.place(x=15,y=235)

ratingClicked = StringVar()
ratingClicked.set("Select a Rating")
ratingField = OptionMenu(root, ratingClicked, "1 star", "2 star", "3 star", "4 star", "5 star")
ratingField.place(x=15,y=325)

busynessClicked = StringVar()
busynessClicked.set("Select a Busyness")
busynessField = OptionMenu(root, busynessClicked, "Low Traffic", "Medium Traffic", "High Traffic")
busynessField.place(x=15,y=415)

#----------------------------------------------------------------------------

#Logic

def location_dropdown(*args):
    global locationDropdownField
    dropdown = str(locationClicked.get())
    #sorting.desired.insert(1,locationClicked.get)
    sorting.desired[1] = locationClicked.get()

    if locationClicked.get() == "Northern Utah":
        for i in data.allAttractions:
            if (i[1] == "Northern Utah"):
                sorting.chosenAttractions.append(i)#data.allAttractions[i]

    elif locationClicked.get() == "Salt Lake Area":
        for i in data.allAttractions:
            if (i[1] == "Salt Lake Area"):
                sorting.chosenAttractions.append(i)#data.allAttra
           
    elif locationClicked.get() == "Western Utah":
        for i in data.allAttractions:
            if (i[1] == "Western Utah"):
                sorting.chosenAttractions.append(i)  # data.allAttra

    elif locationClicked.get() == "Southwestern Utah":
        for i in data.allAttractions:
            if (i[1] == "Southwestern Utah"):
                sorting.chosenAttractions.append(i)  # data.allAttrac

    elif locationClicked.get() == "Eastern Utah":
        for i in data.allAttractions:
            if (i[1] == "Eastern Utah"):
                sorting.chosenAttractions.append(i)

    print(sorting.chosenAttractions)
    sorting.showRecommendedAttractions()
    #sorting.chosenAttractions.clear()
    
# link function to change dropdown
locationClicked.trace('w', location_dropdown)



def attractionType_dropdown(*args):
    global attractionTypeDropdownField
    dropdown2 = str(attractionTypeClicked.get())
    #sorting.desired.insert(2, attractionTypeClicked.get())
    sorting.desired[2] = attractionTypeClicked.get()

    if attractionTypeClicked.get() == "Sports":
        for i in data.allAttractions:
            if (i[2] == "Sports"):
                sorting.chosenAttractions.append(i)
    elif attractionTypeClicked.get() == "Food":
        print(7)
    elif attractionTypeClicked.get() == "Nature / Outdoor":
        print(8)
    elif attractionTypeClicked.get() == "Cultural / Historical":
        print(9)
    elif attractionTypeClicked.get() == "Entertainment":
        print(10)

    print(sorting.chosenAttractions)
    sorting.showRecommendedAttractions()
    #sorting.chosenAttractions.clear()

attractionTypeClicked.trace('w', attractionType_dropdown)


#Price sorted as 1-3
def attractionPrice_dropdown(*args):
    global attractionPriceDropdownField
    dropdown3 = str(attractionPriceClicked.get)
    #sorting.desired[3] = attractionPriceClicked.get()
    if attractionPriceClicked.get() == "$":
        print(11)
        #sorting.desired[3] == 1
    elif attractionPriceClicked.get() == "$$":
        print(12)
        #sorting.desired[3] == 2
    elif attractionPriceClicked.get() == "$$$":
        print(13)
        #sorting.desired[3] == 3

attractionPriceClicked.trace('w', attractionPrice_dropdown)


#Rating sorted as a 1-5
def rating_dropdown(*args):
    global ratingDropdownField
    dropdown4 = str(ratingClicked.get())
    sorting.desired[4] = ratingClicked.get()
    if ratingClicked.get() == "1 star":
        print(14)
        #sorting.desired[4] == 1
    elif ratingClicked.get() == "2 star":
        print(15)
        #sorting.desired[4] == 2

    elif ratingClicked.get() == "3 star":
        print(16)
        #sorting.desired[4] == 3

    elif ratingClicked.get() == "4 star":
        print(17)
        #sorting.desired[4] == 4

    elif ratingClicked.get() == "5 star":
        print(18)
        #sorting.desired[4] == 5

ratingClicked.trace('w', rating_dropdown)


#Busyness sorted on a 1-3
def busyness_dropdown(*args):
    global busynessDropdownField
    dropdown5 = str(busynessClicked.get())
    sorting.desired[5] = busynessClicked.get()
    if busynessClicked.get() == "Low Traffic":
        print(19)
        #sorting.desired[5] == 1
    elif busynessClicked.get() == "Medium Traffic":
        print(20)
        #sorting.desired[5] == 2
    elif busynessClicked.get() == "High Traffic":
        print(21)
        #sorting.desired[5] == 3
    print(sorting.desired)

busynessClicked.trace('w', busyness_dropdown)

#myButton = Button(root, text="Show Selection", command=show).pack()


# def leftclick(event):
#     print("hi")
#     #rerun recommendation algorithm



#dropdown
#attractionType.bind("<Button-1>", leftclick)
#attractionType.pack()

show_AppFrameWidget()
root.mainloop()



