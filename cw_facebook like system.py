##You probably know the "like" system from Facebook and other pages.
##People can "like" blog posts, pictures or other items.
##We want to create the text that should be displayed next to such an item.
##
##Implement a function likes :: [String] -> String,
##which must take in input array, containing the names of
##people who like an item. It must return the display text as shown
##in the examples:
##    likes [] // must be "no one likes this"
##    likes ["Peter"] // must be "Peter likes this"
##    likes ["Jacob", "Alex"] // must be "Jacob and Alex like this"
##    likes ["Max", "John", "Mark"] // must be "Max, John and Mark like this"
##    likes ["Alex", "Jacob", "Mark", "Max"] // must be "Alex, Jacob and 2 others like this"


def likes(names):
    if len(names)==0:return 'no one likes this'
    elif len(names)==1:return (names[0]+' likes this')
    else:
        le=len(names)
        L=[]
        
        if le==2:
            L.append(names[0]);L.append('and');L.append(names[1]);L.append('like this')
        elif le==3:
            L.append(names[0]+',');L.append(names[1]);L.append('and');L.append(names[2]);L.append('like this')
        else:
            L.append(names[0]+',');L.append(names[1]);L.append('and');L.append(str(le-2)+' others');L.append('like this')                    

    return ' '.join(L) 

#for example:
print likes(["Alex", "Jacob", "Mark", "Max",'bob marley'])
                               
        
