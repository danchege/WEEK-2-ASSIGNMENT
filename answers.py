# Question 1: Created an empty list
my_list = []

# Question 2: Appended elements to the list
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)

# Question 3: Inserted 15 at the second position (index 1)
my_list.insert(1, 15)

#Question 4: Extended the list with another list [50, 60, 70]
my_list.extend([50, 60, 70])

# Question 5: Removed the last element from the list
my_list.pop()

# Question 6: Sorted the list in ascending order
my_list.sort()

# Question 7: Find and print the index of the value 30
index_of_30 = my_list.index(30)
print("Index of 30:", index_of_30)

# The final list to verify the result
print("Final list:", my_list)
