import cmd, json, os, atexit
from datetime import datetime

if not os.path.isfile('./listeTask.json'):
    file = open("./listeTask.json",'r')
else:
    file = open('listeTask.json','a+')
    
alltask = []
def checkTask():
    if len(alltask) == 0:
        return 
    else:
        json.dump(alltask, file)

class Task:
    
    idTask = 0
    
    def __init__(self, id=0, createdAt=datetime.now().date().strftime("%d/%m/%y"), updatedAt=datetime.now().date().strftime("%d/%m/%y"), description="", status="in-progress"):
        self.id = id
        self.description = description
        self.status = status
        self.createdAt = createdAt
        self.updatedAt = updatedAt
        Task.idTask +=1
        
    def create(self):
        self.id = Task.idTask    

class MyCLI(cmd.Cmd):
    prompt = "TaskRunner>> "
    intro = "Bienvenue dans le task tracker fait par me" 
    
    def do_add(self, arg):
        if (arg.strip()):
            if os.path.isfile('./listeTask.json'):
                newTask = Task()
                newTask.create()
                newTask.description = arg.strip()
                data_string = {"id":newTask.id, "description": newTask.description, "status":newTask.status, "createdAt": newTask.createdAt, "updatedAt": newTask.updatedAt}
                alltask.append(data_string)
                print(f'La tache a bien été ajouté: (ID:{newTask.id})')
                print(alltask)
                
        else:
            print("ok")
        
    def do_delete(self, arg):
        if(arg.strip()):
            if os.path.isfile():
                f = open('listeTask.json','+a')
                lines = json.load(f)
        
        
    def do_update(self, arg):
        if arg.strip():
            allArgs = arg.split()
            if len(allArgs) > 1 and len(allArgs)<3:
                for args in allArgs:
                    arg1 = allArgs[0]
                    arg2 = allArgs[1]
                f = open('listeTask.json','r')
                convertfile = json.load(f)
                for allTask in convertfile:
                    if allTask["id"] == arg1 :
                        print("Existe")    
            else:
                print("Vous devez saisir comme suit: [id] [tâche remplacante]")
        
    def do_list(self, arg):
        if arg.strip() == "":
            if(os.path.isfile('./listeTask.json')):
                f = open('listeTask.json','r')
                convertfile = json.load(f)
                for task in convertfile:
                    id = task['id']
                    description = task['description']
                    status = task['status']
                    created = task["createdAt"]
                    updated = task["updatedAt"]
                    print("| id | description | status | createdAt | updatedAt |")
                    print("_____________________________________________________")
                    print(f"| {id} | {description} | {status} | {created} | {updated} |")
                    print("_____________________________________________________")
            else:
                print("Le fichier n'existe pas")
        elif arg.strip() == "done":
            f = open('listeTask.json','r')
            convertfile = json.load(f)
            done = []
            for task in convertfile:
                if task['status'] == 'done':
                    done.append(task)
                else:
                    continue
            if len(done):
                for allTask in done:
                    id = allTask["id"]
                    description = allTask["description"]
                    status = allTask["status"]
                    created = allTask["createdAt"]
                    updated= allTask["updatedAt"]
                    print("| id | description | status | createdAt | updatedAt |")
                    print("_____________________________________________________")
                    print(f"| {id} | {description} | {status} | {created} | {updated} |")
                    print("_____________________________________________________")
            else:
                print("Ne contient aucune tâche")
            
        elif arg.strip() =="todo":
            f = open('listeTask.json','r')
            convertfile = json.load(f)
            todo = []
            for task in convertfile:
                if task['status'] == 'todo':
                    todo.append(task)
                else:
                    continue
            if len(todo) != 0:
                for allTask in todo:
                    id = allTask["id"]
                    description = allTask["description"]
                    status = allTask["status"]
                    created = allTask["createdAt"]
                    updated= allTask["updatedAt"]
                    print("| id | description | status | createdAt | updatedAt |")
                    print("_____________________________________________________")
                    print(f"| {id} | {description} | {status} | {created} | {updated} |")
                    print("_____________________________________________________")
            else:
                print("Ne contient aucune tâche")
            
        elif arg.strip() == "in-progress":
            f = open('listeTask.json','r')
            convertfile = json.load(f)
            allProgress = []
            for task in convertfile:
                if task['status'] == 'in-progress':
                    allProgress.append(task)
                else:
                    continue
            if len(allProgress) != 0:
                for allDone in allProgress:
                    id = allDone["id"]
                    description = allDone["description"]
                    status = allDone["status"]
                    created = allDone["createdAt"]
                    updated= allDone["updatedAt"]
                    print("| id | description | status | createdAt | updatedAt |")
                    print("_____________________________________________________")
                    print(f"| {id} | {description} | {status} | {created} | {updated} |")
                    print("_____________________________________________________")
            else:
                print('Ne contient aucune tâche')
     
     
     
     
     
            
    def do_quit(self, line):
        return True
 
atexit.register(lambda: checkTask())
if __name__ == '__main__':
    MyCLI().cmdloop()
    
    
