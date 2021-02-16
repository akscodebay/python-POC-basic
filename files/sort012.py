'''
Created on 20-Nov-2020

@author: AA20090212
'''

def sort012(arr,n):
    # code here
    i=0
    j=n-1
    while i<j:
        if arr[j] == 2:
            j-=1
            continue
        if arr[i] == 2:
            temp = arr[i]
            arr[i] = arr[j]
            arr[j] = temp
            print(arr)
        i+=1
    print('2 sort complete')
    i=0
    if arr[j] == 2:
        j-=1
    while i<j:
        if arr[j] == 1:
            j-=1
            continue
        if arr[i] == 1:
            temp = arr[i]
            arr[i] = arr[j]
            arr[j] = temp
            print(arr)
        i+=1
    return arr

if __name__ == '__main__':
    arr = [int(x) for x in input().strip().split()]
    print(sort012(arr, len(arr)))
    