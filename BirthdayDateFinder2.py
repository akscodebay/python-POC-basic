'''
Created on 14-Oct-2020

@author: AA20090212 - AAYUSH KUMAR SRIVASTAVA
'''

birthDay = {'aayush':'01 January',
            'sam':'02 Feburary',
            'lambda':'03 March',
            'amber':'04 April'
            }

def findBirthDate(name):
    if name.lower() in birthDay:
            return 'Birthday of friend is on ' + birthDay[name]
    else:
        return 'No match for friend name found'
        
if __name__ == '__main__':
    name = input('Enter a Name: ')
    print(findBirthDate(name))
    
    
