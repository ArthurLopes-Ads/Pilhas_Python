class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        return None

    def is_empty(self):
        return len(self.items) == 0

pilha = Stack()
x = input("Digite a string X: ")
y = input("Digite a string Y: ")

for letra in x:
    pilha.push(letra)

x_rev = ""

while not pilha.is_empty():
    x_rev += pilha.pop()

# Fazer comparação para verificar se tá no formato XY
if x_rev == y:
    print("Formato XY válido")
else:
    print("Formato XY inválido")
