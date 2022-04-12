"""
Environment Data ----- 
"""
from tkinter import *


class environement_data:
    global date, place, projectname, object_of_interest
    
    def __init__(self):
        self.envi_wind = Tk()
        self.envi_wind.attributes('-fullscreen', True)
        self.envi_wind.title('environment')
        
        self.frame_exit = Frame(self.envi_wind)
        self.frame = Frame(self.envi_wind)
        keypad_frame = Frame(self.envi_wind)
        
        self.environment_list = ["Date", "Place", "Appelation", "Object Of Int"]
        
        self.button_exit = Button(self.frame_exit, text="Sortir", width=8, height=3, bg='white', fg='blue', font=('helvetica', 14, 'bold'),
                                  command=self.envi_wind.destroy)
        
        
        for i, data in enumerate(self.environment_list):
            label = Label(self.frame, text=data, width=15)
            label.grid(row=i, column=0, padx=10, pady=10, sticky='news')
            
            
        self.entries = [Entry(self.frame, width=30, bd=3, font=('helvetica', 10)) for i in range(len(self.environment_list))]
        self.entry_list = []
        for i,e in enumerate(self.entries):
            e.grid(row=i, column=1, padx=5, pady=5)
            self.entry_list.append(e)
            
        btn_delete = Button(self.frame_exit, text='Del', bd=2, bg='white', fg='blue', font=('helvetica', 12),
                            borderwidth=0, command=self.delete_text).grid(row=0, column=10, padx=5, pady=2, sticky='ne')
        
        btn_save = Button(self.frame_exit, text='Save', bd=2, bg='white', fg='blue', font=('helvetica', 12),
                            borderwidth=0, command=self.save_data).grid(row=0, column=11, padx=5, pady=2, sticky='ne') 
        
        cara = {1: (5, 2), 2: (5, 3), 3: (5, 4),
                        4: (5, 5), 5: (5, 6), 6: (5, 7),
                        7: (5, 8), 8: (5, 9), 9: (5, 10),
                       0: (5, 11), 'A':(6, 2), 'Z':(6, 3), 'E':(6, 4), 'R':(6, 5), 'T': (6, 6), 'Y':(6, 7), 'U':(6, 8), 'I':(6, 9),
                      'O':(6, 10), 'P':(6, 11), 'Q':(7, 2), 'S':(7, 3), 'D':(7, 4), 'F':(7, 5), 'G':(7, 6), 'H':(7, 7),
                      'J':(7, 8), 'K':(7, 9), 'L':(7, 10), 'M':(7, 11), 'W':(8, 2), 'X':(8, 3), 'C':(8, 4), 'V':(8, 5),
                      'B':(8, 6), 'N':(8, 7), ' ':(8, 8), '_':(8, 9), '-':(8, 10)}
        
        
            
        for car, grid_value in cara.items():
            if grid_value[0] == 5:
                button = Button(keypad_frame, text=str(car), bg='white', fg='blue', font=('helvetica', 14, 'bold'),
                            borderwidth=0, command=lambda x=car: self.set_text(x)).grid(row=grid_value[0], column=grid_value[1], padx=1, pady=2, sticky='news')
                
            if grid_value[0] == 6:
                button = Button(keypad_frame, text=str(car), bg='white', fg='blue', font=('helvetica', 14, 'bold'),
                            borderwidth=0, command=lambda x=car: self.set_text(x)).grid(row=grid_value[0], column=grid_value[1], pady=2, sticky='news')
                
            if grid_value[0] == 7:
                button = Button(keypad_frame, text=str(car), bg='white', fg='blue', font=('helvetica', 14, 'bold'),
                            borderwidth=0, command=lambda x=car: self.set_text(x)).grid(row=grid_value[0], column=grid_value[1], pady=2, sticky='news')
                
            if grid_value[0] == 8:
                button = Button(keypad_frame, text=str(car), bg='white', fg='blue', font=('helvetica', 14, 'bold'),
                            borderwidth=0, command=lambda x=car: self.set_text(x)).grid(row=grid_value[0], column=grid_value[1], pady=2, sticky='news')
                
        
        
        
        self.envi_wind.rowconfigure(0, weight=1)
        self.envi_wind.columnconfigure(0, weight=1)
        
        self.frame_exit.grid(row=0, column=0, sticky='ne')
        self.frame.grid(row=0, column=0, sticky='n')
        keypad_frame.grid(row=0, column=0, sticky='s')
        
        
        self.button_exit.grid(row=0, column=0, sticky='news')
        
        
        
        
    def set_text(self, text):
        widget = self.envi_wind.focus_get()
        if widget in self.entries:
            widget.insert("insert", text)
            
    def delete_text(self):
        widget = self.envi_wind.focus_get()
        widget.delete(0, END)
    
    
    def save_data(self):
        global data
        data_dict = {}
        for s, i in enumerate(self.entry_list):
            widget = i
            data = widget.get()
            data_dict[s] = data
            data_dict[self.environment_list[s]] = data_dict.pop(s)
        new_wind = Toplevel()
        new_wind.title("info")
        new_wind.attributes('-fullscreen', True)
        new_lab = Label(new_wind, text="data Saved!").grid(row=0, column=0)
        btn_quit_ = Button(new_wind, text="OK", command=new_wind.destroy).grid(row=1, column=0)
        
        inside_data['WHEN'] = data_dict["Date"]
        inside_data['WHERE'] = data_dict["Place"]
        what_keys = ["Appelation", "Object Of Int"]
        what_subset = {key: data_dict[key] for key in what_keys}
        inside_data['WHAT'] = what_subset
        
        data = data_dict["Date"]
        place = data_dict["Place"]
        projectname = data_dict["Appelation"]
        print(inside_data)
        
        return projectname
        

class others:
    
    def __init__(self):
        self.envi_wind = Tk()
        self.envi_wind.attributes('-fullscreen', True)
        self.envi_wind.title('environment')
        
        self.frame_exit = Frame(self.envi_wind)
        self.frame = Frame(self.envi_wind)
        keypad_frame = Frame(self.envi_wind)
        
        self.environment_list = ["But de Projet", "Type de Projet", "Technique", "Distance objet"]
        
        self.button_exit = Button(self.frame_exit, text="Sortir", width=8, height=3, bg='white', fg='blue', font=('helvetica', 14, 'bold'),
                                  command=self.envi_wind.destroy)
        
        
        for i, data in enumerate(self.environment_list):
            label = Label(self.frame, text=data, width=15)
            label.grid(row=i, column=0, padx=10, pady=10, sticky='news')
            
            
        self.entries = [Entry(self.frame, width=30, bd=3, font=('helvetica', 10)) for i in range(len(self.environment_list))]
        self.entry_list = []
        for i,e in enumerate(self.entries):
            e.grid(row=i, column=1, padx=5, pady=5)
            self.entry_list.append(e)
            
        btn_delete = Button(self.frame_exit, text='Del', bd=2, bg='white', fg='blue', font=('helvetica', 12),
                            borderwidth=0, command=self.delete_text).grid(row=0, column=10, padx=5, pady=2, sticky='ne')
        
        btn_save = Button(self.frame_exit, text='Save', bd=2, bg='white', fg='blue', font=('helvetica', 12),
                            borderwidth=0, command=self.save_data).grid(row=0, column=11, padx=5, pady=2, sticky='ne') 
        
        cara = {1: (5, 2), 2: (5, 3), 3: (5, 4),
                        4: (5, 5), 5: (5, 6), 6: (5, 7),
                        7: (5, 8), 8: (5, 9), 9: (5, 10),
                       0: (5, 11), 'A':(6, 2), 'Z':(6, 3), 'E':(6, 4), 'R':(6, 5), 'T': (6, 6), 'Y':(6, 7), 'U':(6, 8), 'I':(6, 9),
                      'O':(6, 10), 'P':(6, 11), 'Q':(7, 2), 'S':(7, 3), 'D':(7, 4), 'F':(7, 5), 'G':(7, 6), 'H':(7, 7),
                      'J':(7, 8), 'K':(7, 9), 'L':(7, 10), 'M':(7, 11), 'W':(8, 2), 'X':(8, 3), 'C':(8, 4), 'V':(8, 5),
                      'B':(8, 6), 'N':(8, 7), ' ':(8, 8), '_':(8, 9), '-':(8, 10)}
        
        
            
        for car, grid_value in cara.items():
            if grid_value[0] == 5:
                button = Button(keypad_frame, text=str(car), bg='white', fg='blue', font=('helvetica', 14, 'bold'),
                            borderwidth=0, command=lambda x=car: self.set_text(x)).grid(row=grid_value[0], column=grid_value[1], padx=1, pady=2, sticky='news')
                
            if grid_value[0] == 6:
                button = Button(keypad_frame, text=str(car), bg='white', fg='blue', font=('helvetica', 14, 'bold'),
                            borderwidth=0, command=lambda x=car: self.set_text(x)).grid(row=grid_value[0], column=grid_value[1], pady=2, sticky='news')
                
            if grid_value[0] == 7:
                button = Button(keypad_frame, text=str(car), bg='white', fg='blue', font=('helvetica', 14, 'bold'),
                            borderwidth=0, command=lambda x=car: self.set_text(x)).grid(row=grid_value[0], column=grid_value[1], pady=2, sticky='news')
                
            if grid_value[0] == 8:
                button = Button(keypad_frame, text=str(car), bg='white', fg='blue', font=('helvetica', 14, 'bold'),
                            borderwidth=0, command=lambda x=car: self.set_text(x)).grid(row=grid_value[0], column=grid_value[1], pady=2, sticky='news')
                
        
        
        
        self.envi_wind.rowconfigure(0, weight=1)
        self.envi_wind.columnconfigure(0, weight=1)
        
        self.frame_exit.grid(row=0, column=0, sticky='ne')
        self.frame.grid(row=0, column=0, sticky='n')
        keypad_frame.grid(row=0, column=0, sticky='s')
        
        
        self.button_exit.grid(row=0, column=0, sticky='news')
        
        
    def set_text(self, text):
        widget = self.envi_wind.focus_get()
        if widget in self.entries:
            widget.insert("insert", text)
            
    def delete_text(self):
        widget = self.envi_wind.focus_get()
        widget.delete(0, END)
    
    
    def save_data(self):
        global data
        data_dict = {}
        for s, i in enumerate(self.entry_list):
            widget = i
            data = widget.get()
            data_dict[s] = data
            data_dict[self.environment_list[s]] = data_dict.pop(s)
        new_wind = Toplevel()
        new_wind.title("info")
        new_wind.attributes('-fullscreen', True)
        new_lab = Label(new_wind, text="data Saved!").grid(row=0, column=0)
        btn_quit_ = Button(new_wind, text="OK", command=new_wind.destroy).grid(row=1, column=0)
        
        inside_data['WHY'] = data_dict["But de Projet"]
        inside_data['WHY'] = data_dict["Type de Projet"]
        what_keys = ["Technique", "Distance objet"]
        what_subset = {key: data_dict[key] for key in what_keys}
        inside_data['HOW'] = what_subset
        
        print(inside_data)
        
          
