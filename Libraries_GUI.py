from tkinter import*
from tkinter import ttk
from PIL import Image, ImageTk

class RootWindow():
    #Window properties 
    def __init__(self): 
        self.root = Tk()
        self.root.title("Menu")
        self.root.geometry("250x200")
        self.root.configure(bg='lightblue')
        self.root.iconbitmap('GUI_media/book.ico')

        # Label properties
        title = Label(self.root, text="Welcome to the cultural library!")
        title.grid(row = 0, column = 0, columnspan= 2, pady=10)
        label1 = Label(self.root, text="Choose your language")
        label1.grid(row =1, column = 0, columnspan = 2, pady=10)

        # Declaring images to use in buttons
        en_image = Image.open("GUI_media/en.png")
        en_image = en_image.resize((100, 100), Image.ANTIALIAS)
        en_photo = ImageTk.PhotoImage(en_image)

        fr_image = Image.open("GUI_media/fr.png")
        fr_image = fr_image.resize((100, 100), Image.ANTIALIAS)
        fr_photo = ImageTk.PhotoImage(fr_image)

        # Creating buttons
        en_button = Button(self.root, image=en_photo, command=lambda:LibraryMenu("EN"))
        en_button.grid(row=2, column=0, padx=(0, 10))

        fr_button = Button(self.root, image=fr_photo, command=lambda:LibraryMenu("FR"))
        fr_button.grid(row=2, column=1, padx=(10, 0))
        
        self.root.mainloop()


class LibraryMenu:
    def __init__(self, language):
        #Window Properties
        self.width = 854
        self.height = 480
        self.geometry = (str(self.width)+"x"+str(self.height))
        self.library = Toplevel()
        self.library.title("Library Menu")
        self.library.iconbitmap('GUI_media/book.ico')

        #Finding routes for bg picture
        if language == "EN":
            bg_image_path = 'GUI_media/en_bg.jpg'
        elif language == "FR":
            bg_image_path = 'GUI_media/fr_bg.jpg'

        #Setting the background
        bg_image = Image.open(bg_image_path)
        bg_image = bg_image.resize((self.width, self.height), Image.ANTIALIAS)
        bg_image = ImageTk.PhotoImage(bg_image)

        #Creating canvas to display the background
        canvas = Canvas(self.library, width = self.width, height = self.height)
        canvas.grid(row=0, column=0, sticky="nsew")
        canvas.create_image(0, 0, image=bg_image, anchor="nw")
        canvas.image = bg_image

        #Declaration of frames. Each frame will hold a new design for each of the operations
        self.compareFrame = Frame(self.library, bg ="")
        self.queryFrame = Frame(self.library, bg ="")

        # Declaring titles of the frames
        # Compare docs title
        title1_label = Label(self.compareFrame, text="Compare documents through similarity formulas")
        title1_label.grid(row=0, column=0, columnspan=2, pady=10)
        
        #Querying title
        title2_label = Label(self.queryFrame, text = "Input a query")
        title2_label.grid(row =0, column = 0, columnspan=2, pady=10)

        # Create combo boxes for selecting documents
        doc1_label = Label(self.compareFrame, text="Document 1:")
        doc1_label.grid(row=1, column=0)
        doc1_combobox = ttk.Combobox(self.compareFrame)
        doc1_combobox.grid(row=1, column=1)

        doc2_label = Label(self.compareFrame, text="Document 2:")
        doc2_label.grid(row=2, column=0)
        doc2_combobox = ttk.Combobox(self.compareFrame)
        doc2_combobox.grid(row=2, column=1)


        #query_label = Label(self.queryFrame, text = "Type the query you wanna find")

        # Create a combo box for choosing the formula
        formula_label = Label(self.compareFrame, text="Select a formula:")
        formula_label.grid(row=3, column=0)
        formula_combobox = ttk.Combobox(self.compareFrame)
        formula_combobox.grid(row=3, column=1)

        # Create a textbox for displaying the result
        result_label = Label(self.compareFrame, text="Result:")
        result_label.grid(row=4, column=0)
        result_text = Text(self.compareFrame, width=30, height=1)
        result_text.grid(row=4, column=1)

        def display_compareFrame():
            self.queryFrame.grid_forget()
            self.compareFrame.grid(row = 0, column = 0, sticky = "nsew")

        def display_queryFrame():
            self.compareFrame.grid_forget()
            self.queryFrame.grid(row = 0, column = 0, sticky = "nsew")

       
        #Declare a menu bar for the window
        menu_bar = Menu(self.library)
        self.library.config(menu=menu_bar)

        # Add file menu with its options
        file_menu = Menu(menu_bar, tearoff=0)
        menu_bar.add_cascade(label="File", menu=file_menu)
        file_menu.add_command(label="Exit", command=self.library.destroy)

        # Add query menu with its options
        query_menu = Menu(menu_bar, tearoff=0)
        menu_bar.add_cascade(label="Query options", menu=query_menu)
        query_menu.add_command(label="Compare two documents", command = display_compareFrame)
        query_menu.add_command(label="Input a query", command = display_queryFrame)

        # Add db menu with its options
        db_menu = Menu(menu_bar, tearoff=0)
        menu_bar.add_cascade(label="Database options", menu=db_menu)
        db_menu.add_command(label="Manipulate documents")

        self.library.mainloop()

    
RootWindow()