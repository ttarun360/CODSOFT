import tkinter as tk
import math

root = tk.Tk()
root.title('Scientific Calculator')
root.configure(bg='#2C3E50')
root.resizable(width=False, height=False)

ent_field = tk.Entry(root, bg='#34495E', fg='#ECF0F1', font=('Arial', 25),
                     borderwidth=10, justify="right")
ent_field.grid(row=0, columnspan=5, padx=10, pady=10,
               sticky='n'+'s'+'e'+'w')
ent_field.insert(0, '0')

FONT = ('Arial', 10, 'bold')


class SC_Calculator():
    def __init__(self):
        self.current = ''
        self.inp_value = True
        self.result = False

    def Entry(self, value):
        ent_field.delete(0, 'end')
        ent_field.insert(0, value)

    def Enter_Num(self, num):
        self.result = False
        firstnum = ent_field.get()
        secondnum = str(num)
        if self.inp_value:
            self.current = secondnum
            self.inp_value = False
        else:
            self.current = firstnum+secondnum
        self.Entry(self.current)

    def Standard_Ops(self, val):
        temp_str = ent_field.get()
        try:
            if val == '=':
                ans = str(eval(temp_str))
                self.result = True
                self.Entry(ans)
            else:
                self.Entry(temp_str+val)
            self.inp_value = False
        except ValueError:
            self.Entry('Error')
        except SyntaxError:
            self.Entry('Error')

    def Clear_Entry(self):
        self.result = False
        self.current = "0"
        self.Entry(0)
        self.inp_value = True

    def SQ_Root(self):
        try:
            self.current = math.sqrt(float(ent_field.get()))
            self.Entry(self.current)
        except ValueError:
            self.Entry('Error')
        except SyntaxError:
            self.Entry('Error')

    def Pi(self):
        self.result = False
        self.current = math.pi
        self.Entry(self.current)

    def E(self):
        self.result = False
        self.current = math.e
        self.Entry(self.current)

    def Sin(self):
        try:
            self.result = False
            self.current = math.sin(math.radians(float(ent_field.get())))
            self.Entry(self.current)
        except ValueError:
            self.Entry('Error')
        except SyntaxError:
            self.Entry('Error')

    def Cos(self):
        try:
            self.result = False
            self.current = math.cos(math.radians(float(ent_field.get())))
            self.Entry(self.current)
        except ValueError:
            self.Entry('Error')
        except SyntaxError:
            self.Entry('Error')

    def Tan(self):
        try:
            self.result = False
            self.current = math.tan(math.radians(float(ent_field.get())))
            self.Entry(self.current)
        except ValueError:
            self.Entry('Error')
        except SyntaxError:
            self.Entry('Error')


numberpad = "789456123"
i = 0
button = []
for j in range(2, 5):
    for k in range(3):
        button.append(tk.Button(root, text=numberpad[i], font=FONT,
                                fg="white", bg="#34495E", width=6, height=2,
                                highlightbackground='#2C3E50', highlightthickness=2))
        button[i].grid(row=j, column=k, sticky='n' +
                       's'+'e' + 'w', padx=10, pady=10)
        button[i]["command"] = lambda x=numberpad[i]: sc_app.Enter_Num(x)
        i += 1

btn_CE = tk.Button(root, text='CE', command=lambda: sc_app.Clear_Entry(),
                   font=FONT, height=2, fg="#000000",
                   bg="#3498DB", highlightbackground='#2C3E50', highlightthickness=2)
btn_CE.grid(row=1, column=0, columnspan=2,
            sticky='n'+'s'+'e'+'w', padx=10, pady=10)

btn_sqr = tk.Button(root, text='\u221A', command=lambda: sc_app.SQ_Root(),
                    font=FONT, width=6, height=2, fg="#000000",
                    bg="#3498DB", highlightbackground='#2C3E50', highlightthickness=2)
btn_sqr.grid(row=1, column=2, sticky='n'+'s'+'e'+'w', padx=10, pady=10)

btn_0 = tk.Button(root, text='0', command=lambda: sc_app.Enter_Num('0'),
                  font=FONT, width=6, height=2, fg="#000000",
                  bg="#34495E", highlightbackground='#2C3E50', highlightthickness=2)
btn_0.grid(row=5, column=0, columnspan=2,
           sticky='n'+'s'+'e'+'w', padx=10, pady=10)

btn_point = tk.Button(root, text='.', command=lambda: sc_app.Standard_Ops('.'),
                      font=FONT, width=6, height=2, fg="#000000",
                      bg="#34495E", highlightbackground='#2C3E50', highlightthickness=2)
btn_point.grid(row=5, column=2, sticky='n'+'s'+'e'+'w', padx=10, pady=10)

btn_equal = tk.Button(root, text='=', command=lambda: sc_app.Standard_Ops('='),
                      font=FONT, width=6, height=2, fg="#000000",
                      bg="#3498DB", highlightbackground='#2C3E50', highlightthickness=2)
btn_equal.grid(row=5, column=3, sticky='n'+'s'+'e'+'w', padx=10, pady=10)

btn_add = tk.Button(root, text='+', command=lambda: sc_app.Standard_Ops('+'),
                    font=FONT, width=6, height=2, fg="#000000",
                    bg="#34495E", highlightbackground='#2C3E50', highlightthickness=2)
btn_add.grid(row=1, column=3, sticky='n'+'s'+'e'+'w', padx=10, pady=10)

btn_sub = tk.Button(root, text='-', command=lambda: sc_app.Standard_Ops('-'),
                    font=FONT, width=6, height=2, fg="#000000",
                    bg="#34495E", highlightbackground='#2C3E50', highlightthickness=2)
btn_sub.grid(row=2, column=3, sticky='n'+'s'+'e'+'w', padx=10, pady=10)

btn_mul = tk.Button(root, text='*', command=lambda: sc_app.Standard_Ops('*'),
                    font=FONT, width=6, height=2, fg="#000000",
                    bg="#34495E", highlightbackground='#2C3E50', highlightthickness=2)
btn_mul.grid(row=3, column=3, sticky='n'+'s'+'e'+'w', padx=10, pady=10)

btn_div = tk.Button(root, text='/', command=lambda: sc_app.Standard_Ops('/'),
                    font=FONT, width=6, height=2, fg="#000000",
                    bg="#34495E", highlightbackground='#2C3E50', highlightthickness=2)
btn_div.grid(row=4, column=3, sticky='n'+'s'+'e'+'w', padx=10, pady=10)

btn_sin = tk.Button(root, text='sin', command=lambda: sc_app.Sin(),
                    font=FONT, width=5, height=2, fg="#000000",
                    bg="#3498DB", highlightbackground='#2C3E50', highlightthickness=2)
btn_sin.grid(row=3, column=4, sticky='n'+'s'+'e'+'w', padx=10, pady=10)

btn_cos = tk.Button(root, text='cos', command=lambda: sc_app.Cos(),
                    font=FONT, width=5, height=2, fg="#000000",
                    bg="#3498DB", highlightbackground='#2C3E50', highlightthickness=2)
btn_cos.grid(row=3, column=5, sticky='n'+'s'+'e'+'w', padx=10, pady=10)

btn_tan = tk.Button(root, text='tan', command=lambda: sc_app.Tan(),
                    font=FONT, width=5, height=2, fg="#000000",
                    bg="#3498DB", highlightbackground='#2C3E50', highlightthickness=2)
btn_tan.grid(row=3, column=6, sticky='n'+'s'+'e'+'w', padx=10, pady=10)

btn_ln = tk.Button(root, text='ln', command=lambda: sc_app.Ln(),
                   font=FONT, width=5, height=2, fg="#000000",
                   bg="#3498DB", highlightbackground='#2C3E50', highlightthickness=2)
btn_ln.grid(row=5, column=4, sticky='n'+'s'+'e'+'w', padx=10, pady=10)

btn_log10 = tk.Button(root, text='log10', command=lambda: sc_app.Log_10(),
                      font=FONT, width=5, height=2, fg="#000000",
                      bg="#3498DB", highlightbackground='#2C3E50', highlightthickness=2)
btn_log10.grid(row=5, column=5, sticky='n'+'s'+'e'+'w', padx=10, pady=10)

btn_abs = tk.Button(root, text='|x|', command=lambda: sc_app.Abs(),
                    font=FONT, width=5, height=2, fg="#000000",
                    bg="#3498DB", highlightbackground='#2C3E50', highlightthickness=2)
btn_abs.grid(row=5, column=6, sticky='n'+'s'+'e'+'w', padx=10, pady=10)

root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=1)
root.grid_columnconfigure(2, weight=1)
root.grid_columnconfigure(3, weight=1)
root.grid_columnconfigure(4, weight=1)
root.grid_columnconfigure(5, weight=1)
root.grid_columnconfigure(6, weight=1)

root.grid_rowconfigure(0, weight=1)
root.grid_rowconfigure(1, weight=1)
root.grid_rowconfigure(2, weight=1)
root.grid_rowconfigure(3, weight=1)
root.grid_rowconfigure(4, weight=1)
root.grid_rowconfigure(5, weight=1)

sc_app = SC_Calculator()
root.mainloop()