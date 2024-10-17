def handle_task_commands(command, task_list):
    if "add" in command:
        task = command.split("add")[-1].strip()
        task_list.append(task)
        return f"Task '{task}' added to your list."
    
    elif "show" in command:
        if task_list:
            return "Your tasks are: " + ", ".join(task_list) + "."
        else:
            return "You have no tasks in your list."
    
    return "Command not recognized."
