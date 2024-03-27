import customtkinter as ctk
from tkinter import ttk
from customtkinter import CTkLabel
from pytube import YouTube
import os
def download_video():
    url = entry_url.get()
    resolution = resolution_var.get()
    status_label.pack(padx=10, pady=5)
    progress_label.pack(padx=10,pady=5)
    progress_bar.pack(padx=10,pady=5)
    try:
        yt = YouTube(url,on_progress_callback=on_progress)
        stream = yt.streams.filter(res=resolution).first()
        os.path.join("downloads",f"{yt.title}.mp4")
        stream.download(output_path="downloads")
        status_label.configure(text=f"Downloaded{str()}", text_color="white", fg_color="green")
    except Exception as e :
        status_label.configure(text=f"Error{str(e)}",text_color="white",fg_color="red")
def on_progress(stream,chunck,bytes_remaining):
    total_size = stream.filesize
    bytes_downloaded = total_size - bytes_remaining
    percentage_completed = bytes_downloaded / total_size * 100
    progress_label.configure(text=str(int(percentage_completed)) + "%")
    progress_label.update()
    progress_bar.set(float(percentage_completed/100))

#window
root = ctk.CTk()
ctk.set_appearance_mode("System")
ctk.set_default_color_theme("blue")

#title of window
root.title("Youtube Downloader")

#set min and max width
root.geometry("720x480")
root.minsize(720,480)
root.maxsize(1080,720)

#create a frame to hold the content
content_frame = ctk.CTkFrame(root)
content_frame.pack(fill=ctk.BOTH,expand=True,padx=10,pady=10)

#create a label and entry widget for the video url
url_label=ctk.CTkLabel(content_frame,text="Enter the youtube url here: ")
entry_url=ctk.CTkEntry(content_frame,width=400,height=40)
url_label.pack(padx=10, pady=5)
entry_url.pack(padx=10, pady=5)

#create a download button
download_button=ctk.CTkButton(content_frame,text="Download",command=download_video)
download_button.pack(padx=10, pady=5)

#create a resolution combo box
resolutions=["720p","360p","240p"]
resolution_var=ctk.StringVar()
resolution_combobox = ttk.Combobox(content_frame,values=resolutions,textvariable=resolution_var)
resolution_combobox.pack(padx=10, pady=5)
resolution_combobox.set("720p")

#create a label and the progress bar
progress_label = ctk.CTkLabel(content_frame,text="0%")
#progress_label.pack(padx=10,pady=5)

progress_bar = ctk.CTkProgressBar(content_frame,width=400)
progress_bar.set(0)
#progress_bar.pack(padx=10,pady=5)

# create a status label
status_label=ctk.CTkLabel(content_frame,text="")
#status_label.pack(padx=10,pady=5)

#start the app
root.mainloop()