from sys import exit
 
ROT13 = 13
ROT5 = 5
 
lettersU = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
lettersD = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
 
 
def getEncIndex(in_array, begin_index, encoding):
 
  end_index = begin_index + encoding
  if end_index >= len(in_array):
    shift = end_index - (len(in_array) - 1)
    end_index = -1 + shift
 
  return end_index
 
 
def crypt(in_array, sign, encoding):
  begin_index = in_array.index(sign)
  end_index = getEncIndex(in_array, begin_index, encoding)
  return in_array[end_index]
 
 
x = ""
y = ""
while 1 == 1:
  try:
    inp = input()
    if x == "":
      x = inp
    else:
      x+= "\n" + inp
  except EOFError:
    break

 
if x == "":
	print(x)
	exit()
 
for i in x:
  if i in lettersU:
    y += crypt(lettersU, i, ROT13)
  elif i in lettersD:
    y += crypt(lettersD, i, ROT13)
  elif i in numbers:
    y += crypt(numbers, i, ROT5)
  else:
    y += i
 
print(y)
