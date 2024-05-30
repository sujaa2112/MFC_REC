import time
import random
def bubble_sort(arr):
    n=len(arr)
    for i in range(n):
        for j in range(0,n-i-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
def selection_sort(arr):
    n=len(arr)
    for i in range(n):
        min_idx=i
        for j in range(i+1,n):
            if arr[j]<arr[min_idx]:
                min_idx=j
        arr[i],arr[min_idx]=arr[min_idx],arr[i]
arr = [random.randint(1,1000) for k in range(1000)]
start_time = time.time()
bubble_sort(arr.copy())
end_time = time.time()
bubble_sort_time = end_time-start_time
print("Bubble Sort Time:",bubble_sort_time)

start_time = time.time()
selection_sort(arr.copy())
end_time = time.time()
selection_sort_time = end_time-start_time
print("Selection Sort Time:",selection_sort_time)
