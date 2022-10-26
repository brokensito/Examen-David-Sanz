



class Node:
    def __init__(self, data):
        self.data = data
        self.previous = None
        self.next = None

    def __str__(self):
        return f"{self.data}"


class DoublyLinkedList:
    def __init__(self):
        self.comienzo = None
        self.final = None

    def __iter__(self):
        node = self.comienzo
        while node:
            yield node.data
            node = node.next

    def __str__(self):
        return "->".join([str(item) for item in self])

    def __len__(self):
        return len(tuple(iter(self)))

    def insertar_comienzo(self, data):
        self.insertar_indice(0, data)

    def insertar_final(self, data):
        self.insertar_indice(len(self), data)

    def insertar_indice(self, index: int, data):
        if not 0 <= index <= len(self):
            raise IndexError("list index out of range")
        new_node = Node(data)
        if self.comienzo is None:
            self.comienzo = self.final = new_node
        elif index == 0:
            self.comienzo.previous = new_node
            new_node.next = self.comienzo
            self.comienzo = new_node
        elif index == len(self):
            self.final.next = new_node
            new_node.previous = self.final
            self.final = new_node
        else:
            temp = self.comienzo
            for _ in range(0, index):
                temp = temp.next
            temp.previous.next = new_node
            new_node.previous = temp.previous
            new_node.next = temp
            temp.previous = new_node

    def borrar_comienzo(self):
        return self.borrar_indice(0)

    def borrar_final(self):
        return self.borrar_indice(len(self) - 1)

    def borrar_indice(self, index: int):
        if not 0 <= index <= len(self) - 1:
            raise IndexError("list index out of range")
        delete_node = self.comienzo  # default first node
        if len(self) == 1:
            self.comienzo = self.final = None
        elif index == 0:
            self.comienzo = self.comienzo.next
            self.comienzo.previous = None
        elif index == len(self) - 1:
            delete_node = self.final
            self.final = self.final.previous
            self.final.next = None
        else:
            temp = self.comienzo
            for _ in range(0, index):
                temp = temp.next
            delete_node = temp
            temp.next.previous = temp.previous
            temp.previous.next = temp.next
        return delete_node.data

    def borrar(self, data) -> str:
        current = self.comienzo

        while current.data != data:  # Find the position to delete
            if current.next:
                current = current.next
            else:  # We have reached the end an no value matches
                return "No data matching given value"

        if current == self.comienzo:
            self.borrar_comienzo()

        elif current == self.final:
            self.borrar_final()

        else:  # Before: 1 <--> 2(current) <--> 3
            current.previous.next = current.next  # 1 --> 3
            current.next.previous = current.previous  # 1 <--> 3
        return data

    def comprobar_vacio(self):
        return len(self) == 0








