from SinglyLinkedList import SinglyLinkedList

class Main:

    def __init__(self):
        linkedList = SinglyLinkedList()
        linkedList.traversal()
        
        print("\nOK, lets fill up the list")
        val = input("\nEnter the value of new node to append to the list\n:")
        linkedList.append(val)
        val = input("\nEnter the value of new node to append to the list\n:")
        linkedList.append(val)
        val = input("\nEnter the value of new node to append to the list\n:")
        linkedList.append(val)
        val = input("\nEnter the value of new node to append to the list\n:")
        linkedList.append(val)

        linkedList.traversal()

        pos = input("\nEnter the position to insert in the list\n:")
        val = input("\nEnter the value of new node to append to the list\n:")


        linkedList.insert(pos, val)

        linkedList.traversal()
        print(linkedList.count())
        
Main()