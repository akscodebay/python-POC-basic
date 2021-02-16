'''
Created on 14-Oct-2020

@author: AA20090212 - AAYUSH KUMAR SRIVASTAVA
'''

writingFile = open('files/file2.txt', 'w')

with open('files/file1.txt', 'r') as readingFile:
    sentences = readingFile.read().split('.')
    sentences.pop()
    for x in range(len(sentences)-1,-1,-1):
        sentences[x] = sentences[x] + '.'
        if(sentences[x][0] == ' '):
            sentences[x] = sentences[x].strip() + ' '
        if sentences[x][0] == '\n':
            sentences[x] = sentences[x].strip() + '\n'
        writingFile.write(sentences[x])
        
writingFile.close()
print('Sentence order reversed.')