from classes.Node import Node

class Parser:
  def __init__(self, tokens):
    self.tokens = tokens
    self.current_token = tokens[0]
  
  def eat(self, token_type):
    if (token_type == self.current_token.type):
      self.tokens.pop(0)
    else:
      raise Exception(f"Syntax Error in line number {self.current_token.line_number}: Expect {token_type} but saw {self.current_token.type}")
    if (len(self.tokens) != 0): 
      self.current_token = self.tokens[0]
    else: 
      print("Finished parsing: Tokens is empty")
  
  def parse(self):
    # <program>
    tree = self.program()
    return tree
      
# ***************************************GRAMMAR****************************************************************
# 1. Every method is equivalent to one production rule
# 2. All non-terminal is expanded using the equivalent method
# 3. Every method returns a Node (pls check the Node class)
# 4. For Node type, the convention is to use the equivalent production rule name in uppercase
# 5. For Node value, only the identifiers and literals will fill this argument
# 6. If the parsing reaches a terminal, self.eat(<terminal>) will be called (pls check the implementation of self.eat())
# 7. All syntax errors are handled by self.eat()
# 8. If the production rule is recursive, use tail recursion to accumulate all the duplicate nodes in a single children array.
      # (check the printop() and statement() for the pattern)
# 9. For the walrus operator ":=", google "Assignment Expression Python"
# 10. Check our grammar in google docs to see the overall structure. All of this is patterned from it.

# +++++++++++++++++++++++++MULTILINECOMMENT++++++++++++++++++
  def multilinecomment(self):
    # You can leave this empty for now
    return False
    
  
# +++++++++++++++++++++++++CONTROL+++++++++++++++++++++++++++
  def control(self):
    return False

# +++++++++++++++++++++++++DECLARATION+++++++++++++++++++++++
  def declaration(self):
    children = []
    # I HAS A
    if(self.current_token.type == "I_HAS_A_KEYWORD"):
      children.append(Node("I_HAS_A_KEYWORD"))
      self.eat("I_HAS_A_KEYWORD")
    else:
      return False
    
    # varident
    children.append(Node("VAR_IDENTIFIER", self.current_token.name))
    self.eat("VAR_IDENTIFIER")
    
    # I HAS A varident <initialization>
    if (self.current_token.type == "ITZ_KEYWORD"):
      init_node =self.initialization()
      children.append(init_node)
    
    return Node("DECLARATION", children = children)
  
  def initialization(self):
    children = []
    
    children.append(Node("ITZ_KEYWORD"))
    self.eat("ITZ_KEYWORD")

    value_node = self.value()
    children.append(value_node)
    
    return Node("INITIALIZATION", children = children)



# +++++++++++++++++++++++++INPUT+++++++++++++++++++++++++++++
  def input(self):
    return False

# +++++++++++++++++++++++++PRINT+++++++++++++++++++++++++++++
  def print(self):
    children = []
    # VISIBLE
    if(self.current_token.type == "VISIBLE_KEYWORD"):
      children.append(Node("VISIBLE_KEYWORD"))
      self.eat("VISIBLE_KEYWORD")
    else:
      return False
    
    # <printop>
    printop_node = self.printop([])
    children.append(printop_node)
  
    return Node("PRINT", children = children)
  
  # Tail-recursion is used to catch multiple argument in VISIBLE/printing
  def printop(self,children):
    # <value>
    value_node = self.value()
    children.append(value_node)
    
    # <printop><value>
    if (self.current_token.type != "LINEBREAK"):
      self.printop(children)
    
    return Node("PRINTOP", children = children)


# +++++++++++++++++++++++++ASSIGNMENT++++++++++++++++++++++++
  def assign(self):
    children = []
    # <variable>
    variable_node = self.variable()
    if (variable_node):
      children.append(variable_node)
    else:
      return False
    
    # R
    self.eat("R_KEYWORD")
    children.append(Node("R_KEYWORD"))
    
    # <value>
    value_node = self.value()
    children.append(value_node)
  
    return Node("ASSIGN", children = children)
  
  def variable(self):
    children = []
    # varident
    if (self.current_token.type == "VAR_IDENTIFIER"):
      children.append(Node("VAR_IDENTIFIER", value = self.current_token.name))
      self.eat("VAR_IDENTIFIER")
    # IT
    elif (self.current_token.type == "IT_KEYWORD"):
      self.eat("IT_KEYWORD")
      children.append("IT_KEYWORD")
    else:
      return False
    
    return Node("VARIABLE", children = children)
  
  def value(self):
    children = []
    # <variable>
    if (variable_node := self.variable()):
      children.append(variable_node)
    # <expr>
    elif (expr_node := self.expr()):
      children.append(expr_node)
    else:
      # <literal>
      literal_node = self.literal()
      children.append(literal_node)
    
    return Node("VALUE", children = children)
  
  def literal(self):
    children = []
 
    # Catches all the literal
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
    

    
    return Node("LITERAL", children = children)


# ===============CONCATENATION==============
  def concatenation(self):
    children = []
    # SMOOSH
    if (self.current_token.type == "SMOOSH_KEYWORD"):
      self.eat("SMOOSH_KEYWORD")
      children.append(Node("SMOOSH_KEYWORD"))
    else:
      return False
    
    # <strconcat>
    self.strconcat()
    
    return Node("CONCATENATION", children = children)
  
  def strconcat(self):
    return False
    

# ===============COMPARISON=================
  def comparison(self):
    children = []
    # <equal>
    if (equal_node := self.equal()):
      children.append(equal_node)
    # <noequal>
    elif (noequal_node := self.noequal()):
      children.append(noequal_node)
    # <moreequal>
    elif (moreequal_node := self.moreequal()):
      children.append(moreequal_node)
    # <lessequal>
    elif (lessequal_node := self.lessequal()):
      children.append(lessequal_node)
    # <more>
    elif (more_node := self.more()):
      children.append(more_node)
    # <less>
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
    # <bool1>
    if (bool1_node := self.bool1()):
      children.append(bool1_node)
    # <bool2>
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
    # <addition>
    if (addition_node := self.addition()):
      children.append(addition_node)
    # <subtraction>
    elif (subtraction_node := self.subtraction()):
      children.append(subtraction_node)
    # <multiplication>
    elif (multiplication_node := self.multiplication()):
      children.append(multiplication_node)
    # <division>
    elif (division_node := self.division()):
      children.append(division_node)
    # <modulo>
    elif (modulo_node := self.modulo()):
      children.append(modulo_node)
    # <greater>
    elif (greater_node := self.greater()):
      children.append(greater_node)
    # <lesser>
    elif (lesser_node := self.lesser()):
      children.append(lesser_node)
    else:
      return False
    
    return Node("ARITHMETIC", children = children)
  
  def number(self):
    children = []
    
    if (self.current_token.type == "NUMBR_LITERAL"):
      children.append(Node("NUMBR_LITERAL",value = self.current_token.name))
      self.eat("NUMBR_LITERAL")
    else:
      children.append(Node("NUMBAR_LITERAL",value = self.current_token.name))
      self.eat("NUMBAR_LITERAL")
      
    
    return Node("NUMBER", children = children)
  
  def addition(self):
   
    children = []
    # SUM OF
    if (self.current_token.type == "SUM_OF_KEYWORD"):
      children.append(Node("SUM_OF_KEYWORD"))
      self.eat("SUM_OF_KEYWORD")
      
    else:
      return False
    
    # <arithmetic> | <number>
    if (arithmetic_node := self.arithmetic()):
      children.append(arithmetic_node)
    else:
      
      number_node = self.number()
      children.append(number_node)
    
    # AN
    children.append(Node("AN_KEYWORD"))
    self.eat("AN_KEYWORD")
    
    
    # <number>
    number_node = self.number()
    children.append(number_node)
    
    return Node("ADDITION", children = children)
  
  def subtraction(self):
    children = []
    # DIFF OF
    if (self.current_token.type == "DIFF_OF_KEYWORD"):
      children.append(Node("DIFF_OF_KEYWORD"))
      self.eat("DIFF_OF_KEYWORD")
      
    else:
      return False
    
    # <arithmetic> | <number>
    if (arithmetic_node := self.arithmetic()):
      children.append(arithmetic_node)
    else:
      
      number_node = self.number()
      children.append(number_node)
    
    # AN
    children.append(Node("AN_KEYWORD"))
    self.eat("AN_KEYWORD")
    
    
    # <number>
    number_node = self.number()
    children.append(number_node)
    
    return Node("SUBTRACTION", children = children)
    
  def multiplication(self):
    # PRODUKT OF
    children = []
    if (self.current_token.type == "PRODUKT_OF_KEYWORD"):
      children.append(Node("PRODUKT_OF_KEYWORD"))
      self.eat("PRODUKT_OF_KEYWORD")
      
    else:
      return False
    
    # <arithmetic> | <number>
    if (arithmetic_node := self.arithmetic()):
      children.append(arithmetic_node)
    else:
      
      number_node = self.number()
      children.append(number_node)
    
    # AN
    children.append(Node("AN_KEYWORD"))
    self.eat("AN_KEYWORD")
    
    
    # <number>
    number_node = self.number()
    children.append(number_node)
    
    return Node("MULTIPLICATION", children = children)
    
  def division(self):
    # QUOSHUNT OF
    children = []
    if (self.current_token.type == "QUOSHUNT_OF_KEYWORD"):
      children.append(Node("QUOSHUNT_OF_KEYWORD"))
      self.eat("QUOSHUNT_OF_KEYWORD")
      
    else:
      return False
    
    # <arithmetic> | <number>
    if (arithmetic_node := self.arithmetic()):
      children.append(arithmetic_node)
    else:
      
      number_node = self.number()
      children.append(number_node)
    
    # AN
    children.append(Node("AN_KEYWORD"))
    self.eat("AN_KEYWORD")
    
    
    # <number>
    number_node = self.number()
    children.append(number_node)
    
    return Node("DIVISION", children = children)
    
  def modulo(self):
    # MOD OF
    children = []
    if (self.current_token.type == "MOD_OF_KEYWORD"):
      children.append(Node("MOD_OF_KEYWORD"))
      self.eat("MOD_OF_KEYWORD")
      
    else:
      return False
    
    # <arithmetic> | <number>
    if (arithmetic_node := self.arithmetic()):
      children.append(arithmetic_node)
    else:
      
      number_node = self.number()
      children.append(number_node)
    
    # AN
    children.append(Node("AN_KEYWORD"))
    self.eat("AN_KEYWORD")
    
    
    # <number>
    number_node = self.number()
    children.append(number_node)
    
    return Node("MODULO", children = children)
    
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
    # <arithmetic>
    if (arithmetic_node := self.arithmetic()):
      children.append(arithmetic_node)
    # <boolean>
    elif (boolean_node := self.boolean()):
      children.append(boolean_node)
    # <comparison>
    elif (comparison_node := self.comparison()):
      children.append(comparison_node)
    # <concatenation>
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
      
    # <end>
    end_node = self.end()
    children.append(end_node)
      
    return Node("STATEMENT", children = children)
  
  def codeblock(self,children = []):
    # <statement> 
    statement = self.statement()
    children.append(statement)

    # <statement><codeblock>
    token_type = self.current_token.type
    if(token_type != "KTHXBYE_KEYWORD"):
      self.codeblock(children)

    return Node("CODEBLOCK", children = children)
  
  def program(self):
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

  
