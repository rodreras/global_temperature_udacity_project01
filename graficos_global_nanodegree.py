import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

#Inserindo os dados do arquivo CSV
datario = pd.read_csv('data_rio_sma.csv',sep=';')
datamun = pd.read_csv('data_mundo_sma.csv',sep=';')


#Transformando as colunas do arquivo em listas
anos = datario['year'].to_list()
temp = datario['avg_temp_3sma'].to_list()
temp_global = datamun['avg_temp_3sma'].to_list()

#print(anos)
#print(temp)
#print(temp_global)

#Iniciando a Construção do Gráfico

plt.figure()
#Gráfico do Mundo
plt.subplot(511) #Determinando a posição
sns.regplot(x=anos, y=temp_global, data=datamun,color='r',label = 'Trendline') #Colocando linha de tendencia
plt.scatter(anos,temp_global, color = 'y',label = 'Global Avg Temp - C°') #Determinando os dados X e Y
plt.title('Global Avg Temperatures and Trends') #Dando nome ao Gráfico
plt.ylabel('Global Avg Temp') #Dando nome ao eixo Y
plt.legend() #Configurando a legenda
plt.xlim(1832,2014) #Colocando limite do eixo X
plt.tick_params(labelright=True)
plt.ylim(7,10) #Colocando limite do eixo Y
plt.xticks(np.arange(1832, 2014,3),labels='')#Determinando os intervalos do eixo X
plt.yticks(np.arange(7, 10, 0.5)) #Determinando os intervalos do eixo Y


plt.grid(True) #Colocando Grade

#Gráfico do RJ
plt.subplot(512) #Determinando a posição
sns.regplot(x=anos, y=temp, data=datamun,color='r')#, label = 'Trendline')
plt.scatter(anos,temp, label = 'Rio Avg Temp - C°') #Determinando os dados X e Y
plt.ylabel('Rio Avg Temp') #Dando nome ao eixo Y
plt.xlim(1832,2014) #Colocando limite do eixo X
plt.xticks(np.arange(1832, 2014,3),labels='') #Determinando os intervalos do eixo X
plt.tick_params(labelright=True)
plt.ylim(22,25) #Colocando limite do eixo Y
plt.yticks(np.arange(22, 25,0.5)) #Determinando os intervalos do eixo Y
plt.legend()
plt.grid(True) #Colocando grade

#OMAHA GRAPHS______________________________________________________

#Inserindo os dados do arquivo CSV
dataom = pd.read_csv('data_omaha_sma.csv',sep=';')

#Transformando as colunas do arquivo em listas
anos = dataom['year'].to_list()
temp = dataom['avg_temp_3sma'].to_list()

#Iniciando a Construção do Gráfico

#Gráfico do Omaha
plt.subplot(513) #Determinando a posição
sns.regplot(x=anos, y=temp, data=dataom,color='r')#, label = 'Trendline')
#plt.title('Omaha Avg Temperature x Global Avg Temperature')
plt.scatter(anos,temp, color='m',label = 'Omaha Avg Temp - C°') #Determinando os dados X e Y
plt.ylabel('Omaha Avg Temp') #Dando nome ao eixo Y
plt.xlim(1832,2014) #Colocando limite do eixo X
plt.xticks(np.arange(1832, 2014,3),labels='') #Determinando os intervalos do eixo X
plt.tick_params(labelright=True)
plt.ylim(8.5,12) #Colocando limite do eixo Y
plt.yticks(np.arange(8.5, 12,0.5)) #Determinando os intervalos do eixo Y
plt.legend()
plt.grid(True) #Colocando grade

#SHANGHAI GRAPHS________________________________________________________________

#Inserindo os dados do arquivo CSV
datash = pd.read_csv('data_shanghai_sma.csv',sep=';')
#Transformando as colunas do arquivo em listas
anos = datash['year'].to_list()
temp = datash['avg_temp_3sma'].to_list()

#Iniciando a Construção do Gráfico

#Gráfico de Shanghai
plt.subplot(514) #Determinando a posição
sns.regplot(x=anos, y=temp, data=datash,color='r')#, label = 'Trendline')
#plt.title('Shanghai Avg Temperature x Global Avg Temperature')
plt.scatter(anos, temp, color='#060306',label='Shanghai Avg Temp - C°') #Determinando os dados X e Y
plt.ylabel('Shanghai Avg Temp') #Dando nome ao eixo Y
plt.xlim(1832,2014) #Colocando limite do eixo X
plt.xticks(np.arange(1832, 2014,3),labels='') #Determinando os intervalos do eixo X
plt.tick_params(labelright=True)
plt.ylim(14.5,17.5) #Colocando limite do eixo Y
plt.yticks(np.arange(14.5, 17.5,0.5)) #Determinando os intervalos do eixo Y
plt.legend()
plt.grid(True) #Colocando grade

#SYDNEY GRAPHS________________________________________________________
#Inserindo os dados do arquivo CSV
datas = pd.read_csv('data_sydney_sma.csv',sep=';')

#Transformando as colunas do arquivo em listas
anos = datas['year'].to_list()
temp = datas['avg_temp_3sma'].to_list()
temp_global = datamun['avg_temp_3sma'].to_list()

#Iniciando a Construção do Gráfico

#Gráfico de Sydeney
plt.subplot(515) #Determinando a posição
sns.regplot(x=anos, y=temp, data=datas,color='r')#, label = 'Trendline')
#plt.title('Sydney Avg Temperature x Global Avg Temperature')
plt.scatter(anos, temp, color='g',label = 'Sydney Avg Temp - C°') #Determinando os dados X e Y
plt.ylabel('Sydney Avg Temp') #Dando nome ao eixo Y
plt.xlim(1832,2014) #Colocando limite do eixo X
plt.xticks(np.arange(1832, 2014,3),rotation='90') #Determinando os intervalos do eixo X
plt.yticks(np.arange(15.5, 18.5,0.5)) #Determinando os intervalos do eixo Y
plt.ylim(15.5,18.5) #Colocando limite do eixo Y
plt.xlabel('Years') #Dando nome ao eixo X
plt.tick_params(labelright=True)
plt.grid(True) #Colocando grade
plt.legend()
plt.show()