file = open("fil.txt", "w")
curr_long = 10
curr_lat = 20
temp = str(curr_long) + "\n" + str(curr_lat) + "\n"


file.writelines(temp)
file.close()

file = open("fil.txt", "r")
print(file.readline().strip())
print(file.readline().strip())

