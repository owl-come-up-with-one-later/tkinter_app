from tkinter import *
from tkinter import ttk
from tkinter import filedialog

import re

class Tkinter_App:

    def __init__(self, master):
        # Outline
        """

        """
        #### Start - 
        #### End - 
        pass
    
        #### Start - Notebook, 'nbTool_kit'
        self.nbTool_kit = ttk.Notebook(master)
        self.nbTool_kit.grid(row=0,column=0)
        #### End - Notebook, 'nbTool_kit'

        #### Start - Frame, 'frFileSelect'
        self.frFileSelect = ttk.Frame(self.nbTool_kit)
        self.nbTool_kit.add(self.frFileSelect, text = "File selector")

        #TODO Label, lblFilePath
        self.lblFilePath = ttk.Label(self.frFileSelect, text="File path:").grid(row=0,column=0)
        #TODO Entry, enFilePath
        self.enFilePath = ttk.Entry(self.frFileSelect, text="").grid(row=0,column=1, columnspan=2)
        #TODO Button, btnBrowse
        self.btnBrowse = ttk.Button(self.frFileSelect, text="Browse")
        def browse_for_file():
            # Get file name
            self.input_file_name = filedialog.askopenfilename(initialdir = "/",title = "Select a text file",filetypes = (("text files","*.txt"),("all files","*.*")))
            #TODO Update [Entry] with file path
            print(str(self.input_file_name))
            print(self.enFilePath.Get())

        self.btnBrowse.config(command = browse_for_file)
        self.btnBrowse.grid(row=2,column=0)
        #TODO Button, btnClear
        self.btnClear = ttk.Button(self.frFileSelect, text="Clear").grid(row=2,column=1)
        #TODO Label, lblOutput
        self.lblOutput = ttk.Label(self.frFileSelect, text="Output:").grid(row=4,column=0)
        #TODO Text, txtOutput
        self.txtOutput = Text(self.frFileSelect, width = 40, height = 10)
        self.txtOutput.config(
            background = 'light gray',
            wrap = 'word', # 'word'|'char'|'none'
            state='disabled', # 'normal'|'disabled'
            relief = SUNKEN,
            )
        self.txtOutput.grid(row=4,column=1)
        #TODO Button, btnCopyText
        self.btnCopyText = ttk.Button(self.frFileSelect, text="Copy text").grid(row=6,column=0)
        #### End - Frame, 'frFileSelect'

        #### Start - Frame, 'frEdit'
        self.frEdit = ttk.Frame(self.nbTool_kit)
        self.nbTool_kit.add(self.frEdit, text = "Edit")
        #### End - Frame, 'frEdit'

        #### Start - Frame, 'frExtract'
        self.frExtract = ttk.Frame(self.nbTool_kit)
        self.nbTool_kit.add(self.frExtract, text = "Extract")
        #### End - Frame, 'frExtract'

        #### Start - Frame, 'frDelimited'
        self.frDelimited = ttk.Frame(self.nbTool_kit)
        self.nbTool_kit.add(self.frDelimited, text = "Delimited")
        #### End - Frame, 'frDelimited'
        

def main():
    
    root = Tk()
    tkinter_app = Tkinter_App(root)
    root.mainloop()

if __name__ == "__main__":
    main()
