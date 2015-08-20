"""
Oh no! Timmy's List Class has broken! Can you help timmy and fix his class? 
Timmy has a List class he has created, this is used for type strict arrays 
(which timmy calls Lists). 
When timmy calls the Count property of the list it still remains at 0 when 
adding items. Also it fails when timmy trys to chain the adds e.g.:
my_list.add(0).add(1)
  
>>> my_list=List(str)
>>> my_list.add('Hello').count
1
>>> my_list.add(5)
'This item is not of type: str'
>>> my_list.add(' ').add('World!').count
3
"""
class List:

    def __init__(self,type):
        self.type=type
        self.items=[]
        self.count=0
    
    def add(self,item):
        if type(item)!=self.type:
            item_type="str" if self.type==str else "int" if self.type==int else "float"
            return "This item is not of type: %s" %(item_type)
        
        else:
            self.items+=[item]
            self.count+=1
            return self.items

    def count(self):
        return self.count

if __name__ == "__main__":

    import doctest
    doctest.testmod()