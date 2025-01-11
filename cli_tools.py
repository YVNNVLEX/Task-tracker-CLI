import cmd, json, os, atexit
from datetime import datetime
      
class Task:
    
    idTask = 0
    
    def __init__(self, id=0, createdAt=datetime.now().date().strftime("%d/%m/%y"), updatedAt=datetime.now().date().strftime("%d/%m/%y"), description="", status="todo"):
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
                file = open("listeTask.json",'r')
                lines = json.load(file)
                if len(lines) != 0:
                    newTask = Task()
                    newTask.id = lines.index(lines[len(lines)-1])+1
                    newTask.description = arg.strip()
                    data_string = {"id":newTask.id, "description": newTask.description, "status":newTask.status, "createdAt": newTask.createdAt, "updatedAt": newTask.updatedAt}
                    lines.append(data_string)
                    with open("listeTask.json",'w') as f:
                        json.dump(lines,f,indent=4)
                    print(f'La tache a bien été ajouté: (ID:{newTask.id})')
                else:
                   newTask = Task()
                   newTask.create()
                   newTask.description = arg.strip()
                   data_string = {"id":newTask.id, "description": newTask.description, "status":newTask.status, "createdAt": newTask.createdAt, "updatedAt": newTask.updatedAt}
                   lines.append(data_string)
                   with open("listeTask.json",'w') as f:
                        json.dump(lines,f,indent=4)
                   print(f'La tache a bien été ajouté: (ID:{newTask.id})')
            else:
                newTask = Task()
                newTask.create()
                newTask.description = arg.strip()
                data_string = {"id":newTask.id, "description": newTask.description, "status":newTask.status, "createdAt": newTask.createdAt, "updatedAt": newTask.updatedAt}
                with open("listeTask.json",'w') as f:
                    json.dump(lines,f,indent=4)
                print(f'La tache a bien été ajouté: (ID:{newTask.id})')
                print(alltask)    
        else:
            print("Vous devez saisir comme suit: [id] [nouvelle tâche]")
        
    def do_delete(self, arg):
        if(arg.strip()):
            if os.path.isfile('./listeTask.json'):
                f = open('listeTask.json','r')
                lines = json.load(f)
                for task in lines:
                    if task["id"] == int(arg):
                        lines.pop(lines.index(task))
                        with open('listeTask.json','w') as f:
                            json.dump(lines,f, indent=4)
                    else:
                        continue
        else:
            print("Le fichier n'existe pas")
        
    def do_update(self, arg):
        if arg.strip():
            allArgs = arg.split(" ",1)
            print(allArgs)
            if len(allArgs) > 1 and len(allArgs)<3:
                for args in allArgs:
                    arg1 = allArgs[0]
                    arg2 = allArgs[1]
                f = open('listeTask.json','r')
                convertfile = json.load(f)
                for allTask in convertfile:
                    if allTask["id"] == int(arg1) :
                        allTask["description"] = arg2.strip()
                        newDate = datetime.now().date().strftime("%d/%m/%y")
                        data_string = {"id":allTask["id"], "description": allTask["description"], "status":allTask["status"], "createdAt": allTask["createdAt"], "updatedAt": newDate}
                        convertfile[convertfile.index(allTask)] = data_string
                        with open("listeTask.json",'w') as f:
                            json.dump(convertfile, f, indent=4)
                        print("La modification a été effectué")
                    else:
                        print(f"La tâche {arg1} n'existe pas \n Pour la créer entre la syntaxe suivante 'add [ajouter Tâche]'")
                        continue
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
     
    
    def do_todo(self,arg):
        if arg:
            file = open('listeTask.json','r')
            lines = json.load(file)    
            if len(lines) == 0:
                print("La liste ne contient aucune tâche")
            else:
                for task in lines:
                    if task["id"] == int(arg):
                        newDate = datetime.now().date().strftime("%d/%m/%y")
                        data_string = {"id":task["id"], "description": task["description"], "status":"todo", "createdAt": task["createdAt"], "updatedAt": newDate}
                        lines[lines.index(task)] = data_string
                        with open("listeTask.json","w") as f:
                            json.dump(lines,f,indent=4)
                        print(f"Le status de la tâche {arg} a été modifié a todo")
        else:
            print("Vous devez saisir comme suit: ' todo [id]'")
    
    def do_progress(self,arg):
        if arg:
            file = open('listeTask.json','r')
            lines = json.load(file)    
            if len(lines) == 0:
                print("La liste ne contient aucune tâche")
            else:
                for task in lines:
                    if task["id"] == int(arg):
                        newDate = datetime.now().date().strftime("%d/%m/%y")
                        data_string = {"id":task["id"], "description": task["description"], "status":"in-progress", "createdAt": task["createdAt"], "updatedAt": newDate}
                        lines[lines.index(task)] = data_string
                        with open("listeTask.json","w") as f:
                            json.dump(lines,f,indent=4)
                        print(f"Le status de la tâche {arg} a été modifié a in-progress")
        else:
            print("Vous devez saisir comme suit: ' progress [id]'")
     
    
    def do_done(self,arg):
        if arg:
            file = open('listeTask.json','r')
            lines = json.load(file)    
            if len(lines) == 0:
                print("La liste ne contient aucune tâche")
            else:
                for task in lines:
                    if task["id"] == int(arg):
                        newDate = datetime.now().date().strftime("%d/%m/%y")
                        data_string = {"id":task["id"], "description": task["description"], "status":"done", "createdAt": task["createdAt"], "updatedAt": newDate}
                        lines[lines.index(task)] = data_string
                        with open("listeTask.json","w") as f:
                            json.dump(lines,f,indent=4)
                        print(f"Le status de la tâche {arg} a été modifié a done")
        else:
            print("Vous devez saisir comme suit: ' done [id]'")
        
    def do_quit(self, line):
        choice = input("Voulez vous quittez ? Y/N: ")
        if choice == 'Y':
            print("A bientôt")
            return True
        elif choice == "N":
            print("Choisisser ajouter une tâche, modifier ou supprimer")
        else:
            print("Commande mal exécuté: entrer Y/N")

if __name__ == '__main__':
    MyCLI().cmdloop()
    
    
