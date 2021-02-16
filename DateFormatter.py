'''
Created on 14-Oct-2020

@author: AA20090212 - AAYUSH KUMAR SRIVASTAVA 
'''
def dateFormatChanger(date):
    dateSplit = date.split('/')
    return "{}{}{}".format(dateSplit[2],dateSplit[1],dateSplit[0])

if __name__ == '__main__':
    print(dateFormatChanger('12/24/1990'))