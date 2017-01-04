from tkinter import *
tk=Tk()

canvas=Canvas(tk, width=400, height=400)
canvas.pack()

my_image=PhotoImage(file="Mafer.png")
canvas.create_image(0,0,anchor=NW, image=my_image)



def moveimage(event):
    if event.keysym == 'Up':
        canvas.move(1, 0, -3)
    elif event.keysym == 'Down':
        canvas.move(1, 0, 3)
    elif event.keysym == 'Left':
        canvas.move(1, -3, 0)
    else:
        canvas.move(1, 3, 0)

canvas.bind_all('<KeyPress-Up>', moveimage)
canvas.bind_all('<KeyPress-Down>', moveimage)
canvas.bind_all('<KeyPress-Left>', moveimage)
canvas.bind_all('<KeyPress-Right>', moveimage)

tk.mainloop()
