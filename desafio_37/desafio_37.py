from cProfile import label
import os
import matplotlib.pyplot as plt
import pandas as pd

planilha = pd.read_excel('desafio_37/Orçamento da Despesa Pública - 2021.xlsx')

orgao = planilha['Órgão Superior']
gasto = planilha['Valor Pago']

plt.title("Orçamento da Despesa Pública - 2021")

plt.pie(gasto, labels=orgao, autopct='%1.2f%%')

plt.show()

os.system('pause')