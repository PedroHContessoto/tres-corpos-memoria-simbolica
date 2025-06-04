import numpy as np
from scipy.special import gamma
from typing import Callable


class MemoryKernel:
    def __init__(self, phi: float = (1 + 5 ** 0.5) / 2, max_order: int = 20):
        """
        Inicializa o núcleo de memória baseado em expansão fracionária com fator áureo.
        :param phi: Fator de crescimento fracionário (por padrão, o número de ouro).
        :param max_order: Número máximo de termos a serem considerados na expansão truncada.
        """
        self.phi = phi
        self.max_order = max_order

    def fractional_series(self, t: float, initial_conditions: Callable[[float], float]) -> float:
        """
        Avalia a série truncada no tempo t, com base em derivadas fracionárias simbólicas aproximadas.
        :param t: Tempo (float).
        :param initial_conditions: Função que retorna a n-ésima derivada fracionária no instante t=0.
        :return: Aproximação da função r_i(t) com base na expansão fracionária.
        """
        result = 0.0
        for n in range(self.max_order + 1):
            alpha = self.phi * n
            coeff = (t ** self.phi) ** n / gamma(alpha + 1)
            deriv_approx = initial_conditions(alpha)
            result += coeff * deriv_approx
        return result


# Exemplo de uso:
if __name__ == "__main__":
    def mock_initial_conditions(alpha):
        # Exemplo fictício: derivada fracionária no tempo t=0 (poderia vir de uma série simbólica)
        return np.cos(alpha)  # apenas para teste

    kernel = MemoryKernel(max_order=15)
    t = 1.0  # tempo
    result = kernel.fractional_series(t, mock_initial_conditions)
    print(f"r(t={t}) ≈ {result:.6f}")
