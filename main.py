from datetime import datetime
from os import listdir
from datetime import datetime
import piexif
import os
from os.path import isfile, join
from pathlib import Path

jpgFolder = "/Users/eamonbarkhordarian/Downloads/modeling_photos_for_agency copy/completed_names"

if __name__ == '__main__':
    ## count number of photos found
    listOfFolders = [x[0] for x in os.walk(jpgFolder)]
    listOfFolders.pop(0)
    count = 0
    for folderPath in listOfFolders:
        folderName = os.path.basename(folderPath)
        filesInFolder = [f for f in listdir(folderPath) if isfile(join(folderPath, f))]
        count = 0
        for file in filesInFolder:
            print("folder path: " + folderPath)
            print("folder name: " + folderName)
            print("file name: " + file)
            filepath = os.path.join(folderPath, file)
            print("file path: " + filepath)

            oldext = os.path.splitext(file)[1]
            newFileName = folderName + "__" + str(count) + oldext
            os.rename(filepath, os.path.join(folderPath, newFileName))
            count = count + 1


    # print count
    # fileCount = len(listOfFiles)
    # print fileCount

    # ## create datetimeString from JPG filename
    # for jpg in os.listdir(jpgFolder):
    #     filepath = jpgFolder + "\\" + jpg
    #
    #     parsedate = datetime.strptime(jpg[0:16], "%Y-%m-%d-%H-%M-%S")
    #     ## change exif datetimestamp for "Date Taken"
    #     exif_dict = piexif.load(filepath)
    #     newExifDate = parsedate.strftime("%Y:%m:%d %H:%M:%S")
    #     exif_dict['Exif'][piexif.ExifIFD.DateTimeOriginal] = newExifDate
    #     exif_dict['Exif'][piexif.ExifIFD.DateTimeDigitized] = newExifDate
    #     exif_bytes = piexif.dump(exif_dict)
    #     piexif.insert(exif_bytes, filepath)
    # # Press the green button in the gutter to run the script.
