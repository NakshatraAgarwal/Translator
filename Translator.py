from tkinter import *
from tkinter import ttk
from googletrans import Translator, LANGUAGES

translator = Translator()
root = Tk()
root.geometry("1000x500")
root.title("Translator")
root.config(bg="lightgrey")

language = list(LANGUAGES.values())

label = Label(root,text="Translator",font=("Times",40,"bold"),bg="lightgrey")
label.place(relx=0.5,rely=0.1,anchor=CENTER)

label1 = Label(root,text="Enter Text",bg="lightgrey",font=("Times",12))
label1.place(relx=0.1,rely=0.2,anchor=CENTER)

typing = ttk.Combobox(values=language,state="readonly")
typing.place(relx=0.3,rely=0.2,anchor=E)
typing.set("english")

area = Text(root,height=20, wrap=WORD, width = 40, bd=0)
area.place(relx=0.2,rely=0.6,anchor=CENTER)

label2 = Label(root,text="Output",bg="lightgrey",font=("Times",13))
label2.place(relx=0.7,rely=0.2,anchor=CENTER)

output = ttk.Combobox(values=language)
output.place(relx=0.9,rely=0.2,anchor=E)
output.set("marathi")

area2 = Text(root,height=20, wrap=WORD, width=40, bd=0)
area2.place(relx=0.8,rely=0.6,anchor=CENTER)

def translate():
     src_lan = typing.get()
     output_lan = output.get()
     global translator
     src_text = area.get(1.0,END)
     
     
     translated = translator.translate(text = src_text, src=src_lan, dest = output_lan)
     area2.delete(1.0,END)
     area2.insert(1.0, translated.text)
         

        
btn = Button(root,text="Translate",command=translate,width=15,height=3)
btn.place(relx=0.5,rely=0.8,anchor=CENTER)

         
         



root.mainloop()
