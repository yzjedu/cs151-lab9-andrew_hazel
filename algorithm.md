# Algorithm Document
#### PLEASE! PLEASE! PLEASE! THINK before you code...

# Tasks:
Accepting file name

Reading file to list

Format and Display Seats

# Algorithm for accept_file_name
**Purpose:** Check the file name is a valid input

**Name:** accept_file_name

**Parameters:** None

**Return:** file_name

**Algorithm:**
1. Prompt the user to enter a file name
2. While input is not valid
   1. Prompt user to re-enter a valid file name
3. Return file name

# Algorithm for read_file_name
**Purpose:** Convert file data into a list

**Name:** read_file_name

**Parameters:** file_name

**Return:** data

**Algorithm:**
1. Set data as an empty list
2. Prompt user to enter file name
3. With open file_name to read as input file
   1. Set data to the read input file
   2. Return data
4. Output error message and return data


# Algorithm for format_seats
**Purpose:** Output seating chart

**Name:** format_seats

**Parameters:** names_list

**Return:** table

**Algorithm:**
1. Set index = 0
1. Set table and seat to 1
2. for name in names_list
   1. Output '~' * 20
   2. Output "Table" and table variable, "Seat" and seat variable, Output index of the names_list
   3. Output '~' * 20
   4. Increment index
   5. Increment seat
   6. if seat = 5
      1. Increment table
      2. Set seat to 1
4. Output table

# Algorithm for main
**Purpose:** Welcome user and run functions

**Name:** main

**Parameters:** None

**Return:** None

**Algorithm**
1. Print a decorative line and a message indicating the purpose of the program.
1. Call accept_file_name
2. Call read_file_name
3. Call format_seats
4. Print a decorative line and a closing message thanking the user for using the program.