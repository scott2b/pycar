# import modules
import csv

# write your function passing in the file name
def open_csv_file(file_name):

    # create a variable to iterate each row and count the number of lines
    number_of_rows = sum(1 for line in open(file_name))

    # output the number of lines
    print number_of_rows

# run the function when you run the script in the terminal
open_csv_file('fdic_failed_bank_list.csv')