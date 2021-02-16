'''
Created on 14-Oct-2020

@author: AA20090212 - AAYUSH KUMAR SRIVASTAVA
'''
from _functools import reduce
def nameSum(names):
    return len(reduce(lambda x,y: x+y, filter(lambda x: x.islower(),names)))

if __name__ == '__main__':
    names = ['sally', 'Dylan', 'rebecca', 'Diana', 'Joanne', 'keith']
    print(nameSum(names))