'''
Created on 31-Oct-2020

@author: AA20090212
'''

import base64

if __name__ == '__main__':
    pdffile = open('C:\Users\AA20090212\Downloads\M2 Dev Essentials v2_3 Exercises.pdf')
    print(base64.b64decode(pdffile))