class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def push(self, novo):
        self.items.append(novo)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        return None

# Creating a stack instance
pilha = Stack()

# Getting user input
entrada = input("Digite I ou E: ")

# Processing the input
for letra in entrada:
    if letra == "I":
        pilha.push(letra)
    elif letra == "E":
        if not pilha.is_empty():
            pilha.pop()
        else:
            print("A pilha está vazia!")
            break
