import json
import datetime

id = 0

def main():
    user_input = input("> ")
    
    match user_input.trim().split()[0].lower():
        case "add":
            addTask(desc=user_input[1])
        case "update":
            ...
        case "delete":
            ...
        case "mark-in-progress":
            ...
        case "mark-done":
            ...
        case "list":
            ...

    print("Start of the program ")


def addTask(desc):

    data = { id : {"description": desc,
                   "status": "todo",
                   "createdAt": datetime.datetime.now(),
                   "updatedAt": datetime.datetime.now()
                   }
    }
    
    with open("task_data.json", "a") as file:
        json.dump(data, file, indent=4)
    
    id += 1


def updateTask():
    ...

def deleteTask():
    ...


def markTask(taskID):
    ...

def listAllTasks():
    ...

def listDoneTasks():
    ...

def listNotDoneTasks():
    ...

def listInProgressTasks():
    ...

