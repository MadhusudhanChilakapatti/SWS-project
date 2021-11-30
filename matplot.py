import matplotlib.pyplot as plt
from random import random
   
Year = [1920,1930,1940,1950,1960,1970,1980,1990,2000,2010]
Unemployment_Rate = []

i = 0
while(i<10):
    Unemployment_Rate.append(random())
    i = i + 1
  
plt.plot(Year, Unemployment_Rate, color='red', marker='o')
plt.title('Unemployment Rate Vs Year', fontsize=14)
plt.xlabel('Year', fontsize=14)
plt.ylabel('Unemployment Rate', fontsize=14)
plt.grid()
plt.show()
