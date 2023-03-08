#comprando figurinhas até completar o álbum
def SimulAlbum(qtde_albuns = 1):
  album = np.zeros(n_album)
  pacotes = 0
  while not np.all(album >= qtde_albuns):
    pacotinho = np.random.choice(range(n_album), 4)
    pacotes += 1
    for i in pacotinho:
      album[i] += 1
  valor_gasto = qtde_albuns*preco_album + preco_pacote*pacotes
  valor_gasto_album = valor_gasto/qtde_albuns

  return valor_gasto, pacotes, valor_gasto_album

SimulAlbum(2)

def Simulacao(qtde_albuns, simulacoes = 1000, silencio = False):
  valores = []
  for i in range(simulacoes):
    valores.append(SimulAlbum(qtde_albuns)[2])
    if not silencio:
      if (i+1) % 100 == 0:
        print('Simulacoes: ', i+1, '/', simulacoes)
  return valores

sim = Simulacao(qtde_albuns = 2, simulacoes = 100)

sim2 = Simulacao(2, 100, silencio = True)
c2 = np.array(sim2).mean()


sim3 = Simulacao(3, 100, silencio = True)
c3 = np.array(sim3).mean()

print('Custo médio com dois amigos', round(c2, 2))
print('Custo médio com três amigos', round(c3, 2))


def Simulacao(qtde_albuns, simulacoes = 1000, silencio = False):
  valores = []
  for i in range(simulacoes):
    valores.append(SimulAlbum(qtde_albuns)[2])
    if not silencio:
      if (i+1) % 100 == 0:
        print('Simulacoes: ', i+1, '/', simulacoes)
  return valores

sim = Simulacao(qtde_albuns = 2, simulacoes = 100)

import time

def SimulacaoAmigos(amigos = 40, simulacoes = 10):
  medias = []
  amigos = list(range(1, amigos + 1, 1))
  for i in amigos:
    t = time.time()
    aux = Simulacao(i, simulacoes, silencio = True)
    tempo = round(time.time() - t, 2)
    print('Tempo total de {}s para a simulação com {} amigo(s)'.format(tempo, i))
    medias.append(np.array(aux).mean())
  return amigos, medias

sim_amigos = SimulacaoAmigos(amigos = 40, simulacoes = 5)

import math

def GraficoCustoAmigos(simulacao):
  minimo_possivel = math.ceil(n_album/cromos_por_pacote)*preco_pacote

  plt.figure(figsize=(18, 6))
  plt.bar(simulacao[0], simulacao[1], width = 0.5, color = 'royalblue')
  plt.xticks(simulacao[0])
  plt.axhline(y = minimo_possivel, linestyle = 'dashed', color = 'blue')
  plt.title('Custo Médio aproximado para \n completar o álbum em funçaõ do tamanho \n do grupo de pessoas')
  plt.show()

GraficoCustoAmigos(sim_amigos)
