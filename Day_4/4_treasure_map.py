row1 = ["O", "O", "O"]
row2 = ["O", "O", "O"]
row3 = ["O", "O", "O"]

map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")

select_row_column = input("Select row and column number: ")

row_number = int(select_row_column[0])
column_number = int(select_row_column[1])

map[row_number-1][column_number-1] = "X"

print(f"{row1}\n{row2}\n{row3}")
