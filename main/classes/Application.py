from tkinter import *
# from tkinter import ttk
# from tkinter import filedialog
from classes.Interpreter import Interpreter


class Application:
	
	def __init__(self):
		self.lol = Interpreter()

	def update_lexeme_table(self, lexeme_table):
		lexeme_table.delete(*lexeme_table.get_children())	#clear table
		for token in self.lol.tokens:
			lexeme_table.insert(parent='', index='end', text=token.name, values=(token.type))
		
	def update_sym_table(self, sym_table):
		sym_table.delete(*sym_table.get_children())			#clear table
		for key in self.lol.symbol_table:
			if not self.lol.symbol_table[key].value:		#check if value if empty
				continue
			sym_table.insert(parent='', index='end', text=key, values=(self.lol.symbol_table[key].value))

	def update_terminal(self, output_text, string):
		string = str(string)
		# output_text.delete(1.0, END) 			# clear the output text
		# cu = output_text.index("end-1c")
		# cu = cu.split('.')
		# c2 = output_text.index("end")
		# print("CU", cu)
		output_text.insert(END,string+'\n')			# print string
		# output_text.tag_add("text", cu[0]+'.'+cu[1], cu[0]+'.'+str(len(string)+16))
		# output_text.tag_config("text", foreground="white")
		output_text.insert(END,"lol-terminal:~$ ")	# print string
		# output_text.tag_add("terminal", str(float(cu[0])+1), str(int(cu[0])+1)+".15") 
		# output_text.tag_config("terminal", foreground="green")
		output_text.see("end")

	def execute(self, lexeme_table, sym_table, output_text, text_editor):

		try:
			self.lol.text = text_editor.get(1.0, END)	# update based from text_editor contents
			self.lol.run_lexer()
			self.update_lexeme_table(lexeme_table)
			# self.lol.print_tokens()
			self.lol.run_parser()
			# self.lol.print_tree()
			self.lol.run_analyzer(output_text)
			self.update_sym_table(sym_table)
			# print("ANO TOOO")
			# print(self.lol.tree.children)
			# self.update_terminal(output_text)
		except Exception as err:
			# sym_table.delete(*sym_table.get_children())			# clear table
			# lexeme_table.delete(*lexeme_table.get_children())	# lear table
			# output_text.delete(1.0, END) 						# clear the output text
			print(err)
			self.update_terminal(output_text, err)


	def upload(self, text_editor):
		self.lol.readFile()
		text_editor.delete(1.0, END)
		text_editor.insert(END, self.lol.text)
