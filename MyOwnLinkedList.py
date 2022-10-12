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
        return
            
    def search(self, val):
        current = self.head
        while current:
            if current.val == val:
                return True
            else:
                current = current.next
        return False
    
    def delete(self, val):
        if not self.head:
            print("This linked list is empty, there is nothing to delete.")
            return
        
        elif not self.search(val):
            print(f"The value \'{val}\' was not found in the linked list.")
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
                
        return "Not found"
        
    def printList(self):
        lst = []
        current = self.head
        
        while current:
            lst.append(current.val)
            current = current.next
        
        for i, j in enumerate(lst):
            if i == len(lst)-1:
                print(f'{j}')
                return
            else:
                print(f'{j} -> ', end = " ")
        return
    
def main():
    MyList = LList()
    MyList.delete(1)
    MyList.add(8)
    MyList.printList()
    MyList.add(9)
    MyList.search(1)
    MyList.printList()
    MyList.delete(8)
    MyList.printList()
    MyList.add(10)
    MyList.printList()
    MyList.add(13)
    MyList.add(15)
    MyList.add(20)
    MyList.add(5)
    MyList.add(3)
    MyList.add(6)
    MyList.delete(15)
    MyList.printList()

if __name__ == "__main__":
    main()