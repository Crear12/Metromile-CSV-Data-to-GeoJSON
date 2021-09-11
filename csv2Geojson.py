#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep  9 15:00:59 2021

@author: Crear
"""
import csv
import numpy as np

from geojson import LineString


def ReadCSV(csvfile_path):
    csvFile = open(csvfile_path, "r")
    readeritem = []
    csvRaw = csv.reader(csvFile)
    readeritem .extend([row for row in csvRaw])
    return np.array(readeritem)

def folder(folder_path):
    import os
    if folder_path.find('/')<0:
        Folders = folder_path.split('\\')
        RF = True
        for folderr in Folders:
            if RF == True:
                FoldPath = folderr
                RF = False
            else:
                FoldPath+='/'
                FoldPath+=folderr
    else:
        FoldPath = folder_path
    folder = os.listdir(FoldPath)
    folder.sort(key = str.lower)
    folder = [FoldPath + '/' + f for f in folder if not f.startswith(('.'))]
    return folder


if __name__ == '__main__':
    csvFolderPath = "200418500 all_driving_data"
    Canvas = []
    Init = """{
    "type": "FeatureCollection",
    "features": [
      {
        "type": "Feature",
        "properties": {
        "name": "Driving Record",
        "type": "Driving"},
        "geometry": {
        "type": "LineString",
        "coordinates": """
    End = """
                
            }
        }
    ]
}
    """

    f= open("DrivingRecord.txt","w+")
    f.write(Init)
    # count=0
    for csvFile in folder(csvFolderPath):
        timelatlons = ReadCSV(csvFile)[1:,2:6]
        for timelatlon in timelatlons:
            if len(timelatlon[2])>0:
                Canvas.append([float(timelatlon[3]),float(timelatlon[2])])
                # count+=1
        #     if count>1000:
        #         break
        # if count>1000:
        #     break
    f.write(str(Canvas))
    f.write(End)
    f.close()