class Operation:
    def __init__(self, nombre1, nombre2):
        self.nombre1 = nombre1
        self.nombre2 = nombre2

instance_operation = Operation(12, 3)

print("Le nombre1 est", instance_operation.nombre1)
print("Le nombre2 est", instance_operation.nombre2)