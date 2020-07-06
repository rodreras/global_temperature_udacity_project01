import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

#Inserindo os dados do arquivo CSV
datario = pd.read_csv('data_rio_sma.csv',sep=';')
datamun = pd.read_csv('data_mundo_sma.csv',sep=';')

#print(datario.head())
#Transformando as colunas do arquivo em listas
anos = datario['year'].to_list()
temp = datario['avg_temp_3sma'].to_list()
temp_global = datamun['avg_temp_3sma'].to_list()
#print(anos)
#print(temp)
#print(temp_global)


#Iniciando a Construção do Gráfico
plt.figure()

#Gráfico do RJ
plt.subplot(211) #Determinando a posição
sns.regplot(x=anos, y=temp, data=datamun,color='r', label = 'Trendline')
plt.scatter(anos,temp, label = 'Rio Avg Temp - C°') #Determinando os dados X e Y
plt.ylabel('Rio Avg Temp') #Dando nome ao eixo Y
plt.xlim(1832,2014) #Colocando limite do eixo X
plt.xticks(np.arange(1832, 2014,10)) #Determinando os intervalos do eixo X
plt.yticks(np.arange(22, 25.5,0.2)) #Determinando os intervalos do eixo Y
plt.legend(fancybox=True,shadow=True,borderpad=True)
plt.grid(True) #Colocando grade

#Gráfico do Mundo
plt.subplot(212) #Determinando a posição
sns.regplot(x=anos, y=temp_global, data=datamun,color='r',label = 'Trendline') #Colocando linha de tendencia
plt.scatter(anos,temp_global, color = 'y',label = 'Global Avg Temp - C°') #Determinando os dados X e Y
plt.xlabel('Years') #Dando nome ao eixo X
plt.ylabel('Global Avg Temp') #Dando nome ao eixo Y
plt.legend(fancybox=True,shadow=True,borderpad=True) #Configurando a legenda
plt.xlim(1832,2014) #Colocando limite do eixo X
plt.ylim(6.4,11) #Colocando limite do eixo Y
plt.xticks(np.arange(1832, 2014,10))#Determinando os intervalos do eixo X
plt.yticks(np.arange(6.4, 11, 0.2)) #Determinando os intervalos do eixo Y


plt.grid(True) #Colocando Grade

plt.show()