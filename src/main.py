'''
Created on Apr 21, 2017

@author: tyler
'''

from excelHandler import excelHandler
if __name__ == '__main__':
    excel = excelHandler('C:\Users\\tyler\OneDrive\Church\YC 2017\YouthConferenceRegistrantReference.xlsx')
    workbook = excel.openExcelFile()