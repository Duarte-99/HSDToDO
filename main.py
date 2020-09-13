from os import system, name


# Función que permite limpiar la consola
def clear():
    # for windows 
    if name == 'nt':
        _ = system('cls')

        # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')


# Menu actions
add = 1
edit = 2
done = 3
delete = 4
list = 5
close = 6

# Limit options
minOption = 1
maxOption = 6


class Task:
    def __init__(self, name, dueDate):
        self.name = name
        self.dueDate = dueDate
        self.done = False

    def printData(self, index):
        print("{0}. Tarea: {1}, Fecha limite: {2}, Hecha: {3}".format(index, self.name, self.dueDate, self.done))


def printMenu():
    print("")
    print("************************")
    print("* ToDo Manuel          *")
    print("************************")
    print("Seleccione una opcion")
    print("1 Agregar tarea")
    print("2 Editar tarea")
    print("3 Marcar como hecha")
    print("4 Borrar tarea")
    print("5 Listar tareas")
    print("6. Salir")


def printTitleList():
    print("")
    print("*********************")
    print("* LISTADO DE TAREAS *")
    print("*********************")
    print("")


def getOption():
    try:
        value = int(input("Opción: "))
    except ValueError:
        print("Ese no es un número.")

    return value


def getIndex():
    try:
        value = int(input("Digite el número de la tarea: "))
    except ValueError:
        print("Ese no es un número.")

    return value


def getIsDone():
    value = input("Digite 1 para Verdadero, cualquier otra tecla para Falso: ")
    if value == "1":
        return True

    return False


def newToDo():
    return []


def createTask():
    name = input("Nombre: ")
    dueDate = input("Fecha limite: ")
    task = Task(name, dueDate)
    return task


def addTask(task, toDo):
    toDo.append(task)


def delTask(index, toDo):
    del toDo[index - 1]


def editTask(index, newTask, toDo):
    toDo[index - 1] = newTask


def doneTask(index, done, toDo):
    toDo[index - 1].done = done


def printAllTask(toDo):
    index = 0
    for task in toDo:
        index += 1
        task.printData(index)


def isValidOption(option):
    if option < minOption or option > maxOption:
        return False

    return True


def process(option, toDo):
    if option == add:
        clear()
        print("Crear/Editar tarea")
        task = createTask()
        addTask(task, toDo)
        print("*** Tarea creada ***")
        return

    if option == edit:
        clear()
        print("Crear/Editar tarea")
        index = getIndex()
        task = createTask()
        editTask(index, task, toDo)
        print("*** Tarea editada ***")
        return

    if option == done:
        clear()
        print("Marcar tarea como hecha")
        index = getIndex()
        isDone = getIsDone()
        doneTask(index, isDone, toDo)
        print("*** Tarea marcada ***")
        return

    if option == delete:
        clear()
        print("Borrar tarea")
        index = getIndex()
        delTask(index, toDo)
        print("*** Tarea borrada ***")
        return

    if option == list:
        clear()
        printTitleList()
    if option == list:
        clear()
        printTitleList()
        printAllTask(toDo)


def execute():
    option = 0
    toDo = newToDo()

    while option != close:
        printMenu()
        option = getOption()
        if not isValidOption(option):
            print("opción no valida, intente una opción de {0} a {1}".format(minOption, maxOption))
            continue

        process(option, toDo)


execute()
