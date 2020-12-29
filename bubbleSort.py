def bubble_sort(the_list):
    number_of_elements = len(the_list)
    for i in range(number_of_elements-1, 0, -1):
        for j in range(i-1):
            if the_list[j] > the_list[j+1]:
                temp = the_list[j]
                the_list[j] = the_list[j+1]
                the_list[j+1] = temp
            else :
                continue

    print(the_list)


bubble_sort([5, -3, 1, 2, 3, 4, 9, 8, 8, 9, 7, 8, 8, 9])

# invariants
"""

the property that remains unchanged at any point throughout the algorithm
01.  after every traversal, the list has the same elements 
02.  in each traversal at most n-1 swaps are performed, where n
is the length of the list

"""