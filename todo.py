from pywebio.input import *
from pywebio.output import *
from functools import partial


allTasks = []

def completed(task, allTasks):
    allTasks.remove(task)
    clear("scope1")
    with use_scope("scope1"):

        put_table(
                tdata=[
                    [
                    i, put_button(label="Complete", onclick=partial(completed, task=i, allTasks = allTasks ))
                ] for i in allTasks
                ]
            )
    
with use_scope("scope1"):

    while True:
        task = input(label = "Enter a task",placeholder = "Take a bath",required=True)
        allTasks.append(task)
        clear("scope1")
        put_table(
            tdata=[
                [
                i, put_button(label="Complete", onclick=partial(completed, task=i, allTasks = allTasks ))
            ] for i in allTasks
            ]
        )