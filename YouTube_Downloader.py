from dis import Instruction
import tkinter
from tkinter import *
from pytube import YouTube, Stream
from PIL import ImageTk, Image
from pytube import YouTube, Stream
# functions


def Reset():
    Instructions.config(
        text="copy paste your link")
    Instructions.update()


def PopUp():
    Instructions.config(
        text="Your Download is starting ...................!!!")
    Instructions.update()
    inp = inputtxt.get(1.0, "end-1c")
    # xINPUT = DownloadYT()

    pop = Toplevel(frame)
    pop.geometry("300x300")
    pop.title("Progress report")
    pop['background'] = "#E62D27"
    photo_pop = PhotoImage(file="1.png")
    pop.iconphoto(False, photo)

    yt = YouTube(inp)
    filesize1 = yt.streams.get_highest_resolution()
    filesize1.title
    files = filesize1.filesize
    Progress_Report = Label(
        pop, text="Progress Report -: ", font=('Helvetica 15'))

    Progress_Report.pack()
    Progress_Report.config(text="this is progress report")
    Progress_Report.config(bg="#FFFFFF")
    Progress_Report2 = Label(pop, text="\nYour link is  -: \n"+inp +
                             "\nDownloading your video.......\n"+"\nVideo Tittle -: \n" + filesize1.title + "\nVideo Resolution -: " +
                             filesize1.resolution + "\nyour file size is " +
                             str(round(files/1000000, 2))+"mb", font=('Helvetica 15'))

    Progress_Report2.pack()
    # Progress_Report2.config(text="this is progress report")
    Progress_Report2.config(bg="#FFFFFF")
    yt1 = YouTube(inp)
    yt1.streams.filter(res="720p").first().download()


# Tkinter window

frame = Tk()
frame.title("YouTube Video Downloader")
frame.geometry('600x700')
# frame.resizable(false, false)

# Tkinter tittle logo

photo = PhotoImage(file="1.png")
frame.iconphoto(False, photo)

# tkinter background color
frame['background'] = "#E62D27"


# Tkinter  youtube button image on window
x = Image.open("1.png")
resize_image = x.resize((50, 50))
imgLogo = ImageTk.PhotoImage(resize_image)
l = Label(bg="#E62D27", image=imgLogo)
l.pack()
l.place(relx=0.3, rely=0.5, anchor=CENTER)

# Tkinter youtube GIF
youtubeGIF = Image.open("youtube.gif")
resize_youtubeGIF = youtubeGIF.resize((500, 300))
imgYoutube = ImageTk.PhotoImage(resize_youtubeGIF)
youtubeGIF_Label = Label(bg="#E62D27", image=imgYoutube)
youtubeGIF_Label.pack()
youtubeGIF_Label.place(relx=0.5, rely=0.25, anchor=CENTER)


# Tkinter Input Feild


inputtxt = Text(frame,
                height=3,
                width=60)
inputtxt.pack()
inputtxt.place(relx=0.5, rely=0.5, anchor=CENTER)


# Tkinter Downlaod button
imgDownload_button = PhotoImage(file="4.png")
Download_Button = Button(frame, text='Download', bg="#E62D27",
                         image=imgDownload_button, command=PopUp)
Download_Button.pack()
Download_Button.place(relx=0.5, rely=0.7, x=-20)


# Reset

re = Image.open("reset.png")
reset_image = re.resize((50, 50))

imgReset_button = ImageTk.PhotoImage(reset_image)
Rest_Button = Button(frame, text='Reset Button', bg="#E62D27", image=imgReset_button,
                     command=Reset)
Rest_Button.pack()
Rest_Button.place(relx=0.5, rely=0.9, x=-17)


# tkinter label for Instructions
Instructions = Label(frame, bg="#E62D27", text="copy paste your link")
Instructions.pack()
Instructions.place(relx=0.5, y=415, anchor=CENTER)
Instructions.config(font=("Comic Sans", 20))
Instructions.config(fg="#ffe6e6")


# tkinter mainloop
mainloop()
