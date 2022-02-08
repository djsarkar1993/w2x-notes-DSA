import  sys


class Node1:
    def __init__(self, value):
        self.value = value
        self.next = None


class Node2:
    def __init__(self, value):
        self.prev = None
        self.value = value
        self.next = None


class SLL:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0
    

    def __str__(self):
        if self.head:
            result = f'H({self.head.value}) -> '

            current_node = self.head
            while current_node:
                result += f'{current_node.value} -> '
                current_node = current_node.next
            
            result += f'NULL <- T({self.tail.value})'
            
            return result
        else:
            return 'The linked list is empty!'
    

    def insert(self, value, pos=-1, hidePrints=False):
        node = Node1(value)

        if self.head is None:
            if pos not in [1, -1]:
                raise Exception("The linked list is empty. The value of pos should either be 1 or -1.")

            if not hidePrints:
                print('Inserting to an empty linked list.')
            
            self.head = node
            self.tail = node 
        
        else:
            if pos == 1:
                if not hidePrints:
                    print('Inserting to first position')

                node.next = self.head
                self.head = node
            
            elif pos == -1:
                if not hidePrints:
                    print('Inserting to last position')

                self.tail.next = node
                self.tail = node
            
            else:
                if pos > self.length:
                    raise Exception(f"The value of pos should either be 1 or -1 or between 1 & {self.length}")
                
                previous_node = self.head
                current_node = self.head.next
                for i in range(1, pos-1):
                    previous_node = previous_node.next
                    current_node = current_node.next
                
                if not hidePrints:
                    print('Inserting to nth position')

                node.next = current_node
                previous_node.next = node
        
        self.length += 1
    

    def empty(self):
        if self.head:
            self.head = None
            self.tail = None
        else:
            raise Exception("Operation not permitted: the linked list is empty")


class CSLL:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0
    

    def __str__(self):
        if self.head:
            result = f'H({self.head.value}) -> '

            current_node = self.head
            while current_node:
                result += f'{current_node.value} -> '

                if current_node == self.tail:
                    break

                current_node = current_node.next
            
            result += f'... <- T({self.tail.value})'

            return result
        else:
            return 'The linked list is empty!'
    

    def insert(self, value, pos=-1, hidePrints=False):
        node = Node1(value)

        if self.head is None:
            if pos not in [1, -1]:
                raise Exception("The linked list is empty. The value of pos should either be 1 or -1.")
            
            if not hidePrints:
                print('Inserting to empty linked list')

            self.head = node
            self.tail = node

            node.next = node
        
        else:
            if pos == 1:
                if not hidePrints:
                    print('Inserting to first position')

                node.next = self.head
                self.head = node

                self.tail.next = node
            
            elif pos == -1:
                if not hidePrints:
                    print('Inserting to last position')

                self.tail.next = node
                self.tail = node

                node.next = self.head
            
            else:
                if pos > self.length:
                    raise Exception(f"The value of pos should either be 1 or -1 or between 1 & {self.length}")
                
                previous_node = self.head
                current_node = self.head.next
                for i in range(1, pos-1):
                    previous_node = previous_node.next
                    current_node = current_node.next
                
                if not hidePrints:
                    print('Inserting to nth position')

                node.next = current_node
                previous_node.next = node
        
        self.length += 1
    

    def empty(self):
        if self.head:
            self.tail.next = None

            self.head = None
            self.tail = None
        else:
            raise Exception("Operation not permitted: the linked list is empty")


class DLL:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0
    

    def __str__(self):
        if self.head:
            result = f'H({self.head.value}) -> NULL <- '

            current_node = self.head
            while current_node:
                result += f'{current_node.value} <-> '
                current_node = current_node.next
            
            result = result.rstrip('<-> ') + f' -> NULL <- T({self.tail.value})'

            return result
        else:
            return 'The linked list is empty!'
    

    def traverse_backwards(self):
        if self.head:
            result = f'T({self.tail.value}) -> NULL <- '
            
            current_node = self.tail
            while current_node:
                result += f'{current_node.value} <-> '
                current_node = current_node.prev
            
            result = result.rstrip('<-> ') + f' -> NULL <- H({self.head.value})'

            return result
        else:
            return 'The linked list is empty!'
    

    def insert(self, value, pos=-1, hidePrints=False):
        node = Node2(value)

        if self.head is None:
            if pos not in [1, -1]:
                raise Exception('The linked list is empty. The value of pos should either be 1 or -1')
            
            if not hidePrints:
                print('Inserting to empty linked list')

            self.head = node
            self.tail = node
        
        else:
            if pos == 1:
                if not hidePrints:
                    print('Inserting to first position')

                self.head.prev = node

                node.next = self.head

                self.head = node

            elif pos == -1:
                if not hidePrints:
                    print('Inserting to last position')

                self.tail.next = node

                node.prev = self.tail

                self.tail = node
            
            else:
                if pos > self.length:
                    raise Exception(f"The value of pos should either be 1 or -1 or between 1 and {self.length}")
                
                previous_node = self.head
                current_node = self.head.next
                for i in range(1, pos-1):
                    previous_node = previous_node.next
                    current_node = current_node.next
                
                if not hidePrints:
                    print('Inserting to nth position')

                node.prev = previous_node
                node.next = current_node

                previous_node.next = node
                current_node.prev = node
        
        self.length += 1
    

    def empty(self):
        if self.head:
            current_node = self.head
            while current_node:
                current_node.prev = None
                current_node = current_node.next
            
            self.head = None
            self.tail = None
        else:
            raise Exception("Operation not permitted: the linked list is empty")


class CDLL:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0
    

    def __str__(self):
        if self.head is not None:
            result = f'H({self.head.value}) -> ... <- '

            current_node = self.head
            while True:
                result += f'{current_node.value} <-> '

                if current_node == self.tail:
                    break

                current_node = current_node.next
            
            result = result.rstrip('<-> ') + f' -> ... <- T({self.tail.value})'

            return result
        else:
            return 'The linked list is empty!'
    

    def traverse_backwards(self):
        if self.head is not None:
            result = f'T({self.tail.value}) -> ... <- '

            current_node = self.tail
            while True:
                result += f'{current_node.value} <-> '

                if current_node == self.head:
                    break

                current_node = current_node.prev
            
            result = result.rstrip('<-> ') + f' -> ... <- H({self.head.value})'

            return result
        else:
            return 'The linked list is empty!'
    

    def insert(self, value, pos=-1, hidePrints=False):
        node = Node2(value)

        if self.head is None:
            if pos not in [1, -1]:
                raise Exception("The linked list is empty. The value of pos should eitehr be 1 or -1.")
            
            if not hidePrints:
                print('Inserting to empty linked list')

            self.head = node
            self.tail = node

            node.next = node
            node.prev = node
        
        else:
            if pos == 1:
                if not hidePrints:
                    print('Inserting to the first position')

                self.head.prev = node
                self.tail.next = node

                node.next = self.head
                node.prev = self.tail

                self.head = node
            
            elif pos == -1:
                if not hidePrints:
                    print('Inserting to the last position')

                self.tail.next = node
                self.head.prev = node

                node.prev = self.tail
                node.next = self.head

                self.tail = node
            
            else:
                if pos > self.length:
                    raise Exception(f"The value of pos should either be 1 or -1 or between 1 and {self.length}")
                
                previous_node = self.head
                current_node = self.head.next
                for i in range(1, pos-1):
                    previous_node = previous_node.next
                    current_node = current_node.next
                
                if not hidePrints:
                    print('Inserting to the nth position')

                node.prev = previous_node
                node.next = current_node

                previous_node.next = node
                current_node.prev = node
        
        self.length += 1
    

    def empty(self):
        if self.head:
            self.tail.next = None

            current_node = self.head
            while current_node:
                current_node.prev = None
                current_node = current_node.next
            
            self.head = None
            self.tail = None
        else:
            raise Exception("Operation not permitted: the linked list is empty")
