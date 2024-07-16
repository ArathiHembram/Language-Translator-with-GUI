from tkinter import *
from tkinter import ttk #ttk is a module used to style tkinter widget like box etc
from googletrans import Translator,LANGUAGES #googletrans is a free google api that uses Ajax api to make calls,search methods,detect and translate languages
import traceback
import mysql.connector

# Connect to MySQL database
conn = mysql.connector.connect(
    host="localhost",
    user="Arathi",
    password="tiger",
    database="Translator"
)
cursor = conn.cursor()

# Function to save translation to the database
def save_translation(input_text, output_text):
    cursor.execute("INSERT INTO TRANSLATIONS (INPUT, OUTPUT) VALUES (%s, %s)", (input_text, output_text))
    conn.commit()



root=Tk()
root.geometry('1100x320') #x,y
root.resizable(0,0)  #cannot resize the box
#root.iconbitmap('logo simpli.ico')
root['bg']='skyblue'

root.title('Language Translator') #GUI title
Label(root, text = "Language Translator", font = "Arial 20 bold").pack()#Heading


Label(root,text = "Enter Text", font = "arial 13 bold", bg="white smoke").place(x=165,y=90)

Input_text=Entry(root,width=60)
Input_text.place(x=50,y=130)
Input_text.get()

Label(root, text="Output",font="arial 13 bold",bg="white smoke").place(x=780, y=90)

Output_text=Text(root,font="arial 10",height=5, wrap = WORD ,padx=5, pady=5,width=50)
Output_text.place(x=600,y=130)

language = list(LANGUAGES.values())

dest_lang=ttk.Combobox(root, values = language,width=22)
dest_lang.place(x=130,y=180)
dest_lang.set("choose language")


def Translate():
    try:
        input_text=Input_text.get().strip()
        if not input_text:
            Output_text.delete(1.0,END)
            Output_text.insert(END,"Please enter text to translate")
            return
        
        translator=Translator(service_urls=['translate.google.com'],user_agent='Mozilla/5.0')
        translated=translator.translate(text=input_text, dest=dest_lang.get())
        Output_text.delete(1.0,END)
        Output_text.insert(END,translated.text)

     # Save input text and output translation to the database
        save_translation(input_text, translated.text)   

    except Exception as e:
        print(f"Translator error: {e}")
        
        
        

trans_btn=Button(root,text="Translate", font="arial 12 bold",pady=5,command = Translate, bg= "lightpink", activebackground = "pink")
trans_btn.place(x=445,y=180)



root.mainloop()
