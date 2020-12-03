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