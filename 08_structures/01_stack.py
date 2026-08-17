# 01 - Stacks
# Es una coleccion linieal de datos los cuales se apilan uno dentro de otros

stack = []

#Añadir al stack
stack.append(10)
stack.append(20)

print(stack)
element = stack.pop()
print(element)

#Para ver el top
top = stack[-1]
print(top)

print(stack)