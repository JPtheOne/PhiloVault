from tkinter import*
from tkinter import ttk
from PIL import Image, ImageTk

class RootWindow():
    #Window properties 
    def __init__(self): 
        self.root = Tk()
        self.root.title("Menu")
        self.root.geometry("400x200")
        self.root.configure(bg='lightblue')
        self.root.iconbitmap('GUI_media/book.ico')

        # Label properties
        title = Label(self.root, text="Welcome to the cultural library!")
        title.pack(pady=10)
        label1 = Label(self.root, text="Choose your language")
        label1.pack(pady=10)

        # Declaring images to use in buttons
        en_image = Image.open("GUI_media/en.png")
        en_image = en_image.resize((100, 100), Image.ANTIALIAS)
        en_photo = ImageTk.PhotoImage(en_image)

        fr_image = Image.open("GUI_media/fr.png")
        fr_image = fr_image.resize((100, 100), Image.ANTIALIAS)
        fr_photo = ImageTk.PhotoImage(fr_image)

        # Creating buttons
        en_button = Button(self.root, image=en_photo, command=lambda:LibraryMenu("EN"))
        en_button.pack(side="left", padx=(0,10))

        fr_button = Button(self.root, image=fr_photo, command=lambda:LibraryMenu("FR"))
        fr_button.pack(side="right", padx=(10,0))
        
        mainloop()


class LibraryMenu:
    def __init__(self, language):
        #Window Properties
        self.library = Toplevel()
        self.library.title("Library Menu")
        self.geometry = ("854x480")
        self.library.iconbitmap('GUI_media/book.ico')

        #Setting backgrounds
        if language == "EN":
            bg_image_path = 'GUI_media/en_bg.jpg'
        elif language == "FR":
            bg_image_path = 'GUI_media/fr_bg.jpg'

        bg_image = Image.open(bg_image_path)
        bg_image = bg_image.resize((854, 480), Image.ANTIALIAS)
        bg_image = ImageTk.PhotoImage(bg_image)

        canvas = Canvas(self.library, width=854, height=480)
        canvas.pack(fill="both", expand=True)
        canvas.create_image(0, 0, image=bg_image, anchor="nw")

        # Keep a reference to the image object to avoid garbage collection
        canvas.image = bg_image

        # Label properties
        label1 = Label(self.library, text="What you want to do today?")
        label1.place(x=350, y=10) # Adjust x and y values accordingly to position the label

        #Button creation
        button1 = Button(self.library, text="Compare two documents")
        button1.place(x=350, y=150) # Adjust x and y values accordingly to position the button

        button2 = Button(self.library, text="Search relevant documents")
        button2.place(x=350, y=250) # Adjust x and y values accordingly to position the button

        button3 = Button(self.library, text="Manipulate documents")
        button3.place(x=350, y=350) # Adjust x and y values accordingly to position the button

        button4 = Button(self.library, text ="Exit", command=self.library.destroy)
        button4.place(x=700, y= 400)


        self.library.mainloop()


if __name__ == "__main__":
    root_window = RootWindow()