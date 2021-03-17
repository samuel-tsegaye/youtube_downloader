
import tkinter as tk
from tkinter.ttk import Progressbar
from tkinter import *
from PIL import ImageTk
import ttk

splash_root = Tk()
splash_root.title("Downloader")

splash_root.geometry("800x300")
progress = Progressbar(splash_root, style="red.Horizontal.TProgressbar", orient=HORIZONTAL, length=500, mode='determinate', )

splash_root.overrideredirect(True)
#sa = ImageTk.PhotoImage(file="image/211.jpg")
#label1 = Label(splash_root, image=sa)
#label1.place(x=0, y=0)
a = '#283747'
width_of_window = 460
height_of_window = 200
screen_width = splash_root.winfo_screenwidth()
screen_height = splash_root.winfo_screenheight()
x_coordinate = (screen_width / 2) - (width_of_window / 2)
y_coordinate = (screen_height / 5) - (height_of_window / 5)
splash_root.geometry("%dx%d+%d+%d" % (width_of_window, height_of_window, x_coordinate, y_coordinate))


s = ttk.Style()
s.theme_use('clam')
s.configure("red.Horizontal.TProgressbar", foreground='red', background='#4f4f4f')
progress = Progressbar(splash_root, style="red.Horizontal.TProgressbar", orient=HORIZONTAL, length=500, mode='determinate', )


def main_window():
    splash_root.destroy()
    main = tk.Tk()
    main.title("youtube Downloader")
    main.resizable(width=False, height=False)
    main.geometry("800x600")

    rows = 0
    while rows < 50:
        main.rowconfigure(rows, weight=1)
        main.columnconfigure(rows, weight=1)
        rows += 1

    yd = ttk.Notebook(main)
    yd.grid(row=0, column=0, columnspan=50, rowspan=50, sticky="NESW",)

    page1 = ttk.Frame(yd)
    yd.add(page1, text="Direct Downloader ")

    frame1 = Canvas(master=page1, width=200, height=200, bg='#D1F2EB')
    frame1.pack(expand=YES, fill=BOTH)

    page2 = ttk.Frame(yd)
    yd.add(page2, text="Playlist Downloader ")
    frame2 = Canvas(master=page2, width=200, height=200, bg='#FAD7A0')
    frame2.pack(expand=YES, fill=BOTH)

    page3 = ttk.Frame(yd)
    yd.add(page3, text="To Mp3 converter")
    frame3 = Canvas(master=page3, width=200, height=200, bg='#EDBB99')
    frame3.pack(expand=YES, fill=BOTH)

    main.mainloop()


def bar():
    l4 = Label(splash_root, text='Loading...', fg='white', bg=a)
    lst4 = ('Calibri (Body)', 10)
    l4.config(font=lst4)
    l4.place(x=18, y=210)

    import time
    r = 0
    for i in range(100):
        progress['value'] = r
        splash_root.update_idletasks()
        time.sleep(0.03)
        r = r + 1
    b1 = Button(splash_root, width=10, height=1, text='Get Started', command=bar, border=0, fg=a, bg='white')
    b1.place(x=170, y=200)


Frame(splash_root, width=427, height=241, bg=a).place(x=0, y=0)  # 249794

splash_label = Label(splash_root, text="welcome to youtube downloader", fg='white', bg=a)
lst1 = ('Calibri (Body)', 12, 'bold')
splash_label.config(font=lst1)
splash_label.place(x=50, y=50)
splash_label = Label(splash_root, text='creater', fg='white', bg=a)
lst2 = ('Calibri (Body)', 12)
splash_label.config(font=lst2)
splash_label.place(x=270, y=160)

splash_label = Label(splash_root, text='samuel tsegaye', fg='white', bg=a)
lst3 = ('Calibri (Body)', 9)
splash_label.config(font=lst3)
splash_label.place(x=285, y=180)
splash_root.after(3000, main_window)


mainloop()