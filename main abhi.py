from tkinter import *
from tkinter import ttk, messagebox

class Students:
    def __init__(self, root):
        self.root = root
        self.root.title('Student Management System')
        self.root.geometry('1350x720+0+0')
        title = Label(self.root, text='Student Management System', font=('times new roman', 30, 'bold'),
                      bg='yellow', fg='red', bd=10, relief=GROOVE)
        title.pack(side=TOP, fill=X)

        # ====================Variable=======================
        self.s_id = StringVar()
        self.f_name = StringVar()
        self.s_name = StringVar()
        self.c_code = StringVar()
        self.exam_no = StringVar()
        self.t_score = StringVar()
        self.average = StringVar()
        self.ranking = StringVar()

        self.hindi = IntVar()
        self.english = IntVar()
        self.python = IntVar()
        self.physics = IntVar()
        self.computing = IntVar()
        self.business = IntVar()
        self.biology = IntVar()

        # ===============================Frames=================
        F1 = Frame(self.root, bg='#00ffff', relief=RIDGE, bd=4)
        F1.place(x=10, y=65, width=900, height=370)

        F3 = Frame(self.root, relief=RIDGE, bd=4)
        F3.place(x=10, y=440, width=1330, height=190)

        F4 = Frame(self.root, bg='#00ffff', relief=RIDGE, bd=4)
        F4.place(x=10, y=635, width=1330, height=80)

        # ===================Student details=====================
        lbl_id = Label(F1, text='Student ID', bg='#00ffff', font=('times new roman', 18, 'bold'))
        lbl_id.grid(row=0, column=0, padx=20, pady=5, sticky='w')
        txt_id = Entry(F1, font=('times new roman', 15, 'bold'), bd=5, relief=GROOVE, textvariable=self.s_id)
        txt_id.grid(row=0, column=1, pady=5)

        lbl_fn = Label(F1, text='First Name:', bg='#00ffff', fg='black', font=('times new roman', 18, 'bold'))
        lbl_fn.grid(row=1, column=0, padx=20, pady=5, sticky='w')
        txt_fn = Entry(F1, font=('times new roman', 15, 'bold'), bd=5, relief=GROOVE, textvariable=self.f_name)
        txt_fn.grid(row=1, column=1, pady=5, sticky="w")

        lbl_s = Label(F1, text="Surname:", bg='#00ffff', fg='black', font=("times new roman", 18, 'bold'))
        lbl_s.grid(row=2, column=0, pady=5, padx=20, sticky="w")
        txt_s = Entry(F1, font=("times new roman", 15, 'bold'), bd=5, relief=GROOVE, textvariable=self.s_name)
        txt_s.grid(row=2, column=1, pady=5, sticky="w")

        lbl_cc = Label(F1, text="Course Code:", bg='#00ffff', fg='black', font=("times new roman", 18, 'bold'))
        lbl_cc.grid(row=3, column=0, pady=5, padx=20, sticky="w")

        combo_cc = ttk.Combobox(F1, font=("times new roman", 15, 'bold'), state='readonly', width=18, textvariable=self.c_code)
        combo_cc['values'] = ('CC1255', 'CC1256', 'CC1257', 'CC1258', 'CC1259')
        combo_cc.grid(row=3, column=1, pady=5, sticky='w')

        lbl_en = Label(F1, text="Exam No.", bg='#00ffff', fg='black', font=("times new roman", 18, 'bold'))
        lbl_en.grid(row=4, column=0, pady=5, padx=20, sticky="w")
        txt_en = Entry(F1, font=("times new roman", 15, 'bold'), bd=5, relief=GROOVE, textvariable=self.exam_no)
        txt_en.grid(row=4, column=1, pady=5, sticky="w")

        lbl_ts = Label(F1, text="Total Score:", bg='#00ffff', fg='black', font=("times new roman", 18, 'bold'))
        lbl_ts.grid(row=5, column=0, pady=5, padx=20, sticky="w")
        txt_ts = Entry(F1, font=("times new roman", 15, 'bold'), bd=5, relief=GROOVE, textvariable=self.t_score,
                       state=DISABLED)
        txt_ts.grid(row=5, column=1, pady=5, sticky="w")

        lbl_avg = Label(F1, text="Percentage:", bg='#00ffff', fg='black', font=("times new roman", 18, 'bold'))
        lbl_avg.grid(row=6, column=0, pady=5, padx=20, sticky="w")
        txt_avg = Entry(F1, font=("times new roman", 15, 'bold'), bd=5, relief=GROOVE, textvariable=self.average,
                        state=DISABLED)
        txt_avg.grid(row=6, column=1, pady=5, sticky="w")

        lbl_rank = Label(F1, text="Division:", bg='#00ffff', fg='black', font=("times new roman", 18, 'bold'))
        lbl_rank.grid(row=7, column=0, pady=5, padx=20, sticky="w")
        txt_rank = Entry(F1, font=("times new roman", 15, 'bold'), bd=5, relief=GROOVE, textvariable=self.ranking,
                         state=DISABLED)
        txt_rank.grid(row=7, column=1, pady=5, sticky="w")

        # =============================Subjects=========================
        lbl_h = Label(F1, text="Hindi", bg='#00ffff', fg='black', font=("times new roman", 18, 'bold'))
        lbl_h.grid(row=0, column=2, pady=5, padx=40, sticky="w")
        txt_h = Entry(F1, font=("times new roman", 15, 'bold'), bd=5, relief=GROOVE, textvariable=self.hindi)
        txt_h.grid(row=0, column=3, pady=5, sticky="w")

        lbl_e = Label(F1, text="English", bg='#00ffff', fg='black', font=("times new roman", 18, 'bold'))
        lbl_e.grid(row=1, column=2, pady=5, padx=40, sticky="w")
        txt_e = Entry(F1, font=("times new roman", 15, 'bold'), bd=5, relief=GROOVE, textvariable=self.english)
        txt_e.grid(row=1, column=3, pady=5, sticky="w")

        lbl_p = Label(F1, text="Python:", bg='#00ffff', fg='black', font=("times new roman", 18, 'bold'))
        lbl_p.grid(row=2, column=2, pady=5, padx=40, sticky="w")
        txt_p = Entry(F1, font=("times new roman", 15, 'bold'), bd=5, relief=GROOVE, textvariable=self.python)
        txt_p.grid(row=2, column=3, pady=5, sticky="w")

        lbl_ph = Label(F1, text="Physics:", bg='#00ffff', fg='black', font=("times new roman", 18, 'bold'))
        lbl_ph.grid(row=3, column=2, pady=5, padx=40, sticky="w")
        txt_ph = Entry(F1, font=("times new roman", 15, 'bold'), bd=5, relief=GROOVE, textvariable=self.physics)
        txt_ph.grid(row=3, column=3, pady=5, sticky="w")

        lbl_c = Label(F1, text="Computing:", bg='#00ffff', fg='black', font=("times new roman", 18, 'bold'))
        lbl_c.grid(row=4, column=2, pady=5, padx=40, sticky="w")
        txt_c = Entry(F1, font=("times new roman", 15, 'bold'), bd=5, relief=GROOVE, textvariable=self.computing)
        txt_c.grid(row=4, column=3, pady=5, sticky="w")

        lbl_b = Label(F1, text="Biology:", bg='#00ffff', fg='black', font=("times new roman", 18, 'bold'))
        lbl_b.grid(row=5, column=2, pady=5, padx=40, sticky="w")
        txt_b = Entry(F1, font=("times new roman", 15, 'bold'), bd=5, relief=GROOVE, textvariable=self.biology)
        txt_b.grid(row=5, column=3, pady=5, sticky="w")

        lbl_bu = Label(F1, text="Business:", bg='#00ffff', fg='black', font=("times new roman", 18, 'bold'))
        lbl_bu.grid(row=6, column=2, pady=5, padx=40, sticky="w")
        txt_bu = Entry(F1, font=("times new roman", 15, 'bold'), bd=5, relief=GROOVE, textvariable=self.business)
        txt_bu.grid(row=6, column=3, pady=5, sticky="w")

        # ===============================Button=================
        btn_add = Button(F4, text='Add Student', bg='green', fg='white', font=('times new roman', 18, 'bold'),
                         command=self.add_student)
        btn_add.grid(row=0, column=0, padx=10, pady=5)

        btn_show = Button(F4, text='Show Students', bg='blue', fg='white', font=('times new roman', 18, 'bold'),
                          command=self.show_students)
        btn_show.grid(row=0, column=1, padx=10, pady=5)

        btn_reset = Button(F4, text='Reset', bg='orange', fg='black', font=('times new roman', 18, 'bold'),
                           command=self.reset)
        btn_reset.grid(row=0, column=2, padx=10, pady=5)

        btn_exit = Button(F4, text='Exit', bg='red', fg='white', font=('times new roman', 18, 'bold'),
                          command=self.root.quit)
        btn_exit.grid(row=0, column=3, padx=10, pady=5)

        # ============================Treeview==================
        self.tree = ttk.Treeview(F3, columns=("ID", "First Name", "Surname", "Course Code", "Exam No", "Total Score", "Percentage", "Division"), show='headings')
        self.tree.heading('ID', text='Student ID')
        self.tree.heading('First Name', text='First Name')
        self.tree.heading('Surname', text='Surname')
        self.tree.heading('Course Code', text='Course Code')
        self.tree.heading('Exam No', text='Exam No')
        self.tree.heading('Total Score', text='Total Score')
        self.tree.heading('Percentage', text='Percentage')
        self.tree.heading('Division', text='Division')
        self.tree.column("ID", width=100)
        self.tree.column("First Name", width=120)
        self.tree.column("Surname", width=120)
        self.tree.column("Course Code", width=120)
        self.tree.column("Exam No", width=100)
        self.tree.column("Total Score", width=100)
        self.tree.column("Percentage", width=100)
        self.tree.column("Division", width=100)
        self.tree.pack(fill=BOTH, expand=1)

    def add_student(self):
        total_score = (self.hindi.get() + self.english.get() + self.python.get() + 
                       self.physics.get() + self.computing.get() + self.business.get() + 
                       self.biology.get())
        self.t_score.set(total_score)

        if total_score >= 350:
            self.average.set(total_score / 7)
            self.ranking.set("Pass")
        else:
            self.average.set(0)
            self.ranking.set("Fail")

        # Simulate adding to the treeview
        self.tree.insert('', 'end', values=(
            self.s_id.get(),
            self.f_name.get(),
            self.s_name.get(),
            self.c_code.get(),
            self.exam_no.get(),
            self.t_score.get(),
            self.average.get(),
            self.ranking.get()
        ))

        messagebox.showinfo("Success", "Student added successfully!")

    def show_students(self):
        # This function can be expanded for displaying data if needed.
        messagebox.showinfo("Show Students", "Displaying students in the table.")

    def reset(self):
        self.s_id.set("")
        self.f_name.set("")
        self.s_name.set("")
        self.c_code.set("")
        self.exam_no.set("")
        self.t_score.set("")
        self.average.set("")
        self.ranking.set("")
        self.hindi.set(0)
        self.english.set(0)
        self.python.set(0)
        self.physics.set(0)
        self.computing.set(0)
        self.business.set(0)
        self.biology.set(0)

if __name__ == "__main__":
    root = Tk()
    app = Students(root)
    root.mainloop()
