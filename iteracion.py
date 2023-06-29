import psutil as P
import matplotlib.pyplot as plt

a1=[]
a2=[]
v1=0
for process in P.process_iter():
    v1=v1+1
    if v1<=6:
        v2=process.name()
        v3=P.cpu_percent()
        print("Nombre : ", v2,"Porcentaje de CPU : ",v3)
        a1.append(v2)
        a2.append(v3)
        
plt.figure(figsize=(15,7))
plt.xlabel("Apps")
plt.ylabel("Percent")
plt.bar(a1, a2, width=0.5, color=("green","purple","brown","yellow","pink","red"))
plt.show()