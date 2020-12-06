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
    elif(self.current_token.type == "TROOF_LITERAL"):
      children.append(Node("TROOF_LITERAL",value = self.current_token.name))
      self.eat("TROOF_LITERAL")
    
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
    children = []
    
    # Checks the length of the line to see if it is a >= or ==
    look_ahead = self.tokens
    i = 0
    while(look_ahead[i].type != "LINEBREAK" ):
      i = i + 1
    
    if (i != 4):
      return False


    # BOTH SAEM
    if (self.current_token.type == "BOTH_SAEM_KEYWORD"):
      children.append(Node("BOTH_SAEM_KEYWORD"))
      self.eat("BOTH_SAEM_KEYWORD")
      
    else:
      return False

    number_node = self.number()
    children.append(number_node)
    
    # AN
    children.append(Node("AN_KEYWORD"))
    self.eat("AN_KEYWORD")
    
  

    # <number>
    number_node = self.number()
    children.append(number_node)

    return Node("EQUAL",children = children)

  def noequal(self):
    children = []

    # Checks the length of the line to see if it is a <= or !=
    look_ahead = self.tokens
    i = 0
    while(look_ahead[i].type != "LINEBREAK" ):
      i = i + 1
    
    if (i != 4):
      return False


    #NOT EQUAL
    if (self.current_token.type == "DIFFRINT_KEYWORD"):
      children.append(Node("DIFFRINT_KEYWORD"))
      self.eat("DIFFRINT_KEYWORD")
      
    else:
      return False

    number_node = self.number()
    children.append(number_node)
    
    # AN
    children.append(Node("AN_KEYWORD"))
    self.eat("AN_KEYWORD")
    
    

    # <number>
    number_node = self.number()
    children.append(number_node)

    return Node("NOTEQUAL",children = children)
  
  # Pinag-isa ko na lang si >= at =< kasi same sila ng starting keyword
  # Nagkakaroon ng conflict if magkahiwalay
  # moreequal ang gamit dito
  def moreequal(self):
    
    children = []
    # MORE EQUAL || LESS EQUAL
    if (self.current_token.type == "BOTH_SAEM_KEYWORD"):
      children.append(Node("BOTH_SAEM_KEYWORD"))
      self.eat("BOTH_SAEM_KEYWORD")
      
    else:
      return False

    number_node = self.number()
    children.append(number_node)
    
    # AN
    children.append(Node("AN_KEYWORD"))
    self.eat("AN_KEYWORD")
    
    # BIGGR OF
    token_type = ""
    if(self.current_token.type == "BIGGR_OF_KEYWORD"):
      children.append(Node("BIGGR_OF_KEYWORD"))
      self.eat("BIGGR_OF_KEYWORD")
      token_type = "MOREEQUAL"

    elif(self.current_token.type == "SMALLR_OF_KEYWORD"):
      children.append(Node("SMALLR_OF_KEYWORD"))
      self.eat("SMALLR_OF_KEYWORD")
      token_type = "LESSEQUAL"


    number_node = self.number()
    children.append(number_node)
    
    # AN
    children.append(Node("AN_KEYWORD"))
    self.eat("AN_KEYWORD")
    
    # <number>
    number_node = self.number()
    children.append(number_node)

    return Node(token_type,children = children)

  def lessequal(self):
    children = []
    # LeSS EQUAL
    if (self.current_token.type == "BOTH_SAEM_KEYWORD"):
      children.append(Node("BOTH_SAEM_KEYWORD"))
      self.eat("BOTH_SAEM_KEYWORD")
      
    else:
      return False

    number_node = self.number()
    children.append(number_node)
    
    # AN
    children.append(Node("AN_KEYWORD"))
    self.eat("AN_KEYWORD")
    
    # SMALLR OF
    children.append(Node("SMALLR_OF_KEYWORD"))
    self.eat("SMALLR_OF_KEYWORD")

    number_node = self.number()
    children.append(number_node)
    
    # AN
    children.append(Node("AN_KEYWORD"))
    self.eat("AN_KEYWORD")
    
    # <number>
    number_node = self.number()
    children.append(number_node)

    return Node("LESSEQUAL",children = children)

  # Pinag-isa ko na lang si > at < kasi same sila ng starting keyword
  # Nagkakaroon ng conflict if magkahiwalay
  # more ang gamit dito  
  def more(self):
    children = []
    # MORE THAN
    if (self.current_token.type == "DIFFRINT_KEYWORD"):
      children.append(Node("DIFFRINT_KEYWORD"))
      self.eat("DIFFRINT_KEYWORD")
      
    else:
      return False

    number_node = self.number()
    children.append(number_node)
    
    # AN
    children.append(Node("AN_KEYWORD"))
    self.eat("AN_KEYWORD")
    
    token_type = ""
    if(self.current_token.type == "BIGGR_OF_KEYWORD"):
      children.append(Node("BIGGR_OF_KEYWORD"))
      self.eat("BIGGR_OF_KEYWORD")
      token_type = "MORE"

    elif(self.current_token.type == "SMALLR_OF_KEYWORD"):
      children.append(Node("SMALLR_OF_KEYWORD"))
      self.eat("SMALLR_OF_KEYWORD")
      token_type = "LESS"
    number_node = self.number()
    children.append(number_node)
    
    # AN
    children.append(Node("AN_KEYWORD"))
    self.eat("AN_KEYWORD")
    
    # <number>
    number_node = self.number()
    children.append(number_node)

    return Node(token_type,children = children)
  def less(self):
    children = []
    # LESS THAN
    if (self.current_token.type == "DIFFRINT_KEYWORD"):
      children.append(Node("DIFFRINT_KEYWORD"))
      self.eat("DIFFRINT_KEYWORD")
      
    else:
      return False

    number_node = self.number()
    children.append(number_node)
    
    # AN
    children.append(Node("AN_KEYWORD"))
    self.eat("AN_KEYWORD")
    
    # SMALLR OF
    children.append(Node("SMALLR_OF_KEYWORD"))
    self.eat("SMALLR_OF_KEYWORD")

    number_node = self.number()
    children.append(number_node)
    
    # AN
    children.append(Node("AN_KEYWORD"))
    self.eat("AN_KEYWORD")
    
    # <number>
    number_node = self.number()
    children.append(number_node)

    return Node("LESS",children = children)
  
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
    children = []
    if(andLol_node := self.andLol()):
      children.append(andLol_node)
    elif(orLol_node := self.orLol()):
      children.append(orLol_node)
    elif(xorLol_node := self.xorLol()):
      children.append(xorLol_node)
    elif(notLol_node := self.notLol()):
      children.append(notLol_node)
    else:
      return False

    return Node("BOOL1",children = children)
    
  def bool2(self):
    children = []
    if(all_code := self.allLol()):
      children.append(all_code)
    elif(any_code := self.anyLol()):
      children.append(any_code)
    else:
      return False

    return Node("BOOL2",children = children)

  def andLol(self):
    children = []
    # BOTH OF
    if (self.current_token.type == "BOTH_OF_KEYWORD"):
      children.append(Node("BOTH_OF_KEYWORD"))
      self.eat("BOTH_OF_KEYWORD")
      
    else:
      return False
    
    # <bool1> | <troof>
    if (bool_node := self.bool1()):
      children.append(bool_node)
    else:
      
      literal_node = self.literal()
      children.append(literal_node)
    
    # AN
    children.append(Node("AN_KEYWORD"))
    self.eat("AN_KEYWORD")
    
    
    # <troof>
    literal_node = self.literal()
    children.append(literal_node)

    return Node("AND",children = children)
    
  def orLol(self):
    children = []
    # EITHER OF
    if (self.current_token.type == "EITHER_OF_KEYWORD"):
      children.append(Node("EITHER_OF_KEYWORD"))
      self.eat("EITHER_OF_KEYWORD")
      
    else:
      return False
    
    # <bool1> | <troof>
    if (bool_node := self.bool1()):
      children.append(bool_node)
    else:
      
      literal_node = self.literal()
      children.append(literal_node)
    
    # AN
    children.append(Node("AN_KEYWORD"))
    self.eat("AN_KEYWORD")
    
    
    # <troof>
    literal_node = self.literal()
    children.append(literal_node)

    return Node("OR",children = children)
  def xorLol(self):
    children = []
    # WON OF
    if (self.current_token.type == "WON_OF_KEYWORD"):
      children.append(Node("WON_OF_KEYWORD"))
      self.eat("WON_OF_KEYWORD")
      
    else:
      return False
    
    # <bool1> | <troof>
    if (bool_node := self.bool1()):
      children.append(bool_node)
    else:
      
      literal_node = self.literal()
      children.append(literal_node)
    
    # AN
    children.append(Node("AN_KEYWORD"))
    self.eat("AN_KEYWORD")
    
    
    # <troof>
    literal_node = self.literal()
    children.append(literal_node)

    return Node("XOR",children = children)
    
  def notLol(self):
    children = []
    # NOT
    if (self.current_token.type == "NOT_KEYWORD"):
      children.append(Node("NOT_KEYWORD"))
      self.eat("NOT_KEYWORD")
      
    else:
      return False
    
    # <bool1> | <troof>
    if (bool_node := self.bool1()):
      children.append(bool_node)
    else:
      
      literal_node = self.literal()
      children.append(literal_node)
    
    return Node("XOR",children = children)
  
  def boolop(self):
    children = []
    
    children.append(self.bool1())
    while self.current_token.type != "MKAY_KEYWORD":
    
      children.append(Node("AN_KEYWORD"))
      self.eat("AN_KEYWORD")

      children.append(self.bool1())
      
    print("DONE")
    return Node("BOOLOP",children=children)

  def allLol(self):
    children = []
    if(self.current_token.type == "ALL_OF_KEYWORD"):
      children.append(Node("ALL_OF_KEYWORD"))
      self.eat("ALL_OF_KEYWORD")
    else:
      return False
    
    all_node = self.boolop()
    children.append(all_node)

    children.append(Node("MKAY"))
    self.eat("MKAY_KEYWORD")

    return Node("ALL",children = children)

  def anyLol(self):
    children = []
    if(self.current_token.type == "ANY_OF_KEYWORD"):
      children.append(Node("ANY_OF_KEYWORD"))
      self.eat("ANY_OF_KEYWORD")
    else:
      return False
    
    all_node = self.boolop()
    children.append(all_node)

    children.append(Node("MKAY"))
    self.eat("MKAY_KEYWORD")

    return Node("ANY",children = children)

  
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
    # BIGGR OF
    children = []
    if (self.current_token.type == "BIGGR_OF_KEYWORD"):
      children.append(Node("BIGGR_OF_KEYWORD"))
      self.eat("BIGGR_OF_KEYWORD")
      
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
    
    return Node("GREATER", children = children)
    
  def lesser(self):
    
    # SMALLR OF
    children = []
    if (self.current_token.type == "SMALLR_OF_KEYWORD"):
      children.append(Node("SMALLR_OF_KEYWORD"))
      self.eat("SMALLR_OF_KEYWORD")
      
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
    
    return Node("LESSER", children = children)
    

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

  
