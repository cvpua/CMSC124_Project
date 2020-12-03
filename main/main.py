from classes.Interpreter import Interpreter

lol = Interpreter()
lol.readFile()
try:
  lol.run_lexer()
except Exception as err:
  print(err)
# lol.run_parser()
# print(lol.parser)
lol.print_tokens()