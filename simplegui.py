import PySimpleGUI as sg
from cleaner import *
import os

layout = [[sg.Text('Target Root Path'), sg.Input(), sg.FolderBrowse()], [sg.Text('', key='dirs')], [sg.Button('Save'), sg.Button('Exit')]]

def setupaths(folder_to_track):
    extensions_folders = {
    #No name
    'noname' : folder_to_track+"/files-organizer/Other/Uncategorized",
    #Audio
    '.aif' : folder_to_track+"/files-organizer/Media/Audio",
    '.cda' : folder_to_track+"/files-organizer/Media/Audio",
    '.mid' : folder_to_track+"/files-organizer/Media/Audio",
    '.midi' : folder_to_track+"/files-organizer/Media/Audio",
    '.mp3' : folder_to_track+"/files-organizer/Media/Audio",
    '.mpa' : folder_to_track+"/files-organizer/Media/Audio",
    '.ogg' : folder_to_track+"/files-organizer/Media/Audio",
    '.wav' : folder_to_track+"/files-organizer/Media/Audio",
    '.wma' : folder_to_track+"/files-organizer/Media/Audio",
    '.wpl' : folder_to_track+"/files-organizer/Media/Audio",
    '.m3u' : folder_to_track+"/files-organizer/Media/Audio",
    #Text
    '.txt' : folder_to_track+"/files-organizer/Text/TextFiles",
    '.doc' : folder_to_track+"/files-organizer/Text/Microsoft/Word",
    '.docx' : folder_to_track+"/files-organizer/Text/Microsoft/Word",
    '.odt ' : folder_to_track+"/files-organizer/Text/TextFiles",
    '.pdf': folder_to_track+"/files-organizer/Text/PDF",
    '.rtf': folder_to_track+"/files-organizer/Text/TextFiles",
    '.tex': folder_to_track+"/files-organizer/Text/TextFiles",
    '.wks ': folder_to_track+"/files-organizer/Text/TextFiles",
    '.wps': folder_to_track+"/files-organizer/Text/TextFiles",
    '.wpd': folder_to_track+"/files-organizer/Text/TextFiles",
    #Video
    '.3g2': folder_to_track+"/files-organizer/Media/Video",
    '.3gp': folder_to_track+"/files-organizer/Media/Video",
    '.avi': folder_to_track+"/files-organizer/Media/Video",
    '.flv': folder_to_track+"/files-organizer/Media/Video",
    '.h264': folder_to_track+"/files-organizer/Media/Video",
    '.m4v': folder_to_track+"/files-organizer/Media/Video",
    '.mkv': folder_to_track+"/files-organizer/Media/Video",
    '.mov': folder_to_track+"/files-organizer/Media/Video",
    '.mp4': folder_to_track+"/files-organizer/Media/Video",
    '.mpg': folder_to_track+"/files-organizer/Media/Video",
    '.mpeg': folder_to_track+"/files-organizer/Media/Video",
    '.rm': folder_to_track+"/files-organizer/Media/Video",
    '.swf': folder_to_track+"/files-organizer/Media/Video",
    '.vob': folder_to_track+"/files-organizer/Media/Video",
    '.wmv': folder_to_track+"/files-organizer/Media/Video",
    #Images
    '.ai': folder_to_track+"/files-organizer/Media/Images",
    '.bmp': folder_to_track+"/files-organizer/Media/Images",
    '.gif': folder_to_track+"/files-organizer/Media/Images",
    '.ico': folder_to_track+"/files-organizer/Media/Images",
    '.jpg': folder_to_track+"/files-organizer/Media/Images",
    '.jpeg': folder_to_track+"/files-organizer/Media/Images",
    '.png': folder_to_track+"/files-organizer/Media/Images",
    '.ps': folder_to_track+"/files-organizer/Media/Images",
    '.psd': folder_to_track+"/files-organizer/Media/Images",
    '.svg': folder_to_track+"/files-organizer/Media/Images",
    '.tif': folder_to_track+"/files-organizer/Media/Images",
    '.tiff': folder_to_track+"/files-organizer/Media/Images",
    '.CR2': folder_to_track+"/files-organizer/Media/Images",
    #Internet
    '.asp': folder_to_track+"/files-organizer/Other/Internet",
    '.aspx': folder_to_track+"/files-organizer/Other/Internet",
    '.cer': folder_to_track+"/files-organizer/Other/Internet",
    '.cfm': folder_to_track+"/files-organizer/Other/Internet",
    '.cgi': folder_to_track+"/files-organizer/Other/Internet",
    '.pl': folder_to_track+"/files-organizer/Other/Internet",
    '.css': folder_to_track+"/files-organizer/Other/Internet",
    '.htm': folder_to_track+"/files-organizer/Other/Internet",
    '.js': folder_to_track+"/files-organizer/Other/Internet",
    '.jsp': folder_to_track+"/files-organizer/Other/Internet",
    '.part': folder_to_track+"/files-organizer/Other/Internet",
    '.php': folder_to_track+"/files-organizer/Other/Internet",
    '.rss': folder_to_track+"/files-organizer/Other/Internet",
    '.xhtml': folder_to_track+"/files-organizer/Other/Internet",
    #Compressed
    '.7z': folder_to_track+"/files-organizer/Other/Compressed",
    '.arj': folder_to_track+"/files-organizer/Other/Compressed",
    '.deb': folder_to_track+"/files-organizer/Other/Compressed",
    '.pkg': folder_to_track+"/files-organizer/Other/Compressed",
    '.rar': folder_to_track+"/files-organizer/Other/Compressed",
    '.rpm': folder_to_track+"/files-organizer/Other/Compressed",
    '.tar.gz': folder_to_track+"/files-organizer/Other/Compressed",
    '.z': folder_to_track+"/files-organizer/Other/Compressed",
    '.zip': folder_to_track+"/files-organizer/Other/Compressed",
    #Disc
    '.bin': folder_to_track+"/files-organizer/Other/Disc",
    '.dmg': folder_to_track+"/files-organizer/Other/Disc",
    '.iso': folder_to_track+"/files-organizer/Other/Disc",
    '.toast': folder_to_track+"/files-organizer/Other/Disc",
    '.vcd': folder_to_track+"/files-organizer/Other/Disc",
    #Data
    '.csv': folder_to_track+"/files-organizer/Programming/Database",
    '.dat': folder_to_track+"/files-organizer/Programming/Database",
    '.db': folder_to_track+"/files-organizer/Programming/Database",
    '.dbf': folder_to_track+"/files-organizer/Programming/Database",
    '.log': folder_to_track+"/files-organizer/Programming/Database",
    '.mdb': folder_to_track+"/files-organizer/Programming/Database",
    '.sav': folder_to_track+"/files-organizer/Programming/Database",
    '.sql': folder_to_track+"/files-organizer/Programming/Database",
    '.tar': folder_to_track+"/files-organizer/Programming/Database",
    '.xml': folder_to_track+"/files-organizer/Programming/Database",
    '.json': folder_to_track+"/files-organizer/Programming/Database",
    #Executables
    '.apk': folder_to_track+"/files-organizer/Other/Executables",
    '.bat': folder_to_track+"/files-organizer/Other/Executables",
    '.com': folder_to_track+"/files-organizer/Other/Executables",
    '.exe': folder_to_track+"/files-organizer/Other/Executables",
    '.gadget': folder_to_track+"/files-organizer/Other/Executables",
    '.jar': folder_to_track+"/files-organizer/Other/Executables",
    '.wsf': folder_to_track+"/files-organizer/Other/Executables",
    #Fonts
    '.fnt': folder_to_track+"/files-organizer/Other/Fonts",
    '.fon': folder_to_track+"/files-organizer/Other/Fonts",
    '.otf': folder_to_track+"/files-organizer/Other/Fonts",
    '.ttf': folder_to_track+"/files-organizer/Other/Fonts",
    #Presentations
    '.key': folder_to_track+"/files-organizer/Text/Presentations",
    '.odp': folder_to_track+"/files-organizer/Text/Presentations",
    '.pps': folder_to_track+"/files-organizer/Text/Presentations",
    '.ppt': folder_to_track+"/files-organizer/Text/Presentations",
    '.pptx': folder_to_track+"/files-organizer/Text/Presentations",
    #Programming
    '.c': folder_to_track+"/files-organizer/Programming/C&C++",
    '.class': folder_to_track+"/files-organizer/Programming/Java",
    '.dart': folder_to_track+"/files-organizer/Programming/Dart",
    '.py': folder_to_track+"/files-organizer/Programming/Python",
    '.sh': folder_to_track+"/files-organizer/Programming/Shell",
    '.swift': folder_to_track+"/files-organizer/Programming/Swift",
    '.html': folder_to_track+"/files-organizer/Programming/C&C++",
    '.h': folder_to_track+"/files-organizer/Programming/C&C++",
    #Spreadsheets
    '.ods' : folder_to_track+"/files-organizer/Text/Microsoft/Excel",
    '.xlr' : folder_to_track+"/files-organizer/Text/Microsoft/Excel",
    '.xls' : folder_to_track+"/files-organizer/Text/Microsoft/Excel",
    '.xlsx' : folder_to_track+"/files-organizer/Text/Microsoft/Excel",
    #System
    '.bak' : folder_to_track+"/files-organizer/Text/Other/System",
    '.cab' : folder_to_track+"/files-organizer/Text/Other/System",
    '.cfg' : folder_to_track+"/files-organizer/Text/Other/System",
    '.cpl' : folder_to_track+"/files-organizer/Text/Other/System",
    '.cur' : folder_to_track+"/files-organizer/Text/Other/System",
    '.dll' : folder_to_track+"/files-organizer/Text/Other/System",
    '.dmp' : folder_to_track+"/files-organizer/Text/Other/System",
    '.drv' : folder_to_track+"/files-organizer/Text/Other/System",
    '.icns' : folder_to_track+"/files-organizer/Text/Other/System",
    '.ico' : folder_to_track+"/files-organizer/Text/Other/System",
    '.ini' : folder_to_track+"/files-organizer/Text/Other/System",
    '.lnk' : folder_to_track+"/files-organizer/Text/Other/System",
    '.msi' : folder_to_track+"/files-organizer/Text/Other/System",
    '.sys' : folder_to_track+"/files-organizer/Text/Other/System",
    '.tmp' : folder_to_track+"/files-organizer/Text/Other/System",
    }

    return extensions_folders





def makealldirs(folder_to_track,extensions_folders):
    try:
        for key in extensions_folders:
            if os.path.isdir(extensions_folders[key]) is False:
                os.makedirs(extensions_folders[key])
        window.FindElement('dirs').Update("All The Directories have been created..")
    except:
        print("There is a problem occuring!!!!!!")
        

def dobackground(folder_to_track, extensions_folders):
    event_handler = MyHandler(folder_to_track, extensions_folders)
    observer = Observer()
    observer.schedule(event_handler, folder_to_track, recursive=True)
    observer.start()

    try:
        while True:           
            time.sleep(10)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()


if __name__ == "__main__":
    window = sg.Window('Files Organizer').Layout(layout)

    while True:
        event, values = window.read()
        if event in (None, 'Cancel'):
            break

    
        if event == 'Save':
            print(values[0])
            if values[0] is not None:
                folder_to_track = values[0]
                folder_destination = folder_to_track+'/files-organizer'
                extensions_folders = setupaths(folder_to_track)
                makealldirs(folder_to_track, extensions_folders)
                dobackground(folder_to_track,extensions_folders)


    window.close()
    