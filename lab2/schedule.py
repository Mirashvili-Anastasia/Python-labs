import matplotlib.pyplot as plt
import numpy as np
import math
x = np.linspace(0,1,500)
y1 = 8 * x**3 * np.cos(x)
y2 = 4.786 * x - 1.515
plt.title('Вариант 6') # заголовок
plt.xlabel('x1, x2') # ось абсцисс
plt.ylabel('y1, y2') # ось ординат
plt.grid() # включение отображение сетки
plt.plot(x,y1, x,y2)
plt.show()

