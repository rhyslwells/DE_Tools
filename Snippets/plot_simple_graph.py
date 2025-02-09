
Pi=1000
T=1 #period
period=np.array([0,T])
r=0.06 #6%
n=252 #daily interest rate
n=np.array(range(5))
funct=Pi*(1+r/n)**n*T
print(funct)

x=n
y=funct
plt.plot(x,y)
plt.ylabel("Compound interest of £1000")
plt.show()
