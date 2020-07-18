# Desafio Intelie - Dev Backend

Considere um modelo de informação, onde um registro é representado por uma "tupla".
Uma tupla (ou lista) nesse contexto é chamado de fato.

Exemplo de um fato:
- ('joão', 'idade', 18, True)

Nessa representação, a entidade (E) 'joão' tem o atributo (A) 'idade' com o valor (V) '18'.

Para indicar a remoção (ou retração) de uma informação, o quarto elemento da tupla pode ser 'False', para representar que a entidade não tem mais aquele valor associado aquele atributo.

Como é comum em um modelo de entidades, os atributos de uma entidade pode ter cardinalidade 1 ou N (muitos).

Segue um exemplo de fatos no formato de tuplas (i.e. E, A, V, added?)

```
facts = [
  ('gabriel', 'endereço', 'av rio branco, 109', True),
  ('joão', 'endereço', 'rua alice, 10', True),
  ('joão', 'endereço', 'rua bob, 88', True),
  ('joão', 'telefone', '234-5678', True),
  ('joão', 'telefone', '91234-5555', True),
  ('joão', 'telefone', '234-5678', False),
  ('gabriel', 'telefone', '98888-1111', True),
  ('gabriel', 'telefone', '56789-1010', True),
]
```

Vamos assumir que essa lista de fatos está ordenada dos mais antigos para os mais recentes.
Nesse schema, o atributo 'telefone' tem cardinalidade 'muitos' (one-to-many), e 'endereço' é 'one-to-one'.

```
schema = [
    ('endereço', 'cardinality', 'one'),
    ('telefone', 'cardinality', 'many')
]
```

Nesse exemplo, os seguintes registros representam o histórico de endereços que joão já teve:

```
(
    ('joão', 'endereço', 'rua alice, 10', True)
    ('joão', 'endereço', 'rua bob, 88', True),
)
```

E o fato considerado vigente (ou ativo) é o último.

O objetivo desse desafio é escrever uma função que retorne quais são os fatos vigentes sobre essas entidades. Ou seja, quais são as informações que estão valendo no momento atual.

A função deve receber `facts` (todos fatos conhecidos) e `schema` como argumentos.


Resultado esperado para este exemplo (mas não precisa ser nessa ordem):

```
[
  ('gabriel', 'endereço', 'av rio branco, 109', True),
  ('joão', 'endereço', 'rua bob, 88', True),
  ('joão', 'telefone', '91234-5555', True),
  ('gabriel', 'telefone', '98888-1111', True),
  ('gabriel', 'telefone', '56789-1010', True)
]
```

# Solução do desafio:

Para realizar o processamento dos dados, separei cada parte deste processamento em funções. São elas:
- __main__: função principal do sistema, ela é coração do projeto;
- __parse_facts__: Através desta função irei varrer o array facts para processar os dados, gerando uma nova lista;
- __exist_fact_result__: Nesta função irei verificar se o fato que estou lendo já existe dentro da nova lista gerada. Neste caso para deletar o registro ou adicionar o mesmo na nova lista;
- __delete_exist_fact_result__: Deleta o registro da nova lista de resultados, se encontrar (func chamada quando existe um fact=False na lista original)
- __del_fact_in_result__: Deleta um registro da nova lista de resultados;
- __add_fact_in_result__: Adiciona um fato na nova lista de resultados.

Essa foi a melhor solução que encontrei para o desafio.


