print("__________wellcome to our task manager___________")
task = int(input(" how many task to be preformed :  "))
task_list = []

for i in range(1,task+1):
    task_name = input(f"Enter yuor {i} task :  ")
    task_list.append(task_name)
    
print(f" today task are:\n{task_list}")

while True:
    operator = int(input(":1-add\n:2-delet\n:3-view\n:4-update:\n5-exit\n"))
    if operator ==1:
        add_inp = input("enter task: ")
        task_list.append(add_inp)
    elif operator==2:
        del_val = input("which task do you want delete:")
        if del_val in task_list:
            ind = task_list.index(del_val)
            del task_list[ind]
            print(f"{del_val} is deleted...")
    elif operator == 3:
        print(task_list)
    elif operator==4:
        up_val =input("which task you update: ")
        if up_val in task_list:
            ind_up = task_list.index(up_val)
            nwe_task =input("enter update task: ")
            task_list[ind_up] = nwe_task
            print(f"{up_val} is updated: ")
    elif operator==5:
        print("progrma is close: ")
        break
    else:
        print("invalied input: ")

