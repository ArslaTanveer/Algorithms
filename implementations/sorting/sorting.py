#####################################################
# Bubble Sort (Un-optimized)                        #
# - Possible swaps are total array items count - 1  #
# - Main outer loop runs this much time             #
# - Internal loop runs to how many swaps remain     #
#####################################################

def bubble_sort(array):
    SwapCount = len(array) - 1
    for i in range(len(array) - 1):
        for j in range(SwapCount):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
        SwapCount -= 1
    return array

testArray = [9, 3 , 2, 7, 10, 12]
print(bubble_sort(testArray))
############################################################
# Bubble Sort (Optimized) : Introduce a flag to run in loop #
############################################################
def optimized_bubble_sort(array):
    SwapNeeded = True
    SwapCount = len(array) - 1
    while SwapNeeded:
        SwapNeeded = False
        for i in range(SwapCount):
            if array[i] > array[i+1]:
                array[i],array[i+1] = array[i+1],array[i]
                SwapNeeded = True
        SwapCount -= 1
    return array
print(optimized_bubble_sort(testArray))

def insert_sort(array):
    for i in range(1, len(array)):
        MoveItem = array[i]
        BorderItemPosition = i - 1
        while (MoveItem < array[BorderItemPosition]) and (BorderItemPosition > -1) :
            array[BorderItemPosition+1] = array[BorderItemPosition]
            BorderItemPosition -= 1
            array[BorderItemPosition+1] = MoveItem
    return array
print(insert_sort(testArray))
