import tkinter as tk
calc= ""
def add(symbol):
    global calc
    calc += str(symbol)
    result.delete(1.0,"end")
    result.insert(1.0,calc)
def evaluation():
    global calc
    print(calc)
    try:
        calc=str(eval(result))
        result.delete(1.0,"end")
        result.insert(1.0,result)
    except:
        clear_field()
        result.insert(1.0,"error")
        clear_field()
        result.delete(1.0,"end")
def clear_field():
    global calc
    calc=""
    result.delete(1.0,"end")
    pass
def delete():
    pass 
root=tk.Tk()
root.title('mariam-nabukenya-simple calculator')
root.geometry("300x275")
result=tk.Text(root,height=2,width=16,font=("Arial",24))
result.grid(columnspan=5)
but_1 = tk.Button(root,text="1",command=lambda: add(1),width=5 ,font=("Arial",14))
but_1.grid(row=2,column=1)
but_2 = tk.Button(root,text="2",command=lambda: add(2),width=5, font=("Arial",14))
but_2.grid(row=2,column=2)
but_3 = tk.Button(root,text="3",command=lambda: add(3),width=5 ,font=("Arial",14))
but_3.grid(row=2,column=3)
but_4 = tk.Button(root,text="4",command=lambda: add(4),width=5, font=("Arial",14))
but_4.grid(row=3,column=1)
but_5 = tk.Button(root,text="5",command=lambda: add(5),width=5 ,font=("Arial",14))
but_5.grid(row=3,column=2)
but_6 = tk.Button(root,text="6",command=lambda: add(6),width=5 ,font=("Arial",14))
but_6.grid(row=3,column=3)
but_7 = tk.Button(root,text="7",command=lambda: add(7),width=5 ,font=("Arial",14))
but_7.grid(row=4,column=1)
but_8= tk.Button(root,text="8",command=lambda: add(8),width=5, font=("Arial",14))
but_8.grid(row=4,column=2)
but_9 = tk.Button(root,text="9",command=lambda: add(9),width=5 ,font=("Arial",14))
but_9.grid(row=4,column=3)
but_0 = tk.Button(root,text="0",command=lambda: add(0),width=5, font=("Arial",14))
but_0.grid(row=5,column=2)
but_plus = tk.Button(root,text="+",command=lambda: add("+"),width=5, font=("Arial",14))
but_plus.grid(row=2,column=4)
but_subtract= tk.Button(root,text="-",command=lambda: add("-"),width=5 ,font=("Arial",14))
but_subtract.grid(row=3,column=4)
but_multiply = tk.Button(root,text="*",command=lambda: add("*"),width=5, font=("Arial",14))
but_multiply.grid(row=4,column=4)
but_divide= tk.Button(root,text="/",command=lambda: add("/"),width=5, font=("Arial",14))
but_divide.grid(row=5,column=4)
but_br1 = tk.Button(root,text="(",command=lambda: add("("),width=5, font=("Arial",14))
but_br1.grid(row=6,column=1)
but_br2 = tk.Button(root,text=")",command=lambda: add(")"),width=5, font=("Arial",14))
but_br2.grid(row=6,column=2)
but_point = tk.Button(root,text=".",command=lambda: add("."),width=5, font=("Arial",14))
but_point.grid(row=5,column=3)
but_equal = tk.Button(root,text="=",command= evaluation,width=12, font=("Arial",14))
but_equal.grid(row=6,column=3,columnspan=2)
but_clear= tk.Button(root,text="C", command=clear_field(),width=5, font=("Arial",14))
but_clear.grid(row=5,column=1)
root.mainloop()