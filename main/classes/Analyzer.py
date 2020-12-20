from classes.Symbol import Symbol

class Analyzer:
  def __init__(self, tree):
    self.tree = tree
    self.symbol_table = {}
  
  def analyze(self, codeblock):
    for child in codeblock.children:
      statement = child.children[0]
      if (statement.type == "PRINT"):
        self.print(statement)
      elif (statement.type == "DECLARATION"):
        self.declaration(statement)
      elif (statement.type == "ASSIGN"):
        self.assign(statement)
      elif (statement.type == "EXPR"):
        symbol = self.get_value(statement)
        self.insert("IT", symbol)
  
  def assign(self, statement):
    variable = statement.children[0]
    identifier = variable.children[0].value
    self.lookup(identifier)
    value_node = statement.children[2]
    symbol = self.get_value(value_node.children[0])
    self.insert(identifier, symbol)
  
  def declaration(self, statement):
    identifier = statement.children[1].value
    self.insert(identifier)
    if (len(statement.children) > 2):
      init_node = statement.children[2]
      value_node = init_node.children[1]
      symbol = self.get_value(value_node.children[0])
      self.insert(identifier, symbol)
  
  def print(self, statement):
    printop = statement.children[1]
    string = ""
    for value_node in printop.children:
      # literal or variable
      val_type = value_node.children[0]
      symbol = self.get_value(val_type)
      string += str(symbol.value)
    print(string)
  
  def arithmetic(self, node):
    op1_node = node.children[1]
    op1_symbol = self.get_value(op1_node)
    op2_node = node.children[3]
    op2_symbol = self.get_value(op2_node)
    op1_symbol.value = float(op1_symbol.value) if op1_symbol.type == "NUMBAR" else int(op1_symbol.value)
    op2_symbol.value = float(op2_symbol.value) if op2_symbol.type == "NUMBAR" else int(op2_symbol.value)
    
    if (node.type == "ADDITION"):
      ans = op1_symbol.value + op2_symbol.value
    elif (node.type == "SUBTRACTION"):
      ans = op1_symbol.value - op2_symbol.value
    elif (node.type == "MULTIPLICATION"):
      ans = op1_symbol.value * op2_symbol.value
    elif (node.type == "DIVISION"):
      ans = op1_symbol.value / op2_symbol.value
    elif (node.type == "MODULO"):
      ans = op1_symbol.value % op2_symbol.value
    elif (node.type == "GREATER"):
      ans = max(op1_symbol.value, op2_symbol.value)
    elif (node.type == "LESSER"):
      ans = min(op1_symbol.value, op2_symbol.value)
    val_type = "NUMBAR" if (type(ans) == float) else "NUMBR"
    return Symbol(val_type, ans)
  
  def expr(self, node):
    if (node.type == "ARITHMETIC"):
      return self.arithmetic(node.children[0])
    elif (node.type == "COMPARISON"):
      return
    
  def get_value(self, node):
    if (node.type == "VARIABLE"):
      variable = node.children[0]
      identifier = variable.value
      self.lookup(identifier)
      return self.symbol_table[identifier]
    elif (node.type == "EXPR"):
      return self.expr(node.children[0])
    elif (node.type == "ARITHMETIC"):
      return self.arithmetic(node.children[0])
    else:
      value = node.children[0].value
      val_type = node.children[0].type
      return Symbol(val_type, value)
  
  # Adding a new variable or updating the value of the variable
  def insert(self, name, symbol = None):
    self.symbol_table.update({
      name: symbol
    })
  
  # This function is for knowing whether the current variable is already declared
  def lookup(self, name):
    for key in self.symbol_table:
      if (key == name):
        return
    raise Exception(f"Semantic Error: Variable {name} is not yet declared")