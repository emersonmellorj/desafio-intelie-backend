""" Vou apresentar a melhor solução possível"""

import pprint

def main(register, schema):
    """Função principal do sistema"""
    # Transformar o schema em dicionário
    new_schema = dict()
    for line in schema:
        new_schema[line[0]] = line[2]
    print(f'\nNew Schema: {new_schema}\n')

    # Ordenando a lista pela chave 'entidade'
    new_facts = sorted(facts, key=lambda fact: fact[0])
    print(new_facts)
    print()

    facts_result = []
    parse_facts(new_schema, new_facts, facts_result)
    print(f'Lista final:\n')
    pp = pprint.PrettyPrinter(indent=1)
    pp.pprint(facts_result)
    print(f'\nTamanho da lista final: {len(facts_result)}\n')


def parse_facts(new_schema, new_facts, facts_result):
    """Irei varrear a lista ordenada e gerar a saída para uma nova lista"""
    for i in range(len(new_facts)):
        fact = facts[i]
        print(f'i={i} - fact={fact}')
        chave = fact[0]
        propriedade = fact[1]
        valor = fact[2]
        ativo = fact[3]

        if new_schema[fact[1]] == 'many':
            print('Sou de cardinalidade many')
            if not ativo:
                print(f'Sou um fato com False - {fact}')
                delete_exist_fact_result(chave, propriedade, valor, facts_result)
            else: 
                add_fact_in_result(fact, facts_result)
            print()  
        else:
            print('Sou de cardinalidade one')
            exist_fact_result(chave, propriedade, fact, facts_result)


def exist_fact_result(chave, propriedade, fact, facts_result):
    """Verifica se o fato ja existe na nova lista de fatos e insere o mesmo ou deleta da nova lista"""
    if not facts_result == []:
        for j in range(len(facts_result)):
            line = facts_result[j]
            if line[0] == chave and line[1] == propriedade:
                print(f'Ja existe um valor com {chave} - {propriedade} em facts_result!')
                del_fact_in_result(j, line, facts_result)
                add_fact_in_result(fact, facts_result)
                return
            j+=1
        print(f'Não existe um valor com {chave} - {propriedade} em facts_result.') 
    add_fact_in_result(fact, facts_result)


def delete_exist_fact_result(chave, propriedade, valor, facts_result):
    """
    Deleta o registro da nova lista de resultados, 
    se encontrar (func chamada quando existe um fact=False na lista original)
    """
    for y in range(len(facts_result)):
        line = facts_result[y]
        if line[0] == chave and line[2] == valor:
            del_fact_in_result(y, line, facts_result)
            return
        y+=1


def del_fact_in_result(index, line, facts_result):
    """Deleta um registro da nova lista de resultados"""
    print(f'Deletando {line} in facts_result com indice {index}.')
    del facts_result[index]

def add_fact_in_result(fact, facts_result):
    """Adiciona um fact na nova lista de resultados"""
    print(f'Inserindo {fact} in facts_result\n')
    facts_result.append(fact)


"""Start of program"""
if __name__ == '__main__':

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

    schema = [
        ('endereço', 'cardinality', 'one'),
        ('telefone', 'cardinality', 'many')
    ]

    # Chamando a função principal do sistema
    main(facts, schema)