from datetime import date
import json
from collections import Counter
import os

def como_esta_se_sentido(): #função que coleta os dados do usuario
    sentimento = input('Como você tem se sentido hoje? ')
    while True:
        try:
            nota = float(input('De 0 a 5, como você está se sentindo hoje? '))
        except ValueError:
            print('O valor digitado precisa ser um valor numérico entre o e 5!')
            continue
        if nota > 5 or nota < 0:
            print('O valor precisa ser um valor numérico de 0 a 5!')
        else: 
            break
    
    musica_do_dia = input('Digite sua música mais ouvida hoje: ')
    artista_do_dia = input(f'Qual o artista de "{musica_do_dia}"? ')
    dicionario_humor = {
        'Data' : str(date.today()) ,
        'Sentimento' : sentimento ,
        'Humor' : nota , 
        'Musica' : musica_do_dia ,
        'Artista' : artista_do_dia}
    
    return dicionario_humor

def carregar_arquivo_json():
    try:
        with open('dicionario_humor.json', 'r') as arquivo:
            lista = json.load(arquivo)
            return lista
    except FileNotFoundError:
        return []

def salvar_registros(lista):    #salva os registros em json
    with open('dicionario_humor.json', 'w')as arquivo:
        json.dump(lista, arquivo)


def registrar_dia():        #registra o dia ja no dicionario json
    carregar = carregar_arquivo_json()
    dicionario = como_esta_se_sentido()
    carregar.append(dicionario)
    salvar_registros(carregar)
    print('\n')
    

def listar_historico():     #mostra todo o historico de registros
    for i in carregar_arquivo_json():
        print(f'📅 Data:{i['Data']}\n💭 Como estava:{i['Sentimento']}\n⭐ Nota:{i['Humor']}\n🎵 Música do dia:{i['Musica']} - {i['Artista']}\n─────────────────\n')


def relatorio_mes(): #faz um relatorio filtrando as informações
    print('\n')
    lista = carregar_arquivo_json()
    print(f'Total de dias registrados: {len(lista)} dias!')
    humor_soma = 0
    humor_quantidade = 0
    for i in lista:
        humor_soma += i['Humor']
        humor_quantidade += 1
    if humor_quantidade > 0:
        print(f'A sua média de humor é: {humor_soma / humor_quantidade:.2f}!')
    else:
        print('Nenhum registro ainda!')
    musicas = []
    for i in lista:
        musicas.append(i['Musica'])
    contagem = Counter(musicas)
    for musica, quantidade in contagem.most_common(5):
        print(f'A música {musica} foi ouvida {quantidade} vezes!')
    if len(lista) > 0:
        maior_humor = max(lista, key=lambda i: i['Humor'])
        print(f'📅 Seu melhor dia foi: {maior_humor['Data']}\n🎵 Música: {maior_humor['Musica']} - {maior_humor['Artista']}\n⭐ Nota: {maior_humor['Humor']}\n💭 Sentimento: {maior_humor['Sentimento']}')
    else:
        print('Sem registros ainda!')
    print('\n \n')


def menu():  #menu de escolha das opções
    while True:
        try:
            print('''
Qual opção você deseja?
1. Registrar o dia de hoje
2. Ver histórico
3. Ver relatório do mês
4. Sair
                  ''')
            opcao = int(input('Digite a opção que você deseja: '))
            match opcao:
                case 1:
                    print('\nVocê escolheu Registrar o dia de hoje!')
                    registrar_dia()
                case 2:
                    print('\nvocê escolheu Ver histórico!')
                    listar_historico()
                case 3:
                    print('\nVocê escolheu Ver relatório do mês!')
                    relatorio_mes()
                case 4:
                    print('\nApp finalizado')
                    break
                case _:
                    print('\nOpção inválida!')
                    continue
        except ValueError:
            print('\nErro! Opção inválida!')
            continue
        


if __name__ == '__main__':
    menu()