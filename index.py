import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

class file:
    def __init__(self):
        self.filename = 'C:/Users/TUF/Documents/Coding Practice/DIT102/Final Project/agents.csv'
        self.agent_list = []
        self.load_agents()

    def load_agents(self):
        try:
            with open(self.filename, 'r') as file:
                lines = file.readlines()
                headers = lines[0].strip().split(',')
                for line in lines[1:]:
                    data = line.strip().split(',')
                    agent_info = {}
                    col_index = 0
                    for head in headers:
                        agent_info[head] = data[col_index]
                        col_index += 1
                    self.agent_list.append(agent_info)
        except FileNotFoundError:
            print("File not found.")

    def reload_agents(self):
        self.agent_list.clear()
        self.rearrange_file()
        self.load_agents()

    def rewrite(self, name, new_info):
        if new_info is None:
            return
        else:
            updated = False
            with open(self.filename, 'r') as file:
                lines = file.readlines()
            with open(self.filename, 'w') as file:
                for line in lines:
                    agent_info_data = line.strip().split(',')
                    if agent_info_data[1] == name:
                        file.write(new_info + '\n')
                        updated = True
                    else:
                        file.write(line)
                if updated:
                    print('')
                    print("Edited Successfully")
                else:
                    print('')
                    print("Agent not found")
    
    def rearrange_file(self):
        with open(self.filename, 'r') as file:
            lines = file.readlines()
        non_blank_lines = [line for line in lines if line.strip()]
        with open(self.filename, 'w') as file:
            file.writelines(non_blank_lines)

class display(file):
    def __init__(self):
        super().__init__()

    def list(self):
        self.reload_agents()
        list_window = tk.Toplevel()
        list_window.title("Option 1: Display All The Agents")
        list_window.geometry('1080x500')

        text = tk.Text(list_window, wrap='none', font=("Courier New", 10))
        text.pack(expand=True, fill='both')
        text.insert(tk.END, "\nOption 1: Display All the Agents\n\n")
        text.insert(tk.END, f"{'No.':<12s}{'Codename':<19s}{'Full Name':<19s}{'Class':<10s}{'Age':<8s}{'Ethnicity':<19s}{'Role':<19s}{'Ult Points':<16s}{'Pick Rate':<19s}\n")
        for agent in self.agent_list:
            text.insert(tk.END, f"{agent['Agent Number']:<12s}{agent['Codename']:<19s}{agent['Full name']:<19s}{agent['Class']:<10s}{agent['Age']:<8s}{agent['Ethnicity']:<19s}{agent['Role']:<19s}{agent['Ult Points']:<16s}{agent['Pick Rate']:<19s}\n")
        text.config(state=tk.DISABLED)
        close_button = tk.Button(list_window, text="Close", command=list_window.destroy)
        close_button.pack(pady=10)

    def total(self):
        self.reload_agents()
        list_window = tk.Toplevel()
        list_window.title("Option 2: Display The Total Number of Agents")
        count = 0
        for agent in self.agent_list:
            count += 1
        text = tk.Text(list_window, wrap='none', font=("Courier New", 10))
        text.pack(expand=True, fill='both')
        text.insert(tk.END,f'Total Number: {count}')
        text.config(state=tk.DISABLED)
        close_button = tk.Button(list_window, text="Close", command=list_window.destroy)
        close_button.pack(pady=10)

class search(file):
    def __init__(self):
        super().__init__()

    def agentno(self):
        self.reload_agents()
        input_window = tk.Toplevel()

        num = tk.StringVar()

        def create_row(parent, text, variable):
            frame = tk.Frame(parent)
            frame.pack(padx=10, pady=5, fill='x')
            label = tk.Label(frame, text=text)
            label.pack(side=tk.LEFT)
            entry = tk.Entry(frame, textvariable=variable)
            entry.pack(side=tk.LEFT, padx=5, fill='x', expand=True)

        create_row(input_window,"Agent No.",num)

        def display_agent_list():
            agent_num = num.get()

            if (not agent_num):
                messagebox.showerror("Input Error", "Please fill out all fields.")
            else:
                list_window = tk.Toplevel()
                list_window.title("Agent List")
                list_window.geometry('1080x500')

                text = tk.Text(list_window, wrap='none', font=("Courier New", 10))
                text.pack(expand=True, fill='both')
                text.insert(tk.END, f"{'No.':<12s}{'Codename':<19s}{'Full Name':<19s}{'Class':<10s}{'Age':<8s}{'Ethnicity':<19s}{'Role':<19s}{'Ult Points':<16s}{'Pick Rate':<19s}\n")
                for agent in self.agent_list:
                    if agent['Agent Number'] == agent_num:
                        text.insert(tk.END, f"{agent['Agent Number']:<12s}{agent['Codename']:<19s}{agent['Full name']:<19s}{agent['Class']:<10s}{agent['Age']:<8s}{agent['Ethnicity']:<19s}{agent['Role']:<19s}{agent['Ult Points']:<16s}{agent['Pick Rate']:<19s}\n")
                text.config(state=tk.DISABLED)
                close_button = tk.Button(list_window, text="Close", command=list_window.destroy)
                close_button.pack(pady=10)
        
        def cancel_form():
            input_window.destroy()

        def display_and_close():
            display_agent_list()
            cancel_form()

        submit_button = tk.Button(input_window, text="Confirm", command=display_and_close)
        submit_button.pack(pady=10)
    
    def codename(self):
        self.reload_agents()
        input_window = tk.Toplevel()

        codename = tk.StringVar()

        def create_row(parent, text, variable):
            frame = tk.Frame(parent)
            frame.pack(padx=10, pady=5, fill='x')
            label = tk.Label(frame, text=text)
            label.pack(side=tk.LEFT)
            entry = tk.Entry(frame, textvariable=variable)
            entry.pack(side=tk.LEFT, padx=5, fill='x', expand=True)

        create_row(input_window,"Agent Codename",codename)

        def display_agent_list():
            agent_code_name = codename.get()

            if (not agent_code_name):
                messagebox.showerror("Input Error", "Please fill out all fields.")
            else:
                list_window = tk.Toplevel()
                list_window.title("Agent List")
                list_window.geometry('1080x500')

                text = tk.Text(list_window, wrap='none', font=("Courier New", 10))
                text.pack(expand=True, fill='both')
                text.insert(tk.END, f"{'No.':<12s}{'Codename':<19s}{'Full Name':<19s}{'Class':<10s}{'Age':<8s}{'Ethnicity':<19s}{'Role':<19s}{'Ult Points':<16s}{'Pick Rate':<19s}\n")
                for agent in self.agent_list:
                    if agent['Codename'] == agent_code_name:
                        text.insert(tk.END, f"{agent['Agent Number']:<12s}{agent['Codename']:<19s}{agent['Full name']:<19s}{agent['Class']:<10s}{agent['Age']:<8s}{agent['Ethnicity']:<19s}{agent['Role']:<19s}{agent['Ult Points']:<16s}{agent['Pick Rate']:<19s}\n")
                text.config(state=tk.DISABLED)
                close_button = tk.Button(list_window, text="Close", command=list_window.destroy)
                close_button.pack(pady=10)
        
        def cancel_form():
            input_window.destroy()

        def display_and_close():
            display_agent_list()
            cancel_form()

        submit_button = tk.Button(input_window, text="Confirm", command=display_and_close)
        submit_button.pack(pady=10)
    
    def fullname(self):
        self.reload_agents()
        input_window = tk.Toplevel()

        fullname = tk.StringVar()

        def create_row(parent, text, variable):
            frame = tk.Frame(parent)
            frame.pack(padx=10, pady=5, fill='x')
            label = tk.Label(frame, text=text)
            label.pack(side=tk.LEFT)
            entry = tk.Entry(frame, textvariable=variable)
            entry.pack(side=tk.LEFT, padx=5, fill='x', expand=True)

        create_row(input_window,"Agent Full name",fullname)

        def display_agent_list():
            agent_full_name = fullname.get()

            if (not agent_full_name):
                messagebox.showerror("Input Error", "Please fill out all fields.")
            else:
                list_window = tk.Toplevel()
                list_window.title("Agent List")
                list_window.geometry('1080x500')

                text = tk.Text(list_window, wrap='none', font=("Courier New", 10))
                text.pack(expand=True, fill='both')
                text.insert(tk.END, f"{'No.':<12s}{'Codename':<19s}{'Full Name':<19s}{'Class':<10s}{'Age':<8s}{'Ethnicity':<19s}{'Role':<19s}{'Ult Points':<16s}{'Pick Rate':<19s}\n")
                for agent in self.agent_list:
                    if agent['Full name'] == agent_full_name:
                        text.insert(tk.END, f"{agent['Agent Number']:<12s}{agent['Codename']:<19s}{agent['Full name']:<19s}{agent['Class']:<10s}{agent['Age']:<8s}{agent['Ethnicity']:<19s}{agent['Role']:<19s}{agent['Ult Points']:<16s}{agent['Pick Rate']:<19s}\n")
                text.config(state=tk.DISABLED)
                close_button = tk.Button(list_window, text="Close", command=list_window.destroy)
                close_button.pack(pady=10)
        
        def cancel_form():
            input_window.destroy()

        def display_and_close():
            display_agent_list()
            cancel_form()

        submit_button = tk.Button(input_window, text="Confirm", command=display_and_close)
        submit_button.pack(pady=10)

    def Class(self):
        self.reload_agents()
        input_window = tk.Toplevel()

        agent_class = tk.StringVar()

        def create_row(parent, text, variable):
            frame = tk.Frame(parent)
            frame.pack(padx=10, pady=5, fill='x')
            label = tk.Label(frame, text=text)
            label.pack(side=tk.LEFT)
            entry = tk.Entry(frame, textvariable=variable)
            entry.pack(side=tk.LEFT, padx=5, fill='x', expand=True)

        create_row(input_window,"Agent Class",agent_class)

        def display_agent_list():
            agent_species = agent_class.get()

            if (not agent_species):
                messagebox.showerror("Input Error", "Please fill out all fields.")
            else:
                list_window = tk.Toplevel()
                list_window.title("Agent List")
                list_window.geometry('1080x500')

                text = tk.Text(list_window, wrap='none', font=("Courier New", 10))
                text.pack(expand=True, fill='both')
                text.insert(tk.END, f"{'No.':<12s}{'Codename':<19s}{'Full Name':<19s}{'Class':<10s}{'Age':<8s}{'Ethnicity':<19s}{'Role':<19s}{'Ult Points':<16s}{'Pick Rate':<19s}\n")
                for agent in self.agent_list:
                    if agent['Class'] == agent_species:
                        text.insert(tk.END, f"{agent['Agent Number']:<12s}{agent['Codename']:<19s}{agent['Full name']:<19s}{agent['Class']:<10s}{agent['Age']:<8s}{agent['Ethnicity']:<19s}{agent['Role']:<19s}{agent['Ult Points']:<16s}{agent['Pick Rate']:<19s}\n")
                text.config(state=tk.DISABLED)
                close_button = tk.Button(list_window, text="Close", command=list_window.destroy)
                close_button.pack(pady=10)
        
        def cancel_form():
            input_window.destroy()

        def display_and_close():
            display_agent_list()
            cancel_form()

        submit_button = tk.Button(input_window, text="Confirm", command=display_and_close)
        submit_button.pack(pady=10)

    def age(self):
        self.reload_agents()
        input_window = tk.Toplevel()

        age = tk.StringVar()

        def create_row(parent, text, variable):
            frame = tk.Frame(parent)
            frame.pack(padx=10, pady=5, fill='x')
            label = tk.Label(frame, text=text)
            label.pack(side=tk.LEFT)
            entry = tk.Entry(frame, textvariable=variable)
            entry.pack(side=tk.LEFT, padx=5, fill='x', expand=True)

        create_row(input_window,"Agent Age",age)

        def display_agent_list():
            agent_age = age.get()

            if (not agent_age):
                messagebox.showerror("Input Error", "Please fill out all fields.")
            else:
                list_window = tk.Toplevel()
                list_window.title("Agent List")
                list_window.geometry('1080x500')

                text = tk.Text(list_window, wrap='none', font=("Courier New", 10))
                text.pack(expand=True, fill='both')
                text.insert(tk.END, f"{'No.':<12s}{'Codename':<19s}{'Full Name':<19s}{'Class':<10s}{'Age':<8s}{'Ethnicity':<19s}{'Role':<19s}{'Ult Points':<16s}{'Pick Rate':<19s}\n")
                for agent in self.agent_list:
                    if agent['Age'] == agent_age:
                        text.insert(tk.END, f"{agent['Agent Number']:<12s}{agent['Codename']:<19s}{agent['Full name']:<19s}{agent['Class']:<10s}{agent['Age']:<8s}{agent['Ethnicity']:<19s}{agent['Role']:<19s}{agent['Ult Points']:<16s}{agent['Pick Rate']:<19s}\n")
                text.config(state=tk.DISABLED)
                close_button = tk.Button(list_window, text="Close", command=list_window.destroy)
                close_button.pack(pady=10)
        
        def cancel_form():
            input_window.destroy()

        def display_and_close():
            display_agent_list()
            cancel_form()

        submit_button = tk.Button(input_window, text="Confirm", command=display_and_close)
        submit_button.pack(pady=10)

    def ethnicity(self):
        self.reload_agents()
        input_window = tk.Toplevel()

        race = tk.StringVar()

        def create_row(parent, text, variable):
            frame = tk.Frame(parent)
            frame.pack(padx=10, pady=5, fill='x')
            label = tk.Label(frame, text=text)
            label.pack(side=tk.LEFT)
            entry = tk.Entry(frame, textvariable=variable)
            entry.pack(side=tk.LEFT, padx=5, fill='x', expand=True)

        create_row(input_window,"Agent Ethnicity",race)

        def display_agent_list():
            agent_race = race.get()

            if (not agent_race):
                messagebox.showerror("Input Error", "Please fill out all fields.")
            else:
                list_window = tk.Toplevel()
                list_window.title("Agent List")
                list_window.geometry('1080x500')

                text = tk.Text(list_window, wrap='none', font=("Courier New", 10))
                text.pack(expand=True, fill='both')
                text.insert(tk.END, f"{'No.':<12s}{'Codename':<19s}{'Full Name':<19s}{'Class':<10s}{'Age':<8s}{'Ethnicity':<19s}{'Role':<19s}{'Ult Points':<16s}{'Pick Rate':<19s}\n")
                for agent in self.agent_list:
                    if agent['Ethnicity'] == agent_race:
                        text.insert(tk.END, f"{agent['Agent Number']:<12s}{agent['Codename']:<19s}{agent['Full name']:<19s}{agent['Class']:<10s}{agent['Age']:<8s}{agent['Ethnicity']:<19s}{agent['Role']:<19s}{agent['Ult Points']:<16s}{agent['Pick Rate']:<19s}\n")
                text.config(state=tk.DISABLED)
                close_button = tk.Button(list_window, text="Close", command=list_window.destroy)
                close_button.pack(pady=10)
        
        def cancel_form():
            input_window.destroy()

        def display_and_close():
            display_agent_list()
            cancel_form()

        submit_button = tk.Button(input_window, text="Confirm", command=display_and_close)
        submit_button.pack(pady=10)

    def role(self):
        self.reload_agents()
        input_window = tk.Toplevel()

        role = tk.StringVar()

        def create_row(parent, text, variable):
            frame = tk.Frame(parent)
            frame.pack(padx=10, pady=5, fill='x')
            label = tk.Label(frame, text=text)
            label.pack(side=tk.LEFT)
            entry = tk.Entry(frame, textvariable=variable)
            entry.pack(side=tk.LEFT, padx=5, fill='x', expand=True)

        create_row(input_window,"Agent Role",role)

        def display_agent_list():
            agent_role = role.get()

            if (not agent_role):
                messagebox.showerror("Input Error", "Please fill out all fields.")
            else:
                list_window = tk.Toplevel()
                list_window.title("Agent List")
                list_window.geometry('1080x500')

                text = tk.Text(list_window, wrap='none', font=("Courier New", 10))
                text.pack(expand=True, fill='both')
                text.insert(tk.END, f"{'No.':<12s}{'Codename':<19s}{'Full Name':<19s}{'Class':<10s}{'Age':<8s}{'Ethnicity':<19s}{'Role':<19s}{'Ult Points':<16s}{'Pick Rate':<19s}\n")
                for agent in self.agent_list:
                    if agent['Role'] == agent_role:
                        text.insert(tk.END, f"{agent['Agent Number']:<12s}{agent['Codename']:<19s}{agent['Full name']:<19s}{agent['Class']:<10s}{agent['Age']:<8s}{agent['Ethnicity']:<19s}{agent['Role']:<19s}{agent['Ult Points']:<16s}{agent['Pick Rate']:<19s}\n")
                text.config(state=tk.DISABLED)
                close_button = tk.Button(list_window, text="Close", command=list_window.destroy)
                close_button.pack(pady=10)
        
        def cancel_form():
            input_window.destroy()

        def display_and_close():
            display_agent_list()
            cancel_form()

        submit_button = tk.Button(input_window, text="Confirm", command=display_and_close)
        submit_button.pack(pady=10)

    def ultpoint(self):
        self.reload_agents()
        input_window = tk.Toplevel()

        points = tk.StringVar()

        def create_row(parent, text, variable):
            frame = tk.Frame(parent)
            frame.pack(padx=10, pady=5, fill='x')
            label = tk.Label(frame, text=text)
            label.pack(side=tk.LEFT)
            entry = tk.Entry(frame, textvariable=variable)
            entry.pack(side=tk.LEFT, padx=5, fill='x', expand=True)

        create_row(input_window,"Agent Role",points)

        def display_agent_list():
            agent_points = points.get()

            if (not agent_points):
                messagebox.showerror("Input Error", "Please fill out all fields.")
            else:
                list_window = tk.Toplevel()
                list_window.title("Agent List")
                list_window.geometry('1080x500')

                text = tk.Text(list_window, wrap='none', font=("Courier New", 10))
                text.pack(expand=True, fill='both')
                text.insert(tk.END, f"{'No.':<12s}{'Codename':<19s}{'Full Name':<19s}{'Class':<10s}{'Age':<8s}{'Ethnicity':<19s}{'Role':<19s}{'Ult Points':<16s}{'Pick Rate':<19s}\n")
                for agent in self.agent_list:
                    if agent['Ult Points'] == agent_points:
                        text.insert(tk.END, f"{agent['Agent Number']:<12s}{agent['Codename']:<19s}{agent['Full name']:<19s}{agent['Class']:<10s}{agent['Age']:<8s}{agent['Ethnicity']:<19s}{agent['Role']:<19s}{agent['Ult Points']:<16s}{agent['Pick Rate']:<19s}\n")
                text.config(state=tk.DISABLED)
                close_button = tk.Button(list_window, text="Close", command=list_window.destroy)
                close_button.pack(pady=10)
        
        def cancel_form():
            input_window.destroy()

        def display_and_close():
            display_agent_list()
            cancel_form()

        submit_button = tk.Button(input_window, text="Confirm", command=display_and_close)
        submit_button.pack(pady=10)

    def pickrate(self):
        self.reload_agents()
        input_window = tk.Toplevel()

        pickrate = tk.StringVar()

        def create_row(parent, text, variable):
            frame = tk.Frame(parent)
            frame.pack(padx=10, pady=5, fill='x')
            label = tk.Label(frame, text=text)
            label.pack(side=tk.LEFT)
            entry = tk.Entry(frame, textvariable=variable)
            entry.pack(side=tk.LEFT, padx=5, fill='x', expand=True)

        create_row(input_window,"Agent Pick Rate",pickrate)

        def display_agent_list():
            agent_rate = pickrate.get() + '%'

            if (not agent_rate):
                messagebox.showerror("Input Error", "Please fill out all fields.")
            else:
                list_window = tk.Toplevel()
                list_window.title("Agent List")
                list_window.geometry('1080x500')

                text = tk.Text(list_window, wrap='none', font=("Courier New", 10))
                text.pack(expand=True, fill='both')
                text.insert(tk.END, f"{'No.':<12s}{'Codename':<19s}{'Full Name':<19s}{'Class':<10s}{'Age':<8s}{'Ethnicity':<19s}{'Role':<19s}{'Ult Points':<16s}{'Pick Rate':<19s}\n")
                for agent in self.agent_list:
                    if agent['Pick Rate'] == agent_rate:
                        text.insert(tk.END, f"{agent['Agent Number']:<12s}{agent['Codename']:<19s}{agent['Full name']:<19s}{agent['Class']:<10s}{agent['Age']:<8s}{agent['Ethnicity']:<19s}{agent['Role']:<19s}{agent['Ult Points']:<16s}{agent['Pick Rate']:<19s}\n")
                text.config(state=tk.DISABLED)
                close_button = tk.Button(list_window, text="Close", command=list_window.destroy)
                close_button.pack(pady=10)
        
        def cancel_form():
            input_window.destroy()

        def display_and_close():
            display_agent_list()
            cancel_form()

        submit_button = tk.Button(input_window, text="Confirm", command=display_and_close)
        submit_button.pack(pady=10)

class delete(file):
    def __init__(self):
        super().__init__()

    def del_agent(self):
        self.reload_agents()
        input_window = tk.Toplevel()
        input_window.title('Option 5: Delete Agent Information')

        name = tk.StringVar()

        def create_row(parent, text, variable):
            frame = tk.Frame(parent)
            frame.pack(padx=10, pady=5, fill='x')
            label = tk.Label(frame, text=text)
            label.pack(side=tk.LEFT)
            entry = tk.Entry(frame, textvariable=variable)
            entry.pack(side=tk.LEFT, padx=5, fill='x', expand=True)

        create_row(input_window,"Agent Codename",name)

        def display_agent_list():
            agent_name = name.get()

            if (not agent_name):
                messagebox.showerror("Input Error", "Please fill out all fields.")
            else:
                list_window = tk.Toplevel()
                list_window.title("Agent List")
                list_window.geometry('1080x500')

                text = tk.Text(list_window, wrap='none', font=("Courier New", 10))
                text.pack(expand=True, fill='both')
                text.insert(tk.END, f"{'No.':<12s}{'Codename':<19s}{'Full Name':<19s}{'Class':<10s}{'Age':<8s}{'Ethnicity':<19s}{'Role':<19s}{'Ult Points':<16s}{'Pick Rate':<19s}\n")
                for agent in self.agent_list:
                    if agent['Codename'] == agent_name:
                        text.insert(tk.END, f"{agent['Agent Number']:<12s}{agent['Codename']:<19s}{agent['Full name']:<19s}{agent['Class']:<10s}{agent['Age']:<8s}{agent['Ethnicity']:<19s}{agent['Role']:<19s}{agent['Ult Points']:<16s}{agent['Pick Rate']:<19s}\n")
                text.config(state=tk.DISABLED)

                def close_window():
                    list_window.destroy()

                def confirm_and_close():
                    confirm_function()
                    close_window()

                frame = tk.Frame(list_window)
                frame.pack(padx=10, pady=5)
                confirm_button = tk.Button(frame, text="Confirm", command=confirm_and_close)
                confirm_button.pack(side=tk.LEFT, padx=5)
                cancel_button = tk.Button(frame, text="Cancel", command=list_window.destroy)
                cancel_button.pack(side=tk.LEFT, padx=5)
                frame.pack(anchor='center')

        
        def cancel_form():
            input_window.destroy()

        def display_and_close():
            display_agent_list()
            cancel_form()

        submit_button = tk.Button(input_window, text="Confirm", command=display_and_close)
        submit_button.pack(pady=10)

        def confirm_function():
            agent_name = name.get()

            update = False
            with open(self.filename, 'r') as file:
                lines = file.readlines()
            with open(self.filename, 'w') as file:
                for line in lines:
                    agentdata = line.strip().split(',')
                    if agentdata[1] == agent_name:
                        file.write('')
                        update = True
                    else:
                        file.write(line)
            if update: 
                messagebox.showinfo("Confirmation", "Agent Deleted Successfully")
            else:
                messagebox.showerror("Error","Agent Not Found")

class edit(file):
    def __init__(self):
        super().__init__()
        self.new_info = None

    def agentno(self, name):
        self.reload_agents
        input_window = tk.Toplevel()
        input_window.title("")

        num = tk.StringVar()

        def create_row(parent, text, variable):
            frame = tk.Frame(parent)
            frame.pack(padx=10, pady=5, fill='x')
            label = tk.Label(frame, text=text)
            label.pack(side=tk.LEFT)
            entry = tk.Entry(frame, textvariable=variable)
            entry.pack(side=tk.LEFT, padx=5, fill='x', expand=True)
        
        create_row(input_window,"New Agent No.", num)

        def confirm_function():
            new_num = num.get()

            if not new_num:
                messagebox.showerror("Input Error", "Please fill out all fields.")
                return
            
            updated_info = []
            new_agent_info = None
            for agent in self.agent_list:
                if agent['Codename'] == name:
                    updated_info.append(f"{new_num:<12s}{agent['Codename']:<19s}{agent['Full name']:<19s}{agent['Class']:<10s}{agent['Age']:<8s}{agent['Ethnicity']:<19s}{agent['Role']:<19s}{agent['Ult Points']:<16s}{agent['Pick Rate']:<19s}")
                    new_agent_info = f"{new_num},{agent['Codename']},{agent['Full name']},{agent['Class']},{agent['Age']},{agent['Ethnicity']},{agent['Role']},{agent['Ult Points']},{agent['Pick Rate']}"

            if new_agent_info is None:
                messagebox.showerror("Error", "Agent not found.")
                return

            update_window = tk.Toplevel()
            update_window.title("Updated List")
            update_window.geometry("1080x500")

            text = tk.Text(update_window, wrap='none', font=("Courier New", 10))
            text.pack(expand=True, fill='both')
            text.insert(tk.END, f"{'No.':<12s}{'Codename':<19s}{'Full Name':<19s}{'Class':<10s}{'Age':<8s}{'Ethnicity':<19s}{'Role':<19s}{'Ult Points':<16s}{'Pick Rate':<19s}\n")
            for info in updated_info:
                text.insert(tk.END, info + "\n")
            text.config(state=tk.DISABLED)

            def confirm_upd_win():
                self.new_info = new_agent_info
                self.rewrite(name, self.new_info)
                messagebox.showinfo("Confirmation", "Agent No. updated successfully.")

            def close_upd_win():
                update_window.destroy()

            def confirm_close():
                confirm_upd_win()
                close_upd_win()

            frame = tk.Frame(update_window)
            frame.pack(padx=10, pady=5)
            confirm_button = tk.Button(frame, text="Confirm", command=confirm_close)
            confirm_button.pack(side=tk.LEFT, padx=5)
            cancel_button = tk.Button(frame, text="Cancel", command=update_window.destroy)
            cancel_button.pack(side=tk.LEFT, padx=5)
            frame.pack(anchor='center')

        def close_window():
            input_window.destroy()

        def confirm_and_close():
            confirm_function()
            close_window()

        frame = tk.Frame(input_window)
        frame.pack(padx=10, pady=5)
        confirm_button = tk.Button(frame, text="Confirm", command=confirm_and_close)
        confirm_button.pack(side=tk.LEFT, padx=5)
        cancel_button = tk.Button(frame, text="Cancel", command=input_window.destroy)
        cancel_button.pack(side=tk.LEFT, padx=5)
        frame.pack(anchor='center')

    def agentcodename(self, name):
        self.reload_agents
        input_window = tk.Toplevel()
        input_window.title("")

        codename = tk.StringVar()

        def create_row(parent, text, variable):
            frame = tk.Frame(parent)
            frame.pack(padx=10, pady=5, fill='x')
            label = tk.Label(frame, text=text)
            label.pack(side=tk.LEFT)
            entry = tk.Entry(frame, textvariable=variable)
            entry.pack(side=tk.LEFT, padx=5, fill='x', expand=True)
        
        create_row(input_window,"New Agent Codename", codename)

        def confirm_function():
            new_codename = codename.get()

            if not new_codename:
                messagebox.showerror("Input Error", "Please fill out all fields.")
                return
            
            updated_info = []
            new_agent_info = None
            for agent in self.agent_list:
                if agent['Codename'] == name:
                    updated_info.append(f"{agent['Agent Number']:<12s}{new_codename:<19s}{agent['Full name']:<19s}{agent['Class']:<10s}{agent['Age']:<8s}{agent['Ethnicity']:<19s}{agent['Role']:<19s}{agent['Ult Points']:<16s}{agent['Pick Rate']:<19s}")
                    new_agent_info = f"{agent['Agent Number']},{new_codename},{agent['Full name']},{agent['Class']},{agent['Age']},{agent['Ethnicity']},{agent['Role']},{agent['Ult Points']},{agent['Pick Rate']}"

            if new_agent_info is None:
                messagebox.showerror("Error", "Agent not found.")
                return

            update_window = tk.Toplevel()
            update_window.title("Updated List")
            update_window.geometry("1080x500")

            text = tk.Text(update_window, wrap='none', font=("Courier New", 10))
            text.pack(expand=True, fill='both')
            text.insert(tk.END, f"{'No.':<12s}{'Codename':<19s}{'Full Name':<19s}{'Class':<10s}{'Age':<8s}{'Ethnicity':<19s}{'Role':<19s}{'Ult Points':<16s}{'Pick Rate':<19s}\n")
            for info in updated_info:
                text.insert(tk.END, info + "\n")
            text.config(state=tk.DISABLED)

            def confirm_upd_win():
                self.new_info = new_agent_info
                self.rewrite(name, self.new_info)
                messagebox.showinfo("Confirmation", "Codename updated successfully.")

            def close_upd_win():
                update_window.destroy()

            def confirm_close():
                confirm_upd_win()
                close_upd_win()

            frame = tk.Frame(update_window)
            frame.pack(padx=10, pady=5)
            confirm_button = tk.Button(frame, text="Confirm", command=confirm_close)
            confirm_button.pack(side=tk.LEFT, padx=5)
            cancel_button = tk.Button(frame, text="Cancel", command=update_window.destroy)
            cancel_button.pack(side=tk.LEFT, padx=5)
            frame.pack(anchor='center')

        def close_window():
            input_window.destroy()

        def confirm_and_close():
            confirm_function()
            close_window()

        frame = tk.Frame(input_window)
        frame.pack(padx=10, pady=5)
        confirm_button = tk.Button(frame, text="Confirm", command=confirm_and_close)
        confirm_button.pack(side=tk.LEFT, padx=5)
        cancel_button = tk.Button(frame, text="Cancel", command=input_window.destroy)
        cancel_button.pack(side=tk.LEFT, padx=5)
        frame.pack(anchor='center')

    def agentfullname(self, name):
        self.reload_agents
        input_window = tk.Toplevel()
        input_window.title("")

        fullname = tk.StringVar()

        def create_row(parent, text, variable):
            frame = tk.Frame(parent)
            frame.pack(padx=10, pady=5, fill='x')
            label = tk.Label(frame, text=text)
            label.pack(side=tk.LEFT)
            entry = tk.Entry(frame, textvariable=variable)
            entry.pack(side=tk.LEFT, padx=5, fill='x', expand=True)
        
        create_row(input_window,"New Agent Fullname", fullname)

        def confirm_function():
            new_fullname = fullname.get()

            if not new_fullname:
                messagebox.showerror("Input Error", "Please fill out all fields.")
                return
            
            updated_info = []
            new_agent_info = None
            for agent in self.agent_list:
                if agent['Codename'] == name:
                    updated_info.append(f"{agent['Agent Number']:<12s}{agent['Codename']:<19s}{new_fullname:<19s}{agent['Class']:<10s}{agent['Age']:<8s}{agent['Ethnicity']:<19s}{agent['Role']:<19s}{agent['Ult Points']:<16s}{agent['Pick Rate']:<19s}")
                    new_agent_info = f"{agent['Agent Number']},{agent['Codename']},{new_fullname},{agent['Class']},{agent['Age']},{agent['Ethnicity']},{agent['Role']},{agent['Ult Points']},{agent['Pick Rate']}"

            if new_agent_info is None:
                messagebox.showerror("Error", "Agent not found.")
                return

            update_window = tk.Toplevel()
            update_window.title("Updated List")
            update_window.geometry("1080x500")

            text = tk.Text(update_window, wrap='none', font=("Courier New", 10))
            text.pack(expand=True, fill='both')
            text.insert(tk.END, f"{'No.':<12s}{'Codename':<19s}{'Full Name':<19s}{'Class':<10s}{'Age':<8s}{'Ethnicity':<19s}{'Role':<19s}{'Ult Points':<16s}{'Pick Rate':<19s}\n")
            for info in updated_info:
                text.insert(tk.END, info + "\n")
            text.config(state=tk.DISABLED)

            def confirm_upd_win():
                self.new_info = new_agent_info
                self.rewrite(name, self.new_info)
                messagebox.showinfo("Confirmation", "Fullname updated successfully.")

            def close_upd_win():
                update_window.destroy()

            def confirm_close():
                confirm_upd_win()
                close_upd_win()

            frame = tk.Frame(update_window)
            frame.pack(padx=10, pady=5)
            confirm_button = tk.Button(frame, text="Confirm", command=confirm_close)
            confirm_button.pack(side=tk.LEFT, padx=5)
            cancel_button = tk.Button(frame, text="Cancel", command=update_window.destroy)
            cancel_button.pack(side=tk.LEFT, padx=5)
            frame.pack(anchor='center')

        def close_window():
            input_window.destroy()

        def confirm_and_close():
            confirm_function()
            close_window()

        frame = tk.Frame(input_window)
        frame.pack(padx=10, pady=5)
        confirm_button = tk.Button(frame, text="Confirm", command=confirm_and_close)
        confirm_button.pack(side=tk.LEFT, padx=5)
        cancel_button = tk.Button(frame, text="Cancel", command=input_window.destroy)
        cancel_button.pack(side=tk.LEFT, padx=5)
        frame.pack(anchor='center')

    def agentclass(self, name):
        self.reload_agents
        input_window = tk.Toplevel()
        input_window.title("")

        agentclass = tk.StringVar()

        def create_row(parent, text, variable):
            frame = tk.Frame(parent)
            frame.pack(padx=10, pady=5, fill='x')
            label = tk.Label(frame, text=text)
            label.pack(side=tk.LEFT)
            entry = tk.Entry(frame, textvariable=variable)
            entry.pack(side=tk.LEFT, padx=5, fill='x', expand=True)
        
        create_row(input_window,"New Agent Class", agentclass)

        def confirm_function():
            new_class = agentclass.get()

            if not new_class:
                messagebox.showerror("Input Error", "Please fill out all fields.")
                return
            
            updated_info = []
            new_agent_info = None
            for agent in self.agent_list:
                if agent['Codename'] == name:
                    updated_info.append(f"{agent['Agent Number']:<12s}{agent['Codename']:<19s}{agent['Full name']:<19s}{new_class:<10s}{agent['Age']:<8s}{agent['Ethnicity']:<19s}{agent['Role']:<19s}{agent['Ult Points']:<16s}{agent['Pick Rate']:<19s}")
                    new_agent_info = f"{agent['Agent Number']},{agent['Codename']},{agent['Full name']},{new_class},{agent['Age']},{agent['Ethnicity']},{agent['Role']},{agent['Ult Points']},{agent['Pick Rate']}"

            if new_agent_info is None:
                messagebox.showerror("Error", "Agent not found.")
                return

            update_window = tk.Toplevel()
            update_window.title("Updated List")
            update_window.geometry("1080x500")

            text = tk.Text(update_window, wrap='none', font=("Courier New", 10))
            text.pack(expand=True, fill='both')
            text.insert(tk.END, f"{'No.':<12s}{'Codename':<19s}{'Full Name':<19s}{'Class':<10s}{'Age':<8s}{'Ethnicity':<19s}{'Role':<19s}{'Ult Points':<16s}{'Pick Rate':<19s}\n")
            for info in updated_info:
                text.insert(tk.END, info + "\n")
            text.config(state=tk.DISABLED)

            def confirm_upd_win():
                self.new_info = new_agent_info
                self.rewrite(name, self.new_info)
                messagebox.showinfo("Confirmation", "Class updated successfully.")

            def close_upd_win():
                update_window.destroy()

            def confirm_close():
                confirm_upd_win()
                close_upd_win()

            frame = tk.Frame(update_window)
            frame.pack(padx=10, pady=5)
            confirm_button = tk.Button(frame, text="Confirm", command=confirm_close)
            confirm_button.pack(side=tk.LEFT, padx=5)
            cancel_button = tk.Button(frame, text="Cancel", command=update_window.destroy)
            cancel_button.pack(side=tk.LEFT, padx=5)
            frame.pack(anchor='center')

        def close_window():
            input_window.destroy()

        def confirm_and_close():
            confirm_function()
            close_window()

        frame = tk.Frame(input_window)
        frame.pack(padx=10, pady=5)
        confirm_button = tk.Button(frame, text="Confirm", command=confirm_and_close)
        confirm_button.pack(side=tk.LEFT, padx=5)
        cancel_button = tk.Button(frame, text="Cancel", command=input_window.destroy)
        cancel_button.pack(side=tk.LEFT, padx=5)
        frame.pack(anchor='center')

    def agentage(self, name):
        self.reload_agents
        input_window = tk.Toplevel()
        input_window.title("")

        age = tk.StringVar()

        def create_row(parent, text, variable):
            frame = tk.Frame(parent)
            frame.pack(padx=10, pady=5, fill='x')
            label = tk.Label(frame, text=text)
            label.pack(side=tk.LEFT)
            entry = tk.Entry(frame, textvariable=variable)
            entry.pack(side=tk.LEFT, padx=5, fill='x', expand=True)
        
        create_row(input_window,"New Agent Age", age)

        def confirm_function():
            new_age = age.get()

            if not new_age:
                messagebox.showerror("Input Error", "Please fill out all fields.")
                return
            
            updated_info = []
            new_agent_info = None
            for agent in self.agent_list:
                if agent['Codename'] == name:
                    updated_info.append(f"{agent['Agent Number']:<12s}{agent['Codename']:<19s}{agent['Full name']:<19s}{agent['Class']:<10s}{new_age:<8s}{agent['Ethnicity']:<19s}{agent['Role']:<19s}{agent['Ult Points']:<16s}{agent['Pick Rate']:<19s}")
                    new_agent_info = f"{agent['Agent Number']},{agent['Codename']},{agent['Full name']},{agent['Class']},{new_age},{agent['Ethnicity']},{agent['Role']},{agent['Ult Points']},{agent['Pick Rate']}"

            if new_agent_info is None:
                messagebox.showerror("Error", "Agent not found.")
                return

            update_window = tk.Toplevel()
            update_window.title("Updated List")
            update_window.geometry("1080x500")

            text = tk.Text(update_window, wrap='none', font=("Courier New", 10))
            text.pack(expand=True, fill='both')
            text.insert(tk.END, f"{'No.':<12s}{'Codename':<19s}{'Full Name':<19s}{'Class':<10s}{'Age':<8s}{'Ethnicity':<19s}{'Role':<19s}{'Ult Points':<16s}{'Pick Rate':<19s}\n")
            for info in updated_info:
                text.insert(tk.END, info + "\n")
            text.config(state=tk.DISABLED)

            def confirm_upd_win():
                self.new_info = new_agent_info
                self.rewrite(name, self.new_info)
                messagebox.showinfo("Confirmation", "Age updated successfully.")

            def close_upd_win():
                update_window.destroy()

            def confirm_close():
                confirm_upd_win()
                close_upd_win()

            frame = tk.Frame(update_window)
            frame.pack(padx=10, pady=5)
            confirm_button = tk.Button(frame, text="Confirm", command=confirm_close)
            confirm_button.pack(side=tk.LEFT, padx=5)
            cancel_button = tk.Button(frame, text="Cancel", command=update_window.destroy)
            cancel_button.pack(side=tk.LEFT, padx=5)
            frame.pack(anchor='center')

        def close_window():
            input_window.destroy()

        def confirm_and_close():
            confirm_function()
            close_window()

        frame = tk.Frame(input_window)
        frame.pack(padx=10, pady=5)
        confirm_button = tk.Button(frame, text="Confirm", command=confirm_and_close)
        confirm_button.pack(side=tk.LEFT, padx=5)
        cancel_button = tk.Button(frame, text="Cancel", command=input_window.destroy)
        cancel_button.pack(side=tk.LEFT, padx=5)
        frame.pack(anchor='center')

    def agentethnicity(self, name):
        self.reload_agents
        input_window = tk.Toplevel()
        input_window.title("")

        ethnicity = tk.StringVar()

        def create_row(parent, text, variable):
            frame = tk.Frame(parent)
            frame.pack(padx=10, pady=5, fill='x')
            label = tk.Label(frame, text=text)
            label.pack(side=tk.LEFT)
            entry = tk.Entry(frame, textvariable=variable)
            entry.pack(side=tk.LEFT, padx=5, fill='x', expand=True)
        
        create_row(input_window,"New Agent Ethnicity", ethnicity)

        def confirm_function():
            new_ethnicity = ethnicity.get()

            if not new_ethnicity:
                messagebox.showerror("Input Error", "Please fill out all fields.")
                return
            
            updated_info = []
            new_agent_info = None
            for agent in self.agent_list:
                if agent['Codename'] == name:
                    updated_info.append(f"{agent['Agent Number']:<12s}{agent['Codename']:<19s}{agent['Full name']:<19s}{agent['Class']:<10s}{agent['Age']:<8s}{new_ethnicity:<19s}{agent['Role']:<19s}{agent['Ult Points']:<16s}{agent['Pick Rate']:<19s}")
                    new_agent_info = f"{agent['Agent Number']},{agent['Codename']},{agent['Full name']},{agent['Class']},{agent['Age']},{new_ethnicity},{agent['Role']},{agent['Ult Points']},{agent['Pick Rate']}"

            if new_agent_info is None:
                messagebox.showerror("Error", "Agent not found.")
                return

            update_window = tk.Toplevel()
            update_window.title("Updated List")
            update_window.geometry("1080x500")

            text = tk.Text(update_window, wrap='none', font=("Courier New", 10))
            text.pack(expand=True, fill='both')
            text.insert(tk.END, f"{'No.':<12s}{'Codename':<19s}{'Full Name':<19s}{'Class':<10s}{'Age':<8s}{'Ethnicity':<19s}{'Role':<19s}{'Ult Points':<16s}{'Pick Rate':<19s}\n")
            for info in updated_info:
                text.insert(tk.END, info + "\n")
            text.config(state=tk.DISABLED)

            def confirm_upd_win():
                self.new_info = new_agent_info
                self.rewrite(name, self.new_info)
                messagebox.showinfo("Confirmation", "Ethnicity updated successfully.")

            def close_upd_win():
                update_window.destroy()

            def confirm_close():
                confirm_upd_win()
                close_upd_win()

            frame = tk.Frame(update_window)
            frame.pack(padx=10, pady=5)
            confirm_button = tk.Button(frame, text="Confirm", command=confirm_close)
            confirm_button.pack(side=tk.LEFT, padx=5)
            cancel_button = tk.Button(frame, text="Cancel", command=update_window.destroy)
            cancel_button.pack(side=tk.LEFT, padx=5)
            frame.pack(anchor='center')

        def close_window():
            input_window.destroy()

        def confirm_and_close():
            confirm_function()
            close_window()

        frame = tk.Frame(input_window)
        frame.pack(padx=10, pady=5)
        confirm_button = tk.Button(frame, text="Confirm", command=confirm_and_close)
        confirm_button.pack(side=tk.LEFT, padx=5)
        cancel_button = tk.Button(frame, text="Cancel", command=input_window.destroy)
        cancel_button.pack(side=tk.LEFT, padx=5)
        frame.pack(anchor='center')

    def agentrole(self, name):
        self.reload_agents
        input_window = tk.Toplevel()
        input_window.title("")

        role = tk.StringVar()

        def create_row(parent, text, variable):
            frame = tk.Frame(parent)
            frame.pack(padx=10, pady=5, fill='x')
            label = tk.Label(frame, text=text)
            label.pack(side=tk.LEFT)
            entry = tk.Entry(frame, textvariable=variable)
            entry.pack(side=tk.LEFT, padx=5, fill='x', expand=True)
        
        create_row(input_window,"New Agent Role", role)

        def confirm_function():
            new_role = role.get()

            if not new_role:
                messagebox.showerror("Input Error", "Please fill out all fields.")
                return
            
            updated_info = []
            new_agent_info = None
            for agent in self.agent_list:
                if agent['Codename'] == name:
                    updated_info.append(f"{agent['Agent Number']:<12s}{agent['Codename']:<19s}{agent['Full name']:<19s}{agent['Class']:<10s}{agent['Age']:<8s}{agent['Ethnicity']:<19s}{new_role:<19s}{agent['Ult Points']:<16s}{agent['Pick Rate']:<19s}")
                    new_agent_info = f"{agent['Agent Number']},{agent['Codename']},{agent['Full name']},{agent['Class']},{agent['Age']},{agent['Ethnicity']},{new_role},{agent['Ult Points']},{agent['Pick Rate']}"

            if new_agent_info is None:
                messagebox.showerror("Error", "Agent not found.")
                return

            update_window = tk.Toplevel()
            update_window.title("Updated List")
            update_window.geometry("1080x500")

            text = tk.Text(update_window, wrap='none', font=("Courier New", 10))
            text.pack(expand=True, fill='both')
            text.insert(tk.END, f"{'No.':<12s}{'Codename':<19s}{'Full Name':<19s}{'Class':<10s}{'Age':<8s}{'Ethnicity':<19s}{'Role':<19s}{'Ult Points':<16s}{'Pick Rate':<19s}\n")
            for info in updated_info:
                text.insert(tk.END, info + "\n")
            text.config(state=tk.DISABLED)

            def confirm_upd_win():
                self.new_info = new_agent_info
                self.rewrite(name, self.new_info)
                messagebox.showinfo("Confirmation", "Role updated successfully.")

            def close_upd_win():
                update_window.destroy()

            def confirm_close():
                confirm_upd_win()
                close_upd_win()

            frame = tk.Frame(update_window)
            frame.pack(padx=10, pady=5)
            confirm_button = tk.Button(frame, text="Confirm", command=confirm_close)
            confirm_button.pack(side=tk.LEFT, padx=5)
            cancel_button = tk.Button(frame, text="Cancel", command=update_window.destroy)
            cancel_button.pack(side=tk.LEFT, padx=5)
            frame.pack(anchor='center')

        def close_window():
            input_window.destroy()

        def confirm_and_close():
            confirm_function()
            close_window()

        frame = tk.Frame(input_window)
        frame.pack(padx=10, pady=5)
        confirm_button = tk.Button(frame, text="Confirm", command=confirm_and_close)
        confirm_button.pack(side=tk.LEFT, padx=5)
        cancel_button = tk.Button(frame, text="Cancel", command=input_window.destroy)
        cancel_button.pack(side=tk.LEFT, padx=5)
        frame.pack(anchor='center')

    def agentultpoints(self, name):
        self.reload_agents
        input_window = tk.Toplevel()
        input_window.title("")

        points = tk.StringVar()

        def create_row(parent, text, variable):
            frame = tk.Frame(parent)
            frame.pack(padx=10, pady=5, fill='x')
            label = tk.Label(frame, text=text)
            label.pack(side=tk.LEFT)
            entry = tk.Entry(frame, textvariable=variable)
            entry.pack(side=tk.LEFT, padx=5, fill='x', expand=True)
        
        create_row(input_window,"New Agent Ult Points", points)

        def confirm_function():
            new_point = points.get()

            if not new_point:
                messagebox.showerror("Input Error", "Please fill out all fields.")
                return
            
            updated_info = []
            new_agent_info = None
            for agent in self.agent_list:
                if agent['Codename'] == name:
                    updated_info.append(f"{agent['Agent Number']:<12s}{agent['Codename']:<19s}{agent['Full name']:<19s}{agent['Class']:<10s}{agent['Age']:<8s}{agent['Ethnicity']:<19s}{agent['Role']:<19s}{new_point:<16s}{agent['Pick Rate']:<19s}")
                    new_agent_info = f"{agent['Agent Number']},{agent['Codename']},{agent['Full name']},{agent['Class']},{agent['Age']},{agent['Ethnicity']},{agent['Role']},{new_point},{agent['Pick Rate']}"

            if new_agent_info is None:
                messagebox.showerror("Error", "Agent not found.")
                return

            update_window = tk.Toplevel()
            update_window.title("Updated List")
            update_window.geometry("1080x500")

            text = tk.Text(update_window, wrap='none', font=("Courier New", 10))
            text.pack(expand=True, fill='both')
            text.insert(tk.END, f"{'No.':<12s}{'Codename':<19s}{'Full Name':<19s}{'Class':<10s}{'Age':<8s}{'Ethnicity':<19s}{'Role':<19s}{'Ult Points':<16s}{'Pick Rate':<19s}\n")
            for info in updated_info:
                text.insert(tk.END, info + "\n")
            text.config(state=tk.DISABLED)

            def confirm_upd_win():
                self.new_info = new_agent_info
                self.rewrite(name, self.new_info)
                messagebox.showinfo("Confirmation", "Ult Points updated successfully.")

            def close_upd_win():
                update_window.destroy()

            def confirm_close():
                confirm_upd_win()
                close_upd_win()

            frame = tk.Frame(update_window)
            frame.pack(padx=10, pady=5)
            confirm_button = tk.Button(frame, text="Confirm", command=confirm_close)
            confirm_button.pack(side=tk.LEFT, padx=5)
            cancel_button = tk.Button(frame, text="Cancel", command=update_window.destroy)
            cancel_button.pack(side=tk.LEFT, padx=5)
            frame.pack(anchor='center')

        def close_window():
            input_window.destroy()

        def confirm_and_close():
            confirm_function()
            close_window()

        frame = tk.Frame(input_window)
        frame.pack(padx=10, pady=5)
        confirm_button = tk.Button(frame, text="Confirm", command=confirm_and_close)
        confirm_button.pack(side=tk.LEFT, padx=5)
        cancel_button = tk.Button(frame, text="Cancel", command=input_window.destroy)
        cancel_button.pack(side=tk.LEFT, padx=5)
        frame.pack(anchor='center')

    def agentpickrate(self, name):
        self.reload_agents
        input_window = tk.Toplevel()
        input_window.title("")

        rate = tk.StringVar()

        def create_row(parent, text, variable):
            frame = tk.Frame(parent)
            frame.pack(padx=10, pady=5, fill='x')
            label = tk.Label(frame, text=text)
            label.pack(side=tk.LEFT)
            entry = tk.Entry(frame, textvariable=variable)
            entry.pack(side=tk.LEFT, padx=5, fill='x', expand=True)
        
        create_row(input_window,"New Agent Pick Rate", rate)

        def confirm_function():
            new_rate = rate.get()+'%'

            if not new_rate:
                messagebox.showerror("Input Error", "Please fill out all fields.")
                return
            
            updated_info = []
            new_agent_info = None
            for agent in self.agent_list:
                if agent['Codename'] == name:
                    updated_info.append(f"{agent['Agent Number']:<12s}{agent['Codename']:<19s}{agent['Full name']:<19s}{agent['Class']:<10s}{agent['Age']:<8s}{agent['Ethnicity']:<19s}{agent['Role']:<19s}{agent['Ult Points']:<16s}{new_rate:<19s}")
                    new_agent_info = f"{agent['Agent Number']},{agent['Codename']},{agent['Full name']},{agent['Class']},{agent['Age']},{agent['Ethnicity']},{agent['Role']},{agent['Ult Points']},{new_rate}"

            if new_agent_info is None:
                messagebox.showerror("Error", "Agent not found.")
                return

            update_window = tk.Toplevel()
            update_window.title("Updated List")
            update_window.geometry("1080x500")

            text = tk.Text(update_window, wrap='none', font=("Courier New", 10))
            text.pack(expand=True, fill='both')
            text.insert(tk.END, f"{'No.':<12s}{'Codename':<19s}{'Full Name':<19s}{'Class':<10s}{'Age':<8s}{'Ethnicity':<19s}{'Role':<19s}{'Ult Points':<16s}{'Pick Rate':<19s}\n")
            for info in updated_info:
                text.insert(tk.END, info + "\n")
            text.config(state=tk.DISABLED)

            def confirm_upd_win():
                self.new_info = new_agent_info
                self.rewrite(name, self.new_info)
                messagebox.showinfo("Confirmation", "Pick Rate updated successfully.")

            def close_upd_win():
                update_window.destroy()

            def confirm_close():
                confirm_upd_win()
                close_upd_win()

            frame = tk.Frame(update_window)
            frame.pack(padx=10, pady=5)
            confirm_button = tk.Button(frame, text="Confirm", command=confirm_close)
            confirm_button.pack(side=tk.LEFT, padx=5)
            cancel_button = tk.Button(frame, text="Cancel", command=update_window.destroy)
            cancel_button.pack(side=tk.LEFT, padx=5)
            frame.pack(anchor='center')

        def close_window():
            input_window.destroy()

        def confirm_and_close():
            confirm_function()
            close_window()

        frame = tk.Frame(input_window)
        frame.pack(padx=10, pady=5)
        confirm_button = tk.Button(frame, text="Confirm", command=confirm_and_close)
        confirm_button.pack(side=tk.LEFT, padx=5)
        cancel_button = tk.Button(frame, text="Cancel", command=input_window.destroy)
        cancel_button.pack(side=tk.LEFT, padx=5)
        frame.pack(anchor='center')

    def get_agent_name(self):
        self.reload_agents()
        input_window = tk.Toplevel()
        input_window.title("Option 6: Edit Agent Information")

        name = tk.StringVar()

        def create_row(parent, text, variable):
            frame = tk.Frame(parent)
            frame.pack(padx=10, pady=5, fill='x')
            label = tk.Label(frame, text=text)
            label.pack(side=tk.LEFT)
            entry = tk.Entry(frame, textvariable=variable)
            entry.pack(side=tk.LEFT, padx=5, fill='x', expand=True)

        create_row(input_window,"Agent Codename",name)

        def display_agent_list():
            agent_name = name.get()

            if not agent_name:
                messagebox.showerror("Input Error", "Please fill out all fields.")
                return

            list_window = tk.Toplevel()
            list_window.title("Agent List")
            list_window.geometry('1080x800')

            text = tk.Text(list_window, wrap='none', font=("Courier New", 10))
            text.pack(expand=True, fill='both')
            text.insert(tk.END, f"{'No.':<12s}{'Codename':<19s}{'Full Name':<19s}{'Class':<10s}{'Age':<8s}{'Ethnicity':<19s}{'Role':<19s}{'Ult Points':<16s}{'Pick Rate':<19s}\n")
            for agent in self.agent_list:
                if agent['Codename'] == agent_name:
                    text.insert(tk.END, f"{agent['Agent Number']:<12s}{agent['Codename']:<19s}{agent['Full name']:<19s}{agent['Class']:<10s}{agent['Age']:<8s}{agent['Ethnicity']:<19s}{agent['Role']:<19s}{agent['Ult Points']:<16s}{agent['Pick Rate']:<19s}\n")
            text.config(state=tk.DISABLED)

            tk.Label(list_window, text="Which Information do you what to edit?").pack(pady=10)

            options_frame = tk.Frame(list_window)
            options_frame.pack(pady=10)

            selected_option = tk.StringVar()

            for option in search_menu():
                radio_button = tk.Radiobutton(options_frame, text=option, variable=selected_option, value=option)
                radio_button.pack(anchor='w', pady=2)
                
            def close_window():
                list_window.destroy()

            def confirm_and_close():
                confirm_function()
                close_window()

            def confirm_function():
                option = selected_option.get()
                if option == "[1]  AGENT NUMBER":
                    self.new_info = self.agentno(agent_name)
                if option == "[2]  CODENAME":
                    self.new_info = self.agentcodename(agent_name)
                if option == "[3]  FULLNAME":
                    self.new_info = self.agentfullname(agent_name)
                if option == "[4]  CLASS":
                    self.new_info = self.agentclass(agent_name)
                if option == "[5]  AGE":
                    self.new_info = self.agentage(agent_name)
                if option == "[6]  ETHNITICY":
                    self.new_info = self.agentethnicity(agent_name)
                if option == "[7]  ROLE":
                    self.new_info = self.agentrole(agent_name)
                if option == "[8]  ULT POINTS":
                    self.new_info = self.agentultpoints(agent_name)
                if option == "[9]  PICK RATE":
                    self.new_info = self.agentpickrate(agent_name)

            frame = tk.Frame(list_window)
            frame.pack(padx=10, pady=5)
            confirm_button = tk.Button(frame, text="Confirm", command=confirm_and_close)
            confirm_button.pack(side=tk.LEFT, padx=5)
            cancel_button = tk.Button(frame, text="Cancel", command=list_window.destroy)
            cancel_button.pack(side=tk.LEFT, padx=5)
            frame.pack(anchor='center')
                
        def cancel_form():
            input_window.destroy()

        def display_and_close():
            display_agent_list()
            cancel_form()

        submit_button = tk.Button(input_window, text="Confirm", command=display_and_close)
        submit_button.pack(pady=10)

class add(file):
    def __init__(self):
        super().__init__()
    
    def add_agent(self, full_agent_info):
        self.reload_agents()
        f = open('C:/Users/TUF/Documents/Coding Practice/DIT102/Final Project/agents.csv', 'a')
        f.write(f"\n{full_agent_info}")
        f.close()

    def add(self):
        self.reload_agents()
        list_window = tk.Toplevel()
        list_window.title("Option 3: Add Agent")

        agent_num_var = tk.StringVar()
        agent_codename_var = tk.StringVar()
        agent_fullname_var = tk.StringVar()
        agent_class_var = tk.StringVar()
        agent_age_var = tk.StringVar()
        agent_ethnicity_var = tk.StringVar()
        agent_role_var = tk.StringVar()
        agent_ult_points_var = tk.StringVar()
        agent_pick_rate_var = tk.StringVar()

        def create_row(parent, label_text, text_variable):
            frame = tk.Frame(parent)
            frame.pack(padx=10, pady=5, fill='x')
            label = tk.Label(frame, text=label_text)
            label.pack(side=tk.LEFT)
            entry = tk.Entry(frame, textvariable=text_variable)
            entry.pack(side=tk.LEFT, padx=5, fill='x', expand=True)

        create_row(list_window, "Enter Agent Number:", agent_num_var)
        create_row(list_window, "Enter Agent Codename:", agent_codename_var)
        create_row(list_window, "Enter Agent Full Name:", agent_fullname_var)
        create_row(list_window, "Enter Agent Class:", agent_class_var)
        create_row(list_window, "Enter Agent Age:", agent_age_var)
        create_row(list_window, "Enter Agent Ethnicity:", agent_ethnicity_var)
        create_row(list_window, "Enter Agent Role:", agent_role_var)
        create_row(list_window, "Enter Agent Ult Points:", agent_ult_points_var)
        create_row(list_window, "Enter Agent Pick Rate:", agent_pick_rate_var)

        def submit_form():
            self.reload_agents()
            agent_number = agent_num_var.get()
            agent_codename = agent_codename_var.get()
            agent_fullname = agent_fullname_var.get()
            agent_class = agent_class_var.get()
            agent_age = agent_age_var.get()
            agent_ethnicity = agent_ethnicity_var.get()
            agent_role = agent_role_var.get()
            agent_ult_points = agent_ult_points_var.get()
            agent_pick_rate = agent_pick_rate_var.get()

            full_agent_info = (f'{agent_number},{agent_codename},{agent_fullname},{agent_class},{agent_age},{agent_ethnicity},{agent_role},{agent_ult_points},{agent_pick_rate}%')

            if (not agent_number or not agent_codename or not agent_fullname or
                not agent_class or not agent_age or not agent_ethnicity or
                not agent_role or not agent_ult_points or not agent_pick_rate):
                # Display an error message
                messagebox.showerror("Input Error", "Please fill out all fields.")
            else:
                self.add_agent(full_agent_info)
                list_window.destroy()

        def cancel_form():
            list_window.destroy()

        button_frame = tk.Frame(list_window)
        button_frame.pack(pady=10)
        submit_button = tk.Button(button_frame, text="Submit", command=submit_form)
        submit_button.pack(side=tk.LEFT, padx=5)
        cancel_button = tk.Button(button_frame, text="Cancel", command=cancel_form)
        cancel_button.pack(side=tk.RIGHT, padx=5)

def menu():
    return [
        "[1]  Display All The Agents",
        "[2]  Display The Total Number of Agents",
        "[3]  Add New Agent",
        "[4]  Search Agent Information",
        "[5]  Delete Agent Information",
        "[6]  Edit Agent Information",
        '[0]  Exit Program'
    ]

def search_menu():
    return [
        "[1]  AGENT NUMBER",
        "[2]  CODENAME",
        "[3]  FULLNAME",
        "[4]  CLASS",
        "[5]  AGE",
        "[6]  ETHNITICY",
        "[7]  ROLE",
        "[8]  ULT POINTS",
        "[9]  PICK RATE",
    ]

def search_option():
    list_window = tk.Toplevel()
    list_window.title("Option 4: Search Agent Information")

    tk.Label(list_window, text="Search Agent by").pack(pady=10)

    selected_var_info = tk.StringVar(value="")

    for option in search_menu():
        radio_button = tk.Radiobutton(list_window, text=option, variable=selected_var_info, value=option)
        radio_button.pack(anchor='w', pady=2)

    def show_selected_info():
        option = selected_var_info.get()
        if option:
            if option == "[1]  AGENT NUMBER":
                search().agentno()
            elif option == "[2]  CODENAME":
                search().codename()
            elif option == "[3]  FULLNAME":
                search().fullname()
            elif option == "[4]  CLASS":
                search().Class()
            elif option == "[5]  AGE":
                search().age()
            elif option == "[6]  ETHNITICY":
                search().ethnicity()
            elif option == "[7]  ROLE":
                search().role()
            elif option == "[8]  ULT POINTS":
                search().ultpoint()
            elif option == "[9]  PICK RATE":
                search().pickrate()
        else:
            print("No option selected.")

    def close_form():
        list_window.destroy()

    def show_and_close():
        show_selected_info()
        close_form()
    
    submit_button = tk.Button(list_window, text="Confirm", command=show_and_close)
    submit_button.pack(pady=10)

def show_selected():
    selected_option = selected_var.get()
    if selected_option:
        if selected_option == "[1]  Display All The Agents":
            display().list()
        elif selected_option == "[2]  Display The Total Number of Agents":
            display().total()
        elif selected_option == "[3]  Add New Agent":
            add().add()
        elif selected_option == "[4]  Search Agent Information":
            search_option()
        elif selected_option == "[5]  Delete Agent Information":
            delete().del_agent()
        elif selected_option == "[6]  Edit Agent Information":
            edit().get_agent_name()
        elif selected_option == "[0]  Exit Program":
            root.destroy()
    else:
        print("No option selected.")

root = tk.Tk()
root.title('Agents Database')

tk.Label(root, text="Menu").pack(pady=10)

selected_var = tk.StringVar(value="")

for option in menu():
    radio_button = tk.Radiobutton(root, text=option, variable=selected_var, value=option)
    radio_button.pack(anchor='w', pady=2)

submit_button = tk.Button(root, text="Confirm", command=show_selected)
submit_button.pack(pady=10)

root.mainloop()

# Project by
# 6609063 - Saw Aung Kaung Thant