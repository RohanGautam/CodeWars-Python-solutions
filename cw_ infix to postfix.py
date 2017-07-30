class stack:
    '''Stack implementation'''
    def __init__(self,fixed=False):
        self.L=[]
        self.counter=1
        self.fixed=fixed
        
    def push(self,ele): #accept element, add to stack
        if self.fixed ==False: #if it's not fixed
            self.L.append(ele)
            return 'push successful'
        elif self.counter<=self.fixed:
            self.L.append(ele)
            self.counter+=1
            return 'push successful'
        return 'Stack length exceeded!!Cannot push to stack.'
    def pop(self):  #return last element if list is not empty
        return self.L.pop() if self.L  else 'Stack is empty'
    
    def display(self):  #view entire stack
        print '\n'.join(map(str,self.L[::-1])) if self.L  else '[], Stack is empty'
    
    def peek(self): #view last element of stack
        return self.L[-1] if self.L  else False
        
        
        
        
    
def to_postfix(E):
    precedence={'(':-100,'-':1,'+':1,'*':2,'/':2,'**':3,'^':3,')':100}    #operator precedence. here, '(' is considered to have least precedence, and ')' the maximum.
    
    def tokenize(e):
        import re
        pattern=r'\*\*|\d|\*|\+|\-|\/|\(|\)|[A-Za-z]|\^'
        L=re.findall(pattern,e)
        return L+[')']  #'(' is added directly to stack; see reason where this is done
    P=''    #the resultant postfix expression, P
    s=stack()  #creating a stack
    s.push('(')     #this is done so that while comparing precedence, stack is not empty
    operators='+/-**^'
    for element in tokenize(E):
        if element not in operators+'()': # if it's a number, or any variable,
            P+=element
        elif element in operators:  # if its an operator,
            if precedence[element]>precedence[s.peek()]:
                s.push(element)
            else: 
                while True: #you have to remove ALL OPERATORS from stack until one with lower is reached.
                    if precedence[s.peek()]<precedence[element]:
                        break                    
                    P+=s.pop()
                s.push(element)
        else:                       #if it's an opening or closing bracket
            if element=='(':        #if it's a opening bracket, just push that shit
                s.push(element)
            elif element==')':  #if it's a closing bracket, pop everything from the stack until corresponding opening bracket encountered.
                while True:
                    op=s.pop()
                    if op=='(':break
                    P+=op
    return P