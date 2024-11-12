# Programmers: Andrew Leimbach & Hazel Osborne
# Course:  CS151, Zelalem Yalew
# Due Date: 11/13/24
# Lab Assignment:  Lab 09
# Problem Statement: Read in all the attendees and then output the seat assignment.
# Data In: File Name
# Data Out:  Seating Chart and Total number of tables
# Credit: Class Notes 23 CS151
# Input Files: isaacman.txt, nweke.txt, yalew.txt, they all have lists of student names


import os

# Purpose: Check the file name is a valid input
# Parameters: none
# Return: file_name
def accept_file_name():

    #Prompt user to input file name
    name = input("Please enter the file you would like to use: ")

    #Ensure file name exists
    while not os.path.isfile(name):
        name = input("File does not exist. Please enter again: ")
    return name

# Purpose: Covert file data into a list
# Parameters: file_name
# Return: file_name
def read_file_name(file_name):
    data = []

    #Take names from the file and put into list 'data'
    with open(file_name, 'r') as input_file:
        data = input_file.readlines()
        return data

    #Error Message if names are unable to be converted
    print("Error converting data from file. Please try again.")
    return data

# Purpose: Output Seating Chart
# Parameters: names_list
# Return: none
def format_seats(names_list):

    #Initialize counting variables
    index = 0
    table = 1
    seat = 1

    for name in names_list:

        #Outputing seating chart
        print('~' * 25)
        print(f'Table {table}, Seat {seat}, {names_list[index]}', '~' * 25, sep = '')
        index += 1
        seat += 1
        if seat > 5:
            table += 1
            seat = 1

    #Outputing number of tables needed.
    print("You need", (table-1), "tables.")

# Purpose: Welcome user and run functions
# Parameters: none
# Return: none
def main():

    #Output opening message
    print("\nWelcome! This program is designed to read all the attendees in a file of your choice \n"
          "and then output seating assignments!")
    print('-'*85)

    #Running functions
    file_name = accept_file_name()
    names_list = read_file_name(file_name)
    format_seats(names_list)

    #Output closing messages
    print('-'*85)
    print("Thank you for using this program!")

#Run main
main()