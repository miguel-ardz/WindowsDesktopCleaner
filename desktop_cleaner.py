"""
---------------------------------------------------------------------------------------------
os module
---------------------------------------------------------------------------------------------
is a built-in module that provides a way to interact with the operating 
system's underlying functionality. It allows you to perform various tasks related to file and 
directory operations, environment variables, and process management.
---------------------------------------------------------------------------------------------
 """
import os
"""
---------------------------------------------------------------------------------------------------
shutil module
---------------------------------------------------------------------------------------------------
(short for "shell utilities") module in Python 
is another built-in module that provides a higher-level interface for file and directory operations. 
It builds upon the functionality provided by the os module and offers more convenient and intuitive 
ways to work with files and directories. The shutil module is especially useful when you need to perform 
tasks like file copying, moving, archiving, and more.
---------------------------------------------------------------------------------------------------
 """
import shutil
"""
---------------------------------------------------------------------------------------------------
pythoncom module
---------------------------------------------------------------------------------------------------
The pythoncom module in Python is part of the pywin32 library, which provides access to many 
Windows-specific functionalities through COM (Component Object Model) interfaces. It allows Python 
programs to interact with COM objects, which are binary interfaces used in Windows for interprocess 
communication and software components.
---------------------------------------------------------------------------------------------------
 """
import pythoncom

from win32com.shell import shell, shellcon


def get_desktop_path():
    desktop_pidl = shell.SHGetFolderLocation(0, shellcon.CSIDL_DESKTOP, 0, 0)
    desktop_path = shell.SHGetPathFromIDList(desktop_pidl)
    return desktop_path

def clean_desktop():
    desktop_path = get_desktop_path()
    files = os.listdir(desktop_path) #  Returns a list of filenames in the given directory.

    for file in files:
        if os.path.isfile(os.path.join(desktop_path, file)): # This line checks if the current file (the one being iterated) is a regular file (not a directory)

            """
            The os.path.splitext() function returns a tuple with two elements: the filename without the extension and the extension itself (including the dot). 
            We are interested in the extension, so we use [1] to get the second element of the tuple, which is the extension:
            """
            file_extension = os.path.splitext(file)[1].lower()

            """ 
            In this next bit I am making the file_extension into a string, bc from my understanding it is
            dealing with bytes, not strings. So changing the variable to a string and checking if it is
            a ini file or a Windows Links File and if it is, to not do anything. Because I dont want those
            in folders.
             """
            temp = str(file_extension)
            if file_extension in (".ini", "b'.lnk'"):
                continue

            target_folder = os.path.join(desktop_path, file_extension[1:])

            # Create the target folder if it doesn't exist
            if not os.path.exists(target_folder):
                os.makedirs(target_folder)

            # Move the file to the target folder
            """
            After ensuring that the target_folder exists, this line moves the current file 
            from the desktop_path to the target_folder using shutil.move() function.
            """
            shutil.move(os.path.join(desktop_path, file), os.path.join(target_folder, file))

if __name__ == "__main__":
    clean_desktop()


""" 
Created by Miguel Rodriguez on (7.22.2023) ༼ つ ◕_◕ ༽つ
 """
