from node import *        

# A class implementing Multiset as a linked list.

class Multiset:

    def __init__(self):
        """
        Produces a newly constructed empty Multiset.
        __init__: -> Multiset
        Field: _head points to the first node in the linked list
        """
        self._head = None

    def empty(self):
        """
        Checks emptiness of Multiset.
        empty: Multiset -> Bool
        :return: True if Multiset is empty and False otherwise.
        """
        return self._head == None

    def __contains__(self, value):
        """
        Checks existence of value in the Multiset.
        __contains__: Multiset Any -> Bool
        :param value: the value to be check.
        :return: True if Multiset is in the Multiset and False otherwise.
        """
        current = self._head
        while current is not None:
            if current.item == value:
                return True
            else:
                current = current.next
        return False

    def add(self, value):
        """
        Adds the value to multiset.

        :param value: the value to be added.
        """
        if self._head is None:
            self._head = Node(value)
        else:
            rest = self._head
            self._head = Node(value)
            self._head.next = rest

    def delete(self, value):
        """

        :param value: value first occurrence of which should be deleted.
        """
        current = self._head
        previous = None
        while current is not None and current.item != value:
            previous = current
            current = current.next
        if current is not None:
            if previous is None:
                self._head = self._head.next
            else:
                previous.next = current.next

    def remove_all(self):
        '''
        Removes linked structure.
        '''
        self._head = None


    def split_half(self):
        '''
        Splits the structure on two different ones.
        :return: two structures which contain the data from the original one.
        '''
        current = self._head
        struct_len = 0
        indexx = 0
        struct1 = Multiset()
        struct2 = Multiset()
        while current is not None:
            struct_len += 1
            current = current.next
        if struct_len == 1:
            return None
        current = self._head
        half_struct = struct_len // 2
        while current != None:
            if indexx < half_struct:
                struct1.add(current.data)
            elif indexx >= half_struct:
                struct2.add(current.data)
            indexx += 1
            current = current.next

        return struct1, struct2

