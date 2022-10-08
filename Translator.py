from tkinter import *
from PIL import ImageTk , Image
from tkinter import ttk
from googletrans import Translator , LANGUAGES
from googletrans import Translator
from googletrans import LANGUAGES

root = Tk()
root.geometry("1000x1000")
root.title("Translator")
root.config(bg="white")

title_label = Label(root,text="Translator",bg="white")
title_label.place(relx=0.5,rely=0.1,anchor=CENTER)

label1 = Label(root,text="Enter Text")
label1.place(relx=0.2,rely=0.3,anchor=W)
textarea1 = Text(root,width=30,height=10)
textarea1.place(relx=0.1,rely=0.5,anchor=W)
root.mainloop()
root.title("Language Translator")
root.geometry("600x400")
root.configure(bg = "#fced95")
language = list(LANGUAGES.values())


label_heading = Label(root, text = "Language Translator", bg = "#fced95", font = ("SF Pro Display", 30, "bold"))
label_heading.place(relx = 0.5, rely = 0.1, anchor = CENTER)

input_label = Label(root, text = "Enter Text", bg = "#fced95", font = ("SF Pro Display", 17 , "bold"))
input_label.place(relx = 0.02, rely = 0.3, anchor = W)

d1 = ttk.Combobox(root, state = "readonly", values = language, width = 25)
d1.place(relx = 0.02, rely = 0.2, anchor = W)
d1.set("English")

input_text = Text(root, bg = "#f2b8da", font = ("SF Pro Display", 15, "bold"), height = 6, wrap = WORD, width = 20, padx = 10, pady = 1, bd = 0)
input_text.place(relx = 0.02, rely = 0.55, anchor = W)

output_label = Label(root, text = "Output", bg = "#fced95", font = ("SF Pro Display", 20, "bold"))
output_label.place(relx = 0.98, rely = 0.3, anchor = E)

d2 = ttk.Combobox(root, state = "readonly", values = language, width = 25)
d2.place(relx = 0.98, rely = 0.2, anchor = E)
d2.set("Choose Output Language")

output_text = Text(root, bg = "#f2b8da", font = ("SF Pro Display", 15, "bold"), height = 6, wrap = WORD, width = 20, padx = 10, pady = 1, bd = 0)
output_text.place(relx = 0.98, rely = 0.55, anchor = E)

translate_btn = Button(root, text = "Translate", font = ("Bell MT", 15, "bold"), bg = "#f2b8da", fg = "black", relief = FLAT, padx = 10, pady = 1)
translate_btn.place(relx = 0.5, rely = 0.8, anchor = CENTER)

root.mainloop()