from tkinter import *

def convert():
    global eq
    global unit1
    global unit2
    try:
        n = float(entry.get())
        unit1 = clicked.get()
        unit2 = clicked2.get()
        eq = 0

    
        if unit1 == unit2:
            eq = n
        #Ton#######################
        elif unit1 == "Ton" and unit2 == "Kilogram":
            eq = n * 1000
        elif unit1 == "Ton" and unit2 == "Decagram":
            eq = n * 1000000
        elif unit1 == "Ton" and unit2 == "Gram":
            eq = n * 100000
        elif unit1 == "Ton" and unit2 == "Miligram":
            eq = n * 1000000000
        elif unit1 == "Ton" and unit2 == "US Pound":
            eq = n * 2205
        elif unit1 == "Ton" and unit2 == "Ounce":
            eq = n * 35270
        #Kilogram#############################
        elif unit1 == "Kilogram" and unit2 == "Decagram":
            eq = n * 100
        elif unit1 == "Kilogram" and unit2 == "Gram":
            eq = n * 1000
        elif unit1 == "Kilogram" and unit2 == "Miligram":
            eq = n * 1000000
        elif unit1 == "Kilogram" and unit2 == "US Pound":
            eq = n * 2.205
        elif unit1 == "Kilogram" and unit2 == "Ounce":
            eq = n * 35.274
        #Decagram#####################################
        elif unit1 == "Decagram" and unit2 == "Gram":
            eq = n * 10
        elif unit1 == "Decagram" and unit2 == "Miligram":
            eq = n * 10000
        elif unit1 == "Decagram" and unit2 == "Ounce":
            eq = n * 0.35
        elif unit1 == "Decagram" and unit2 == "US Pound":
            eq = n * 0.022
        #Gram##########################################
        elif unit1 == "Gram" and unit2 == "Miligram":
            eq = n * 1000
        #Pound#######################
        elif unit1 == "US Pound" and unit2 == "Ounce":
            eq = n * 16
        elif unit1 == "US Pound" and unit2 == "Gram":
            eq = n * 454
        elif unit1 == "US Pound" and unit2 == "Miligram":
            eq = n * 453600
        #Ounce####################
        elif unit1 == "Ounce" and unit2 == "Gram":
            eq = n * 28.35
        elif unit1 == "Ounce" and unit2 == "Miligram":
            eq = n * 28350
        #Smaller to bigger###############
        elif unit1 == "Kilogram" and unit2 == "Ton":
            eq = n / 1000
        elif unit1 == "Gram" and unit2 == "Ton":
            eq = n / 1000000
        elif unit1 == "Gram" and unit2 == "Kilogram":
            eq = n / 1000
        elif unit1 == "Gram" and unit2 == "Decagram":
            eq = n / 100
        elif unit1 == "Gram" and unit2 == "US Pound":
            eq = n / 454
        elif unit1 == "Gram" and unit2 == "Ounce":
            eq = n / 28.35
        elif unit1 == "Miligram" and unit2 == "Ton":
            eq = n / 1000000000
        elif unit1 == "Miligram" and unit2 == "Kilogram":
            eq = n / 1000000
        elif unit1 == "Miligram" and unit2 == "Decagram":
            eq = n / 10000
        elif unit1 == "Miligram" and unit2 == "Gram":
            eq = n / 1000
        elif unit1 == "Miligram" and unit2 == "US Pound":
            eq = n / 453600
        elif unit1 == "Miligram" and unit2 == "Ounce":
            eq = n / 28350
        elif unit1 == "US Pound" and unit2 == "Ton":
            eq = n / 2205
        elif unit1 == "US Pound" and unit2 == "Kilogram":
            eq = n / 2.205
        elif unit1 == "Ounce" and unit2 == "Ton":
            eq = n / 35270
        elif unit1 == "Ounce" and unit2 == "Kilogram":
            eq = n / 35.274
        elif unit1 == "Ounce" and unit2 == "US Pound":
            eq = n / 16
        elif unit1 == "Decagram" and unit2 == "Ton":
            eq = n / 100000
        elif unit1 == "Decagram" and unit2 == "Kilogram":
            eq = n / 100
        elif unit1 == "Ounce" and unit2 == "Decagram":
            eq = n / 0.35

        eq = str(eq)
        n = str(n)
        eqLabel.set(n + " " + unit1 + " = " + eq + " " + unit2)
    except Exception:
        eq = ""    
        eqLabel.set(eq)  


window = Tk()
window.geometry("400x170")
window.title("Mass Calculator")
window.config(bg="#000000")

entry = Entry(window, width = 20, font= 25)
entry.pack()

frame = Frame(window)
frame.pack()


options = [
    "Ton",
    "Kilogram",
    "Decagram",
    "Gram",
    "Miligram",
    "US Pound",
    "Ounce"
]

options2 = [
    "Ton",
    "Kilogram",
    "Decagram",
    "Gram",
    "Miligram",
    "US Pound",
    "Ounce"
]

clicked = StringVar()
clicked2 = StringVar()
clicked.set(options[0])
clicked2.set(options2[0])

drop = OptionMenu(window, clicked, *options)
drop.pack()
to = Label(window, text="To", font= 25)
to.pack()
drop2 = OptionMenu(window, clicked2, *options2)
drop2.pack()

convert = Button(window, text = "Convert", font = 35, command=convert)
convert.pack()

eqLabel = StringVar()

label = Label(window, textvariable = eqLabel, font = 35, bg= "white")
label.pack()


window.mainloop()