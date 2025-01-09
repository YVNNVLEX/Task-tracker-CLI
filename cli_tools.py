import cmd, json, os
from datetime import datetime

file = open('listeTask.json','w')

class Task:
    def __init__(self, id=0, createdAt=datetime.now().date().strftime("%d/%m/%y"), updatedAt=datetime.now().date().strftime("%d/%m/%y"), description="", status="todo"):
        self.id = id
        self.description = description
        self.status = status
        self.createdAt = createdAt
        self.updatedAt = updatedAt
    def create(self):
        self.id += 1

class MyCLI(cmd.Cmd):
    prompt = "TaskRunner>> "
    intro = "Bienvenue dans le task tracker fait par me" 
    
    def do_add(self, arg):
        if (arg.strip()):
            newTask = Task()
            newTask.create()
            newTask.description = arg.strip()
            if os.path.isfile('./listeTask.json'):
                data_string = {"id":newTask.id, "description": newTask.description, "status":newTask.status, "createdAt": newTask.createdAt, "updatedAt": newTask.updatedAt}
                json.dump(data_string, file)
                print('La tache a bien été ajouté')
        else:
            print("ok")
        
    def do_list(self):
        if(os.path.isfile('./listTask.json')):
            f = open('listeTask.json','r')
            lines = f.readlines()
            if lines is None:
                print('Le fichier est vide')
            else:
                print("+++++++++++++++++++++++++++++++++++++++++++++++++++++")
                print("| id | description | status | createdAt | updatedAt |")
                print("+++++++++++++++++++++++++++++++++++++++++++++++++++++")
        
    def do_quit(self, line):
        return True

    
if __name__ == '__main__':
    MyCLI().cmdloop()
    
