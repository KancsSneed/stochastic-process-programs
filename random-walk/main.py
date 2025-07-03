import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

# Parâmetros
num_particulas = 10000 
num_passos = 100
Namt = 100

posicoes_finais = np.zeros(num_particulas)

for _ in range(Namt):
    posicoes = np.zeros(num_particulas)
    for _ in range(num_passos):
        posicoes += np.random.choice([-1, 1], size=num_particulas)
    posicoes_finais += posicoes

posicoes_finais /= Namt

media_empirica = np.mean(posicoes_finais)

valores, bins = np.histogram(posicoes_finais, bins=80, density=True)
centros = (bins[:-1] + bins[1:]) / 2
largura_bin = bins[1] - bins[0]

media_teorica = 0
desvio_padrao = np.sqrt(num_passos / Namt)
x = np.linspace(bins[0], bins[-1], 1000)
pdf = norm.pdf(x, loc=media_teorica, scale=desvio_padrao)

plt.figure(figsize=(10, 5))
plt.bar(centros, valores, width=largura_bin, color='skyblue', edgecolor='blue', alpha=0.6, label='simulacao')
plt.plot(x, pdf, '-', color='red', linewidth=2, label='distribuicao normal')
plt.axvline(media_empirica, color='green', linestyle='--', linewidth=2, label='media da caminhada')
plt.title("caminhada aleatoria no eixo x")
plt.xlabel("posicao final")
plt.ylabel("probabilidade")
plt.legend()
plt.grid(True, linestyle='--', alpha=0.6)
plt.show()
