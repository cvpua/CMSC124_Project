from classes.Interpreter import Interpreter

lol = Interpreter()
lol.readFile()
try:
  lol.run_lexer()
except Exception as err:
  print(err)
finally:
  lol.print_tokens()
  
try:
  lol.run_parser()
except Exception as err:
  print(err)
finally:
  lol.print_tree()