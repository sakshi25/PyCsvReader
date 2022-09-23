import pandas as pd
import csv
from csv import DictReader
import dbInsert as db

import os
#C:\Users\saabhatn\Documents\EmployeeDetails.csv

class csvReader:

    def __init__(self):
        '''   '''
        self.list_of_dict = None

    def openCsv(self,filePath):
        ''' Function to Open csv file and return data'''
        with open(filePath, 'r') as f:
            dict_reader = DictReader(f)
            self.list_of_dict = list(dict_reader)

    def validateData(self):
        return True

if __name__ == '__main__':
    print("-----Csv Reader Main Function started-------")
    #filePath = input("Enter the path of csv file: ")
    filePath  = 'C:\\Users\\saabhatn\\AppData\\Local\\Temp\\EmployeeDetails.csv'
    #list_of_dict = []
    if os.path.exists(filePath):
        mycsvReader = csvReader()
        mycsvReader.openCsv(filePath)
        if mycsvReader.validateData():
            dbConn = db.PostgreSQlWrapper()
            dbConn.createConnection()
            dbConn.copyTabletoDB(mycsvReader.list_of_dict)
            dbConn.closeConnetion()
        else:
            print("CSV Validation failed")

    else:
        print("Incorrect location :  " + str(filePath))
