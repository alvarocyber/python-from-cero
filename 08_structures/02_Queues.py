# 02 - Colas
# Sirgue la estructura FIFO (First in First out)

from collections import deque

cola = deque()

cola.append("Ana")
cola.append("Lucia")
cola.append("Jose")

print(cola)

primero = cola.popleft()
print(primero)