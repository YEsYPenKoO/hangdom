from tkinter import *

root = Tk()
root.title('Hangman')
canvas = Canvas(root, width=600, height=600)
canvas.pack()

def b():
    y = 0
    while y<600:
        x=0
        while x<600:
            canvas.create_rectangle(x,y, x+20, y+20, fill='white', outline='black')
            x=x+20
        y=y+20
# b()

entrance = '''Try playing hangman. You have 6 guessing attempts'''

canvas.create_text(290, 98, text=entrance,fill='red', font=('Helvetica', '14'))
b1=Button(root, text='Play', width=10, height=2)
b1.place(x=258, y=300)
root.mainloop()