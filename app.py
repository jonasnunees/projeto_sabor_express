# Importa o módulo 'os', que dá acesso a funções do sistema operacional
import os

# lista com os nomes dos restaurantes cadastrados
restaurantes = [{'nome':'Menino do Açai', 'categoria':'Hamburgueria', 'ativo':True},
                {'nome':'Don Leal', 'categoria':'Pizzaria', 'ativo':False},
                {'nome':'Xodó da Praia', 'categoria':'Quiosque', 'ativo':False}]

def exibir_cabecalho():
    print("""
░██████╗░█████╗░██████╗░░█████╗░██████╗░  ███████╗██╗░░██╗██████╗░██████╗░███████╗░██████╗░██████╗
██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
╚█████╗░███████║██████╦╝██║░░██║██████╔╝  █████╗░░░╚███╔╝░██████╔╝██████╔╝█████╗░░╚█████╗░╚█████╗░
░╚═══██╗██╔══██║██╔══██╗██║░░██║██╔══██╗  ██╔══╝░░░██╔██╗░██╔═══╝░██╔══██╗██╔══╝░░░╚═══██╗░╚═══██╗
██████╔╝██║░░██║██████╦╝╚█████╔╝██║░░██║  ███████╗██╔╝╚██╗██║░░░░░██║░░██║███████╗██████╔╝██████╔╝
╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝  ╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░  
    """)

def exibir_menu():
    
    print('1. Cadastrar restaurante')
    print('2. Listar restaurante')
    print('3. Ativar restaurante')
    print('4. Desativar restaurante')
    print('5. Sair\n')

def cadastrar_restaurante():

    """Função para cadastrar um novo restaurante na lista de restaurantes.

    Inputs:
    - nome_do_restaurante: str
    - categoria_do_restaurante: str

    Outputs:
    - None
    """

    # mostra um subtítulo na tela para indicar que o usuário está na tela de cadastro
    exibir_subtitulo('Cadastro de novos restaurantes')

    # pede ao usuário que digite o nome do restaurante e converte a entrada para string
    nome_do_restaurante = str(input('Digite o nome do restaurante que deseja cadastrar: '))

    # pede ao usuário que digite a categoria do restaurante e usa o nome informado na mensagem
    categoria_do_restaurante = str(input(f'Digite a categoria do restaurante {nome_do_restaurante}: '))

    # cria um dicionário com as informações do restaurante:
    # - 'nome' recebe o nome informado
    # - 'categoria' recebe a categoria informada
    # - 'ativo' inicia como False indicando que o restaurante está inativo por padrão
    dados_do_restaurante = {'nome': nome_do_restaurante, 'categoria': categoria_do_restaurante, 'ativo': False}

    # adiciona esse dicionário à lista global 'restaurantes' para armazenar o novo cadastro
    restaurantes.append(dados_do_restaurante)

    # informa ao usuário que o restaurante foi cadastrado com sucesso
    print(f'\nO restaurante {nome_do_restaurante} foi cadastrado com sucesso!')

    # espera o usuário pressionar uma tecla e então retorna ao menu principal chamando a função apropriada
    voltar_ao_menu_principal()

def listar_restaurante():
    
    # Exibe um subtítulo na tela para indicar ao usuário que está na lista de restaurantes.
    exibir_subtitulo('Lista de restaurantes:')

    # Imprime o cabeçalho da "tabela" com colunas alinhadas.
    # 'ljust' ajusta (preenche) a string à esquerda para garantir alinhamento das colunas.
    print(f'{"Nome do restaurante".ljust(22)} | {"Categoria".ljust(20)} | Status')

    # Percorre cada item (cada restaurante) presente na lista 'restaurantes'.
    for restaurante in restaurantes:

        # Pega o valor da chave 'nome' do dicionário do restaurante atual.
        nome_do_restaurante = restaurante['nome']

        # Pega o valor da chave 'categoria' do dicionário do restaurante atual.
        categoria_do_restaurante = restaurante['categoria']

        # Verifica se o restaurante está ativo (True) ou não (False) e
        # atribui a string apropriada para mostrar ao usuário.
        status_do_restaurante = 'Ativo' if restaurante['ativo'] else 'Inativo'

        # Imprime uma linha com os dados do restaurante formatados e alinhados.
        # O '- ' no começo é só para estilo; depois usamos 'ljust' para manter colunas retas.
        print(f'- {nome_do_restaurante.ljust(20)} | {categoria_do_restaurante.ljust(20)} | Status: {status_do_restaurante}')
    
    # Após listar todos os restaurantes, chama a função que espera o usuário
    # e retorna ao menu principal.
    voltar_ao_menu_principal()

def ativar_restaurante():

    # Chama a função que limpa a tela e exibe um subtítulo informando a ação atual
    exibir_subtitulo('Ativar restaurante')

    # Mostra um cabeçalho simples para listar os restaurantes inativos
    print('Restaurantes inativos:')

    # Percorre cada restaurante na lista 'restaurantes'
    for restaurante in restaurantes:

        # Verifica se o restaurante está inativo (False)
        if not restaurante['ativo']:

            # Exibe o nome do restaurante inativo, com um traço para formatar a lista
            print(f'- {restaurante["nome"]}')

    # Pede ao usuário que digite o nome do restaurante que deseja ativar
    nome_do_restaurante = str(input('\nDigite o nome do restaurante que deseja ativar: '))

    # Percorre novamente a lista de restaurantes para encontrar o que o usuário informou
    for restaurante in restaurantes:

        # Compara o nome armazenado com o nome digitado pelo usuário
        if restaurante['nome'] == nome_do_restaurante:

            # Se encontrar, altera o campo 'ativo' para True (ativa o restaurante)
            restaurante['ativo'] = True

            # Informa ao usuário que a ativação foi bem-sucedida
            print(f'O restaurante {nome_do_restaurante} foi ativado com sucesso!')

            # Sai do laço porque já encontrámos e atualizamos o restaurante
            break
    else:
        # Este bloco é executado se o laço terminar sem encontrar (sem executar 'break')
        # Informa ao usuário que o restaurante não foi encontrado
        print(f'O restaurante {nome_do_restaurante} não foi encontrado.')

    # Chama a função que espera o usuário e retorna ao menu principal
    voltar_ao_menu_principal()

def desativar_restaurante():

    # Limpa a tela e exibe um subtítulo informando a ação atual.
    exibir_subtitulo('Desativar restaurante')

    # Mostra um cabeçalho simples que indica quais restaurantes estão ativos.
    print('Restaurantes ativos:')

    # Percorre todos os restaurantes cadastrados na lista 'restaurantes'.
    for restaurante in restaurantes:

        # Verifica se o restaurante atual está ativo (True).
        if restaurante['ativo']:

            # Se estiver ativo, exibe o nome para que o usuário veja as opções.
            print(f'- {restaurante["nome"]}')

    # Pede ao usuário para digitar o nome do restaurante que deseja desativar.
    nome_do_restaurante = str(input('\nDigite o nome do restaurante que deseja desativar: '))

    # Percorre novamente a lista para encontrar o restaurante informado pelo usuário.
    for restaurante in restaurantes:

        # Compara o nome do restaurante atual com o nome digitado pelo usuário.
        if restaurante['nome'] == nome_do_restaurante:

            # Se encontrar, define o campo 'ativo' como False, desativando o restaurante.
            restaurante['ativo'] = False

            # Informa ao usuário que a desativação foi concluída com sucesso.
            print(f'O restaurante {nome_do_restaurante} foi desativado com sucesso!')
            
            # Interrompe o laço porque já localizamos e atualizamos o restaurante.
            break
    else:
        # Este bloco é executado se nenhum restaurante com o nome informado for encontrado.
        print(f'O restaurante {nome_do_restaurante} não foi encontrado.')

    # Chama a função que espera o usuário pressionar uma tecla e então volta ao menu principal.
    voltar_ao_menu_principal()

def finalizar_app():
    exibir_subtitulo('Encerrando o programa...')

def opcao_invalida():
    print('\nOpção inválida!\n')
    voltar_ao_menu_principal()

def voltar_ao_menu_principal():
    input('\nDigite uma tecla para voltar ao menu principal: ')
    main()

def exibir_subtitulo(texto):
    os.system('cls')
    linha = '*' * (len(texto))
    print(linha)
    print(texto)
    print(linha)
    print()

def escolher_opcao():
    try:
        opcao_escolhida = int(input('Escolha uma opção: '))

        # Usa a instrução 'match' (Python 3.10+) para comparar o valor de 'opcao_escolhida'
        match opcao_escolhida: 
            case 1: 
                cadastrar_restaurante()
            case 2: 
                listar_restaurante()
            case 3: 
                ativar_restaurante()
            case 4: 
                desativar_restaurante()
            case 5:
                finalizar_app()
            # '_' é o curinga: cai aqui quando nenhum dos casos acima foi correspondido
            case _: 
                opcao_invalida()
    except:
        opcao_invalida()


# Função principal do programa
# A ideia é centralizar aqui a sequência de passos que o app executa qunado é iniciado
def main():
    os.system('cls')
    exibir_cabecalho()
    exibir_menu()
    escolher_opcao()

# Executa main() somente quando este arquivo é rodado diretamente.
# Se for importado como módulo, main() não é chamada automaticamente.
if __name__ == '__main__':
    main()