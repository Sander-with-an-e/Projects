import matplotlib.pyplot as plt
x=[1,2,5,10]
y=[2,4,6,8]
plt.plot(x, y, "r:")
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('My Plot')
plt.grid(True)
plt.legend('L')
plt.show()
