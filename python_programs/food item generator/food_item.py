from tkinter import *
from tkinter import filedialog
from PIL import ImageTk, Image

root = Tk()

root.geometry("1000x900")
root.config(bg="dark gray")

title_frame = Frame(root, bg="dark gray")
title_frame.pack()

image1 = Image.open("logo.png")
logo = ImageTk.PhotoImage(image1)

logo_label = Label(title_frame, image=logo, bg="dark gray")
logo_label.pack()

main_frame = Frame(root, bg="dark gray")
main_frame.pack()

frame = Frame(main_frame)
frame.grid(row=0, column=0, pady= 20, padx = 20)

bottomframe = Frame(main_frame)
bottomframe.grid(row = 0, column = 1, pady= 20, padx = 20)

namespace =''
identifier =''
foil = ''
stack_size = ''
nutrition = ''
saturation = ''
always_eat = ''
text_color = ''

namespace_label = Label(frame, text = "What namespace do you want?")
identifier_label = Label(frame, text = "What's the identifier for your food item?")
foil_label = Label(frame, text = "Do you want it to be shiny? (true / false)")
stack_size_label = Label(frame, text = "What stack size do you want? (number)")
nutrition_label = Label(frame, text = "What nutrition value do you want (up to 20 hunger points)")
saturation_label = Label(frame, text = "What saturation? (poor, low, normal, high, good, max and supernatural")
always_eat_label = Label(frame, text = "Do you want to always be able to eat this? (true/false)")
text_color_label = Label(frame, text = "What color text do you want?")
text_color_label_options = Label(frame, text = "dark blue, dark green, dark aqua, dark red, dark purple")
text_color_label_options2 = Label(frame, text = "gold, gray, dark gray, indigo, green, aqua, red, pink, yellow, white")


namespace_entry = Entry(frame)
identifier_entry = Entry(frame)
foil_entry = Entry(frame)
stack_size_entry = Entry(frame)
nutrition_entry = Entry(frame)
saturation_entry = Entry(frame)
always_eat_entry = Entry(frame)
text_color_entry = Entry(frame)

namespace_label.pack()
namespace_entry.pack()

identifier_label.pack()
identifier_entry.pack()

foil_label.pack()
foil_entry.pack()

stack_size_label.pack()
stack_size_entry.pack()

nutrition_label.pack()
nutrition_entry.pack()

saturation_label.pack()
saturation_entry.pack()

always_eat_label.pack()
always_eat_entry.pack()

text_color_label.pack()
text_color_label_options.pack()
text_color_label_options2.pack()
text_color_entry.pack()

def save_file():
    final_code = text_box.get(0.0, END)
    file_final = filedialog.asksaveasfile(mode='w', defaultextension= ".json")
    file_final.write(final_code)

def fill_code():
    global namespace
    global identifier
    global foil
    global stack_size
    global nutrition
    global saturation
    global always_eat
    global text_color
    global food_code
    global text_box
    namespace = namespace_entry.get()
    identifier = identifier_entry.get()
    foil = foil_entry.get()
    stack_size = stack_size_entry.get()
    nutrition = nutrition_entry.get()
    saturation = saturation_entry.get()
    always_eat = always_eat_entry.get()
    text_color = text_color_entry.get()
    
    food_code = (
    '{\n'
    '"format_version": "1.12.0",\n'
    '"minecraft:item": {\n'
    '    "description": {\n'
    f'        "identifier": "{namespace}:{identifier}"\n'
    '    },\n'
    '    "components": {\n'
    '        "minecraft:hand_equipped": false,\n'
    '        "minecraft:stacked_by_data": true,\n'
    f'        "minecraft:foil": {foil},\n'
    f'        "minecraft:max_stack_size": {stack_size},\n'
    '        "minecraft:use_duration": 32,\n'
    '        "minecraft:food": {\n'
    f'            "nutrition": {nutrition},\n'
    f'            "saturation_modifier": "{saturation}",\n'
    f'            "can_always_eat": {always_eat}\n'
    '            }\n'
    '         }\n'
    '     }\n'
    '}'
    )

    food_code_rp = (
    '{\n'
    '    "format_version": "1.10",\n'
    '        "minecraft:item": {\n'
    '            "description": {\n'
    f'               "identifier": "{namespace}:{identifier}",\n'
    '                "category": "Nature"\n'
    '                   },\n'
    '       "components": {\n'
    f'           "minecraft:icon": "{identifier}",\n'
    '           "minecraft:use_animation": "eat",\n'
    f'           "minecraft:hover_text_color": "{text_color}",\n'
    '           "minecraft:render_offsets": "apple"\n'
    '               }\n'
    '       }\n'
    '}'
    )

    for widget in bottomframe.winfo_children():
        widget.destroy()
    text_box = Text(
        bottomframe,
        height=20,
        width=60
            )
    text_box.insert('end', food_code)
    text_box.grid(row= 2, column= 1)
    save = Button(bottomframe, text='Save BP file to JSON', command= save_file).grid(row= 7, column= 1)

    text_box2 = Text(
        bottomframe,
        height=20,
        width=60
            )
    text_box2.insert('end', food_code_rp)
    text_box2.grid(row= 8, column= 1)
    save2 = Button(bottomframe, text='Save RP file to JSON', command= save_file).grid(row= 15, column= 1)

#######
message = "Your code will appear here."

text_box = Text(
    bottomframe,
    height=20,
    width=60
            )
text_box.insert('end', message)
text_box.grid(row= 2, column= 1)
save = Button(bottomframe, text='Save BP file to JSON', command= save_file).grid(row= 7, column= 1)

text_box2 = Text(
    bottomframe,
    height=20,
    width=60
        )
text_box2.insert('end', message)
text_box2.grid(row= 8, column= 1)
save2 = Button(bottomframe, text='Save RP file to JSON', command= save_file).grid(row= 15, column= 1)

submit = Button(frame, text = "Submit", command = fill_code)
submit.pack()

root.mainloop()