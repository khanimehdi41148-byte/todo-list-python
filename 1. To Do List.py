import csv

#Represents a single task 
class Task:
    
# Initialize a new task.
    def __init__(self, name, description, priority):
        self.name = name
        self.description = description
        self.priority = priority
        
# Return a readable string representation of the task.
    def __str__(self):
        return f"name: {self.name} | description: {self.description} | priority: {self.priority}"
    
# Manages all tasks and file operations.
class TodoList:
    def __init__(self, filename="task.csv"):
        self.filename = filename
        self.tasks = []
        
    # Add a new task to the list.
    def add_task(self, task):
        self.tasks.append(task)

    # Remove a task by its displayed number.
    def remove_task(self, index):
        try:
            index = int(index) -1
        except ValueError:
            print("invalid syntax")
            return
        
        if 0 <= index < len(self.tasks):
            removed = self.tasks.pop(index)
            print(f"deleted {removed.name}")
        else:
            print("not found task")

    # Display all tasks.
    def show_tasks(self):
        if not self.tasks:
            print("task list is empty")
            return
        print("task list: ")
        for i, task in enumerate(self.tasks, start=1):
            print(f"{i}. {task}")

    # Save all tasks to a CSV file.
    def save_tasks(self):
        with open(self.filename, "w", newline="", encoding = "utf-8") as file:
            writer = csv.writer(file)
            
            writer.writerow(["name", "description", "priority"])
            
            for task in self.tasks:
                writer.writerow(
                    [task.name, task.description, task.priority]
                    )
                
    # Load tasks from a CSV file.
    def load_tasks(self):
        try:
            
            with open(self.filename, "r", encoding="utf-8") as file:
                reader = csv.reader(file)
                
                next(reader, None)                
                self.tasks.clear()
                for row in reader:
                    if len(row) == 3:
                        task = Task(row[0], row[1], row[2])
                        self.tasks.append(task)
        except FileNotFoundError:
            pass

# Main program
def main():
    todo = TodoList()
    todo.load_tasks()
    
    # Display the menu until the user exits.
    while True:
        print("\n==== managing work ====")
        print("1. add task")
        print("2. remove task")
        print("3. show tasks")
        print("4. exit")
        choice = input("choose an option: ")
        
        if choice == "1":
            name = input("name of task: ")
            description = input("description: ")
            priority = input("priority(low / medium / high): ")
            task = Task(name, description, priority)
            todo.add_task(task)
            print("work added")
    
            
        elif  choice == "2":
            todo.show_tasks()
            try:
                number = int(input("number of work for removing: "))
                todo.remove_task(number)
            except ValueError:
                print("please enter a number.")
        elif choice  == "3":
            todo.show_tasks()
        elif choice == "4":
            print("exit the program...")
            print("saving task")
            todo.save_tasks()
            break
        else:
            print("invalid choice.")
if __name__ == "__main__":
    main()
    
    
    