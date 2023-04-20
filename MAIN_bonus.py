json_file_location=[]

d1={'A': 'z', 'B': 'y', 'C': 'x', 'D': 'w', 'E': 'v', 'F': 'u', 'G': 't', 'H': 's', 'I': 'r', 'J': 'q', 'K': 'p', 'L': 'o', 'M': 'n', 'N': 'm', 'O': 'l', 'P': 'k', 'Q': 'j', 'R': 'i', 'S': 'h', 'T': 'g', 'U': 'f', 'V': 'e', 'W': 'd', 'X': 'c', 'Y': 'b', 'Z': 'a'}
d2={'a': 'Z', 'b': 'Y', 'c': 'X', 'd': 'W', 'e': 'V', 'f': 'U', 'g': 'T', 'h': 'S', 'i': 'R', 'j': 'Q', 'k': 'P', 'l': 'O', 'm': 'N', 'n': 'M', 'o': 'L', 'p': 'K', 'q': 'J', 'r': 'I', 's': 'H', 't': 'G', 'u': 'F', 'v': 'E', 'w': 'D', 'x': 'C', 'y': 'B', 'z': 'A'}
class encryption:
    def __init__(self,file_location)-> None:
        pass
        
    def encryptor(self,file_location,password):
            import copy
            file_name=[]
            l=file_location.split('/')
            file_name.append(l[-1])
            fi=open(file_location,"rb")
            data=fi.read().decode("utf")
            fi.close()
            newstr="" 
            for j in data:
                string = j
                for i  in range(len(string)):
                    element = string[i]
                    if element in d1:
                        newstr += d1[element]
                    elif element in d2:
                        newstr += d2[element]
                    else:
                        newstr += element

            modified_password=""
            for t in password:
                string = t
                for i  in range(len(string)):
                    element = string[i]
                    if element in d1:
                        modified_password += d1[element]
                    elif element in d2:
                        modified_password += d2[element]
                    else:
                        modified_password += element
            import os
            t=os.getcwd()
            file_string=str(t)+"\encrypted.json"
            json_file_location.append(file_string)
            f=open(file_string,"w")
            import json
            final_data={}
            final_data[file_name[0]]={"file_location":f"{file_location}","password":modified_password,"data":newstr}
            json.dump(final_data,f,indent=4,separators=(',',': '))
            f.close()

    def decryptor(self,filelocation):
            import copy
            import tkinter
            parent = tkinter.Tk()
            from tkinter import simpledialog
            from tkinter import messagebox
            import json
            with open(json_file_location[0]) as f:
                ddt = json.loads(f.read())

            for i in range(4):
                old_password = simpledialog.askstring('Enter Password', 'Enter password', parent=parent)
                d1={'z': 'A', 'y': 'B', 'x': 'C', 'w': 'D', 'v': 'E', 'u': 'F', 't': 'G', 's': 'H', 'r': 'I', 'q': 'J', 'p': 'K', 'o': 'L', 'n': 'M', 'm': 'N', 'l': 'O', 'k': 'P', 'j': 'Q', 'i': 'R', 'h': 'S', 'g': 'T', 'f': 'U', 'e': 'V', 'd': 'W', 'c': 'X', 'b': 'Y', 'a': 'Z'}
                d2={'Z': 'a', 'Y': 'b', 'X': 'c', 'W': 'd', 'V': 'e', 'U': 'f', 'T': 'g', 'S': 'h', 'R': 'i', 'Q': 'j', 'P': 'k', 'O': 'l', 'N': 'm', 'M': 'n', 'L': 'o', 'K': 'p', 'J': 'q', 'I': 'r', 'H': 's', 'G': 't', 'F': 'u', 'E': 'v', 'D': 'w', 'C': 'x', 'B': 'y', 'A': 'z'}
                def decript(x):
                    s=""
                    for i in x:
                        if i in d2:
                            s=s+d2[i]
                        elif i in d1:
                            s=s+d1[i]
                        else:
                            s=s+i
                    return s
                old_pas=decript(ddt[filelocation]["password"])
                
                if old_password == old_pas:
                    fileip=open(json_file_location[0],"r")
                    import json
                    data_needed=json.load(fileip)
                    k=data_needed[filelocation]['data']
                    d1={'z': 'A', 'y': 'B', 'x': 'C', 'w': 'D', 'v': 'E', 'u': 'F', 't': 'G', 's': 'H', 'r': 'I', 'q': 'J', 'p': 'K', 'o': 'L', 'n': 'M', 'm': 'N', 'l': 'O', 'k': 'P', 'j': 'Q', 'i': 'R', 'h': 'S', 'g': 'T', 'f': 'U', 'e': 'V', 'd': 'W', 'c': 'X', 'b': 'Y', 'a': 'Z'}
                    d2={'Z': 'a', 'Y': 'b', 'X': 'c', 'W': 'd', 'V': 'e', 'U': 'f', 'T': 'g', 'S': 'h', 'R': 'i', 'Q': 'j', 'P': 'k', 'O': 'l', 'N': 'm', 'M': 'n', 'L': 'o', 'K': 'p', 'J': 'q', 'I': 'r', 'H': 's', 'G': 't', 'F': 'u', 'E': 'v', 'D': 'w', 'C': 'x', 'B': 'y', 'A': 'z'}
                    def decript(x):
                        s=""
                        for i in x:
                            if i in d2:
                                s=s+d2[i]
                            elif i in d1:
                                s=s+d1[i]
                            else:
                                s=s+i
                        return s
                    decrypted=decript(k)
                    t=[i for i in data_needed.keys()]
                    import tkinter
                    parent = tkinter.Tk()
                    from tkinter import filedialog
                    write_file=filedialog.askdirectory( title='Please select the directory to save the file.', parent=parent)+"/"+t[0]
                    tyu=open(write_file,"wb")
                    dataff=decrypted.encode("utf")
                    tyu.write(dataff)
                    tyu.close()
                    break
                else:
                    print("INCORRECT PASSWORD")
                    if i==3:
                        print("Maximum attempts exceeded")
                        import datetime
                        from datetime import time
                        time = datetime.datetime.now()     
                        time = str(time.time())
                        time = time.split(":")
                        minute = int(time[1])
                        minute += 15
                        time = str(time[0])+":"+str(minute)
                        info = messagebox.showinfo('Maximum limit Exceeded!', "Try again after 15 minutes i.e after ( "+time+":00 )",parent=parent)
        
    def change_password(self,file_location):
            import copy
            import tkinter
            parent = tkinter.Tk()
            from tkinter import simpledialog
            from tkinter import messagebox
            import json
            with open(json_file_location[0]) as f:
                ddt = json.loads(f.read())

            for i in range(4):
                old_password = simpledialog.askstring('Enter Previous Password', 'Enter Previous password', parent=parent)
                d1={'z': 'A', 'y': 'B', 'x': 'C', 'w': 'D', 'v': 'E', 'u': 'F', 't': 'G', 's': 'H', 'r': 'I', 'q': 'J', 'p': 'K', 'o': 'L', 'n': 'M', 'm': 'N', 'l': 'O', 'k': 'P', 'j': 'Q', 'i': 'R', 'h': 'S', 'g': 'T', 'f': 'U', 'e': 'V', 'd': 'W', 'c': 'X', 'b': 'Y', 'a': 'Z'}
                d2={'Z': 'a', 'Y': 'b', 'X': 'c', 'W': 'd', 'V': 'e', 'U': 'f', 'T': 'g', 'S': 'h', 'R': 'i', 'Q': 'j', 'P': 'k', 'O': 'l', 'N': 'm', 'M': 'n', 'L': 'o', 'K': 'p', 'J': 'q', 'I': 'r', 'H': 's', 'G': 't', 'F': 'u', 'E': 'v', 'D': 'w', 'C': 'x', 'B': 'y', 'A': 'z'}
                def decript(x):
                    s=""
                    for i in x:
                        if i in d2:
                            s=s+d2[i]
                        elif i in d1:
                            s=s+d1[i]
                        else:
                            s=s+i
                    return s
                old_pas=decript(ddt[file_location]["password"])
                
                if old_password == old_pas:
                    while True:
                        passcode=simpledialog.askstring('Enter new Password', 'Enter new password', parent=parent)
                        if passcode==old_password:
                            info = messagebox.showinfo('Retry!', 'Old and New password Cannot be SAME!',parent=parent)
                            continue
                        sym=["@","#","$","%","&"]
                        d=0
                        l=0
                        u=0
                        s=0
                        if 1<len(passcode)<8:
                            error = messagebox.showerror('Weak password !', 'password length must be ">=8"',parent=parent)    
                        elif passcode=='':
                            empty = messagebox.showerror('Weak password !', 'password cannot be empty',parent=parent)
                        for i in passcode:
                            if i.isdigit():
                                d+=1
                            if i.islower():
                                l+=1
                            if i.isupper():
                                u+=1
                            if i in sym:
                                s+=1
                            else:
                                continue
                        
                        if d>0 and l>0 and u>0 and s>0 :
                            conf_passcode=simpledialog.askstring('Enter New Confirm Password', 'Enter New Confirm password', parent=parent)
                            if passcode == conf_passcode:
                                cnf=copy.copy(conf_passcode)
                                modified_one=""
                                for t in conf_passcode:
                                    string = t
                                    for i  in range(len(string)):
                                        element = string[i]
                                        if element in d1:
                                            modified_one += d1[element]
                                        elif element in d2:
                                            modified_one+= d2[element]
                                        else:
                                            modified_one += element
                                ddt[str(file_location)]["password"] = modified_one
                                info = messagebox.showinfo('New Password set successfully', 'Successfully Changed the Password!',parent=parent)
                                break
                            else:
                                info = messagebox.showinfo('Password Mismatch', "Your passwords didn't match Enter Again !",parent=parent)
                                continue
                        else:
                            error = messagebox.showerror('Weak password !', 'use symbols(@#%&$),Numbers with lower and uppercase letters',parent=parent)
                            continue
                            
                    with open(json_file_location[0],"w") as f:
                        json.dump(ddt,f,indent=4,separators=(',',': '))
                    print("Password updated successfully")
                    break
                else:
                    print("INCORRECT PASSWORD")
                    if i==3:
                        print("Maximum attempts exceeded")
                        import datetime
                        from datetime import time
                        time = datetime.datetime.now()     
                        time = str(time.time())
                        time = time.split(":")
                        minute = int(time[1])
                        minute += 15
                        time = str(time[0])+":"+str(minute)
                        info = messagebox.showinfo('Maximum limit Exceeded!', "Try again after 15 minutes i.e after ( "+time+":00 )",parent=parent)

import copy
import tkinter
parent = tkinter.Tk()
from tkinter import simpledialog
from tkinter import messagebox
info = messagebox.showinfo('Welcome!', 'Welcome to Caesar cipher Cryptography!',parent=parent)
required_password=[]
while True:
    tasks=["(1). Encrypt a file.","(2). Decrypt a file.","(3). Change the password for the file.","(4). EXIT from the program."]
    for i in tasks:
        print(i)
    user_input=int(input("what would you like to do ? Enter an option : "))
    
    if user_input==1:
        from tkinter import filedialog
        file_imported = filedialog.askopenfilename( title='Please select a file:', parent=parent) 
        while True:
            passcode=string_value = simpledialog.askstring('Enter Password', 'Enter password', parent=parent)
            sym=["@","#","$","%","&"]
            d=0
            l=0
            u=0
            s=0
            if 1<len(passcode)<8:
                error = messagebox.showerror('Weak password !', 'password length must be ">=8"',parent=parent)    
            elif passcode=='':
                empty = messagebox.showerror('Weak password !', 'password cannot be empty',parent=parent)
            for i in passcode:
                if i.isdigit():
                    d+=1
                if i.islower():
                    l+=1
                if i.isupper():
                    u+=1
                if i in sym:
                    s+=1
                else:
                    continue
            
            if d>0 and l>0 and u>0 and s>0 :
                conf_passcode=simpledialog.askstring('Enter Password', 'Enter Confirm password', parent=parent)
                if passcode == conf_passcode:
                    cnf=copy.copy(conf_passcode)
                    required_password.append(conf_passcode)
                    
                    info = messagebox.showinfo('Password set successfully', 'YAY! you have created a strong password.',parent=parent)
                    break
                else:
                    info = messagebox.showinfo('Password Mismatch', "Your passwords didn't match Enter Again !",parent=parent)
                    continue
            else:
                error = messagebox.showerror('Weak password !', 'use symbols(@#%&$),Numbers with lower and uppercase letters',parent=parent)
                continue
        call=encryption(file_imported) 
        call.encryptor(file_imported,required_password[0])
    elif user_input==2:
        import json
        try:
            with open(json_file_location[0],"r")as flop:
                ddt = json.loads(flop.read())
        except:
            file_types = [('JSON files', '*.json;*.pyw')] 
            from tkinter import filedialog
            file_name = filedialog.askopenfilename(title='Select a JSON file', filetypes=file_types,parent=parent)
            json_file_location.append(file_name)
            with open(json_file_location[0],"r")as flop:
                ddt = json.loads(flop.read())
        flop.close()
        lst=[i for i in ddt.keys()]
        dic={i+1:lst[i] for i in range(len(lst))}
        print("Which file you want to decrypt choose a number!")
        for i in dic.keys():
            print(f"({i}). {dic[i]}")
        imp=int(input("Enter your choice number :^) "))
        call=encryption(dic[imp]) 
        call.decryptor(dic[imp])
    
    elif user_input==3:
        import json
        try:
            with open(json_file_location[0],"r")as flop:
                ddt = json.loads(flop.read())
        except:
            file_types = [('JSON files', '*.json;*.pyw')] 
            from tkinter import filedialog
            file_name = filedialog.askopenfilename(title='Select a JSON file', filetypes=file_types,parent=parent)
            json_file_location.append(file_name)
            with open(json_file_location[0],"r")as flop:
                ddt = json.loads(flop.read())
        flop.close()
        lst=[i for i in ddt.keys()]
        dic={i+1:lst[i] for i in range(len(lst))}
        print("Which file you want to decrypt choose a number!")
        for i in dic.keys():
            print(f"({i}). {dic[i]}")
        imp=int(input("Enter your choice number :^) "))
        
        call=encryption(dic[imp]) 
        call.change_password(dic[imp])
        
    elif user_input==4:
        try:
            print()
            print("You have successfully exited from the program!")
            info = messagebox.showinfo('Exited!', 'You have successfully exited from the program.',parent=parent)
            break
        except:
            break



