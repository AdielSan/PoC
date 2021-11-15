# SDN-MMM
sdn machine learning model distribution mechanism (SDN-MMM)

Repositório público contendo a infraestrutura utilizada na Prova de Conceito (PoC) do artigo "Estimando métricas de serviço através de In-band Network Telemetry", submetido ao XXXIX Simpósio Brasileiro de Redes de Computadores e Sistemas Distribuídos.

## Desafio
- Distribuir da melhor forma possível modelos de aprendizado de máquina na rede.
- Considerar a capacidade de cada dispositivo em uma rede com configurações heterogênias.

## Arquitetura Proposta

![Image of Yaktocat](/imagens/Foto-InicioDim-Videos.jpg)


## Requisitos:

A proposta depende dos seguintes programas para funcionar:

* Software
1. [P4-Utils](https://github.com/nsg-ethz/p4-utils)
2. [PI LIBRARY REPOSITORY](https://github.com/p4lang/PI) **is required only for topologies with
   P4Runtime switches**
3. [BEHAVIORAL MODEL (bmv2)](https://github.com/p4lang/behavioral-model)
4. [p4c](https://github.com/p4lang/p4c)
5. [Mininet](https://github.com/mininet/mininet)
6. [FRRouting](https://github.com/FRRouting/FRR) **is required
   only for topologies with routers**

P4-Utils depends on the following programs in the given order:
* Hardware





## Requisitos:

- 200 GB de espaço em disco
- 32 GB de memória RAM
- Processadores intel Xeon E5-2630 2.60GHz (ou similar)


## Topologia


## Passo a passo para executar a PoC
