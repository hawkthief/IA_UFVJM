import csv

class grafo:
  def __init__(self, dir):
    self.dir = bool(dir)
    self.nodes = []
    self.links = []

  def addnode(self, node):
    self.nodes.append(node)
  
  def addlink(self, nodea, nodeb, value):
    link = []
    if nodea in self.nodes and nodeb in self.nodes:
      link.append(nodea)
      link.append(nodeb)
      link.append(value)      
      self.links.append(link)
    else:
      raise ReferenceError("Um dos nodos a ser conectados não existe")

def legrafo(arquivo):
  try:
    arquivo = str(arquivo)
  except:
    raise TypeError("Parâmetro inválido (uma string era o esperado)")
  a = open(arquivo) #a = ARQUIVO
  a = csv.reader(a)
  a = list(a)

  d = a.pop(0) #d = GRAFO DIRECIONADO
  d = int(d[0])

  graph = grafo(d)

  for x in a.pop(0):
    graph.addnode(x)

  for x in a:
    graph.addlink(x[0],x[1],x[2])

  return graph
  
def graph():
  graf = legrafo("grafo.csv")


  element = ["X"]
  element.extend(graf.nodes)

  tabela=[]
  tabela.append(element)
  flag = True

  for x in graf.nodes:
    element = [x]
    for y in graf.nodes:
      flag = True
      for z in graf.links:
        if (z[0] == x and z[1] == y) or (z[1] == x and z[0] == y):
          element.append(z[2])
          flag = False
      if flag:
        element.append("X")      
    tabela.append(element)

          
  for x in tabela:
    print(x)