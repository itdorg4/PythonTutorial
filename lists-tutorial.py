# data = "Good Morning!"

# Ordered collection of 
# Zero / Multiple items with same / different data types
# It can have duplicates
# Mutable = Modifiable


# data = []

# data = [1, 5, 7]

# data = ["India", "US", "AUS"]

# data = [True, False]

# data = [[1, 2, 5], [4, 5, 8]]


# data = [1, 5, 7, "India", "US", "AUS", True, False, [4, 5, 8], None]


# data = [1, 5, 5]
# print(countries[-3:-5])
# print(countries[:])
# print(countries[:-2])
# print(countries[::-1])

# print(countries[-1])

# print(type(countries[-1]))

# print(type(countries))


# countries = ["IND", "USA", "AUS", "SL", "JPN", "UAE", True, 100]



# print(countries[-3][0]) #acccessing / reading

# print(countries)

# twos_table = [[2, 1, 2], 
#               [2, 2, 4], 
#               [2, 3, 6], 
#               [2, 4, 8], 
#               [2, 5, 10]]



# print(twos_table[4][2])

# countries = ["IND", "SL"]

# print("before", countries)
# print(id(countries))

# countries[0] = "BHU"

# print("after", countries)
# print(id(countries))

# south_states = ['KA', "KE", "TE", 'AP', "TN"]
# north_states = ['AS', 'BI', 'CH', 'DL', 'GU']


# states = [south_states, north_states]

# print(states)
# print(south_states)
# print(north_states)
# print("south_states", id(south_states))
# print("north_states", id(north_states))
# print("states[1]", id(states[1]))
# print("states", id(states))


# states[1] = ['MH', 'MP', 'MG']



# print(states)
# print(south_states)
# print(north_states)
# print("south_states", id(south_states))
# print("north_states", id(north_states))
# print("states[1]", id(states[1]))
# print("states", id(states))




# print(id(data1), data1)

# print(id(data2), data2)

# print("*" * 20)

# data2 = ['C', 'D']

# print(id(data1), data1)

# print(id(data2), data2)


# data1 = 100
# data2 = data1
# master_data = [data1, data2]

# print("master_data's address ", id(master_data))
# print("master_data's 0th el address ", id(master_data[0]))
# print("master_data's 1st el address ", id(master_data[1]))
# print("data1 address ", id(data1))
# print("data2 address ", id(data2))
# print(master_data)

# master_data[1] = 200

# print("\n"*3,"*" * 10 , "After Change", "*" * 10)
# print("master_data's address ", id(master_data))
# print("master_data's 0th el address ", id(master_data[0]))
# print("master_data's 1st el address ", id(master_data[1]))
# print("data1 address ", id(data1))
# print("data2 address ", id(data2))


# print(master_data)
# print(data1)
# print(data2)


# south_states = ['KA', "KE", "TE", 'AP']

# south_states[3:] = ['AP', 'TN', '']
# # south_states[0] = [ 'TN', 'MP', 'MH']
# # south_states[0:0] = [ 'TN', 'MP', 'MH']

# print(south_states)


# states = ['KA', "KE", "TE", 'AP']

# states = states + [ 'TN', 'MP', 'MH']


# print(states)


# append, extend, copy, count, index, 
# insert, pop, remove, reverse, sort


# states_1 = ['KA', "KE", "TE", 'AP']
# states_2 = states_1



# # states_1 = states_1 + [ 'TN', 'MP', 'MH']

# states_1.extend(['TN'])

# print(states_1)
# print(states_2)


# even_numbers = [2, 4, 6, 8, 10]

# # Add
# # even_numbers.append(12) # to add an element at the end of the input
# # even_numbers.extend([14, 16, 18, 20]) # to add / join new list into an existing list
# # even_numbers.insert(2, 100) # to insert an element into a particular position 



# print(id(even_numbers))


# # Remove
# # even_numbers.pop()


# even_numbers.remove(6)

# print(even_numbers)


# states = ['KA', "KE", "TE", 'AP']


# # states.remove("TE")

# # states.pop(0)

# del states[0]

# print(states)


# Copy

# states_1 = ['KA', "KE", "TE", 'AP']

# states_2 = states_1.copy()


# print(id(states_1))
# print(id(states_2))


# states_1.append('MH')



# print("states_1 ==>", states_1)
# print("states_2 ==>", states_2)


# states_1 = ['KA', "KE", "TE", 'AP']

# # states_1.reverse()

# states_1.sort(reverse=True)

# print(states_1)




# states_1 = ['KA', "KE", "TE", 'AP']
# states_2 = states_1

# print(states_1, id(states_1))
# print(states_2, id(states_2))


# # states_1.clear()


# # states_1.append('GU')

# del states_1

# # print(states_1, id(states_1))
# # print(states_2, id(states_2))


# print(states_1)

# # split
# # list()

# # list to string

states_1 = ['KA', "KE", "TE", 'AP','KA','KA','KA','KA']


# out = "".join(states_1)


# print(out)

print(states_1.pop())

