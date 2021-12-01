from threading import *
from time import sleep
import threading

def square_number(number):
  #print("Square Number")
  for i in number:
    print("Square:", i * i)
    sleep(5)

def cube_number(number):
  #print("Cube Number")
  for j in number:
    print("Cube:", j * j * j)
    sleep(5)

lst = [1,2,3,4,5]

Th1 = threading.Thread(target= square_number,args = (lst,))
Th2 = threading.Thread(target= cube_number, args = (lst,))

Th1.start()
sleep(2)
Th2.start()

Th1.join()
Th2.join()

print("all the values are printed!")
