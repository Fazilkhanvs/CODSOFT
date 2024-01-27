from tkinter import *
from tkinter import messagebox

def newTask():
    task = my_entry.get()
    if task != "":
        lb.insert(END, task)
        my_entry.delete(0, "end")
    else:
        messagebox.showwarning("warning", "Please enter some task.")

def deleteTask():
    lb.delete(ANCHOR)
    
ws = Tk()
ws.geometry('600x400+400+250')
ws.title('PythonGuides')
ws.config(bg='#DCF2F1')
ws.resizable(width=False, height=False)

frame = Frame(ws)
frame.pack(pady=10)

lb = Listbox(
    frame,
    width=35,
    height=4,
    font=('poppins small', 18),
    bd=0,
    fg='#0F0F0F',
    highlightthickness=0,
    selectbackground='#0F1035',
    activestyle="none",
    
)
lb.pack(side=LEFT, fill=BOTH)

task_list = []

for item in task_list:
    lb.insert(END, item)

sb = Scrollbar(frame)
sb.pack(side=RIGHT, fill=BOTH)

lb.config(yscrollcommand=sb.set)
sb.config(command=lb.yview)

my_entry = Entry(
    ws,
    font=('poppins small',20)
    )

my_entry.pack(pady=10)

button_frame = Frame(ws)
button_frame.pack(pady=10)

addTask_btn = Button(
    button_frame,
    text='Add Task',
    font=('times 14'),
    bg='#176B87',
    padx=10,
    pady=10,
    command=newTask
)
addTask_btn.pack(fill=BOTH, expand=True, side=LEFT)

delTask_btn = Button(
    button_frame,
    text='Delete Task',
    font=('times 14'),
    bg='#365486',
    padx=20,
    pady=10,
    command=deleteTask
    
)
delTask_btn.pack(fill=BOTH, expand=True, side=LEFT)


ws.mainloop()
