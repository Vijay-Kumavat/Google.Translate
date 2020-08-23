from tkinter import * #import tkinter for python GUI
from tkinter import ttk  # import ttk for combobox
from methods import Mytranslator # import the method class (Mytranslate)

#inital object of tkinter
app=Tk()

# geometry for python GUI
app.geometry('350x520') 

#title of GUI
app.title('Google Translate')

app.resizable(0,0)

#bg color of GUI
app.config(bg='#3385ff') #config of GUI

#app icon
app.wm_iconbitmap('icon.ico')

# make the get method for text in frame
def get():
    s = srcLangs.get()
    d = destLangs.get()
    message=sourceText.get( 1.0,END)
    translator=Mytranslator()
    text = translator.run(txt=message,src=s,dest=d)
    destText.delete(1.0,END) # default delete text
    destText.insert(END,text) # delete then after you can see the translate text

appName=Label(app,text='Google Translate',font=('serif',20),bg="#4dff4d",fg='black',height=2) #create the app name
appName.pack(side=TOP,fill=BOTH,pady=0) #place of appname 
version = Label(app,text='beta',bg='#4dff4d').place(x=250,y=45) #for beta

#create the frame for write the some
frame=Frame(app).pack(side=BOTTOM)

#for text size and color
sourceText=Text(frame,font=('serif',10),height=11,wrap=WORD)

#add 5px padding in up-down(y) and left-right(x) 
sourceText.pack(side=TOP,padx=5,pady=5)#widget of tkinter #pack - close the pack

#translate btn
# relief : btn style and command : when you click the transbtn then get method call and you have see your text to translate
transBtn = Button(frame,text='Translate',font=('serif',12),border=('2px','black'),fg='white',bg='black',activebackground='#4dff4d',relief=SOLID,command=get)
transBtn.pack(side=TOP,pady=15)# position of transbtn

#write the lang for translate
# langs=['English','Gujarati','Hindi'] #list
langs = Mytranslator().langs #create the new variable for lang

#create the dropdown in python GUI using ttk.Combobox
srcLangs = ttk.Combobox(frame,values=langs,width=10) #combobox for showing the all langs #srcLang : writen lang
srcLangs.place(x=30,y=280)

#default lang
srcLangs.set('english')

#create the dropdown in python GUI using ttk.Combobox
destLangs = ttk.Combobox(frame,values=langs,width=10) # destLang : traslate lang
destLangs.place(x=240,y=280)

#default lang
destLangs.set('hindi')

#for text size and color
destText=Text(frame,font=('serif',10),height=11,wrap=WORD)

#add 5px padding in up-down(y) and left-right(x) 
destText.pack(side=TOP,padx=5,pady=5)


#call the tkinter
app.mainloop()
