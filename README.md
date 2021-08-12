#
![Python](https://img.shields.io/static/v1?label=python&message=v3.8.9&color=blue&logo=PYTHON)

# Problema
Balanceamento de carga é muito importante em ambientes Cloud. Estamos sempre tentando minimizar os custos para que possamos manter o número de servidores o menor possível. Em contrapartida a capacidade e performance aumenta quando adicionamos mais servidores. Em nosso ambiente de simulação, em cada tick  (unidade básica de tempo da simulação), os usuários conectam aos servidores disponíveis e executam uma tarefa. Cada tarefa leva um número de ticks para ser ﬁnalizada (o número de ticks de uma tarefa é representado por ttask ), e após isso o usuário se desconecta automaticamente.

Os servidores são máquinas virtuais que se auto criam para acomodar novos usuários. Cada servidor custa R$ 1,00 por tick e suporta no máximo umax usuários simultaneamente. Você deve ﬁnalizar servidores que não estão sendo mais usados. O desaﬁo é fazer um programa em Python que recebe usuários e os aloca nos servidores tentando manter o menor custo possível.

## input
Um arquivo onde: a primeira linha possui o valor de ttask ;
a segunda linha possui o valor de umax ;
as demais linhas contém o número de novos usuários para cada tick.

## output
Um arquivo onde cada linha contém uma lista de servidores disponíveis no ﬁnal de cada tick , representado pelo número de usuários em cada servidor separados por vírgula e, ao ﬁnal, o custo total por utilização dos servidores

## Limites
1 ≤ ttask ≤ 10 <br>
1 ≤ umax ≤ 10

# Tecnologias utilizadas: 
- Python
- unittest (Módulo Python para testes unitários)

# Execução do projeto:
1 - Faça o clone ou download do projeto.\
2 - Execute a aplicação através do comando\
```$ python load_balancing.py``` ou ```$ python3 load_balancing.py```\
3 - Para a execução dos testes, execute o comando:\
```$ python test_load_balancing.py``` ou ```$ python test_load_balancing.py```

#
Desenvolvido por [Thiago Souza](https://www.linkedin.com/in/thiagosouzalink/)
