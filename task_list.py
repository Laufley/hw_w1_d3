tasks = [
    { "description": "Wash Dishes", "completed": False, "time_taken": 10 },
    { "description": "Clean Windows", "completed": False, "time_taken": 15 },
    { "description": "Make Dinner", "completed": True, "time_taken": 30 },
    { "description": "Feed Cat", "completed": False, "time_taken": 5 },
    { "description": "Walk Dog", "completed": True, "time_taken": 60 },
]


# 1. Print a list of uncompleted tasks

# PSEUDOCODE:
# loop through all the tasks 
# check their completed status
# if they are not completed aka False
# return the name of the task

def get_uncompleted_tasks(list_of_tasks): #adding the parameter cos I want to make it reusable
    uncompleted = []
    for task in list_of_tasks:
        if task["completed"] == False:
            uncompleted.append(task["description"])
    print("HEY HEY! Duck reminder - Aren't you forgetting something?")        
    return(uncompleted)

print(get_uncompleted_tasks(tasks))

# Feedback: it took me over an hour to figure a few errors. One of them was that I wrote the return inside the if conditional, so it was only returning one value. Gods.
# added print with a fancy intro message cause this exercise deserved it

# 2. Print a list of completed tasks

def completed_tasks(list_of_tasks):
    super_done = []
    for task in list_of_tasks:
        if task["completed"] == True:
            super_done.append(task["description"])
    print("OMG so proud of you for doing:")
    return(super_done)

print(completed_tasks())

# 3. Print a list of all task descriptions

# PSEUDOCODE
# loop through the array
# find the task names aka descriptions
# add them to a list to print them

def to_do_list(list_of_tasks):
    pending_tasks = []
    for task in list_of_tasks:
        pending_tasks.append(task["description"])
    print("when life gives you lemons... don't forget to do your chores:")
    return(pending_tasks)

print(to_do_list())

 # 4. Print a list of tasks where time_taken is at least a given time

# make a f(x) declaring a parameter where we'll put "X time" argument to compare with tasks when we call f(x)
# loop through all the tasks
# find the time for every task
# compare the parameter/argument to the time found on every task
# if they are >= the parameter, return the name of the task aka description


def done_in_expected_time(list_of_tasks):
    list_of_chores = []
    for task in list_of_tasks:
        task["time_taken"]
        if task["time_taken"] >= time:
            list_of_chores.append(task["description"])
    print("Acknowledged. Here are the tasks matching your time stamp:")
    return(list_of_chores)

print(done_in_expected_time(60))

# Hit a wall here because it only returned "Walk Dog" all the time... 
# 20 min later - update: Solved. I just realized I had added the list within the for loop. Gods.


# 5. Print any task with a given description

# define a function with a paramenter for the future argument
# loop away to check on every task
# compare the argument with the description of the task
# print the whole task array

def task_checker(list_of_tasks):
    for task in list_of_tasks:
        if task["description"] == name:
            return(f"Yes! your {task['description']} task")

print(task_checker("Walk Dog")) 

# f