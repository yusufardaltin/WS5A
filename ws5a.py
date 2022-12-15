"""
    Stage: Development-01
    @author: Deniz Günenç, 120200078
    @author: Bukre Yagmur Turkoglu, 119200054

    Stage: Development-02
    @author: Yusuf Arda Altin, 119202054
    @author: Wafaa Al Bacha, 121202106

"""

import tkinter as tk


class LoginWindow:
    # constructor
    def __init__(self):
        self.window = tk.Tk()

        self._initializeGUI()
        self._addGUIElementsToFrame()

        # start the GUI frame
        self.window.mainloop()


    """
        Initialize GUI elements. If it is necessary, you can add
        more elements.
        ! PLEASE RENAME THE OBJECTS ACCORDING TO THEIR PURPOSES !
        ! YOU CAN ADD MORE ELEMENTS IF IT IS NECESSARY !
    """
    def _initializeGUI(self):
        # set title of the window
        self.window.title("Login Window")

        # welcom message
        self.welcomelabel = tk.Label(text="Welcome to our supermarket!")

        # username and password labels
        self.lbl01 = tk.Label(text="Username:")
        self.lbl02 = tk.Label(text="Password:")

        # username and password text fields
        self.txt01 = tk.Entry()
        self.txt02 = tk.Entry()

        # login and exit buttons
        self.loginbtn = tk.Button(text="Login")
        self.exitbtn = tk.Button(text="Exit")

        # add action listeners to the buttons
        self.loginbtn.bind("<Button-1>", self.handle_click)
        self.exitbtn.bind("<Button-1>", self.handle_click)


    """
        Add GUI elements to the layout of the frame. If it is necessary,
        you can add more elements.
    """
    def _addGUIElementsToFrame(self):
        # add elements to the frame
        self.welcomelabel.grid(row=0, column=0, padx=10, pady=5, columnspan=2)

        self.lbl01.grid(row=1, column=0, padx=10, pady=5)
        self.txt01.grid(row=1, column=1, padx=10, pady=5)

        self.lbl02.grid(row=2, column=0, padx=10, pady=5)
        self.txt02.grid(row=2, column=1, padx=10, pady=5)

        self.loginbtn.grid(row=3, column=0, padx=10, pady=5)
        self.exitbtn.grid(row=3, column=1, padx=10, pady=5)


    """
        Action listener for the buttons. If "event.widget" is from
        one of the buttons, apply the related operation.
        :param event: action event for detecting which button is clicked
    """
    def handle_click(self, event):
        # check which button is clicked
        if event.widget == self.loginbtn:
            # call login method
            self.login()
        elif event.widget == self.exitbtn:
            # call exit method
            self.exit()
        
    # login function for checking the username and password
    def login(self):
        # check if the username and password are admin
        if self.txt01.get() == "admin" and self.txt02.get() == "admin":
            # create a new window for success message
            top = tk.Toplevel()
            top.geometry("350x200")
            top.title("FOODS AND BEVERAGES")
            top.frame = tk.Toplevel(text="Username")
            top.frame = "Username"
            top.mainloop()

        
    # exit function for quitting the application
    def exit(self):
        self.window.destroy()        


    




# main method for testing the application
if __name__ == "__main__":
    LoginWindow()