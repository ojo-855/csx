"""
Here we will show a couple of examples of functions that use loops and conditionals
"""

unsorted_num_list = [3456, 43659, 123, 9029, 750, 5, 100000]

# theres a million ways to get it- choose one

# music lyrics aside, theres so many ways to solve the same problem in coding
# we will start off real complex, then break it down to a built in function

def sort_a_list(data_list):
    new_list = []

    while data_list:
        minimum = data_list[0]  # arbitrary number in list
        for x in data_list: 
            if x < minimum:
                minimum = x
        new_list.append(minimum)
        data_list.remove(minimum)

    print(new_list)

sort_a_list(unsorted_num_list)

##################################################################################################

# this function does the same thing as the function above
# an important lesson about becoming a programmer is that you need to understand
# underlying concepts. There will always be a tool for you to automatically accomplish
# a task, but what will make you a better programmer is knowing how those tools work
print(sorted(unsorted_num_list))

# lets try a for loop within a for loop

adjective = ["red", "big", "tasty"]
fruits = ["cherry", "coconut", "mango"]

for word in adjective:
    for fruit in fruits:
        print(word, fruit)

##################################################################################################

# below you will see your first sorting algorithm. there are many varieties of sorting algorithms
num_list_unsorted = [8,2,1,3,5,4]

def insertion_sort(num_list):
    """the sorting algorithm starts with the first item in a list and sorts it accordingly onward"""
    # for every element in our array
    for index in range(1, len(num_list)):
        current = num_list[index]
        position = index

        while position > 0 and num_list[position-1] > current:
            print("Swapped {} for {}".format(num_list[position], num_list[position-1]))
            num_list[position] = num_list[position-1]
            print(num_list)
            position -= 1

        num_list[position] = current

    return num_list

print(insertion_sort(num_list_unsorted))

##################################################################################################

# below we want to iterate through a list of lists using a nested for loop,
# or in simpler terms a for loop within a for loop. this is very common
# in data structures and you will master this in no time!

my_movies = [
    ['How I Met Your Mother', 'Friends', 'Silicon Valley'],
    ['Family Guy', 'South Park', 'Rick and Morty'],
    ['Breaking Bad', 'Game of Thrones', 'The Wire']
]

for sublist in my_movies:
    for movie_name in sublist:
        char_num = len(movie_name)
        print("The title " + movie_name + " is " + str(char_num) + " characters long.")
        