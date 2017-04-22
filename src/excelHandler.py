'''
Created on Apr 21, 2017

@author: tyler
'''

import openpyxl

class excelHandler:

    def __init__(self, path_to_excel):
        self.path_to_excel = path_to_excel
    
    def openExcelFile(self):
        self.workbook = openpyxl.load_workbook(filename = self.path_to_excel)        
        print(type(self.workbook))
        #TODO - how to close the workbook?
    