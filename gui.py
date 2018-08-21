from tkinter import *
import infer
def find_news():
    global e
    string = e.get()
    ans=infer.fake_fake(string)
    if(ans==0):
        w.config(text="FAKE",bg="red",fg="white",font="none 19 bold")
    else:
        w.config(text="REAL",bg="green",fg="white",font="none 19 bold")



window = Tk()

window.title('Fake News Detector')
window.geometry("600x600")

window.configure(background='black')
l1 = Label(window,text="FND",bg="black",fg="white",font="none 19 bold")
l1.pack()
l1.focus_set()

frame=Frame(width=5,height=50,bg="black")
frame.pack()

l = Label(window,text="Enter headline of news:",bg="black",fg="white",font="none 12 bold")
l.pack()
l.focus_set()

e = Entry(window,width=100)
e.pack()
e.focus_set()
frame=Frame(width=5,height=100,bg="black")
frame.pack()
w = Label(window, bg="black")
w.pack()

b = Button(window,text='submit',command=find_news)
b.pack(side='bottom')
window.mainloop()