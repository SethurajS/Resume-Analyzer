
""" Importing the requirements """

from tkinter import *
from tkinter import filedialog
from ttkthemes import themed_tk as tk
import tkinter.messagebox
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import HTMLConverter
from pdfminer.pdfpage import PDFPage
from tkinter import ttk
import io
import bs4
import nltk
import re
from nltk.corpus import stopwords
stop = stopwords.words('english')
import shutil


""""""""""""""""""""""""""""""""""""""""""""""""" ANALYZER GUI """""""""""""""""""""""""""""""""""""""""""""

""" Title """
root = tk.ThemedTk()
root.get_themes()
root.set_theme("radiance")
root.title("CV_Analyzer")


""" Menu bar """
menubar = Menu(root, activeborderwidth=0)
root.config(menu=menubar, highlightthickness=0)
root.config(bg='#ddd', menu=menubar)


""" Sub menus """
subMenu1 = Menu(menubar, tearoff=0)
subMenu2 = Menu(menubar, tearoff=0)
subMenu3 = Menu(menubar, tearoff=0)

""" Themes for GUI """
def _Light_Theme():
    root.configure(bg='#eee')
    subMenu1.configure(bg="#eee", fg='#161b21')
    subMenu2.configure(bg="#eee", fg='#161b21')
    subMenu3.configure(bg="#eee", fg='#161b21')
    f1.configure(bg="#eee")
    f2.configure(bg="#eee")
    f3.configure(bg="#eee")
    f4.configure(bg="#eee")
    label.configure(bg="#eee", fg='#161b21')
    label1.configure(bg="#eee", fg='#161b21')
    label2.configure(bg="#eee", fg='#161b21')
    label3.configure(bg="#eee", fg='#161b21')
    qualification.configure(bg="#eee", fg='#161b21')
    experience.configure(bg="#eee", fg='#161b21')
    coding.configure(bg="#eee", fg='#161b21')
    skillss.configure(bg="#eee", fg='#161b21')

def _Dark_Theme():
    root.configure(bg='#161b21')
    subMenu1.configure(bg="#161b21", fg='#eee')
    subMenu2.configure(bg="#161b21", fg='#eee')
    subMenu3.configure(bg="#161b21", fg='#eee')
    f1.configure(bg="#161b21")
    f2.configure(bg="#161b21")
    f3.configure(bg="#161b21")
    f4.configure(bg="#161b21")
    label.configure(bg="#161b21", fg='#eee')
    label1.configure(bg="#161b21", fg='#eee')
    label2.configure(bg="#161b21", fg='#eee')
    label3.configure(bg="#161b21", fg='#eee')
    qualification.configure(bg="#161b21", fg='#eee')
    experience.configure(bg="#161b21", fg='#eee')
    coding.configure(bg="#161b21", fg='#eee')
    skillss.configure(bg="#eee", fg='#161b21')


""" Functions for GUI """

def _browse():
    raise_frame(f3)

def _quit():
    root.quit()

def _about():

    tkinter.messagebox.showinfo(
        'CV_analyzer','Cv_Analyser 1.0   "An NLP and ML implementation"\n'
        '\n@ cv.analyzer@gmail.com\n\n'
        'Verifies CVs and arrange them according to companies requirements.'
    )


""" Menu bar & sub bar """
menubar.add_cascade(label="File", menu=subMenu1)
subMenu1.add_command(label="Open", command=_browse)
subMenu1.add_command(label="Exit", command=_quit)

menubar.add_cascade(label="Settings", menu=subMenu2)
subMenu2.add_command(label="Light Theme", command_=_Light_Theme)
subMenu2.add_command(label="Dark Theme", command_=_Dark_Theme)

menubar.add_cascade(label="About", menu=subMenu3)
subMenu3.add_command(label="About CV_Analyzer", command=_about)

""" Window Configurations """

root.geometry('700x500')
root.configure(bg='#eee')
root.iconbitmap(r'cv_analyzer.ico')
root.resizable(0, 0)


def raise_frame(frame):
    frame.tkraise()


f1 = Frame(root)
f2 = Frame(root)
f3 = Frame(root)
f4 = Frame(root)

for frame in (f1, f2, f3, f4):
    frame.grid(row=0, column=0, sticky='news')


""""""""""""""""""""""""""""""""""""""""""""" CODE FOR ANALYZER """""""""""""""""""""""""""""""""""""""""


""" Function for extracting text from PDF """

path = ''
def extract_text_from_pdf(pdf_path):
    global path
    path=pdf_path
    resource_manager = PDFResourceManager()
    fake_file_handle = io.BytesIO()
    converter = HTMLConverter(resource_manager, fake_file_handle)
    page_interpreter = PDFPageInterpreter(resource_manager, converter)
    with open(pdf_path, 'rb') as fh:
        for page in PDFPage.get_pages(fh,
                                      caching=True,
                                      check_extractable=True):
            page_interpreter.process_page(page)
        text = fake_file_handle.getvalue()
    converter.close()
    fake_file_handle.close()
    if text:
        return text


""" Extracting text from PDF files """


def _browse(case):
    if __name__ == '__main__':
        convert = (extract_text_from_pdf(filedialog.askopenfilename()))
        fileHTML = 'D:/Project/SETHU CVS/pdfconverted1.html'
    if case == 'HTML' :
        fileConverted = open(fileHTML, "wb")
        fileConverted.write(convert)
        fileConverted.close()


""" Reverse Engineering """

datas = []
def reverseEng():
    f = open('D:/Project/SETHU CVS/pdfconverted1.html', 'r')
    html_string = f.read()
    new_file = open('new_file.txt', 'w')
    new_file.write(html_string)
    soup = bs4.BeautifulSoup(html_string,"html.parser")
    soup.get_text()
    converted = open('converted_text.txt', 'w')
    converted.write(soup.get_text())
    f.close()
    if converted:
        tkinter.messagebox.showinfo('CV_analyzer', 'Reverse engineering completed')
    converted.close()
    new_file.close()

    with open("D:/Project/SETHU CVS/converted_text.txt") as file:
        lines = file.read().split()
        global datas
        datas = lines
        print(datas)
        return datas


""" Comparing Data """


li = []
def get_data(values):
    global li
    li.append(values)
    print(li)
    return li


pcount = 0
ncount = 0
def compare():
    globals()['pcount'] = 0
    globals()['ncount'] = 0

    for i in li:
        for j in datas:
            if (i == j):
                globals()['pcount'] = pcount + 1
            else:
                globals()['ncount'] = ncount - 1
    print(pcount)


""" Extracting essential features for displaying """


def extract_phone_numbers(stringdata):
    r = re.compile(r'(\d{3}[-\.\s]??\d{3}[-\.\s]??\d{4}|\(\d{3}\)\s*\d{3}[-\.\s]??\d{4}|\d{3}[-\.\s]??\d{4})')
    phone_numbers = r.findall(stringdata)
    return [re.sub(r'\D', '', number) for number in phone_numbers]


def extract_email_addresses(stringdata):
    r = re.compile(r'[\w\.-]+@[\w\.-]+')
    return r.findall(stringdata)


def ie_preprocess(stringdata):
    stringdata = ' '.join([i for i in stringdata.split() if i not in stop])
    sentences = nltk.sent_tokenize(stringdata)
    sentences = [nltk.word_tokenize(sent) for sent in sentences]
    sentences = [nltk.pos_tag(sent) for sent in sentences]
    return sentences

def extract_names(stringdata):
    names = []
    sentences = ie_preprocess(stringdata)
    for tagged_sentence in sentences:
        for chunk in nltk.ne_chunk(tagged_sentence):
            if type(chunk) == nltk.tree.Tree:
                if chunk.label() == 'PERSON':
                    names.append(' '.join([c[0] for c in chunk]))
    return names


""" Checking new Resumes/CVs """


def check():

    if(pcount>(len(li)/2)):
        tkinter.messagebox.showinfo(
                                    'CV_Analyzer',
                                    'Analysis Completed : ''GooD'
                                    )

        with open("D:/Project/SETHU CVS/converted_text.txt") as file:
            stringdata = file.read()

        numbers = extract_phone_numbers(stringdata)
        emails = extract_email_addresses(stringdata)
        names = extract_names(stringdata)
        info = open('goodresumeinfo.csv', 'w')
        num = ', '.join(numbers)
        mails = ', '.join(emails)
        name = ', '.join(names)
        print("The name is ", name)
        print("The phone number is ", num)
        print("The email address is ", mails)
        shutil.copy(path, 'D:/Project/SETHU CVS/GoodResumes/')
        info.write(num)
        info.write(mails)
        info.close()

    else:
        tkinter.messagebox.showinfo(
                                    'CV_Analyzer',
                                    'Analysis Completed : ''NoT GooD'
                                    )

        with open("D:/Project/SETHU CVS/converted_text.txt") as file:  # file "converted.txt" opened.
            stringdata = file.read()

        numbers = extract_phone_numbers(stringdata)
        emails = extract_email_addresses(stringdata)
        names = extract_names(stringdata)
        info = open('badresumeinfo.csv', 'w')
        num = ', '.join(numbers)
        mails = ', '.join(emails)
        name = ', '.join(names)
        print("The name is ", name)
        print("The phone number is ", num)
        print("The email address is ", mails)
        shutil.copy(path, 'D:/Project/SETHU CVS/BadResumes')

        info.write(name)
        info.write(num)
        info.write(mails)
        info.close()


def check_another():
    datas_clear()
    globals()['pcount'] = 0
    globals()['ncount'] = 0


def new():
    globals()['pcount'] = 0
    globals()['ncount'] = 0
    datas_clear()
    li.clear()
    variable.set(None)
    variable1.set(None)
    variable2.set(None)
    variable3.set(None)
    variable4.set(None)
    variable5.set(None)
    variable7.set(None)
    print(li)


def datas_clear():
    datas.clear()


""" Requirement selection for analyzing new CVs """


var = StringVar()
label3 = Label( f1, textvariable=var)
label3.configure(font=("Helvetica", "13"))
var.set("\n\nInput Your 'REQUIREMENTS'")
label3.pack()
label3.place(x=235,y=0)

var1 = StringVar()
qualification = Label( f1, textvariable=var1)
var1.set("Qualification")
qualification.pack()
qualification.place(x=190, y=90)

var2 = StringVar()
experience = Label( f1, textvariable=var2)
var2.set("Experiences")
experience.pack()
experience.place(x=190, y=140)

var3 = StringVar()
coding = Label( f1, textvariable=var3)
var3.set("Coding")
coding.pack()
coding.place(x=190, y=190)

var4 = StringVar()
skillss = Label( f1, textvariable=var4)
var4.set("Skills")
skillss.pack()
skillss.place(x=190, y=240)


analysebtn = ttk.Button(
                        f1, text="Analyse",
                        command=lambda: [compare(), check()]
                        ).place(x=180, y=340)

analysebtnss = ttk.Button(
                        f1, text="Check_Another",
                        command=lambda: [check_another, raise_frame(f3)]
                        ).place(x=320, y=340)

analysebtnsss = ttk.Button(
                        f1, text="Clear_ReQ",
                        command=lambda: [new(), raise_frame(f3)]
                        ).place(x=470, y=340)


variable = StringVar(f1)
variable.set(None)
qualifications = ttk.OptionMenu(
                                f1, variable, "None", "MCA",
                                "BCA", "Btech", "Mtech",
                                command=get_data
                                ).place(x=290, y=90)

variable1 = StringVar(f1)
variable1.set(None)
experiences = ttk.OptionMenu(
                            f1, variable1, "None", "Fresher",
                            "OneYear", "TwoYears", "FiveYears",
                            command=get_data
                            ).place(x=290, y=140)

variable2 = StringVar(f1)
variable2.set(None)
language1 = ttk.OptionMenu(
                            f1, variable2, "None", "C++", "C#",
                            "Java", "Python", "JavaScript",
                            "PHP", "HTML", "MySQL",
                            "CSS", "Kotlin", "Android",
                            command=get_data
                            ).place(x=290, y=190)

variable3 = StringVar(f1)
variable3.set(None)
language2 = ttk.OptionMenu(
                            f1, variable3, "None", "C++", "Kotlin",
                            "Android", "C#", "Java", "Python", "JS",
                            "JQuery", "PHP", "HTML", "MySQL", "CSS",
                            command=get_data
                            ).place(x=370, y=190)

variable4 = StringVar(f1)
variable4.set(None)
language3 = ttk.OptionMenu(
                            f1, variable4, "None", "C++" , "C#", "Kotlin",
                            "Android", "Java", "Python", "JS", "JQuery",
                            "PHP", "HTML", "MySQL", "CSS",
                            command=get_data
                            ).place(x=450, y=190)

variable5 = StringVar(f1)
variable5.set(None)
language4 = ttk.OptionMenu(
                            f1, variable5, "None", "C++", "C#", "Java",
                            "Python", "JS", "JQuery", "Kotlin", "Android",
                            "PHP", "HTML", "MySQL", "CSS",
                            command=get_data
                            ).place(x=530, y=190)

variable7 = StringVar(f1)
variable7.set(None)
skills = ttk.OptionMenu(
                        f1, variable7, "None", "Creativity", "Networking",
                        "Interpersonal", "Positive", "TeamWork",
                         command=get_data
                        ).place(x=290, y=240)


""" Button GUIs """

ttk.Button(f3,text="Upload_CV",command=lambda:[_browse(case='HTML'),raise_frame(f2)]).pack(pady=(210),padx=(260))
ttk.Button(f2,text="ReverseEngineering",command=lambda:[reverseEng(),raise_frame(f1)]).pack(pady=(210),padx=(260))
ttk.Button(f4, text='Start processing', command=lambda:raise_frame(f3)).pack(pady=(210),padx=(290))

var = StringVar()
label = Label( f4, textvariable=var)
labelname = "CV_Analyzer"
labelname.casefold()
label.configure(font=("Helvetica", "13"))
var.set(labelname+"\n\nA Machine Learning and NLP innovative\n for analysing 'RESUMES' ")
label.pack()
label.place(x=215,y=120)

var = StringVar()
label1 = Label( f3, textvariable=var)
labelname.casefold()
label1.configure(font=("Helvetica", "13"))
var.set(labelname+"\n\nUpload the resume that \nyou need to analyse. ")
label1.pack()
label1.place(x=270,y=120)

var = StringVar()
label2 = Label( f2, textvariable=var)
labelname.casefold()
label2.configure(font=("Helvetica", "13"))
var.set(labelname+"\n\nArt of breaking files into \nit's simple form. ")
label2.pack()
label2.place(x=270,y=120)


root.mainloop()


