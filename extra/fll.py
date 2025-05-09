# This module contains a set of functions that operate on linked lists in a functional way.
# The linked list is represented as a tuple where the first element is the head and the second element is the tail.
# None represents the empty list, the end.
# LL = (4, (12, (5, (-18, (-12, (16, (3, None)))))))

def selectionSort(LL):
    if not LL:
        return LL

    tuple = None

    if LL[0] > _get_min(LL):
        tuple = _switch(LL, _get_min(LL), LL[0])
        return (tuple[0], selectionSort(tuple[1]))
    else:
        return (LL[0], selectionSort(LL[1]))

def _get_min(LL):
    if not LL[1]:
        return LL[0]

    min = _get_min(LL[1])
    if LL[0] < min:
        return LL[0]
    else:
        return min

def _switch(LL, menor_valor, maior_valor):
    if not LL:
        return LL

    if LL[0] == menor_valor:
        return (maior_valor, _switch(LL[1], menor_valor, maior_valor))
    elif LL[0] == maior_valor:
        return (menor_valor, _switch(LL[1], menor_valor, maior_valor))
    else:
        return (LL[0], _switch(LL[1], menor_valor, maior_valor))
        
def primeLL(LL):
  if not LL:
      return LL
  elif LL[0] <= 0:
      return primeLL(LL[1])

  if _prime(LL[0]) is False:
    return primeLL(LL[1])
  else:
    return (LL[0], primeLL(LL[1]))

def _prime(n, quociente=2):
  if n == 1:
    return False
  elif n == 2:
    return True
    
  if n % quociente == 0:
    return False
  
  if quociente >= n**1/2:
    return n
  
  return _prime(n, quociente + 1)

def factLL(LL):
  if not LL:
    return LL
  else:
    return (_factN(LL[0]), factLL(LL[1]))

def _factN(n):
  if n <= 0:
    return 1
  else:
    return n * _factN(n - 1)

def ll2l(LL):
  if not LL:
    return []
  else:
     return [LL[0]] + ll2l(LL[1])

def l2ll(L):
  if not L:
    return None
  else:
    return (L[0], l2ll(L[1]))

def head(LL):
    return LL[0]

def tail(LL):
    return LL[1]

def count(LL):
  if not LL:
    return 0
  else:
    return 1 + count(LL[1])

def add(num, LL):
  return (num, LL)

def _sum(x, y):
  return x + y

def decinc(LL, num):
  if not LL:
    return None
  else:
    return (_sum(LL[0], num), decinc(LL[1], num))