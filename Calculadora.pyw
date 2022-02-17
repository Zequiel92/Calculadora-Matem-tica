from tkinter import *
import parser

root = Tk()

i = 0

def get_numbers(n):
	global i
	display.insert(i, n)
	i+=1

def get_operations(operation):
	global i
	operation_length = len(operation)
	display.insert(i, operation)
	i+=operation_length

def clear_display():
	display.delete(0, END)

def undo():
	display_state = display.get()
	if len(display_state):
		display_new_state = display_state[:-1]
		clear_display()
		display.insert(0, display_new_state)
	else:
		clear_display()
		display.insert(0, "Error")

def clculate():
	display_state = display.get()
	try:
		math_expresion = parser.expr(display_state).compile()
		resultado = eval(math_expresion)
		clear_display()
		display.insert(0, resultado)
	except Exception as e:
		clear_display()
		display.insert(0, "Error")

root.title("Calculadora matemática")

display = Entry(root)
display.grid(row=1, columnspan=20,sticky=W+E)

#Botones numericos
Button(root,text="1", command=lambda:get_numbers(1),width=6, height=6,bg="limegreen").grid(row=2, column=0,sticky=W+E)
Button(root,text="2", command=lambda:get_numbers(2),width=6, height=6,bg="limegreen").grid(row=2, column=1,sticky=W+E)
Button(root,text="3", command=lambda:get_numbers(3),width=6, height=6,bg="limegreen").grid(row=2, column=2,sticky=W+E)

Button(root,text="4", command=lambda:get_numbers(4),width=6, height=6,bg="limegreen").grid(row=3, column=0,sticky=W+E)
Button(root,text="5", command=lambda:get_numbers(5),width=6, height=6,bg="limegreen").grid(row=3, column=1,sticky=W+E)
Button(root,text="6", command=lambda:get_numbers(6),width=6, height=6,bg="limegreen").grid(row=3, column=2,sticky=W+E)

Button(root,text="7", command=lambda:get_numbers(7),width=6, height=6,bg="limegreen").grid(row=4, column=0,sticky=W+E)
Button(root,text="8", command=lambda:get_numbers(8),width=6, height=6,bg="limegreen").grid(row=4, column=1,sticky=W+E)
Button(root,text="9", command=lambda:get_numbers(9),width=6, height=6,bg="limegreen").grid(row=4, column=2,sticky=W+E)
Button(root,text="0", command=lambda:get_numbers(0),width=6, height=6,bg="limegreen").grid(row=5,column=1,sticky=W+E)

#Simbolos aritmeticos
Button(root,text="AC", command=lambda:clear_display(), width=6, height=6,bg="yellow").grid(row=2, column=4,sticky=W+E)
Button(root,text="←", command=lambda:undo(), width=6, height=6,bg="yellow").grid(row=2, column=5,sticky=W+E)
Button(root,text="-", command=lambda:get_operations("-"), width=6, height=6,bg="yellow").grid(row=3, column=4,sticky=W+E)
Button(root,text="+", command=lambda:get_operations("+"), width=6, height=6,bg="yellow").grid(row=3, column=5,sticky=W+E)
Button(root,text="x", command=lambda:get_operations("*"),width=6, height=6,bg="yellow").grid(row=4, column=4,sticky=W+E)
Button(root,text="/", command=lambda:get_operations("/"), width=6, height=6,bg="yellow").grid(row=4, column=5,sticky=W+E)
Button(root,text="=", command=lambda:clculate(), width=6, height=6,bg="yellow").grid(row=5, column=4,sticky=W+E)



root.mainloop()