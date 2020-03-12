# importing required modules 
import PyPDF2
import os
import glob, os


"""
Sudo Code:

Get all the files in the folder
Go through each file and get the date
Add the date to the beginning of the FN ie: 1-4-19_Thank you for your payment.pdf
Rename the file and move to the next

"""
def main():
          list_of_files = list_files()
          for file_n in list_of_files:
                    pdfFileObj = open("receipts/" + file_n, 'rb') 
                    pdfReader = PyPDF2.PdfFileReader(pdfFileObj) 
                    pageObj = pdfReader.getPage(0) 
                    extracted_text = pageObj.extractText()
                    extracted_date = extract_date(extracted_text)
                    date = convert_date(extracted_date)
                    #rename(date, file_n)
                    pdfFileObj.close()



def extract_date(s):
          starting_index = s.find("Date") + 6 #"Date :" = 6 spaces
          ending_index = s.find(" at ")
          date = s[starting_index:ending_index]
          return date

def convert_date(date_str):
          month_int = convert_month(date_str)
          month_str = extract_month_string(date_str)
          day = extract_day(date_str, month_str)
          year = extract_year(date_str)
          return str(month_int)+ "-" + day + "-" + year

def convert_month(s):
          months = ["January", "February", "March", "April", "May", "June", "July", "August","September","October","November","December"]
          month_number = 0
          for x in months:
                    month_number+=1
                    if s.find(x) != -1:
                              return month_number

def extract_month_string(s):
          months = ["January", "February", "March", "April", "May", "June", "July", "August","September","October","November","December"]
          month_number = 0
          for x in months:
                    if s.find(x) != -1:
                              return x
def extract_day(s, month):
          month_length = len(month)
          day_index = month_length + 1
          if s[day_index+1] != ",":
                    end_day_index = day_index + 2
          else:
                    end_day_index = day_index + 1
          return s[day_index:end_day_index]
def extract_year(s):
          end_of_string = len(s)
          year = s[end_of_string-4:end_of_string]
          return year

def rename(date, file_name):
          new_file_name = date + "_" + file_name
          os.rename("receipts/" + file_name, "receipts/" + new_file_name)

def list_files():
          file_array = []
          for file_n in glob.glob("receipts/*.pdf"):
              file_array.append(file_n[9:])
          return file_array

main()

