from scipy import fft
import numpy as np

line =[]
corrente = []
vibracao = []
i = 0

# Number of sample points
N = 5000

# sample spacing
T = 1.0 / 1500.0

with open("C:\\Users\Matias\Desktop\eletrica\Projeto_de_formatura\sensores\sensores\monitor.txt" , "r") as f:

    for line in f:
       
        if not line:
            break
        elif i <=10 :
            f.readline()
            i += 1
        else :   
            i += 1
            words = line.split()
            if words != []: 
                words[0]: corrente
                words[1]: vibracao
                corrente.append(float(words[0]))
                vibracao.append((words[1]))

            if i >= N:
                break


yfcorrente = fft(corrente)
yfvibracao = fft(vibracao)

xf = np.linspace(0.0, 1.0/(2.0*T), N//2)

import matplotlib.pyplot as plt

plt.subplot(2, 1, 1)
plt.plot(xf[:-5],  2.0/N * np.abs( yfcorrente[0:N//2] )  ) #, 'ko-')
plt.title('Monitor FFT - EMIDIT')
plt.ylabel('Corrente')
plt.grid()
plt.subplot(2, 1, 2)
plt.plot(xf[:-5], 2.0/N * np.abs(yfvibracao[0:N//2]))
plt.xlabel('frequencia (Hz) ')
plt.ylabel('Vibracao')

plt.grid()
plt.show()




