'''
Created on 14-Oct-2020

@author: AA20090212 - AAYUSH KUMAR SRIVASTAVA
'''

def commonItemsFinder(list1, list2):
    duplicateCommonItems = [x for x in list1 if x in list2]

    commonItems = []
    
    for x in duplicateCommonItems:
        if x not in commonItems:
            commonItems.append(x) 
    
    return commonItems

if __name__ == '__main__':
    list1 = [1, 1, 2, 2, 3, 3, 3, 5, 8, 13, 21, 34, 55, 89]
    list2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
    print(commonItemsFinder(list1, list2))