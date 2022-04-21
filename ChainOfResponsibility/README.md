# Chain of Responsibility
O Chain of Responsibility é um padrão de projeto comportamental que permite que você passe pedidos por uma corrente de handlers. Ao receber um pedido, cada handler decide se processa o pedido ou o passa adiante para o próximo handler na corrente.


## Quando usar?
O padrão Chain of Responsibility cai como uma luva quando temos uma lista de comandos a serem executados de acordo com algum cenário em específico, e sabemos também qual o próximo cenário que deve ser validado, caso o anterior não satisfaça a condição.

Nesses casos, o Chain of Responsibility nos possibilita a separação de responsabilidades em classes pequenas e enxutas, e ainda provê uma maneira flexível e desacoplada de juntar esses comportamentos novamente.

No Chain of Responsibility cada "estratégia" também possui a responsabilidade de descobrir se ela deve ser aplicada e, caso não aplique, delegar para a próxima. Por isso tem nas classes como Desconto_por_cinco_itens aquele if, e por isso ela deve saber do próximo:

```
# -*- coding: UTF-8 -*-
# descontos.py
class Desconto_por_cinco_itens(object):

  def __init__(self, proximo_desconto):
    self._proximo_desconto = proximo_desconto

  def calcular(orcamento):

    if orcamento.total_itens > 5:
        return orcamento.valor * 0.1
    else: 
      return self._proximo_desconto.calcular(orcamento)
```


Links Úteis: 
https://refactoring.guru/pt-br/design-patterns/chain-of-responsibility