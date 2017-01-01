##Complete the method/function so that it converts dash/underscore delimited
##words into camel casing. The first word within the output should be
##capitalized only if the original word was capitalized.
##
##Examples:
##
## returns "theStealthWarrior"
##to_camel_case("the-stealth-warrior") 
##
## returns "TheStealthWarrior"
##to_camel_case("The_Stealth_Warrior")

def to_camel_case(text):
    xo=list(text)
    for i in range(len(xo)):
        if xo[i]=='_'or xo[i]=='-':xo[i]=' '    
    L=''.join(xo).split(' ')
    final=L[0]
    for i in range(1,len(L)):
        final=final+L[i].title()
    return final
print to_camel_case("the_Stealth-Warrior")
