# Creating a bubble sort function  
def bubble_sort(list1):  
    # Outer loop for traverse the entire list  
    for i in range(0,len(list1)-1):  
        for j in range(len(list1)-1):  
            if(list1[j]>list1[j+1]):  
                temp = list1[j]  
                list1[j] = list1[j+1]  
                list1[j+1] = temp  
    return list1  
  
list1 = [5, 3, 8, 6, 7, 2]  
print("The unsorted list is: ", list1)  
# Calling the bubble sort function  
print("The sorted list is: ", bubble_sort(list1))  
Output:

The unsorted list is:  [5, 3, 8, 6, 7, 2]
The sorted list is:  [2, 3, 5, 6, 7, 8]
Explanation:

In the above code, we have defined a bubble_sort() function which takes list1 as an argument.

Inside the function, we have defined two for loop - first for loop iterates the complete list and the second for loop iterates the list and the compare the two elements in every outer loop iterations.
The for loop will be terminated when it reaches at the end.
We have defined the condition in the inner for loop; if a first index value is greater than the second index value, swap their positions with each other.
We called the function and passed a list; it iterated and returned the sorted list.
Without using a temp variable
We can also swap the elements without using the temp variable. Python has a very unique syntax. We can use the following lines of code.

Example -

def bubble_sort(list1):  
    # Outer loop for traverse the entire list  
    for i in range(0,len(list1)-1):  
        for j in range(len(list1)-1):  
            if(list1[j]>list1[j+1]):   
                # here we are not using temp variable  
                list1[j],list1[j+1] = list1[j+1], list1[j]  
    return list1  
  
list1 = [5, 3, 8, 6, 7, 2]  
print("The unsorted list is: ", list1)  
# Calling the bubble sort function  
print("The sorted list is: ", bubble_sort(list1))  
