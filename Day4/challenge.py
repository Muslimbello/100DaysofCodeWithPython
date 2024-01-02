import random

x_position = input("Enter the column position then the vertical\n")
row1 = ["⬜️", "⬜️", "⬜️"]
row2 = ["⬜️", "⬜️", "⬜️"]
row3 = ["⬜️", "⬜️", "⬜️"]

column_position = int(x_position[0])
vertical_position = int(x_position[1])
map = [row1, row2, row3]
map[column_position][vertical_position] = "x"
print(f"{row1}\n {row2}\n {row3}\n")
