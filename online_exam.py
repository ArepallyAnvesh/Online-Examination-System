import sqlite3
import random
import tkinter as tk
from tkinter import ttk, messagebox

DB = "question_bank.db"
TOTAL_Q = 20
DURATION = 20 * 60  # seconds

NAVY, BLUE, GREEN, ORANGE, RED, GRAY = "#1a2557", "#2563eb", "#16a34a", "#f59e0b", "#dc2626", "#64748b"
BG, CARD, LIGHT = "#eef3fb", "#ffffff", "#f3f6fb"

SEED = [
    ("Which keyword is used to inherit from another class?", "extends", "inherits", "class", "Python uses class syntax", "D"),
    ("Which Tkinter widget is used to display a button?", "Button", "Click", "Command", "Action", "A"),
    ("What is the output of 10 // 3?", "3.33", "4", "3", "1", "C"),
    ("Which keyword is used to define a function in Python?", "function", "fun", "def", "define", "C"),
    ("Which collection does not allow duplicate values?", "list", "tuple", "set", "dict keys list", "C"),
    ("What does SQL stand for?", "Structured Query Language", "Simple Query Logic", "Standard Query List", "Sequential Query Language", "A"),
    ("Which widget is commonly used to select one option from multiple options in Tkinter?", "Checkbutton", "Radiobutton", "Entry", "Label", "B"),
    ("Which method removes the last item from a list?", "remove()", "delete()", "pop()", "discard()", "C"),
    ("Which data type stores True or False?", "int", "str", "bool", "float", "C"),
    ("Which function returns the number of items in a collection?", "size()", "count()", "length()", "len()", "D"),
    ("What is the output? x = [10,20,30]; print(x[1])", "10", "20", "30", "Error", "B"),
    ("Which method adds an element to the end of a list?", "add()", "insert()", "append()", "push()", "C"),
    ("Which module is used to work with SQLite in Python?", "sqlite", "sqlite3", "pysql", "dbm", "B"),
    ("What does OOP stand for?", "Object Oriented Programming", "Object Operating Program", "Open Object Programming", "Ordered Object Process", "A"),
    ("Which function is used to get input from the user?", "input()", "scan()", "read()", "get()", "A"),
    ("Which keyword handles exceptions?", "catch", "try", "handle", "error", "B"),
    ("Which operator is used for exponentiation?", "^", "**", "//", "%%", "B"),
    ("Which keyword is used to create a class?", "object", "class", "def", "new", "B"),
    ("Which method starts the Tkinter application event loop?", "start()", "run()", "mainloop()", "loop()", "C"),
    ("Which symbol is used for comments in Python?", "//", "#", "/* */", "--", "B"),
    ("Which function converts a string to an integer?", "str()", "int()", "float()", "chr()", "B"),
    ("Which keyword is used to exit a loop immediately?", "stop", "exit", "break", "continue", "C"),
]

def init_db():
    con = sqlite3.connect(DB)
    con.execute("""CREATE TABLE IF NOT EXISTS questions(
        id INTEGER PRIMARY KEY AUTOINCREMENT, question TEXT, a TEXT, b TEXT,
        c TEXT, d TEXT, answer TEXT)""")
    if con.execute("SELECT COUNT(*) FROM questions").fetchone()[0] == 0:
        con.executemany("INSERT INTO questions(question,a,b,c,d,answer) VALUES(?,?,?,?,?,?)", SEED)
    con.commit()
    con.close()


def db_all():
    con = sqlite3.connect(DB)
    rows = con.execute("SELECT id,question,a,b,c,d,answer FROM questions").fetchall()
    con.close()
    return rows

def db_exec(sql, args=()):
    con = sqlite3.connect(DB)
    con.execute(sql, args)
    con.commit()
    con.close()


def grade_of(p):
    for limit, g in ((90, "A+"), (80, "A"), (70, "B"), (60, "C"), (40, "D")):
        if p >= limit:
            return g
    return "F"


class ExamApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Online Examination System")
        self.geometry("1100x680")
        self.minsize(900, 600)
        self.configure(bg=BG)
        self.timer_id = None
        self.welcome_screen()

    def clear(self):
        if self.timer_id:
            self.after_cancel(self.timer_id)
            self.timer_id = None
        for w in self.winfo_children():
            w.destroy()

    def header(self, title, sub=None, timer=False):
        h = tk.Frame(self, bg=NAVY)
        h.pack(fill="x")
        if timer:
            tk.Label(h, text=title, bg=NAVY, fg="white", font=("Segoe UI", 18, "bold")).pack(side="left", padx=20, pady=14)
            self.timer_lbl = tk.Label(h, text="20:00", bg=NAVY, fg="#fbbf24", font=("Consolas", 20, "bold"))
            self.timer_lbl.pack(side="right", padx=20)
        else:
            tk.Label(h, text=title, bg=NAVY, fg="white", font=("Segoe UI", 20, "bold")).pack(pady=(12, 0))
            tk.Label(h, text=sub or "", bg=NAVY, fg="#cbd5e1", font=("Segoe UI", 9)).pack(pady=(0, 10))

    def welcome_screen(self):
        self.clear()
        self.header("ONLINE EXAMINATION SYSTEM", "Python Programming Assessment")
        card = tk.Frame(self, bg=CARD, highlightbackground="#cbd5e1", highlightthickness=1)
        card.place(relx=0.5, rely=0.5, anchor="center", width=520, height=460)
        tk.Label(card, text="Welcome to the Examination", bg=CARD, fg=NAVY, font=("Segoe UI", 20, "bold")).pack(pady=(30, 4))
        tk.Label(card, text="Test your Python programming knowledge", bg=CARD, fg=GRAY).pack()
        tk.Label(card, text="Student Name", bg=CARD, fg=NAVY, font=("Segoe UI", 10, "bold")).pack(anchor="w", padx=40, pady=(25, 4))
        self.name_var = tk.StringVar()
        e = tk.Entry(card, textvariable=self.name_var, font=("Segoe UI", 12), relief="solid", bd=1)
        e.pack(fill="x", padx=40, ipady=5)
        e.focus()
        info = tk.Frame(card, bg=LIGHT)
        info.pack(fill="x", padx=40, pady=20)
        tk.Label(info, text="Exam Details", bg=LIGHT, fg=NAVY, font=("Segoe UI", 10, "bold")).pack(anchor="w", padx=10, pady=(8, 2))
        for t in (f"• Questions: {TOTAL_Q}", f"• Duration: {DURATION // 60} Minutes", "• One correct answer per question",
                  "• Mark questions for review", "• Exam will auto-submit when time expires"):
            tk.Label(info, text=t, bg=LIGHT, fg=GRAY, font=("Segoe UI", 9)).pack(anchor="w", padx=10)
        tk.Label(info, bg=LIGHT).pack()
        tk.Button(card, text="START EXAM", bg=BLUE, fg="white", font=("Segoe UI", 11, "bold"), relief="flat",
                  padx=30, pady=8, command=self.start_exam).pack(pady=(0, 8))
        tk.Button(card, text="Question Bank Management", bg="#e2e8f0", relief="flat", padx=12, pady=4,
                  command=self.bank_window).pack()
        self.bind("<Return>", lambda e: self.start_exam())

    def start_exam(self):
        name = self.name_var.get().strip()
        if not name:
            messagebox.showwarning("Name Required", "Please enter your name.")
            return
        bank = db_all()
        if len(bank) < TOTAL_Q:
            messagebox.showerror("Question Bank", f"Need at least {TOTAL_Q} questions. Currently: {len(bank)}.")
            return
        self.unbind("<Return>")
        self.student = name
        self.questions = random.sample(bank, TOTAL_Q)  # random questions, random order
        self.answers = [None] * TOTAL_Q
        self.marked = [False] * TOTAL_Q
        self.cur = 0
        self.remaining = DURATION
        self.exam_screen()
        self.tick()

    def exam_screen(self):
        self.clear()
        self.header("PYTHON PROGRAMMING EXAM", timer=True)
        body = tk.Frame(self, bg=BG)
        body.pack(fill="both", expand=True, padx=12, pady=12)

        left = tk.Frame(body, bg=CARD)
        left.pack(side="left", fill="both", expand=True)
        self.q_no = tk.Label(left, bg=CARD, fg=BLUE, font=("Segoe UI", 12, "bold"))
        self.q_no.pack(anchor="w", padx=20, pady=(18, 6))
        self.q_text = tk.Label(left, bg=CARD, font=("Segoe UI", 12), wraplength=620, justify="left")
        self.q_text.pack(anchor="w", padx=20, pady=(0, 15))
        self.sel = tk.StringVar()
        self.opts = []
        for letter in "ABCD":
            r = tk.Radiobutton(left, variable=self.sel, value=letter, bg=LIGHT, anchor="w", font=("Segoe UI", 11),
                               padx=12, pady=10, activebackground=LIGHT, command=self.save_answer)
            r.pack(fill="x", padx=20, pady=5)
            self.opts.append(r)
        bar = tk.Frame(left, bg=CARD)
        bar.pack(side="bottom", fill="x", padx=20, pady=15)
        self.prev_btn = tk.Button(bar, text="← Previous", bg=GRAY, fg="white", relief="flat", padx=14, pady=8,
                                  font=("Segoe UI", 9, "bold"), command=lambda: self.goto(self.cur - 1))
        self.prev_btn.pack(side="left")
        self.mark_btn = tk.Button(bar, bg=ORANGE, fg="white", relief="flat", padx=14, pady=8,
                                  font=("Segoe UI", 9, "bold"), command=self.toggle_mark)
        self.mark_btn.pack(side="left", padx=8)
        self.next_btn = tk.Button(bar, bg=BLUE, fg="white", relief="flat", padx=18, pady=8,
                                  font=("Segoe UI", 9, "bold"), command=self.next_or_finish)
        self.next_btn.pack(side="right")

        right = tk.Frame(body, bg=CARD, width=250)
        right.pack(side="right", fill="y", padx=(12, 0))
        right.pack_propagate(False)
        tk.Label(right, text="Question Navigator", bg=CARD, fg=NAVY, font=("Segoe UI", 11, "bold")).pack(pady=12)
        grid = tk.Frame(right, bg=CARD)
        grid.pack()
        self.nav = []
        for i in range(TOTAL_Q):
            b = tk.Button(grid, text=str(i + 1), width=4, relief="flat", bd=2, command=lambda i=i: self.goto(i))
            b.grid(row=i // 4, column=i % 4, padx=3, pady=3)
            self.nav.append(b)
        tk.Button(right, text="SUBMIT EXAM", bg=RED, fg="white", relief="flat", font=("Segoe UI", 11, "bold"),
                  pady=10, command=self.confirm_submit).pack(side="bottom", fill="x", padx=10, pady=12)
        legend = tk.Frame(right, bg=CARD)
        legend.pack(side="bottom", anchor="w", padx=12)
        for c, t in ((GREEN, "Answered"), (ORANGE, "Marked"), (GRAY, "Unanswered")):
            tk.Label(legend, text="■ " + t, fg=c, bg=CARD, font=("Segoe UI", 8, "bold")).pack(anchor="w")
        self.show_question()

    def show_question(self):
        q = self.questions[self.cur]
        self.q_no.config(text=f"Question {self.cur + 1} / {TOTAL_Q}")
        self.q_text.config(text=q[1])
        for r, letter, text in zip(self.opts, "ABCD", q[2:6]):
            r.config(text=f"{letter}. {text}")
        self.sel.set(self.answers[self.cur] or "")
        self.prev_btn.config(state="normal" if self.cur > 0 else "disabled")
        self.next_btn.config(text="Finish →" if self.cur == TOTAL_Q - 1 else "Next →")
        self.mark_btn.config(text="★ Unmark Review" if self.marked[self.cur] else "☆ Mark for Review",
                             bg=RED if self.marked[self.cur] else ORANGE)
        self.refresh_nav()

    def refresh_nav(self):
        for i, b in enumerate(self.nav):
            if self.marked[i]:
                bg, fg = ORANGE, "white"
            elif self.answers[i]:
                bg, fg = GREEN, "white"
            else:
                bg, fg = "#e2e8f0", "#334155"
            b.config(bg=bg, fg=fg, activebackground=bg,
                     highlightthickness=2 if i == self.cur else 0, highlightbackground="black",
                     relief="solid" if i == self.cur else "flat")

    def save_answer(self):
        self.answers[self.cur] = self.sel.get()
        self.refresh_nav()

    def toggle_mark(self):
        self.marked[self.cur] = not self.marked[self.cur]
        self.show_question()

    def goto(self, i):
        if 0 <= i < TOTAL_Q:
            self.cur = i
            self.show_question()

    def next_or_finish(self):
        if self.cur == TOTAL_Q - 1:
            self.confirm_submit()
        else:
            self.goto(self.cur + 1)

    def tick(self):
        m, s = divmod(self.remaining, 60)
        self.timer_lbl.config(text=f"{m:02d}:{s:02d}", fg="#ef4444" if self.remaining <= 60 else "#fbbf24")
        if self.remaining <= 0:
            messagebox.showinfo("Time Up", "Time is over. Your exam is being auto-submitted.")
            self.submit()
            return
        self.remaining -= 1
        self.timer_id = self.after(1000, self.tick)

    def confirm_submit(self):
        answered = sum(1 for a in self.answers if a)
        marked = sum(self.marked)
        msg = (f"Are you sure you want to submit the exam?\n\n"
               f"Answered   : {answered}\nUnanswered : {TOTAL_Q - answered}\nMarked     : {marked}")
        if messagebox.askyesno("Submit Exam", msg):
            self.submit()

    def submit(self):
        if self.timer_id:
            self.after_cancel(self.timer_id)
            self.timer_id = None
        rows, correct, wrong, un = [], 0, 0, 0
        for i, q in enumerate(self.questions):
            ans = self.answers[i]
            if not ans:
                status, un = "Unanswered", un + 1
            elif ans == q[6]:
                status, correct = "Correct", correct + 1
            else:
                status, wrong = "Wrong", wrong + 1
            rows.append((i + 1, q[1], ans or "-", q[6], status))
        pct = correct * 100 / TOTAL_Q
        self.result_screen(rows, correct, wrong, un, pct)

    def result_screen(self, rows, correct, wrong, un, pct):
        self.clear()
        self.header("EXAM RESULT", f"Student: {self.student}")
        summary = tk.Frame(self, bg=CARD)
        summary.pack(fill="x", padx=15, pady=10)
        tk.Label(summary, text=f"{pct:.2f}%", bg=CARD, fg=BLUE, font=("Segoe UI", 30, "bold")).pack(pady=(10, 0))
        tk.Label(summary, text=f"Grade: {grade_of(pct)}", bg=CARD, font=("Segoe UI", 14, "bold")).pack()
        passed = pct >= 40
        tk.Label(summary, text="PASS" if passed else "FAIL", bg=CARD, fg=GREEN if passed else RED,
                 font=("Segoe UI", 13, "bold")).pack(pady=4)
        stats = tk.Frame(summary, bg=CARD)
        stats.pack(fill="x", padx=15, pady=10)
        for i, (v, t, c) in enumerate(((TOTAL_Q, "Total", BLUE), (correct, "Correct", GREEN),
                                       (wrong, "Wrong", RED), (un, "Unanswered", ORANGE))):
            f = tk.Frame(stats, bg=LIGHT)
            f.grid(row=0, column=i, sticky="nsew", padx=4)
            stats.columnconfigure(i, weight=1)
            tk.Label(f, text=str(v), bg=LIGHT, fg=c, font=("Segoe UI", 18, "bold")).pack(pady=(8, 0))
            tk.Label(f, text=t, bg=LIGHT, fg=GRAY).pack(pady=(0, 8))

        lf = tk.LabelFrame(self, text="Question-wise Analysis", bg=BG, fg=NAVY, font=("Segoe UI", 10, "bold"))
        lf.pack(fill="both", expand=True, padx=15, pady=(0, 10))
        cols = ("#", "Question", "Your Answer", "Correct Answer", "Status")
        tree = ttk.Treeview(lf, columns=cols, show="headings")
        widths = (40, 520, 100, 110, 100)
        for c, w in zip(cols, widths):
            tree.heading(c, text=c)
            tree.column(c, width=w, anchor="w" if c == "Question" else "center")
        tree.tag_configure("Correct", foreground=GREEN)
        tree.tag_configure("Wrong", foreground=RED)
        tree.tag_configure("Unanswered", foreground=ORANGE)
        for r in rows:
            tree.insert("", "end", values=r, tags=(r[4],))
        sb = ttk.Scrollbar(lf, orient="vertical", command=tree.yview)
        tree.configure(yscrollcommand=sb.set)
        sb.pack(side="right", fill="y")
        tree.pack(fill="both", expand=True)
        tk.Button(self, text="Back to Home", bg=BLUE, fg="white", relief="flat", padx=20, pady=6,
                  command=self.welcome_screen).pack(pady=(0, 10))

    def bank_window(self):
        win = tk.Toplevel(self)
        win.title("Question Bank Management")
        win.geometry("900x560")
        win.configure(bg=BG)
        cols = ("ID", "Question", "A", "B", "C", "D", "Ans")
        tree = ttk.Treeview(win, columns=cols, show="headings", height=10)
        for c, w in zip(cols, (40, 300, 110, 110, 110, 110, 40)):
            tree.heading(c, text=c)
            tree.column(c, width=w)
        tree.pack(fill="both", expand=True, padx=10, pady=10)

        def load():
            tree.delete(*tree.get_children())
            for r in db_all():
                tree.insert("", "end", values=r)
        load()

        form = tk.Frame(win, bg=BG)
        form.pack(fill="x", padx=10)
        ents = {}
        for i, lab in enumerate(("Question", "A", "B", "C", "D")):
            tk.Label(form, text=lab, bg=BG).grid(row=i, column=0, sticky="w", pady=2)
            e = tk.Entry(form, width=90)
            e.grid(row=i, column=1, pady=2, padx=6)
            ents[lab] = e
        tk.Label(form, text="Correct (A-D)", bg=BG).grid(row=5, column=0, sticky="w")
        ans = ttk.Combobox(form, values=list("ABCD"), width=5, state="readonly")
        ans.grid(row=5, column=1, sticky="w", padx=6, pady=2)

        def add():
            vals = [ents[k].get().strip() for k in ("Question", "A", "B", "C", "D")]
            if not all(vals) or not ans.get():
                messagebox.showwarning("Missing", "Fill all fields and choose the correct answer.", parent=win)
                return
            db_exec("INSERT INTO questions(question,a,b,c,d,answer) VALUES(?,?,?,?,?,?)", (*vals, ans.get()))
            for e in ents.values():
                e.delete(0, "end")
            load()

        def delete():
            sel = tree.selection()
            if sel and messagebox.askyesno("Delete", "Delete selected question?", parent=win):
                db_exec("DELETE FROM questions WHERE id=?", (tree.item(sel[0])["values"][0],))
                load()

        btns = tk.Frame(win, bg=BG)
        btns.pack(pady=10)
        tk.Button(btns, text="Add Question", bg=GREEN, fg="white", relief="flat", padx=14, pady=5, command=add).pack(side="left", padx=5)
        tk.Button(btns, text="Delete Selected", bg=RED, fg="white", relief="flat", padx=14, pady=5, command=delete).pack(side="left", padx=5)


if __name__ == "__main__":
    init_db()
    ExamApp().mainloop()