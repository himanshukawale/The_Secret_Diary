from tkinter import ttk
import tkinter as tk
import ast
hrk_secret_dict = {'a': '!', 'b': '@', 'c': '#', 'd': '$', 'e': '%', 'f': '^', 'g': '&', 'h': '*','i': '(', 'j': ')', 'k': '_', 'l': '+', 'm': '|', 'n': '}', 'o': '{', 'p': ':','q': ';', 'r': ']', 's': '[', 't': '0', 'u': '=', 'v': '-', 'w': ',', 'x': '.','y': '/', 'z': '?', ' ': '1', '!': 'a', '@': 'b', '#': 'c', '$': 'd', '%': 'e', '^': 'f', '&': 'g', '*': 'h', '(': 'i', ')': 'j','_': 'k', '+': 'l', '|': 'm', '}': 'n', '{': 'o', ':': 'p', ';': 'q', ']': 'r', '[': 's', '0': 't', '=': 'u', '-': 'v', ',': 'w','.': 'x', '/': 'y', '?': 'z', '"': '2', "'": "3"}

def create_dict(user_str):
    splited_str = user_str.split(":")
    i = 1
    key_list = []
    value_list = []

    for item in splited_str:
        q = i % 2
        if q == 0:
            value_list.append(item)
        else:
            key_list.append(item)
        i += 1
    created_dict = {}

    for key in key_list:
        for value in value_list:
            created_dict[key] = value
            value_list.remove(value)
            break

    return created_dict

def generate_hrk_code(inp1, in_file):
    inp = str(inp1)
    print(inp)
    converted = ""
    i = 0
    u = 0
    p_letter = None

    for letter in inp:
        letter = letter.lower()
        s_letter = hrk_secret_dict.get(letter)
        print(letter)
        print(s_letter)
        if u == 1:
            u = 0
            continue
        if s_letter == None:
            u += 1
            continue
        converted += s_letter
        i += 1
        if i > 100 and p_letter == ",":
            converted += "\n"
            i = 0
        p_letter = s_letter

    with open(in_file, "a") as f1:
        f1.writelines(f"{converted}\n")

def read_hrk_code(read_file):
    string = ""
    is_dict = 0
    temp_str = ""
    dict1 = {}
    i = 0

    with open(read_file, "r") as f:
        for lines in f.readlines():
            for items in lines:
                for key, value in hrk_secret_dict.items():
                    if items == value:
                        if key == "{":
                            is_dict = 1
                            i += 1
                        if is_dict == 1:
                            temp_str += key
                            if key == "}":
                                is_dict = 0
                                dict1[i] = temp_str
                                temp_str = ""
                        else:
                            string += key
            if is_dict != 1:
                string += "\n"
    return string, dict1

read_file = None
fil = None
y = None
searcht = None
wfil = None
wtext = None

def search():
    global read_file
    global fil
    global y
   # read_file=fil.get("text")
    # read_file=(fil.get())
    read_file = y
    if read_file == None:
        read_file = input("Enter a file name\n")
        # read_file=fil
    x = read_hrk_code(read_file)
    normal_text = x[0]
    dictionary = x[1]
    return normal_text, dictionary

# # Welcome screen
root = tk.Tk()
root.geometry("1500x1000")

i = 0

def display():
    global searcht
    disp = tk.Frame(bg="#001840")
    para = tk.Label(disp, text="Here's what we found",
                    bg="#001840", fg="white", font=("Eras Demi ITC", 25))
    para.pack(side="top", pady=90, anchor="n")
    okbtn = tk.Button(disp, text="OK", width=13, height=2, bg="#2982ff",
                      fg="white", font=("Eras Demi ITC", 12), command=home)
    okbtn.place(x=610, y=790)
    disp.place(width="1500", height="1000",
               rely=0.5, relx=0.5, anchor="center")

    if str(searcht.get()) != "" and i == 1:
        search_inp = str(searcht.get())
        for num, dicts in search()[1].items():
            num = ast.literal_eval(dicts)
            if search_inp in dicts:
                for key, value in num.items():
                    if search_inp in value:
                        print(num)
                        show = num
                        leb = tk.Label(disp, text=show, bg="#599eff",
                                       fg="white", font=("Eras Demi ITC", 14))
                        leb.place(x=250, y=180, width=1000, height=600,)
                    elif search_inp == key:
                        print(value)
                        show = value
                        leb = tk.Label(disp, text=show, bg="#599eff",
                                       fg="white", font=("Eras Demi ITC", 14))
                        leb.place(x=250, y=180, width=1000, height=600,)

    elif i == 2:
        print(search()[1])
        print(search()[0])
        show = f"{search()[1]}\n{search()[0]}"
        leb = tk.Label(disp, text=show, bg="#599eff",
                       fg="white", font=("Eras Demi ITC", 14))
        leb.place(x=250, y=180, width=1000, height=600,)

def iv1():
    global i
    global y
    y = str(fil.get())
    i = 1
    display()

def iv2():
    global i
    global y
    i = 2
    y = str(fil.get())
    display()

def Read():
    global read_file
    global fil
    global y
    global searcht
    read = tk.Frame(bg="#001840")
    para1 = tk.Label(read, text="Enter a file name (*)",
                     bg="#001840", fg="white", font=("Eras Demi ITC", 18))
    para1.place(x=460, y=200)
    fil = tk.Entry(read, width=25, font=("Arial", 20))
    fil.place(x=700, y=200)
    b1 = tk.Button(read, text="Read file", width=13, height=2,
                   bg="#2982ff", fg="white", font=("Eras Demi ITC", 12), command=iv2)
    b1.place(x=700, y=250)
    para2 = tk.Label(read, text="Enter something, you want to search (Optional)",
                     bg="#001840", fg="white", font=("Eras Demi ITC", 18))
    para2.place(x=150, y=400)
    searcht = tk.Entry(read, width=25, font=("Arial", 20))
    searcht.place(x=700, y=400)
    b2 = tk.Button(read, text="Search", width=13, height=2, bg="#2982ff",
                   fg="white", font=("Eras Demi ITC", 12), command=iv1)
    b2.place(x=700, y=450)
    backbtn = tk.Button(read, text="Back", width=13, height=2, bg="#2982ff",
                        fg="white", font=("Eras Demi ITC", 12), command=home)
    backbtn.place(x=610, y=790)
    read.place(width="1500", height="1000",
               rely=0.5, relx=0.5, anchor="center")

def submit_nor():
    global wfil
    global wtext
    user_text = str(wtext.get("1.0", "end"))
    user_file = str(wfil.get())
    generate_hrk_code(user_text, user_file)
    home()

def Write_nor():
    global wfil
    global wtext
    writ = tk.Frame(bg="#001840")
    para = tk.Label(writ, text="Enter a file name (*)",
                    bg="#001840", fg="white", font=("Eras Demi ITC", 18))
    para.place(x=460, y=197)
    wfil = tk.Entry(writ, width=25, bg="#2982ff",
                    fg="white", font=("Eras Demi ITC", 14),)
    wfil.place(x=700, y=200)
    para = tk.Label(writ, text="Write here, you want to convert\ninto the secret code",
                    bg="#001840", fg="white", font=("Eras Demi ITC", 18))
    para.place(x=300, y=400)
    wtext = tk.Text(writ, bg="#2982ff", fg="white",
                    font=("Eras Demi ITC", 14),)
    wtext.place(x=700, y=290, width=700, height=450)
    submitbtn = tk.Button(writ, text="Submit", width=13, height=2, bg="#2982ff",
                          fg="white", font=("Eras Demi ITC", 12), command=submit_nor)
    submitbtn.place(x=610, y=790)
    backbtn = tk.Button(writ, text="Back", width=5, height=1, bg="#2982ff",
                        fg="white", font=("Eras Demi ITC", 12), command=home)
    backbtn.place(x=50, y=90)
    writ.place(width="1500", height="1000",
               rely=0.5, relx=0.5, anchor="center")

def submit_dict():
    global wfil
    global wtext
    user_text = str(wtext.get("1.0", "end"))
    user_file = str(wfil.get())
    generate_hrk_code(create_dict(user_text), user_file)
    home()

def write_dict():
    global wfil
    global wtext
    writ1 = tk.Frame(bg="#001840")
    para1 = tk.Label(writ1, text="Enter a file name (*)",
                     bg="#001840", fg="white", font=("Eras Demi ITC", 18))
    para1.place(x=460, y=197)
    wfil = tk.Entry(writ1, width=25, bg="#2982ff",
                    fg="white", font=("Eras Demi ITC", 14),)
    wfil.place(x=700, y=200)
    para1 = tk.Label(writ1, text="Write your dictionary here\nUse (:) as a seperator as shown below\nkey1:value1:key2:value2:key3:value3....",
                     bg="#001840", fg="white", font=("Eras Demi ITC", 18))
    para1.place(x=200, y=350)
    wtext = tk.Text(writ1, bg="#2982ff", fg="white",
                    font=("Eras Demi ITC", 14),)
    wtext.place(x=700, y=290, width=700, height=450)
    submitbtn = tk.Button(writ1, text="Submit", width=13, height=2, bg="#2982ff",
                          fg="white", font=("Eras Demi ITC", 12), command=submit_dict)
    submitbtn.place(x=610, y=790)
    backbtn = tk.Button(writ1, text="Back", width=5, height=1, bg="#2982ff",
                        fg="white", font=("Eras Demi ITC", 12), command=home)
    backbtn.place(x=50, y=90)
    writ1.place(width="1500", height="1000",
                rely=0.5, relx=0.5, anchor="center")


def home():
    hom = tk.Frame(bg="#001840")
    def twobtn():
        dictbtn = tk.Button(hom, text="Dictionary", width=13, height=2, bg="#2982ff",
                            fg="white", font=("Eras Demi ITC", 12), command=write_dict)
        dictbtn.place(x=800, y=550)
        norbtn = tk.Button(hom, text="Normal text", width=13, height=2, bg="#2982ff",
                           fg="white", font=("Eras Demi ITC", 12), command=Write_nor)
        norbtn.place(x=800, y=500)
    heading = tk.Label(hom, text="Welcome HRk\nThis is secret code converter", font=(
        "Algerian", 50), bg="#001840", fg="white")
    heading.pack(side="top", pady=90, anchor="n")
    b1 = tk.Button(hom, text="Read", width=13, height=2, bg="#2982ff",
                   fg="white", font=("Eras Demi ITC", 12), command=Read)
    b1.place(x=500, y=500)
    b2 = tk.Button(hom, text="Write", width=13, height=2, bg="#2982ff",
                   fg="white", font=("Eras Demi ITC", 12), command=twobtn)
    b2.place(x=800, y=500)
    hom.place(width="1500", height="1000", rely=0.5, relx=0.5, anchor="center")

home()
tk.mainloop()
