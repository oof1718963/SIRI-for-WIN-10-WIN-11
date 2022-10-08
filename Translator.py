from tkinter import *
from tkinter import ttk
from googletrans import Translator, LANGUAGES

root = Tk()
root.geometry("1080x400")
root.configure(bg="#F2CCC3")
root.title("Language Translator")

language=list(Languages.values())
lb_title=Label(root, text="LANGUAGE TRANSLATOR", bg="#F2CCC3")
lb_title.place(relx=0.5,rely=0.1,anchor=CENTER)

label_input=Label(root, text="Enter Text", bg="#F2CCC3", font="arial 13 bold"
label_input.place(relx=0.02,rely=0.2,anchor=W)
src_lang=ttk.Combobox(root, values=language, width=23, state="readonly")
src_lang.place(relx=0.13,rely=0.2,anchor=W)
src_lang.set("english")

lb_output=Label(root, text="Enter Text", bg="#F2CCC3", font="arial 13 bold"
lb_output.place(relx=0.81,rely=0.2,anchor=E)
dest_lang=ttk.Combobox(root, values=language, width=22, state="readonly")
dest_lang.place(relx=0.98,rely=0.2,anchor=E)
dest_lang.set("choose output language")

Input_text=Text(root,font="arial 10",height=11,wrap=WORD,padx=5,pady=5)
Input_text.place(relx=0.02,rely=0.5,anchor=W)
Output_text=Text(root,font="arial 10",height=11,wrap=WORD,padx=5,pady=5)
Output_text.place(relx=0.98,rely=0.5,anchor=E)

def Translate():
    translator=Translator()
    try:
        translated=translator.translate(text=Input_text.get(1.0,END), src=src)
        Output_text.delete(1.0,END)
        Output_text.insert(END, translated.text)
    except:
        print("try again")
        
trans_btn=Button(root,text="Translate",font="arial 12 bold",pady=5,command=Translate)
trans_btn.place(relx=0.5,rely=0.85,anchor=CENTER)
lb_footer=Label(root, text="Created By Whitehat Jr Team", bg="#F2CCC3", font="arial 13 bold"
lb_footer.place(relx=0.81,rely=0.2,anchor=CENTER))
lb_footer.place(relx=0.5,rely=0.97,anchor=CENTER)
root.mainloop()
