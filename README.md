# 🪐 Uma Nova Arquitetura Matemática para o Problema dos Três Corpos

Este repositório contém o artigo científico e implementações experimentais associadas à proposta de uma formulação computável e simbólica para o clássico Problema dos Três Corpos, utilizando operadores espectrais, memória fracionária, funções teta multivariadas e estruturas topológicas.

---

## 📄 Artigo

O artigo completo está disponível em formato LaTeX no diretório principal. Ele propõe:

- Uma arquitetura funcional simbólica baseada em derivadas fracionárias com fator áureo;
- O modelo hierárquico de memória `\(\Psi_\infty\)`;
- Uma equação computável de reconstrução via transformada inversa e função teta;
- Discussão de aplicabilidade e generalizações futuras.

> **Título:** Uma Nova Arquitetura Matemática para o Problema dos Três Corpos  
> **Autor:** Pedro Henrique Cavalhieri Contessoto  
> **Data:** 4 de junho de 2025

---

## 📁 Estrutura do Repositório

```plaintext
📦 tres-corpos-memoria
├── article/
│   ├── tres-corpos.tex       # Arquivo principal do artigo (LaTeX)
│   ├── imagens/              # (Opcional) Diagramas, ilustrações, gráficos
│   └── tres-corpos.pdf       # PDF gerado
├── src/
│   ├── psi_infty_simulator.py   # Código experimental de simulação
│   ├── memory_kernel.py         # Implementação da série funcional com truncamento
│   └── examples/                # Casos de teste numérico
├── README.md
└── LICENSE
