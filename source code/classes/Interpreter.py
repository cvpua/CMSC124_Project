import tkinter
from tkinter.filedialog import askopenfilename

from classes.Lexer import Lexer
from classes.Parser import Parser
from classes.Analyzer import Analyzer
from utils.tokexp import TOK_EXP


class Interpreter:
  def __init__(self):
    self.tokens = []
    self.text = ""
    self.tree = None
    self.symbol_table = {}
  
  def readFile(self):
    filename = askopenfilename()
    if filename:
      file = open(filename,'r')
      self.text = file.read()
      return filename
    else:
      return None

  def run_lexer(self):
    if (self.text != ""):
      # Source Code and Token Expression fed to the Lexer
      lexer = Lexer(self.text, TOK_EXP)
    else:
      raise Exception("FAILED TO RUN THE LEXER: Empty file or set the file first")
    # Tokenizing the source code using the token expressions and returns the list of tokens
    self.tokens = lexer.tokenize()
  
  def run_parser(self):
    if (len(self.tokens) != 0):
      # The list of tokens is fed to the Parser
      parser = Parser(self.tokens)
    else:
      raise Exception("Parsing Error: The list of tokens is empty")
    # Returns the root node of the parse tree
    self.tree = parser.parse()
  
  def run_analyzer(self, output_text):
    if (self.tree != None):
      # The parse tree is fed to the analyzer
      analyzer = Analyzer(self.tree, output_text)
    else:
      raise Exception("Error in Analyzer: The tree is still empty")
        
    # Analyzing the the parse tree
    analyzer.start_analyze()
    # Returns the symbol table produced by Analyzer
    self.symbol_table = analyzer.symbol_table
    print(self.symbol_table["IT"].value)
  
  def print_text(self):
    print(self.text)
  
  def print_tokens(self):
    print("\n")
    print("==========TOKENS==========")
    for token in self.tokens:
      print('"' + token.name + '"' + "\n\t" + token.type )
    print("========END TOKENS========")
    print("\n")
  
  def print_tree(self,iteration = 0, node = None):
    if (iteration == 0):
      print("\n")
      print("==========TREE==========")
      children = self.tree.children
    else:
      children = node.children
    for child in children:
      value = "- " + child.value if child.value else ""
      print("    "*iteration + child.type  + value)
      if(child.children):
        self.print_tree(iteration + 1, child)
    if (iteration == 0):
      print("========END TREE========")
      print("\n")