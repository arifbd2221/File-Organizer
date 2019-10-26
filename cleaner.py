from watchdog.observers import Observer
import time
from watchdog.events import FileSystemEventHandler
import os 
import json
import shutil
from datetime import datetime
from time import gmtime, strftime



class MyHandler(FileSystemEventHandler):

    def __init__(self, folder_to_track, extensions_folders):
        self.folder_to_track = folder_to_track
        self.extensions_folders = extensions_folders

    def on_modified(self, event):
        for filename in os.listdir(self.folder_to_track):
            print(filename)
            i = 1
            if filename != 'files-organizer':
                print(filename)
                new_name = filename
                extension = 'noname'
                try:
                    extension = str(os.path.splitext(self.folder_to_track + '/' + filename)[1])
                    path = self.extensions_folders[extension]
                except Exception:
                    extension = 'noname'

                now = datetime.now()
                year = now.strftime("%Y")
                month = now.strftime("%m")

                folder_destination_path = self.extensions_folders[extension]
                    
                year_exists = False
                month_exists = False
                for folder_name in os.listdir(self.extensions_folders[extension]):
                    if folder_name == year:
                        folder_destination_path = self.extensions_folders[extension] + "/" +year
                        year_exists = True
                        for folder_month in os.listdir(folder_destination_path):
                            if month == folder_month:
                                folder_destination_path = self.extensions_folders[extension] + "/" + year + "/" + month
                                month_exists = True
                if not year_exists:
                        os.mkdir(self.extensions_folders[extension] + "/" + year)
                        folder_destination_path = self.extensions_folders[extension] + "/" + year
                if not month_exists:
                        os.mkdir(folder_destination_path + "/" + month)
                        folder_destination_path = folder_destination_path + "/" + month


                file_exists = os.path.isfile(folder_destination_path + "/" + new_name)
                while file_exists:
                    i += 1
                    new_name = os.path.splitext(self.folder_to_track + '/' + filename)[0] + str(i) + os.path.splitext(self.folder_to_track + '/' + filename)[1]
                    new_name = new_name.split("/")[4]
                    file_exists = os.path.isfile(folder_destination_path + "/" + new_name)
                src = self.folder_to_track + "/" + filename

                new_name = folder_destination_path + "/" + new_name
                os.rename(src, new_name)




