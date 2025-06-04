# 🪐 Uma Nova Arquitetura Matemática para o Problema dos Três Corpos

Este repositório contém o artigo científico e as implementações computacionais associadas à proposta de uma formulação computável e simbólica para o clássico Problema dos Três Corpos, utilizando operadores espectrais, memória fracionária, funções teta multivariadas e estruturas topológicas.

---

## 📄 Artigo

O artigo completo está disponível em LaTeX no diretório `article/` e propõe:

* Uma arquitetura funcional hierárquica baseada em derivadas fracionárias com fator áureo ($\phi = \frac{1+\sqrt{5}}{2}$);
* O modelo $\Psi_\infty$, baseado em camadas espectrais com regularização topológica;
* Uma equação computável para reconstrução de trajetórias baseada em:

  ```math
  \vec{r}_i(t) = \Re \left\{ \mathbb{F}^{-1} \left[ \Theta\left( \int_0^t \omega(\tau) \, d\tau \right) \cdot e^{2\pi i \langle \mathbf{Q}, \tau(t) \rangle} \cdot \psi_\infty(\tau(t)) \right] \right\}
  ```
* Discussão sobre estabilidade, convergência e aplicações futuras em sistemas n-corpos.

**Título:** Uma Nova Arquitetura Matemática para o Problema dos Três Corpos
**Autor:** Pedro Henrique Cavalhieri Contessoto
**Data:** 4 de junho de 2025

---

## 📁 Estrutura do Repositório

```
📦 tres-corpos-memoria
├── article/
│   ├── modelo-psi-infty-tres-corpos.tex     # Artigo LaTeX
│   ├── imagens/                             # Gráficos e diagramas
│   └── modelo-psi-infty-tres-corpos.pdf     # Versão final em PDF
├── src/
│   ├── psi_infty_simulator.py              # Simulação hierárquica
│   ├── memory_kernel.py                    # Cálculo de derivadas fracionárias
│   ├── spectral_transform.py               # Operadores espectrais e F^-1
│   ├── omega_theta_module.py               # Função \omega e modulação \Theta
│   └── examples/
│       ├── exemplo1.py                     # Simulação com 1 corpo
│       ├── exemplo2.py                     # Explora\(\psi_\infty\) com diferentes camadas
│       ├── exemplo3.py                     # Métricas de convergência
│       ├── exemplo4.py                     # Comparativo com modelo harmônico
│       └── exemplo5.py                     # Equação completa com F^-1 e modulação
├── assets/
│   └── comparacao_psi_vs_newton_exemplo5.png # Imagem gerada por simulação
├── README.md
└── LICENSE
```

---

## ⚙️ Requisitos

* Python 3.10+
* Bibliotecas:

  * `numpy`
  * `matplotlib`
  * `scipy`

Para instalar:

```bash
pip install -r requirements.txt
```

---

## ▶️ Como Executar um Exemplo

```bash
cd src/examples
python exemplo5.py
```

Isso gerará o gráfico comparando a dinâmica da simulação de Newton com a arquitetura $\Psi_\infty$.

---

## 📊 Resultados

* O modelo $\Psi_\infty$ apresenta convergência suave, estrutura caótica limitada e estabilidade espectral;
* Comparado ao modelo de Newton (3 corpos), a nova arquitetura se aproxima da dinâmica clássica no caso de 2 corpos;
* O erro relativo médio foi computado em unidades reais (km) usando distâncias normalizadas e simulação paralela;
* A equação geral foi aplicada com FFT para recuperação temporal dos sinais orbitais.

---

## 📚 Referências-chave

* Podlubny (1999), *Fractional Differential Equations*
* Arnold (1989), *Mathematical Methods of Classical Mechanics*
* Mumford (1983), *Tata Lectures on Theta*
* Olver et al. (2010), *NIST Handbook of Mathematical Functions*
* Poincaré, *Les Méthodes Nouvelles de la Mécanique Céleste*
