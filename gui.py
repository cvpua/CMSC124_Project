from tkinter import *
from tkinter import ttk
from tkinter import filedialog

def execute():
	output_text.delete(1.0, END) 			# clear the output text
	string = text_editor.get(1.0, END)		# get string, for now get from text editor
	output_text.insert(END,string)			# print string

def upload():
	# for aaron's directory
	lol = filedialog.askopenfilename(initialdir="/home/aaron/Desktop/124/CMSC124_Project", 
		title="Open a .lol file", 
		filetypes=(	("IN Files", "*.lol"),
					("All Files", "*.*")))
	# default
	# file = filedialog.askopenfilename(initialdir="/", 
	# 	title="Open a .lol file", 
	# 	filetypes=(	("LOL Files", "*.lol"),
	# 				("All Files", "*.*")))

	if lol:
		f = open(lol, "r")
		file = f.readlines()	# read by line
		f.close()

		text_editor.delete(1.0, END)
		for i in file:
			text_editor.insert(END,i)
		


root = Tk()
root.title("LOLTERPRETER")
root.geometry("1000x620")
root.resizable(0, 0)

# text editor frame, for button and text box
text_editor_frame = Frame(root)

# upload button in text editor
upload_button = Button(text_editor_frame, text="Upload File", width=47, height=1, command=upload)
upload_button.pack()

# text editor
text_editor = Text(text_editor_frame, width=50,height=20)
text_editor.pack()
text_editor_frame.grid(row=0,column=0)

# lexeme table
lexeme_table_frame = Frame(root)
lexeme_label = Label(lexeme_table_frame, text="LEXEMES", font=('Roboto', 15, 'bold'))
lexeme_label.pack()
lexeme_scroll = Scrollbar(lexeme_table_frame)
lexeme_scroll.pack(side=RIGHT, fill=Y)
lexeme_table =  ttk.Treeview(lexeme_table_frame, yscrollcommand=lexeme_scroll.set, height=16)
lexeme_table.pack()
lexeme_scroll.config(command=lexeme_table.yview)
lexeme_table['columns'] = ("Classification")
lexeme_table.column("#0",width=140, minwidth=50, stretch=NO)
lexeme_table.column("Classification", anchor=W, width=140, minwidth=50, stretch=NO)
lexeme_table.heading("#0", text="Lexeme", anchor=CENTER)
lexeme_table.heading("Classification", text="Classification", anchor=CENTER)

c = 0
while c < 50:	#dummy values
	lexeme_table.insert(parent='', index='end', text="test"+str(c), values=("test"+str(c)))
	c = c + 1
lexeme_table_frame.grid(row=0, column=1)

# symbol table
symbol_table_frame = Frame(root)
symbol_label = Label(symbol_table_frame, text="SYMBOL TABLE", font=('Roboto', 15, 'bold'))
symbol_label.pack()
symbol_scroll = Scrollbar(symbol_table_frame)
symbol_scroll.pack(side=RIGHT, fill=Y)
symbol_table =  ttk.Treeview(symbol_table_frame, yscrollcommand=symbol_scroll.set, height=16)
symbol_table.pack()
symbol_scroll.config(command=symbol_table.yview)
symbol_table['columns'] = ("Value")
symbol_table.column("#0",width=140, minwidth=50, stretch=NO)
symbol_table.column("Value", anchor=W, width=140, minwidth=50, stretch=NO)
symbol_table.heading("#0", text="Identifier", anchor=CENTER)
symbol_table.heading("Value", text="Value", anchor=CENTER)

c = 0
while c < 50:	#dummy values
	symbol_table.insert(parent='', index='end', text="test"+str(c), values=("test"+str(c)))
	c = c + 1
symbol_table_frame.grid(row=0, column=2)

# execute button
execute_button = Button(root, text="Execute", width=121, command=execute)
execute_button.grid(row=1, column=0, columnspan=3)

# output text
output_text_frame = Frame(root)
output_text = Text(output_text_frame, width=124,height=12)
output_text.pack()
# output_text.insert(END,"Some Text")
output_text.bind("<Key>", lambda e: "break")
output_text_frame.grid(row=2,column=0,columnspan=3)

root.mainloop()