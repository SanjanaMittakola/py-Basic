#Write a function that checks if a row in Sudoku (list of 9 digits) has all values from 1–9 exactly once. input and output
def sudoku(lst):
    for i in range(len(lst)):
       lst[i] = int(lst[i])
       
    if len(lst) != 9 :
        print("Row must contain exactly 9 digits")
        return

        for i in range (9):
            if lst[i] < 1 or lst[i] > 9:  
                print("Numbers must be between 1 and 9.")
                return

    for i in range (9):
        for j in range(i+1,9):
            if(lst[i]==lst[j]):
                print("Duplicate found : ",lst[i])
                return 

    print("Valid Sudoku row. All numbers from 1 to 9 are present exactly once.")

lst = input("Enter list elements separated by space: ").split()
print("Your list:", lst)
sudoku(lst) 
