import numpy as np
import matplotlib.pyplot as plt
from src.psi_infty_simulator import PsiInftySimulator

import matplotlib
matplotlib.use("TkAgg")

def exemplo_derivadas(alpha: float) -> float:
    """
    Função modelo para derivadas fracionárias no instante t = 0.
    Esta função pode ser substituída por uma série simbólica real ou outro modelo físico.

    :param alpha: Ordem fracionária da derivada.
    :return: Valor estimado da derivada fracionária de ordem alpha.
    """
    return np.exp(-alpha) * np.cos(alpha)


# Parâmetros da simulação temporal
tempo_inicial = 0.0
tempo_final = 20.0
n_pontos = 500
t_values = np.linspace(tempo_inicial, tempo_final, n_pontos)

# Inicialização do simulador com 5 camadas hierárquicas de memória
simulador = PsiInftySimulator(max_layers=5)

# Execução da simulação usando o modelo de derivadas fornecido
r_values = simulador.simulate(t_values, exemplo_derivadas)

# Visualização dos resultados
plt.figure(figsize=(10, 5))
plt.plot(t_values, r_values, label=r"Simulação $\Psi_\infty(t)$", color='darkblue')
plt.title("Dinâmica Temporal com Arquitetura Hierárquica $\Psi_\infty$")
plt.xlabel("Tempo $t$")
plt.ylabel("Estado $r(t)$")
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()
