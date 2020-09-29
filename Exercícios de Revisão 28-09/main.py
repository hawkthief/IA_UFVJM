from operator import attrgetter
import re

class task:
  def __init__(self, content, priority):
    try:
      self.content = str(content)
      self.priority = int(priority)
    except:
      self.content = " "
      self.priority = 0
      raise TypeError("Erro ao inicializar Tarefa")
    else:
      if(self.priority>5 or self.priority<0):
        self.priority=0
        print("Prioridade inválida (atribuindo valor 0 automaticamente)")

  def imprime(self):
    print('Tarefa: ' + self.content + "\n" + "Prioridade: " + str(self.priority))

def hw():
  print('hello World')

def vec():
  i = 0
  vet = []
  while(i<10):
    op=input('Insira um Número:')
    try:
      op = float(op)
    except:
      print('Opção inválida!')
    else:
      i+=1
      vet.append(op)
  return(vet)

def mat():
  i = 0
  mat = []
  while(i<10):
    try:
      mat.append(vec())
    except:
      print('Erro inesperado ao receber vetor no índice "' + i + '" (0 ~ 9)')
    else:
      i+=1
  return(mat)

def stac():
  i = 0
  stack = []
  while(i<10):
    op=input('Insira um Número:')
    try:
      op = float(op)
    except:
      print('Opção inválida!')
    else:
      i+=1
      stack.append(op)
  
  for x in range(10):
    print (stack.pop())

def q():
  i = 0
  queue = []
  while(i<10):
    op=input('Insira um Número:')
    try:
      op = float(op)
    except:
      print('Opção inválida!')
    else:
      i+=1
      queue.append(op)
  
  for x in range(10):
    print (queue.pop(0))

def tasc():
  i=0
  pri = []
  while(i<10):
    try:
      pri.append(task(input('insira a tarefa (texto)'),input('insira a prioridade (0~5)')))
    except:
      print('Erro ao inicializar Tarefa')
    else:
      i+=1

  pri.sort(key=attrgetter('priority') ,reverse=True)

  for x in pri:
    x.imprime()

a=True
while(a):
  op=input('Escolha o número correspondente à atividade desejada (de 1 a 6, 0 para sair):')
  try:
    op = int(op)
  except:
    print('Opção inválida!')
  else:
    if(op>6 or op<0):
      print('Opção inválida!')
    else:
      if(op==1):
        hw()
      elif(op==2):
        print(vec())
      elif(op==3):
        print(mat())
      elif(op==4):
        stac()
      elif(op==5):
        q()
      elif(op==6):
        tasc()
      else:
        a=False

