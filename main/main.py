from classes.Interpreter import Interpreter

lol = Interpreter()
lol.readFile()

try:
  lol.run_lexer()
  lol.print_tokens()
  lol.run_parser()
  lol.print_tree()
  lol.run_analyzer()
except Exception as err:
  print(err)

  