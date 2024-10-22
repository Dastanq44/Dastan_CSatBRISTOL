
#_____________________________________--- QUESTION 2

MY_LIST = [3, 7, 2, 9, 4, 1, 8]

#Adding 5 at the end
MY_LIST.append(5)

#Removing all vars with value 9
for a in range(len(MY_LIST)-1):
    if MY_LIST[a] == 9:
        MY_LIST.pop(a)

#Sorting the list (METHOD FOR WEAK MINDS)
#MY_LIST.sort()
#print(MY_LIST)
#Sorting the list (Sigma method)
temp = 0
count = 0
for c in range(0, len(MY_LIST)-1):
    for i in range((c+1), len(MY_LIST)):
        if MY_LIST[c] > MY_LIST[i]:
            temp = MY_LIST[c]
            MY_LIST[c] = MY_LIST[i]
            MY_LIST[i] = temp
print(MY_LIST)

#Reversing the list
#MY_LIST.reverse()
#print(MY_LIST)
REVERSED_LIST = []
for a in range(len(MY_LIST)-1, -1, -1):
    REVERSED_LIST.append((MY_LIST[a]))
print(REVERSED_LIST)

#Inserting 6 at index 2
MY_LIST.insert(2, 6)
print(MY_LIST)

#Printing the index of 4 in list
for e in range(0, len(MY_LIST)-1):
    if MY_LIST[e] == 4:
        print(e)
        break

#_____________________________________--- QUESTION 3

my_tuple = (15, "Python", 3.14, True, 42, False)

#Printing the index of string PYTHON
for i in range(0, len(my_tuple)-1):
    if str(my_tuple[i]) == "Python":
        print(i)
        break

#Counting the TRUE's in tuple
COUNT_TRUES = 0
for i in range(0, len(my_tuple)-1):
    if my_tuple[i] == True:
        COUNT_TRUES = COUNT_TRUES + 1
print(COUNT_TRUES)

#Print indexes 1 to 4
for i in range(1, 5):
    print(my_tuple[i])

#_____________________________________--- QUESTION 4

#Creating a dictionary and then adding a new item inside
STUDENT_MARKS = {"Bob":12, "Steven":10, "Arnur":59, "Baurzhan":2, "Zhandaulet":65, "Isatayus":90, "Daniq":69, "Arthur":4}
STUDENT_MARKS["Askar"] = 100

#Printing all names and marks
for i in STUDENT_MARKS:
    print(i, STUDENT_MARKS[i])
#I dont use this type of for loop commonly but I guess it is very useful in Python dictionaries