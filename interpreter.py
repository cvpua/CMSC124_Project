# TO DO
# [ ] Parser: Function definition for every production rule in our grammar
# [ ] Analyzer: Pag-cacatch ng mga instances na pwedeng magpabago sa symbol table at yung mga kailangang iexecute like GIMMEH and VISIBLE


import re
import tkinter
from tkinter.filedialog import askopenfilename

TOK_EXP = [
    (r"^HAI\s", "HAI_KEYWORD"),
    (r"^KTHXBYE\s|^KTHXBYE$", "KTHXBYE_KEYWORD"),
    (r"^BTW\s", "BTW_KEYWORD"),
    (r"^OBTW\s", "OBTW_KEYWORD"),
    (r"^TLDR\s", "TLDR_KEYWORD"),
    (r"^I HAS A\s", "I_HAS_A_KEYWORD"),
    (r"^ITZ\s", "ITZ_KEYWORD"),
    (r"^R\s", "R_KEYWORD"),
    (r"^SUM OF\s", "SUM_OF_KEYWORD"),
    (r"^DIFF OF\s", "DIFF_OF_KEYWORD"),
    (r"^PRODUKT OF\s", "PRODUKT_OF_KEYWORD"),
    (r"^QUOSHUNT OF\s", "QUOSHUNT_OF_KEYWORD"),
    (r"^MOD OF\s", "MOD_OF_KEYWORD"),
    (r"^BIGGR OF\s", "BIGGR_OF_KEYWORD"),
    (r"^SMALLR OF\s", "SMALLR_OF_KEYWORD"),
    (r"^BOTH OF\s", "BOTH_OF_KEYWORD"),
    (r"^EITHER OF\s", "EITHER_OF_KEYWORD"),
    (r"^WON OF\s", "WON_OF_KEYWORD"),
    (r"^NOT\s", "NOT_KEYWORD"),
    (r"^ANY OF\s", "ANY_OF_KEYWORD"),
    (r"^ALL OF\s", "ALL_OF_KEYWORD"),
    (r"^BOTH SAEM\s", "BOTH_SAEM_KEYWORD"),
    (r"^DIFFRINT\s", "DIFFRINT_KEYWORD"),
    (r"^SMOOSH\s", "SMOOSH_KEYWORD"),
    (r"^MAEK\s", "MAEK_KEYWORD"),
    (r"^A\s", "A_KEYWORD"),
    (r"^IS NOW A\s", "IS_NOW_A_KEYWORD"),
    (r"^VISIBLE\s", "VISIBLE_KEYWORD"),
    (r"^GIMMEH\s", "GIMMEH_KEYWORD"),
    (r"^O RLY\?\s", "O_RLY?_KEYWORD"),
    (r"^YA RLY\s", "YA_RLY_KEYWORD"),
    (r"^MEBBE\s", "MEBBE_KEYWORD"),
    (r"^NO WAI\s", "NO_WAI_KEYWORD"),
    (r"^OIC\s", "OIC_KEYWORD"),
    (r"^WTF\?\s", "WTF?_KEYWORD"),
    (r"^OMG\s", "OMG_KEYWORD"),
    (r"^OMGWTF\s", "OMGWTF_KEYWORD"),
    (r"^IM IN YR\s", "IM_IN_YR_KEYWORD"),
    (r"^UPPIN\s", "UPPIN_KEYWORD"),
    (r"^NERFIN\s", "NERFIN_KEYWORD"),
    (r"^YR\s", "YR_KEYWORD"),
    (r"^TIL\s", "TIL_KEYWORD"),
    (r"^WILE\s", "WILE_KEYWORD"),
    (r"^IM OUTTA YR\s", "IM_OUTTA_YR_KEYWORD"),
    (r"^(-?[0-9]+)\s", "NUMBR_LITERAL"),
    (r"^(-)?[0-9]*(\.)[0-9]+\s", "NUMBAR_LITERAL"),
    (r"^\".+\"\s", "YARN_LITERAL"),
    (r"^(WIN|FAIL)\s", "TROOF_LITERAL"),
    (r"^(NOOB|NUMBR|NUMBAR|YARN|TROOF)\s", "TYPE_LITERAL"),
    (r"^[a-zA-Z][a-zA-Z0-9_]*\s", "VAR_IDENTIFIER"),
  ]


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
      print("Please set the file first")
      return False
    tokens = lexer.tokenize()
    if (tokens):
      self.tokens = tokens
    else:
      return False
  
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

class Token:
  def __init__(self, name, type):
    self.name = name
    self.type = type


class Lexer:
  def __init__(self, text, TOK_EXP):
    self.text = text
    self.token_expressions = TOK_EXP

  def tokenize(self):
    tokens = []
    lines = self.text.split("\n")
    line_number = 1
    for line in lines:
      line = line.strip()
      line = line + "\n"
      while (line != "" and line != "\n"):
        for token_exp in self.token_expressions:
          pattern, tag = token_exp
          match = re.match(pattern, line)
          if (match):
            if(tag == 'YARN_LITERAL'):
              name = match.group(0)[1:-2]
            else:
              name = match.group(0)[:-1]
            tokens.append(
                Token(name,tag)
              )
            line = line[match.end(0):]
            break
        else:
          print(f"Error in line number {line_number}; Invalid token")
          return False
      line_number += 1
    return tokens

class Node:
  def __init__(self, type, value = None, children = None):
    self.type = type
    self.value = value
    self.children = children

  def printSelf(self):
    print(self.type)
    print(self.value)
    print(self.children)


class Parser:
  def __init__(self, tokens):
    self.tokens = tokens
    self.current_token = tokens[0]
  
  def eat(self, token_type):
    if (token_type == self.current_token.type):
      self.tokens.pop(0)
    if (len(self.tokens) != 0): 
      self.current_token = self.tokens[0]
    else: 
      print("Tokens is empty")
      return False
    return True
  



  def codeblock(self,children):  
    # Ang naiisip ko dito ay, mahabang if-elif-else na magcacatch sa lahat ng possible abstraction    
    # Naglagay ako ng children na parameter, para yung nauupdate na children ay laging sa current line/group

    if(self.current_token.type == "VISIBLE_KEYWORD"):
      self.eat("VISIBLE_KEYWORD") 
      #Creates a node then i-assign as children yung corresponding grammar/abstract
      children.append(Node("PRINT", children = self.visible_block([Node("VISIBLE")])))
    
    elif(self.current_token.type == "I_HAS_A_KEYWORD"):
      self.eat("I_HAS_A_KEYWORD")
      #Creates a node then i-assign as children yung corresponding grammar/abstract
      children.append(Node("DECLARATION",children = self.declaration([Node("I HAS A")])))
      
      # Since sa I HAS A pa lang naman nalabas si ITZ, nilagay ko muna siya sa loob ng I HAS A
      # Para rin maging magkalevel sila ni  I HAS A, if inilabas kasi to, di na sila magiging magkalevel
      if(self.current_token.type == "ITZ_KEYWORD"):
        self.eat("ITZ_KEYWORD")
        children.append(Node("ASSIGNMENT",children= self.itz([Node("ITZ")])))


    # I-cacatch ulit lahat ng possible abstraction/grammar for multiple codeblocks
    token_type = self.current_token.type
    if(token_type == "VISIBLE_KEYWORD" or token_type == "I_HAS_A_KEYWORD" or token_type == "ITZ"):
      children.append(Node("CODEBLOCK",children=[]))
      lenChildren = len(children)
      self.codeblock(children[lenChildren-1].children)


    return Node("CODEBLOCK", children = children)
  
  # Tail-recursion is used to catch multiple argument in VISIBLE/printing
  def visible_block(self,children):
    isValid = False
    # Catches all of the terminal
    if(self.current_token.type == "YARN_LITERAL"):
      children.append(Node("YARN_LITERAL", value= self.current_token.name))
      self.eat("YARN_LITERAL")
      isValid = True

    elif(self.current_token.type == "VAR_IDENTIFIER"):
      children.append(Node("VAR_IDENTIFIER",value= self.current_token.name))
      self.eat("VAR_IDENTIFIER")
      isValid = True

    elif(self.current_token.type == "NUMBR_LITERAL"):
      children.append(Node("NUMBR_LITERAL",value= self.current_token.name))
      self.eat("NUMBR_LITERAL")
      isValid = True

    elif(self.current_token.type == "NUMBAR_LITERAL"):
      children.append(Node("NUMBAR_LITERAL",value= self.current_token.name))
      self.eat("NUMBAR_LITERAL")
      isValid = True
    
    if(isValid and (self.tokens[0].type == "NUMBAR_LITERAL" or self.tokens[0].type == "NUMBR_LITERAL" or self.tokens[0].type == "YARN_LITERAL" or self.tokens[0].type == "VAR_IDENTIFIER")  ):
      self.visible_block(children)
    
    return children
  


  def declaration(self,children):
    
    if(self.current_token.type == "VAR_IDENTIFIER"):
      token_type = "VAR_IDENTIFIER"
      children.append(Node(token_type,value=self.current_token.name))
      self.eat(token_type)
      
    return children

  def itz(self,children):
    # Catches all of the terminal
    if(self.current_token.type == "YARN_LITERAL"):
      children.append(Node("YARN_LITERAL", value= self.current_token.name))
      self.eat("YARN_LITERAL")
      

    elif(self.current_token.type == "VAR_IDENTIFIER"):
      children.append(Node("VAR_IDENTIFIER",value= self.current_token.name))
      self.eat("VAR_IDENTIFIER")
      

    elif(self.current_token.type == "NUMBR_LITERAL"):
      children.append(Node("NUMBR_LITERAL",value= self.current_token.name))
      self.eat("NUMBR_LITERAL")
      

    elif(self.current_token.type == "NUMBAR_LITERAL"):
      children.append(Node("NUMBAR_LITERAL",value= self.current_token.name))
      self.eat("NUMBAR_LITERAL")

    return children


  def printParseTree(self,iteration,children):
    for i in range(len(children)):
      print("\t"*iteration + children[i].type + ' - '  + str(children[i].value))
      if(children[i].children):
        self.printParseTree(iteration + 1, children[i].children)
  

  def program(self):
    children = []
    
    if (self.current_token.type == "HAI_KEYWORD"):
      self.eat("HAI_KEYWORD")
      children.append(Node("HAI_KEYWORD"))
    else:
      print("Invalid Syntax: Expect HAI_KEYWORD but saw " + self.current_token.type)
      return False
    

    children.append(self.codeblock([]))
    

    if (self.current_token.type == "KTHXBYE_KEYWORD"):
      self.eat("KTHXBYE_KEYWORD")
      children.append(Node("KTHXBYE_KEYWORD"))
    else:
      print("Invalid Syntax: Expect KTHXBYE_KEYWORD but saw " + self.current_token.type)
      return False
    
    
    self.printParseTree(0,children)


    return Node("PROGRAM", children = children)
  
  def parse(self):
    return self.program()

class Symbol:
  def __init__(self, type, value):
    self.type = type
    self.value = value
    

class Analyzer:
  def __init__(self, tree):
    self.tree = tree
    self.symbol_table = {}
  
  def analyze(self, current_node):
    # set conditions for all nodes that change the value of a variable or declare it
    # for example:
    if (current_node.type == "VAR_INIT"):
      # thinking...antok na ako, basta ivivisit niya yung children then kukunin niya yung variable identifier and yung literal
      # pagkakuha ng value, icacall si insert, name = variable identifier, type = value.type, value = literal.value
      print()
      
      
      
    # Mahaba to 
      
    
    
    for child in current_node.children:
      self.analyze(child)
  
  # Adding a new variable or updating the value of the variable
  def insert(self, name, type, value = None):
    new_symbol = Symbol(type, value)
    self.symbol_table.update({
      name: new_symbol
    })
  
  # This function is for knowing whether the current variable is already declared
  def lookup(self, name):
    for key in self.symbol_table:
      if (key == name):
        return True
    return False
    
      
lol = Interpreter()
lol.readFile()
lol.run_lexer()
lol.run_parser()
# print(lol.parser)
# lol.print_tokens()