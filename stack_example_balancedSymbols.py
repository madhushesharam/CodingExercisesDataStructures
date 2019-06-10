'''
Simple example of stack implementation in python to check if SYMBOLS are balanced.
'''
import unittest

class Stack:
    def __init__ (self):
        self.items = []
    
    def push(self, item):
        self.items.append(item)
    
    def pop (self):
        if self.items:
            return self.items.pop()
    
    def is_empty(self):
        return self.items == []
        
    
    def peek(self):
        if self.items:
            return self.items[len(self.items)-1]
    
    def size(self):
        return len(self.items)
    
    
    
def myfunction(string):
    symbol_pairs = {
            '(': ')',
            '[': ']',
            '{': '}',
            '<': '>'
    }
    s= Stack()
    for i in string:
        
        if i in symbol_pairs.keys():
            s.push(i)
        else:
            if s.is_empty():
               return False
            else:
                temp = s.pop()
                if i != symbol_pairs[temp]:
                    return False
                
                
    if s.is_empty():
        return True
    else:
        return False
                

class TestSymbols(unittest.TestCase):
    def testpositive(self):
        self.assertEqual(myfunction ('(<[{}]>)'), True)
    
    def testNegative(self):
        self.assertEqual(myfunction ('<(([{}]])>'), False)
        

unittest.main()            
            
            
    

  