def insertion_sort(the_list):
    number_of_elements = len(the_list)

    for i in range(1, number_of_elements, 1):
        for j in range(i, 0, -1):
            if the_list[j] < the_list[j - 1]:
                temp = the_list[j]
                the_list[j] = the_list[j - 1]
                the_list[j - 1] = temp

    print(the_list)


insertion_sort([5, -3, 1, 2, 3, 4, 9, 8, 8, 6, 9, 7, 8, 8, -9])


# invariants
"""

the property that remains unchanged at any point throughout the algorithm
01.  after every traversal, the list has the same elements 
02.  after every traversal the list is sorted for the first n elements, where n is the number of iterations performed

"""
