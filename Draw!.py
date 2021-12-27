from tkinter import *
app = Tk()
app.geometry("400x400")
app.mainloop()
canvas = Canvas(app, bg='black')
canvas.pack(anchor='nw', fill='both', expand=1)
def get_x_and_y(event):
    global lasx, lasy
    lasx, lasy = event.x, event.y

def draw_smth(event):
    global lasx, lasy
    canvas.create_line((lasx, lasy, event.x, event.y), 
                      fill='red', 
                      width=2)
    lasx, lasy = event.x, event.y
canvas.bind("<Button-1>", get_x_and_y)
canvas.bind("<B1-Motion>", draw_smth)
