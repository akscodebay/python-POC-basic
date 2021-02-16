'''
Created on 14-Oct-2020

@author: AA20090212 - AAYUSH KUMAR SRIVASTAVA
'''

class Polygon:
    '''
    classdocs
    '''
    def __init__(self):
        '''
        Constructor
        '''
        self.sides = []
    
    def setSides(self):
        pass
    
    def displaySides(self):
        print('\nsides: {}\n'.format(self.sides))

class Square(Polygon):
    def setSides(self):
        self.sides.append(float(input('Enter side')))
    def calculateArea(self):
        return self.sides[0]*self.sides[0]
    
class Triagle(Polygon):
    def setSides(self):
        self.sides.append(float(input('Enter side 1')))
        self.sides.append(float(input('Enter side 2')))
        
    def calculateArea(self):
        return (self.sides[0]*self.sides[1])/2
    
square = Square()
triangle = Triagle()
prev_choice = ''

while True:
    print('Menu')
    print('input 1 for Square Area Calculation')
    print('input 2 for Trianle Area Calculation')
    print('input 3 to Display Sides')
    print('input any other key exit')
    choice = input('Enter choice: ')
    if choice == '1':
        prev_choice = '1'
        square.sides.clear()
        square.setSides()
        print('\nArea of Square: ' + str(square.calculateArea()) + '\n')
        
    elif choice == '2':
        prev_choice = '2'
        triangle.sides.clear()
        triangle.setSides()
        print('\nArea of Triangle: ' + str(triangle.calculateArea()) + '\n')    
    
    elif choice == '3':
        if prev_choice == '':
            print('\nNo Sides Available to Display\n')
        elif prev_choice == '1':
            square.displaySides() 
        else:
            triangle.displaySides()
    
    else:
        print('exiting...')
        exit(0)
    