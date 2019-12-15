# -*- coding: utf-8 -*-
"""
Created on Thu Apr 28 08:31:49 2016

@author: rajan
"""

print('Enter the operands and operators.')
print('The end of the operands is indicated by double hit of Enter Key')
operation = []
while True:
    line = input()
    if line:
        operation.append(line)
    else:
        break
text = ' '.join(operation)
text = text.split()
print(text)


output = 0.0
for tx in text:
    
           
    if tx.startswith('+'):
        output = output + float(tx[1:])
        
    elif tx.startswith('-'):
        output = output - float(tx[1:])
        
    elif tx.startswith('*'):
        output = output * float(tx[1:])
    

    elif tx.startswith('/'):
        output = output / float(tx[1:])
        
    elif tx.startswith('//'):
        output = output // float(tx[1:])
        
    elif tx.startswith('%'):
        output = output % float(tx[1:])
        
        
    else:
        output = output + float(tx)
            
     
   
print(output)
