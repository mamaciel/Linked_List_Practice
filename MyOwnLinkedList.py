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
                current_prev = current
                current = current.next
            
            #delete middle
            if current.next != None:
                current.val = current.next.val
                current.next = current.next.next
            
            #delete tail
            elif current.next == None:
                current = current_prev
                current.next = None
                
        return
    
    def update(self, idx, val):
        current = self.head
        index = 0
        if idx > self.size()-1:
            print("Index is out of range, please try again")
            return
        
        while idx != index:
            current = current.next
            index += 1
        
        current.val = val
            
    def size(self):
        current = self.head
        count = 0
        while current:
            current = current.next
            count += 1
        return count
            
    def printList(self):
        lst = []
        current = self.head
        
        while current:
            lst.append(current.val)
            current = current.next
        
        #Used enumerate so we know which node is last
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
    MyList.add(1)
    #MyList.printList()
    MyList.add(2)
    MyList.search(1)
    #MyList.printList()
    MyList.delete(8)
    #MyList.printList()
    MyList.add(3)
    #MyList.printList()
    MyList.add(4)
    MyList.add(5)
    MyList.add(6)
    MyList.add(7)
    MyList.add(8)
    MyList.add(9)
    #MyList.printList()
    MyList.delete(5)
    #MyList.printList()
    MyList.delete(9)
    #MyList.printList()
    MyList.add(10)
    #MyList.printList()
    MyList.update(8, 99)
    MyList.update(5, 99)
    MyList.printList()

if __name__ == "__main__":
    main()