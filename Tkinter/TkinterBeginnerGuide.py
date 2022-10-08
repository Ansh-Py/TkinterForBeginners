#IMPORT MODULES
from tkinter import *
from tkinter import ttk

#Create Window
window = Tk()
window.title("BeginnersGuideToTkinter")
window.geometry("600x600")

#Create Label Widget
message_text = StringVar()
message_text.set("Hello World")
message = Label(window, textvariable=message_text)
message.pack()

#Spacing - IGNORE THIS
space0 = StringVar()
space0.set("\n")
space_label = Label(window, textvariable=space0)
space_label.pack()

#Create Entry Widget
entry = Entry(window)
entry.pack()

#Spacing - IGNORE THIS
space1 = StringVar()
space1.set("\n")
space_label = Label(window, textvariable=space1)
space_label.pack()

#Create Button Widget
button_text = StringVar()
button_text.set("Click Me")
button = Button(window, textvariable=button_text)
button.pack()

#Spacing - IGNORE THIS
space2 = StringVar()
space2.set("\n")
space_label = Label(window, textvariable=space2)
space_label.pack()

#Create Option Menu Widget
options = ["UNSELECTED", "1", "2", "3"]
chosen_option = StringVar()
chosen_option.set(options[0])
option_menu = OptionMenu(window, chosen_option, *options)
option_menu.pack()

#Spacing - IGNORE THIS
space3 = StringVar()
space3.set("\n")
space_label = Label(window, textvariable=space3)
space_label.pack()

#Create CheckButton Widget
check_option0 = Checkbutton(window, text="UNSELECTED")
check_option0.pack()
check_option1 = Checkbutton(window, text="Apple")
check_option1.pack()
check_option2 = Checkbutton(window, text="Banana")
check_option2.pack()
check_option3 = Checkbutton(window, text="Orange")
check_option3.pack()

#Spacing - IGNORE THIS
space4 = StringVar()
space4.set("\n")
space_label = Label(window, textvariable=space4)
space_label.pack()

#Create Radio Button Widget
radio_variable = StringVar()
radio_option0 = Radiobutton(window, text="UNSELECTED", value="UNSELECTED", variable=radio_variable)
radio_option0.select()
radio_option0.pack()

radio_option1 = Radiobutton(window, text="Red", value="Red", variable=radio_variable)
radio_option1.deselect()
radio_option1.pack()

radio_option2 = Radiobutton(window, text="Blue", value="Blue", variable=radio_variable)
radio_option2.deselect()
radio_option2.pack()

radio_option3 = Radiobutton(window, text="Green", value="Green", variable=radio_variable)
radio_option3.deselect()
radio_option3.pack()

#End
window.mainloop()