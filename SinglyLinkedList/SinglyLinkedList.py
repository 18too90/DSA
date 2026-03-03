from Node import Node

class SinglyLinkedList:
    def __init__(self):
        self.head= None

    def append(self, val):
        if(self.head == None):
            self.head = Node(val)
        else:
            cur = self.head
            while(cur.Next is not None):
                cur = cur.Next
            cur.Next = Node(val)

    def traversal(self):
        cur = self.head
        if cur is None:
            print("No nodes found in this LinkedList")
        else:
            while(cur is not None):
                print(f"{cur.val} -> ")
                cur = cur.Next

    def insert(self, pos, val):
        try:
            posint = int(pos)
        except:
            print("Invalid position")
            return
        new_node = Node(val)
        if posint == 0:
            new_node.Next = self.head
            self.head = new_node
        else:            
            cur = self.head
            while posint > 0:
                prev_node = cur
                cur = cur.Next
                posint = posint -1
            prev_node.Next = new_node
            new_node.Next = cur

    def count(self) -> int:
        count = 0
        cur = self.head
        while(cur is not None):
            count = count + 1
            cur = cur.Next
        return count


