import tkinter as tk

from pytube import YouTube



def download_video():
     url=YouTube(str(link.get()))
     # video=url.streams.filter(file_extension="mp4").first() # mp4 format video
     video=url.streams.filter(res="360p").first()

     video.download()
     tk.Label(root,text='your video is download',font='arial 15',fg='white',bg='#EC7063').place(x=10,y=140)

root=tk.Tk()
root.geometry("1000x800")
root.config(bg="blue")
root.resizable(width=False,height=False)
root.title("downloader")
link=tk.StringVar()
tk.Label(root,text='   vidow  downloder      ',font='arial 20 bold',fg="white",bg="black").pack()
tk.Label(root,text='   paste your youtube link here      ',font='arial 20 bold',fg="black",bg="#EC7063").place(x=5,y=60)

link_enter=tk.Entry(root,width=53,textvariable=link,font='arial 16 bold',bg='lightgreen').place(x=5,y=100)
tk.Button(root,text=" DOWNLOAD VIDEO",font="arial 15 bold",fg="white",bg="black",padx=2,command=download_video).place(x=385,y=140)


root.mainloop()


