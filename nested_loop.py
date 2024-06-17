# nested loop = the inner loop will finish all of its iteration before finishing one iteration of the out

# py_rows = int(input("Please enter rows: "))
# py_cols = int(input("Please enter columns: "))
# py_sym = input("Please enter symbols: ")

# for row in range(0,py_rows):
#     for col in range(0,py_cols - row):
#     # for col in range(0,py_cols):
#         print(" ",end="")
#     for k in range(0,row+1):
#     # for k in range(0,row):
#         print(py_sym, end=" ")
#     print(" ")

import time
py_row = int(input("Please enter your desire rows:")) 
py_col = int(input("Please enter your desire columns:")) 
py_sym = input("Please enter your desire symbols:")

for i in range(0,py_row):
    for j in range(0,py_col-i-1):
        print(" ",end="")
    for k in range(0,i+1):
        print(py_sym, end=" ")
    print("")
    time.sleep(1)