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