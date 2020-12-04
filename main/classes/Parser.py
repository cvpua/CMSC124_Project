from classes.Node import Node

class Parser:
  def __init__(self, tokens):
    self.tokens = tokens
    self.current_token = tokens[0]
  
  def eat(self, token_type):
    if (token_type == self.current_token.type):
      self.tokens.pop(0)
    else:
      raise Exception(f"Syntax Error: Expect {token_type} but saw {self.current_token.type}")
    if (len(self.tokens) != 0): 
      self.current_token = self.tokens[0]
    else: 
      print("End parsing: Tokens is empty")

# +++++++++++++++++++++++++MULTILINECOMMENT++++++++++++++++++
  def multilinecomment(self):
    return False
    
  
# +++++++++++++++++++++++++CONTROL+++++++++++++++++++++++++++
  def control(self):
    return False

# +++++++++++++++++++++++++DECLARATION+++++++++++++++++++++++
  def declaration(self):
    print("declaration")
    children = []
    if(self.current_token.type == "I_HAS_A_KEYWORD"):
      self.eat("I_HAS_A_KEYWORD")
      children.append(Node("I_HAS_A_KEYWORD"))
    else:
      return False
    
    self.eat("VAR_IDENTIFIER")
    children.append(Node("VAR_IDENTIFIER", self.current_token.name))
    
    if (self.current_token.type == "ITZ_KEYWORD"):
      init_node =self.initialization()
      children.append(init_node)
    
    return Node("DECLARATION", children = children)
  
  def initialization(self):
    children = []
    self.eat("ITZ_KEYWORD")
    children.append(Node("ITZ_KEYWORD"))
    
    value_node = self.value()
    children.append(value_node)
    
    return Node("INITIALIZATION", children = children)



# +++++++++++++++++++++++++INPUT+++++++++++++++++++++++++++++
  def input(self):
    return False

# +++++++++++++++++++++++++PRINT+++++++++++++++++++++++++++++
  def print(self):
    print("print")
    children = []
    if(self.current_token.type == "VISIBLE_KEYWORD"):
      self.eat("VISIBLE_KEYWORD") 
      children.append(Node("VISIBLE_KEYWORD"))
    else:
      return False
    
    printop_node = self.printop()
    children.append(printop_node)

    return Node("PRINT", children = children)
  
  # Tail-recursion is used to catch multiple argument in VISIBLE/printing
  def printop(self,children = []):
    value_node = self.value()
    children.append(value_node)
    
    if (self.current_token.type != "LINEBREAK"):
      self.printop(children)
    
    return Node("PRINTOP", children = children)


# +++++++++++++++++++++++++ASSIGNMENT++++++++++++++++++++++++
  def assign(self):
    children = []
    variable_node = self.variable()
    if (variable_node):
      children.append(variable_node)
    else:
      return False
    
    self.eat("R_KEYWORD")
    children.append(Node("R_KEYWORD"))
    
    value_node = self.value()
    children.append(value_node)
  
    return Node("ASSIGN", children = children)
  
  def variable(self):
    children = []
    if (self.current_token.type == "VAR_IDENTIFIER"):
      children.append(Node("VAR_IDENTIFIER", value = self.current_token.name))
      self.eat("VAR_IDENTIFIER")
    elif (self.current_token.type == "IT_KEYWORD"):
      print("it")
      self.eat("IT_KEYWORD")
      children.append("IT_KEYWORD")
    else:
      return False
    
    return Node("VARIABLE", children = children)
  
  def value(self):
    children = []
    if (variable_node := self.variable()):
      children.append(variable_node)
    elif (expr_node := self.expr()):
      children.append(expr_node)
    else:
      literal_node = self.literal()
      children.append(literal_node)
    
    return Node("VALUE", children = children)
  
  def literal(self):
    children = []
    
    # Catches all the literal
    if(self.current_token.type == "YARN_LITERAL"):
      print("yarn literal")
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
    
    return Node("LITERAL", children = children)


# ===============CONCATENATION==============
  def concatenation(self):
    children = []
    if (self.current_token.type == "SMOOSH_KEYWORD"):
      self.eat("SMOOSH_KEYWORD")
      children.append(Node("SMOOSH_KEYWORD"))
    else:
      return False
    
    self.strconcat()
    
    return Node("CONCATENATION", children = children)
  
  def strconcat(self):
    return False
    

# ===============COMPARISON=================
  def comparison(self):
    children = []
    if (equal_node := self.equal()):
      children.append(equal_node)
    elif (noequal_node := self.noequal()):
      children.append(noequal_node)
    elif (moreequal_node := self.moreequal()):
      children.append(moreequal_node)
    elif (lessequal_node := self.lessequal()):
      children.append(lessequal_node)
    elif (more_node := self.more()):
      children.append(more_node)
    elif (less_node := self.less()):
      children.append(less_node)
    else:
      return False

    return Node("COMPARISON", children = children)
  
  def equal(self):
    return False
  def noequal(self):
    return False
  def moreequal(self):
    return False
  def lessequal(self):
    return False
  def more(self):
    return False
  def less(self):
    return False
  
# ===============BOOLEAN====================
  def boolean(self):
    children = []
    if (bool1_node := self.bool1()):
      children.append(bool1_node)
    elif (bool2_node := self.bool2()):
      children.append(bool2_node)
    else:
      return False
    
    return Node("BOOLEAN", children = children)
  
  def bool1(self):
    return False
  def bool2(self):
    return False
  def andLol(self):
    pass
  def orLol(self):
    pass
  def xorLol(self):
    pass
  def notLol(self):
    pass
# ==============ARITHMETIC==================

  def arithmetic(self):
    children = []
    
    if (addition_node := self.addition()):
      print("addition")
      children.append(addition_node)
    elif (subtraction_node := self.subtraction()):
      print("subtraction")
      children.append(subtraction_node)
    elif (multiplication_node := self.multiplication()):
      print("mult")
      children.append(multiplication_node)
    elif (division_node := self.division()):
      print("div")
      children.append(division_node)
    elif (modulo_node := self.modulo()):
      print("div")
      children.append(modulo_node)
    elif (greater_node := self.greater()):
      print("div")
      children.append(greater_node)
    elif (lesser_node := self.lesser()):
      print("div")
      children.append(lesser_node)
    else:
      return False
    
    return Node("ARITHMETIC", children = children)
  
  def number(self):
    children = []
    
    if (self.current_token.type == "NUMBR_LITERAL"):
      self.eat("NUMBR_LITERAL")
      children.append(Node("NUMBR_LITERAL"))
    else:
      self.eat("NUMBAR_LITERAL")
      children.append(Node("NUMBAR_LITERAL"))
    
    return Node("NUMBER", children = children)
  
  def addition(self):
    children = []
    # SUM OF
    if (self.current_token.type == "SUM_OF_KEYWORD"):
      self.eat("SUM_OF_KEYWORD")
      children.append(Node("SUM_OF_KEYWORD"))
    else:
      return False
    
    # <arithmetic> | <number>
    if (arithmetic_node := self.arithmetic()):
      children.append(arithmetic_node)
    else:
      number_node = self.number()
      children.append(number_node)
    
    # AN
    self.eat("AN_KEYWORD")
    children.append(Node("AN_KEYWORD"))
    
    # <number>
    number_node = self.number()
    children.append(number_node)
    
    return Node("ADDITION", children = children)
  
  def subtraction(self):
    return False
    # DIFF OF
    
    # <arithmetic> | <number>
    
    # AN
    
    # <number>
    
  def multiplication(self):
    return False
    # PRODUKT OF
    
    # <arithmetic> | <number>
    
    # AN
    
    # <number>
    
  def division(self):
    return False
    # QUOSHUNT OF
    
    # <arithmetic> | <number>
    
    # AN
    
    # <number>
    
  def modulo(self):
    return False
    # MOD OF
    
    # <arithmetic> | <number>
    
    # AN
    
    # <number>
    
  def greater(self):
    return False
    # BIGGR OF
    
    # <arithmetic> | <number>
    
    # AN
    
    # <number>
    
  def lesser(self):
    return False
    # SMALLR OF
    
    # <arithmetic> | <number>
    
    # AN
    
    # <number>


# +++++++++++++++++++++++EXPRESSION+++++++++++++++++++++++++
  def expr(self):
    children = []
    
    if (arithmetic_node := self.arithmetic()):
      children.append(arithmetic_node)
    elif (boolean_node := self.boolean()):
      children.append(boolean_node)
    elif (comparison_node := self.comparison()):
      children.append(comparison_node)
    elif (concatenation_node := self.concatenation()):
      children.append(concatenation_node)
    else:
      return False
    
    return Node("EXPR", children = children)

  
  def end(self):
    self.eat("LINEBREAK")
    
    return Node("LINEBREAK")
  
  def statement(self):
    children = []
    # <expr>
    if (expr_node := self.expr()):
      children.append(expr_node)
    # <assign>
    elif (assign_node := self.assign()):
      children.append(assign_node)
    # <print>
    elif (print_node := self.print()):
      children.append(print_node)
    # <input>
    elif (input_node := self.input()):
      children.append(input_node)
    # <declaration>
    elif (declaration_node := self.declaration()):
      children.append(declaration_node)
    # <control>
    elif (control_node := self.control()):
      children.append(control_node)
    # # <multilinecomment>
    elif (multilinecomment_node := self.multilinecomment()):
      children.append(multilinecomment_node)
    
    end_node = self.end()
    children.append(end_node)
      
    return Node("STATEMENT", children = children)
  
  def codeblock(self,children = []):
    print("codeblock")
    # <statement> 
    statement = self.statement()
    children.append(statement)

    # <statement><codeblock>
    token_type = self.current_token.type
    if(token_type != "KTHXBYE_KEYWORD"):
      self.codeblock(children)

    return Node("CODEBLOCK", children = children)
  
  def program(self):
    print("program")
    children = []
    # HAI
    self.eat("HAI_KEYWORD")
    children.append(Node("HAI_KEYWORD"))
    
    # <linebreak>
    self.eat("LINEBREAK")
    children.append(Node("LINEBREAK"))

    # <codeblock>
    codeblock = self.codeblock()
    children.append(codeblock)
    
    # KTHXBYE
    self.eat("KTHXBYE_KEYWORD")
    children.append(Node("KTHXBYE_KEYWORD"))

    # <linebreak>
    self.eat("LINEBREAK")
    children.append(Node("LINEBREAK"))

    return Node("PROGRAM", children = children)

  def parse(self):
    # <program>
    tree = self.program()
    print("End parsing")
    return tree
