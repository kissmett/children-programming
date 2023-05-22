# please write bubble sort
def bubble_sort(lst):
    for i in range(len(lst)): # n-times loop, aka the number of swaps.
        for j in range(0, len(lst) - i - 1): # n-1 times for the whole list.
            if lst[j] > lst[j + 1]: # if the element at j is greater than the element at j+1.
                lst[j], lst[j + 1] = lst[j + 1], lst[j] # swap them.
    return lst
lst = [1, 5, 2, 7, 3, 9, 4, 6, 8] # list to be sorted.
print(lst) # print the original list.
lst = bubble_sort(lst) # call the function.
print(lst) # print the sorted list.


lst = [2, 1, 3, 4, 5, 6, 7, 8, 9] # [1, 2, 3, 4, 5, 6, 7, 8, 9]
lst = bubble_sort(lst) # [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(lst)
# please write a quick sort 
def quick_sort(lst):
    if len(lst) <= 1:
        return lst
    pivot = lst[0]
    less = [i for i in lst[1:] if i <= pivot]
    greater = [i for i in lst[1:] if i > pivot]
    return quick_sort(less) + [pivot] + quick_sort(greater)


lst = [2, 1, 3, 4, 5, 6, 7, 8, 9] # [1, 2, 3, 4, 5, 6, 7, 8, 9]
lst = quick_sort(lst) # [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(lst)

import random as r

person = r.choice(['tianfei','tyj','tyq'])
print(person)

#please write quick_sort function
def quick_sort(lst):
    if len(lst) <= 1: 		# if the length of the list is less than or equal to 1, then it's sorted.
        return lst 			# return the list.
    pivot = lst[0]			# set the pivot as the first element.
    less = [i for i in lst[1:] if i <= pivot] # set the list less to the list without the pivot.
    greater = [i for i in lst[1:] if i > pivot] # set the list greater to the list without the pivot.
    return quick_sort(less) + [pivot] + quick_sort(greater) # recursively sort the less and greater parts.
# end of quick_sort function.
'''
This is a quick sort algorithm, which is based on the concept of partition method. It's really simple and fast. It's really fast. It's really
simple and fast. It's really fast. 
'''
lst = [2,3,4,9,4,5,8,2,4,7,6]
lst2 = quick_sort(lst)
print(lst)
print(lst2)