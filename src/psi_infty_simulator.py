import numpy as np
import matplotlib.pyplot as plt
from src.memory_kernel import MemoryKernel


import matplotlib
matplotlib.use("TkAgg")


class PsiInftySimulator:
    """
    Simulador do modelo hierárquico Psi_infty com camadas fracionárias de memória.
    """

    def __init__(self, max_layers: int = 5, phi: float = (1 + 5 ** 0.5) / 2):
        """
        Inicializa o simulador baseado na arquitetura Psi_infty.

        :param max_layers: Número de camadas hierárquicas de memória (truncamento da expansão).
        :param phi: Fator fracionário (por padrão, o número de ouro).
        """
        self.max_layers = max_layers
        self.phi = phi
        self.kernels = [
            MemoryKernel(phi=phi, max_order=10 + i * 5)
            for i in range(max_layers)
        ]

    def simulate(self, t_values: np.ndarray, initial_condition_func) -> np.ndarray:
        """
        Simula a trajetória r(t) ao longo de valores de tempo utilizando o modelo Psi_infty.

        :param t_values: Array de tempos para simulação.
        :param initial_condition_func: Função que retorna a derivada fracionária no tempo t=0, para uma ordem alpha.
        :return: Trajetória r(t) simulada como array NumPy.
        """
        trajectory = []

        for t in t_values:
            r_t = 0.0
            decay = np.exp(-t * 0.1)  # amortecimento artificial para estabilidade

            for i, kernel in enumerate(self.kernels):
                layer_weight = 1.0 / (i + 1)
                r_t += layer_weight * kernel.fractional_series(t, initial_condition_func)

            trajectory.append(r_t * decay)

        return np.array(trajectory)


# ============================
# Exemplo de uso
# ============================

if __name__ == "__main__":
    def mock_deriv(alpha):
        """
        Modelo simplificado da derivada fracionária no instante t=0.
        """
        return np.sin(alpha) / (1 + alpha ** 1.5)


    # Configura e executa o simulador
    simulator = PsiInftySimulator(max_layers=4)
    t_vals = np.linspace(0, 10, 300)
    r_vals = simulator.simulate(t_vals, mock_deriv)

    # Plota o resultado
    plt.figure(figsize=(10, 4))
    plt.plot(t_vals, r_vals, label=r"$\Psi_\infty(t)$", color="blue")
    plt.title("Simulação Hierárquica com Memória Fracionária (Modelo $\Psi_\infty$)")
    plt.xlabel("Tempo $t$")
    plt.ylabel("r(t)")
    plt.grid(True)
    plt.legend()
    plt.tight_layout()
    plt.show()
