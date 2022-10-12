class Node(): 
    def __init__(self, val, next = None):
        self.val = val
        self.next = next
        
class LList():
    def __init__(self):
        self.head = None
        
    def add(self, val):
        newNode = Node(val)
        if not self.head:
            self.head = newNode
            
        else:
            current = self.head
        
            while current.next:
                current = current.next
            current.next = newNode
    
    def delete(self, val):
        if not self.head:
            return
        
        #delete head
        current = self.head
        if current.val == val:
            self.head = current.next
        
        else:   
            
            while current.val != val:
                current.prev = current
                current = current.next
            
            #delete middle
            if current.next != None:
                current.prev.next = current.next
            
            #delete tail
            elif current.next == None:
                current.prev.next = None
        
    def printList(self):
        lst = []
        current = self.head
        while current:
            lst.append(current.val)
            current = current.next
        return lst
    
def main():
    MyList = LList()
    MyList.add(8)
    print(MyList.printList())
    MyList.add(9)
    print(MyList.printList())
    MyList.delete(8)
    print(MyList.printList())
    MyList.add(10)
    print(MyList.printList())

if __name__ == "__main__":
    main()