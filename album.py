import numpy as np
def SimulAlbum():
  n_album = 212
  preco_pacote = 4
  cromos_por_pacote = 4
  preco_album = 10
  pacotes = 0
  album = np.zeros(n_album)
  while True:
    pacotinho = np.random.choice(np.arange(0, n_album), size = 4)
    pacotes += 1;
    for i in [0, 1, 2, 3]:
      album[pacotinho[i]]+=1

    if np.all(album >= 1):
      break

  custo = pacotes*preco_pacote + preco_album
  return custo

S = 1000
resultados = []
for i in range(S):
  pessoa = SimulAlbum()
  resultados.append(pessoa)

gasto = np.array(resultados).mean()

print("O gasto médio com pacotes vale", gasto,)

numero_de_pacotes = (gasto - 10)/4

print("O número de pacotes médio comprados é", numero_de_pacotes)

import matplotlib.pyplot as plt

sim = np.array(resultados)

plt.hist(sim, bins = 20, density = True, color = 'royalblue', edgecolor = 'black')
plt.title('Distribuição Empírica do Valor Gasto para Completar o Álbum')
plt.show()

prob1 = sum(np.array(sim) < 1500)/S
prob2 = sum(np.array(sim) > np.array(sim).mean())/S

print('A probabilidade de se gastar menos de 1500 é {:.2f}%' .format(prob1*100))
print('A probabilidade de se gastar mais do que a média é {:.2f}%' .format(prob2*100))

qts = np.quantile(sim, [0.025, 0.975])
qts

print('O intervalo de valores com confiança de 95% vai de {} a {:.2f}'.format(qts[0], qts[1]))

def SimulAlbum(n_pessoas):
  n_album = 212
  preco_pacote = 4
  cromos_por_pacote = 4
  preco_album = 10
  pacotes = 0
  album = np.zeros(n_album)
  while True:
    pacotinho = np.random.choice(np.arange(0, n_album), size = 4)
    pacotes += 1;
    for i in [0, 1, 2, 3]:
      album[pacotinho[i]]+=1

    if np.all(album >= n_pessoas):
      break

  custo = pacotes*preco_pacote + preco_album
  return custo/n_pessoas

