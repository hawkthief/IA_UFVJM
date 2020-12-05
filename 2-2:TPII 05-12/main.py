# TRABALHO PRÁTICO 2 DE INTELIGÊNCIA ARTIFICIAL
# DESENVOLVIDO POR DANIEL LOPES BUENO LOBATO
# REFERENTE AO SEGUNDO SEMESTRE DE 2020

from operator import attrgetter
import copy as cp
import os

def cls():
  os.system('cls' if os.name=='nt' else 'clear')
  lambda: os.system('cls')

cls()

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

def dfs(arvore, objetivo):
  exn = 1
  def deep(raiz):
    nonlocal path
    nonlocal result
    nonlocal exn
    exn += 1
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

  def displacement(path):
    disp =[]
    a =[]
    for x in objetivo:
      for y in x:
        a.append(y)
    
    for x in range(len(path)):
      b =[]
      for y in path[x]:
        for z in y:
          b.append(z)
      cont = len(a)
      for n in range(len(a)):
        if a[n]==b[n]:
          cont-= 1
      disp.append(cont)
    return disp

  result = False
  path = []

  for x in arvore.root.next:
    if not result:
      path = []
      deep(x)
      if result:
        path.append(x.data)
  
  path.append(arvore.root.data)
  path.reverse()
  
  disp = displacement(path)

  print ("resultado encontrado após expandir ",exn," nós")

  return path, disp, result;

def bfs(arvore, objetivo):
  path = ['-']
  disp = ['-']
  def breadth(camada, objetivo):
    proxcamada = []
    for x in camada:
      proxcamada.extend(x.next)
      if(x.data == objetivo):
        return True
    try:
      return  breadth(proxcamada,objetivo)
    except:
      return False
  
  proxcamada = []
  proxcamada.extend(arvore.root.next)
  if(arvore.root.data == objetivo):
    result =True
  else:
    result = breadth(proxcamada,objetivo)
  
  return path, disp, result

def astar(arvore,objetivo):
  class task: #this is spaghetti code and i stopped caring long ago
    exp = 0
    lista = []
    obj = False
    def __init__(self, content, parent):
      self.path = []
      if parent:
        self.path = cp.deepcopy(parent.path)
      temp = []
      temp.append(content)
      self.content = content
      if task.obj:
        self.priority = self.dist(self.content.data,task.obj)
        a = 0
        for x in task.obj:
          for y in x:
            a +=1
        temp.append (a-self.priority)
        self.priority = self.mandis(self.content.data,task.obj)
      else:
        self.priority = 0
        temp.append (self.priority)
      self.path.append(temp)
      task.lista.append(self)
      task.lista.sort(key=attrgetter('priority') ,reverse=True)

    def next(self):
      try:
        return task.lista.pop()
      except:
        return False

    def ob(self,obj):
      task.obj = obj
      i=0
      for x in obj:
        for y in x:
          i+=1      
      task.lista[0].path[0][1] = i-self.dist(task.lista[0].path[0][0].data,task.obj)


    def dist(self,atual,alvo):
      at = []
      al = []
      
      for x in atual:
        for y in x:
          at.append(y)
      
      for x in alvo:
        for y in x:
          al.append(y)

      if len(at)==len(al):
        cont = 0
        for x in range(len(al)):
          if at[x]==al[x]:
            cont+=1
        return cont
      else:
        return False

    def mandis(self,atual,alvo):
      cont = 0
      for x in range(len(alvo)):
        for y in range(len(alvo)):
          for i in range(len(alvo)):
            for j in range(len(alvo)):
              if atual[x][y]==alvo[i][j]:
                cont =+abs(x-i)
                cont =+abs(y-j)

      return cont
  
  def estrela(r,objetivo):
    pos = r.next()
    if pos:
      r.exp += 1
      nod = pos.content
      if nod.data == objetivo:
        return pos
      for x in nod.next:
        task(x,pos)
      return estrela(r,objetivo)
    return False
      
  r = task(arvore.root,False)
  r.ob(objetivo)
  result = estrela(r,objetivo)
  if result:
    print("Resultado encontrado após expandir ",r.exp," nós")
  caminho =[]
  disp = []
  for x in result.path:
    caminho.append(x[0].data)
    disp.append(x[1])


  return caminho, disp

def greedy(arvore, objetivo):
  class task: #this is spaghetti code and i stopped caring long ago
    exp = 0
    lista = []
    obj = False
    def __init__(self, content, parent):
      self.path = []
      if parent:
        self.path = cp.deepcopy(parent.path)
      temp = []
      temp.append(content)
      self.content = content
      if task.obj:
        self.priority = self.dist(self.content.data,task.obj)
        a = 0
        for x in task.obj:
          for y in x:
            a +=1
        temp.append (a-self.priority)
      else:
        self.priority = 0
        temp.append (self.priority)
      self.path.append(temp)
      task.lista.append(self)
      task.lista.sort(key=attrgetter('priority') ,reverse=False)

    def next(self):
      try:
        return task.lista.pop()
      except:
        return False

    def ob(self,obj):
      task.obj = obj
      i=0
      for x in obj:
        for y in x:
          i+=1
      task.lista[0].path[0][1] = i-self.dist(task.lista[0].path[0][0].data,task.obj)


    def dist(self,atual,alvo):
      at = []
      al = []
      
      for x in atual:
        for y in x:
          at.append(y)
      
      for x in alvo:
        for y in x:
          al.append(y)

      if len(at)==len(al):
        cont = 0
        for x in range(len(al)):
          if at[x]==al[x]:
            cont+=1
        return cont
      else:
        return False
  
  def guloso(r,objetivo):
    pos = r.next()
    if pos:
      r.exp += 1
      nod = pos.content
      if nod.data == objetivo:
        return pos
      for x in nod.next:
        task(x,pos)
      return guloso(r,objetivo)
    return False
      
  r = task(arvore.root,False)
  r.ob(objetivo)
  result = guloso(r,objetivo)
  if result:
    print("Resultado encontrado após expandir ",r.exp," nós")
  caminho =[]
  disp = []
  for x in result.path:
    caminho.append(x[0].data)
    disp.append(x[1])


  return caminho, disp

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
  path = []
  dis = []
  for x in range(len(lis[0])):
    path.append(lis[0][x])
    dis .append(lis[1][x])

  a=0
  for x in path:
    b=0
    for y in path[0]:
      print(path[a][b])
      b+=1
    a+=1
    print("peças fora do lugar: ", dis[a-1])
    print ("----") 

def geraarvore():
  global OBJ
  def add (opcoes, nodo, arvore):
    for x in opcoes:
      if not bfs(arvore,x)[2]:
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

  resolver = puzzle(3)

  objective = cp.deepcopy(genobj(3))

  OBJ = True

  mat = [[1,2,3],[4,5,6],[0,7,8]]
  #mat = [[4,1,2],[8,0,3],[5,7,6]] 
  #mat = cp.deepcopy(resolver.fill()) 

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

  return arv


arv = geraarvore()
objetivo = cp.deepcopy(genobj(3))

#lis = bfs(arv,objetivo)
#lis = dfs(arv,objetivo)
#lis = astar(arv, objetivo)
lis = greedy(arv,objetivo)


imprimelista(lis)
