from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from pytube import YouTube
import os

root = Tk()

file_type_str = StringVar()
quality_str = StringVar()

# create any callback functions for events here

def download_video():
    try:
        vid = YouTube(link.get())
    except:
        messagebox.showinfo("Error", "Unable to fetch video from link!")
        return
    
    files = vid.streams.filter(file_extension=file_type_str.get(), res=quality_str.get())
    if (len(files) == 0):
        messagebox.showinfo("Error", "Unable to fetch video with specified filetype/resolution!")
        return
    try:
        files.first().download(os.getcwd())
        messagebox.showinfo("Success!", "Your video has been successfully downloaded!")
    except:
        messagebox.showinfo("Error", "Failed to download video!")
        return

# create initial GUI here
# things to make:
# * Text box for link (Entry type)
# * Dropdown for file type (Listbox type)
# * Dropdown for quality (Listbox type)
# * File picker for save location (Don't have to, just drop where its executed)
# * Button to download (Button type)
link = Entry(root)
link_label = Label(root, text = "Link: ")
file_type = ttk.Combobox(root, textvariable=file_type_str)
file_type['values'] = ('mp3',
                       'mp4',
                       'mov',
                       'wav',
                       'mkv')
file_type_label = Label(root, text = "File type: ")
quality = ttk.Combobox(root, textvariable=quality_str)
quality['values'] =   ('144p',
                       '240p',
                       '360p',
                       '480p',
                       '720p',
                       '1080p',
                       '1440p')
quality_label = Label(root, text = "Quality: ")
download_button = Button(root, text = "Download", command=download_video)

# pack elements
link_label.pack()
link.pack()
file_type_label.pack()
file_type.pack()
quality_label.pack()
quality.pack()
download_button.pack()

root.mainloop()
