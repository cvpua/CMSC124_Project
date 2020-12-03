import tkinter
from tkinter.filedialog import askopenfilename

from classes.Lexer import Lexer
from classes.Parser import Parser
from utils.tokexp import TOK_EXP


class Interpreter:
  def __init__(self):
    self.tokens = []
    self.text = ""
    self.tree = None
    self.symbol_table = {}
  
  def readFile(self):
    # To do: 
    # [ ] check if the file type is lol, if not, then print an error
    filename = askopenfilename()
    file = open(filename,'r')
    self.text = file.read()
  
  def run_lexer(self):
    if (self.text != ""):
      lexer = Lexer(self.text, TOK_EXP)
    else:
      raise Exception("FAILED TO RUN THE LEXER: Empty file or set the file first")
    self.tokens = lexer.tokenize()
  
  def run_parser(self):
    if (len(self.tokens) != 0):
      parser = Parser(self.tokens)
    else:
      print("The list of tokens is empty")
      return False
    self.tree = parser.parse()
    return True
  
  # def run_analyzer(self):
  #   if (self.tree != None):
  #     analyzer = Analyzer(self.tree)
  #   else:
  #     print("The tree is still empty")
  #     return False
  #   analyzer.analyze()
  #   self.symbol_table = analyzer.symbol_table
  #   return True
  
  # def interpret(self):
  #   is_successful = self.run_lexer()
  #   if (not(is_successful)):
  #     print("Tokenizing is not successful")
  #     return False

  #   is_successful = self.run_parser()
  #   if (not(is_successful)):
  #     print("Parsing is not successful")
  #     return False
    
  #   is_successful = self.run_analyzer()
  #   if (not(is_successful)):
  #     print("Semantic analysis is not successful")
  #     return False
  
  def print_text(self):
    print(self.text)
  
  def print_tokens(self):
    for token in self.tokens:
      print('"' + token.name + '"' + "\n\t" + token.type )
  
  # TO DO:
  # [ ] Print Tree
  # - this function will print the visualization of the parse tree
  # def print_tree(self):
  
  # [ ] Print Symbol Table
  # def print_symbol_table(self):
