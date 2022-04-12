"""
Photographer data 
"""
from tkinter import *
import subprocess 

class photographer_data(Tk):
    def __init__(self):
        Tk.__init__(self)
        self.attributes('-fullscreen', True) 
        self.data = ["GROUPE", "PRENOM NOM 0", "PRENOM NOM 1", "PRENOM NOM 2", "AFFILIATION", "EXPERIENCE"]
        
        keypad_frame = Frame(self)
        exit_frame = Frame(self)
        label_frame = Frame(self)
        
        for i,d in enumerate(self.data):
            self.label = Label(label_frame, text=" "+d+" ", height=2, bd=2, width=15, relief="ridge", font=('helvetica', 10),
                                  ).grid(row=i+1, column=0, padx=15, pady=5, sticky='news')
        label_frame.grid(row=0, column=0, padx=5, pady=5, sticky='n')
        
        
       
        self.entries = [Entry(label_frame, width=30, bd=3, font=('helvetica', 10)) for i in range(len(self.data))]
        self.entry_list = []
        for i,e in enumerate(self.entries):
            e.grid(row=i+1, column=1, padx=5, pady=5)
            self.entry_list.append(e)
        label_frame.grid(row=0, column=1, padx=5, pady=5, sticky='n')
        
        

        
        btn_quit = Button(exit_frame, text='Sortir', bd=2, bg='white', fg='blue', font=('helvetica', 12),
                            borderwidth=0, command=self.destroy).grid(row=0, column=9, padx=5, pady=2, sticky='ne')
        
        btn_delete = Button(exit_frame, text='Del', bd=2, bg='white', fg='blue', font=('helvetica', 12),
                            borderwidth=0, command=self.delete_text).grid(row=0, column=10, padx=5, pady=2, sticky='ne')
        
        btn_save = Button(exit_frame, text='Save', bd=2, bg='white', fg='blue', font=('helvetica', 12),
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
                
        
        keypad_frame.grid(row=0, column=0, sticky='s')
        exit_frame.grid(row=0, column=0, sticky='ne')
         

    def set_text(self, text):
        widget = self.focus_get()
        if widget in self.entries:
            widget.insert("insert", text)
            
    def delete_text(self):
        widget = self.focus_get()
        widget.delete(0, END)
    
    
    def save_data(self):
        global who
        global data
        who = {}
        for s, i in enumerate(self.entry_list):
            widget = i
            data = widget.get()
            data_dict[s] = data
            data_dict[self.data[s]] = data_dict.pop(s)
        new_wind = Toplevel(self)
        new_wind.title("info")
        new_wind.attributes('-fullscreen', True)
        new_lab = Label(new_wind, text="data Saved!").grid(row=0, column=0)
        btn_quit_ = Button(new_wind, text="OK", command=new_wind.destroy).grid(row=1, column=0)
        print(who)
        inside_data['WHO'] = who
        print(inside_data)


#################################################################################################
###############################  Camera INFOs ##################################################
class camera_info(Tk):
    global camera
    camera = {}
    def __init__(self):
        Tk.__init__(self)
        self.attributes('-fullscreen', True) 
        
        keypad_frame = Frame(self)
        exit_frame = Frame(self)
        label_frame = Frame(self)
        
        if camera_available() == True :
        
            camera_infos = []
            for line in about_camera():
                line = str(line)[2:].split(':')
                camera_infos.append(line)
                
            display_list = ['Manufacturer', 'Model', '  Serial Number', 'Capture Formats']
            
            camera_list = []
            for data in camera_infos:
                for j in display_list:
                    if data[0] == j:
                        camera_list.append(data[1][:-1])
                        camera[j] = data[1][:-1]
            print(camera)
                        
                
            
            for i,d in enumerate(display_list):
                self.label = Label(label_frame, text=" "+d+" ", height=2, bd=2, width=15, relief="flat", font=('helvetica', 12, 'bold')
                                      ).grid(row=i+1, column=0, padx=15, pady=5, sticky='news')
            self.label = Label(label_frame, text=" Lens ", height=2, bd=2, width=15, relief="flat", font=('helvetica', 12, 'bold')
                          ).grid(row=len(display_list)+1, column=0, padx=15, pady=5, sticky='news')
            self.entry_lens = Listbox(label_frame, height=1, exportselection=0)
            self.entry_lens.insert(END, "Zoom")
            self.entry_lens.insert(END, "Prime")
            self.entry_lens.grid(row=len(display_list)+1, column=1, padx=15, pady=5, sticky='news')
            
            self.entry_lens.bind('<<ListboxSelect>>', self.select_text)
            
            
            for i,d in enumerate(camera_list):
                self.label = Label(label_frame, text=" "+d+" ", height=2, bd=2, bg='white', width=40, font=('helvetica', 10, 'bold')
                                      ).grid(row=i+1, column=1, padx=15, pady=5, sticky='news')
        
        else :
            self.label = Label(label_frame, text="No Camera detected, please connect it!", bd=2, bg='white', width=40, font=('helvetica', 14, 'bold')
                               ).grid(row=0, column=1, padx=15, pady=5, sticky='news')
            
        
       

        
        self.btn_quit = Button(exit_frame, text='Sortir', bd=2, bg='white', fg='blue', font=('helvetica', 12),
                            borderwidth=0, command=self.destroy).grid(row=0, column=9, padx=5, pady=2, sticky='ne')
        
        self.btn_ok = Button(exit_frame, text='OK', bd=2, bg='white', fg='blue', font=('helvetica', 12), state=DISABLED,
                            borderwidth=0, command=self.save_data)
        self.btn_ok.grid(row=0, column=10, padx=5, pady=2, sticky='ne')
                
        
        
        exit_frame.grid(row=0, column=0, sticky='ne')
        label_frame.grid(row=0, column=1, sticky='n')
        

    def select_text(self, text):
        self.btn_ok['state'] = NORMAL
        self.selection = text.widget.curselection()
        self.index = self.selection[0]
        self.value = text.widget.get(self.index)
        camera['Lens'] = self.value
            
    
    def save_data(self):
        global data_dict
        global data
        global which
        which={}
        which['Camera'] = camera
        print(which)
        inside_data['WHICH'] = which
        print(inside_data)
        
def camera_available():
    p = subprocess.Popen(['gphoto2', '--auto-detect'], stdout=subprocess.PIPE)
    out, err = p.communicate()
    if len(out.splitlines()) == 3 :
        camera_is_available = True
    else:
        camera_is_available = False
    return camera_is_available

        