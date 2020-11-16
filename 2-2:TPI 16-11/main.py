# TRABALHO PRÁTICO DE INTELIGÊNCIA ARTIFICIAL
# DESENVOLVIDO POR DANIEL LOPES BUENO LOBATO
# REFERENTE AO SEGUNDO SEMESTRE DE 2020

import copy as cp

class tree:
  def __init__(self, rootinfo):
    self.root = node(rootinfo)

  def print(self):
    global printlist
    printlist = []
    printlist.append(self.root.data)
    self.root.printnext()

class node:
  def __init__(self,info):
    self.data = cp.deepcopy(info)
    self.next = []
    global printlist

  def newnext(self,info):
    self.next.append(node(info))

  def printnext(self):
    if self.next != []:  
      for x in self.next:
        printlist.append(x.data)
      
      for x in self.next:
        x.printnext() 

class puzzle:
  def __init__(self,tam):
    self.mat = cp.deepcopy(genobj(tam))    
    self.h = tam

  def fill(self):
    for x in range(self.h):
      for y in range(self.h):
        max = str((self.h) * (self.h) -1)
        m = "Insira um numero entre 0 e " + max + " sem repetir um dos números anteriores "
        self.mat[x][y] = int(input(m))
    return self.mat

  def generate(self,current):
    
    self.x = -1
    self.y = -1

    for x in range(self.h):
      for y in range (self.h):
        if (current[x][y] == 0):
          self.x = x
          self.y = y
    
    x=self.x 
    y=self.y 

    
    self.list = []

    if (self.x > 0):
      self.temp = None
      self.temp = cp.deepcopy(current)
      self.temp[x][y] = self.temp[x-1][y]
      self.temp[x-1][y] = 0
      self.list.append(self.temp)
    
    if (self.x < (self.h-1) and self.x != -1):

      self.temp = None
      self.temp = cp.deepcopy(current)
      self.temp[x][y] = self.temp[x+1][y]
      self.temp[x+1][y] = 0
      self.list.append(self.temp)

    if (self.y > 0):
      self.temp = None
      self.temp = cp.deepcopy(current)
      self.temp[x][y] = self.temp[x][y-1]
      self.temp[x][y-1] = 0
      self.list.append(self.temp)

    if (self.y < (self.h-1) and self.y != -1):
      self.temp = None
      self.temp = cp.deepcopy(current)
      self.temp[x][y] = self.temp[x][y+1]
      self.temp[x][y+1] = 0
      self.list.append(self.temp)

    return self.list

def add (opcoes, nodo, arvore):
  for x in opcoes:
    if not bfs(arvore,x):
      nodo.newnext(x)
  return nodo.next

def iterate(front,arvore):
  f=[]
  for x in front:
    f.extend(add(resolver.generate(x.data),x,arvore))
  return f

def check(front,arvore):
  nodes = front
  front = []
  front = iterate(nodes,arvore)

  for x in front:
    if objective == x.data:
      global OBJ
      OBJ = False

  return front

def dfs(arvore, objetivo):

  def deep(raiz):
    nonlocal path
    nonlocal result

    for x in raiz.next:
      if (x.data == objetivo):
        result = True
        path.append(x.data)
        return True
      deep(x)
      if result == True:
        path.append(x.data)
        return True
    
    return False

  result = False
  path = []

  for x in arvore.root.next:
    if not result:
      path = []
      deep(x)
      if result:
        path.append(x.data)
  
  path.append(arvore.root.data)

  return result, path;

def bfs(arvore, objetivo):
  
  def breadth(camada, objetivo):
    proxcamada = []
    for x in camada:
      proxcamada.extend(x.next)
      if(x.data == objetivo):
        return True
    try:
      return breadth(proxcamada,objetivo)
    except:
      return False
  
  proxcamada = []
  proxcamada.extend(arvore.root.next)
  if(arvore.root.data == objetivo):
    return True
  return breadth(proxcamada,objetivo)

def genobj(n):
  num = 1
  objective = []
  for x in range(n):
    objective.append([])
    for y in range(n):
      objective[x].extend([num]) 
      num += 1
  objective[n-1][n-1] = 0
  return objective
      
def imprimelista(lis):
  a=0
  for x in lis:
    b=0
    for y in lis[0]:
      print(lis[a][b])
      b+=1
    a+=1
    print ("----") 

def MAIN():

  resolver = puzzle(3)

  objective = cp.deepcopy(genobj(3))

  OBJ = True

  mat = cp.deepcopy(resolver.fill()) #mat = [[4,1,2],[8,0,3],[5,7,6]] 

  arv = tree(mat)

  frontier = []
  nodes = []

  lis = resolver.generate(arv.root.data)
  frontier.extend(add(lis,arv.root,arv))

  for x in frontier:
    if objective == x.data:
      OBJ = False

  while OBJ:
    frontier = check(frontier,arv)

  lis = dfs(arv,objective)[1]

  imprimelista(lis)

MAIN()