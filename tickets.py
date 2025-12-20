#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
SigTicket - Sistema de Gerenciamento de Tickets
Versão: 1.0.0
Data: Dezembro/2025
Descrição:
Sistema simples para gerenciamento de tickets de suporte.
Permite criar, listar, buscar e alterar status de tickets com validações completas.
Autores:
Ed Hungria
Emerson
Paulo
Alex
Disciplina: Engenharia de Software II
"""

from datetime import datetime
from config import USUARIOS, STATUS_VALIDOS, MAX_TENTATIVAS_DATA

# Base de dados em memória (não persistida entre execuções)
tickets = []
# Contador global para IDs sequenciais (inicia em 1)
contador_id = 1


def menu_principal():
    """
    Exibe o menu principal do sistema com as opções disponíveis.
    """
    print("\n" + "="*50)
    print("       SIGTICKET - Sistema de Tickets")
    print("="*50)
    print("1. Criar novo ticket")
    print("2. Listar todos os tickets")
    print("3. Mudar status de um ticket")
    print("4. Buscar ticket por ID")
    print("5. Sair")
    print("="*50)


def validar_data(data_str):
    """
    Valida se uma string representa uma data válida no formato DD/MM/AAAA.

    Args:
        data_str (str): String contendo a data a ser validada

    Returns:
        tuple: (bool, str) onde:
            - bool: True se válida, False se inválida
            - str: Data formatada se válida, mensagem de erro se inválida

    Examples:
        >>> validar_data("15/12/2025")
        (True, "15/12/2025")
        >>> validar_data("32/13/2025")
        (False, "Data inválida")
    """
    # Remove espaços extras
    data_str = data_str.strip()

    # Verifica formato básico (10 caracteres com barras nas posições corretas)
    if len(data_str) != 10 or data_str[2] != '/' or data_str[5] != '/':
        return False, "Use formato DD/MM/AAAA"

    try:
        # Converte string para objeto datetime
        data_obj = datetime.strptime(data_str, "%d/%m/%Y")

        # Regra de negócio: não aceita datas futuras
        if data_obj > datetime.now():
            return False, "Data não pode ser futura"

        # Regra de negócio: não aceita datas antes de 2000
        if data_obj.year < 2000:
            return False, "Ano deve ser >= 2000"

        # Data válida
        return True, data_str
    except ValueError:
        # Erro ao converter (ex: 32/13/2025 ou mês inválido)
        return False, "Data inválida"


def criar_ticket():
    """
    Cria um novo ticket no sistema com validação completa dos dados.

    Validações realizadas:
    - Título não pode estar vazio
    - Descrição não pode estar vazia
    - Usuário não pode estar vazio
    - Data deve ser válida no formato DD/MM/AAAA
    - Data não pode ser futura
    - Data não pode ser antes de 2000

    O usuário tem MAX_TENTATIVAS_DATA tentativas para informar uma data válida.

    Returns:
        None: Modifica a lista global 'tickets'
    """
    print("\n=== CRIAR TICKET ===")

    # Coleta e valida título
    titulo = input("Título: ").strip()
    if not titulo:
        print("✗ Título obrigatório")
        return

    # Coleta e valida descrição
    descricao = input("Descrição: ").strip()
    if not descricao:
        print("✗ Descrição obrigatória")
        return

    # Coleta e valida usuário solicitante
    usuario = input("Usuário: ").strip()
    if not usuario:
        print("✗ Usuário obrigatório")
        return

    # Validação de data com múltiplas tentativas
    for tentativa in range(MAX_TENTATIVAS_DATA):
        data = input("Data (DD/MM/AAAA): ").strip()
        valida, msg = validar_data(data)
        if valida:
            data = msg  # msg contém a data quando válida
            break
        else:
            print(f"✗ {msg}")
        if tentativa < MAX_TENTATIVAS_DATA - 1:
            print(f" Tentativas restantes: {MAX_TENTATIVAS_DATA - tentativa - 1}")
    else:
        print("✗ Máximo de tentativas. Operação cancelada.")
        return

    # Cria o dicionário do ticket com ID sequencial
    novo_ticket = {
        "id": len(tickets) + 1,
        "titulo": titulo,
        "descricao": descricao,
        "usuario": usuario,
        "data": data,
        "status": "aberto"  # Todo ticket inicia como aberto
    }

    # Adiciona à base em memória
    tickets.append(novo_ticket)

    # Feedback ao usuário
    print(f"✓ Ticket #{novo_ticket['id']} criado com sucesso!")


def listar_tickets():
    """
    Lista todos os tickets cadastrados em formato tabular.

    Se não houver tickets, exibe mensagem informativa.
    """
    if not tickets:
        print("\nNenhum ticket cadastrado ainda.")
        return

    print("\n" + "="*80)
    print(f"{'ID':<5} {'Título':<30} {'Status':<15} {'Data':<12}")
    print("="*80)

    for t in tickets:
        print(f"{t['id']:<5} {t['titulo']:<30} {t['status']:<15} {t['data']:<12}")

    print("="*80)
    print(f"Total: {len(tickets)} ticket(s)")


def mudar_status():
    """
    Altera o status de um ticket existente com validação completa.

    Validações:
    - ID deve ser numérico e existir
    - Status deve estar na lista STATUS_VALIDOS (config.py)
    """
    listar_tickets()

    try:
        ticket_id = int(input("\nID do ticket: "))
    except ValueError:
        print("✗ ID inválido")
        return

    # Exibe status válidos para auxiliar o usuário
    print("\nStatus válidos:")
    for s in STATUS_VALIDOS:
        print(f" - {s}")

    novo_status = input("\nNovo status: ").strip().lower()

    if novo_status not in STATUS_VALIDOS:
        print(f"✗ Status inválido! Use: {', '.join(STATUS_VALIDOS)}")
        return

    # Busca e atualiza o ticket
    for t in tickets:
        if t["id"] == ticket_id:
            t["status"] = novo_status
            print(f"✓ Status alterado para: {novo_status}")
            return

    print("✗ Ticket não encontrado")


def buscar_ticket(ticket_id):
    """
    Busca e exibe detalhes completos de um ticket específico pelo ID.

    Args:
        ticket_id (int): ID do ticket a ser buscado
    """
    for t in tickets:
        if t["id"] == ticket_id:
            print("\n" + "="*50)
            print(f"TICKET #{t['id']}")
            print("="*50)
            print(f"Título:      {t['titulo']}")
            print(f"Descrição:   {t['descricao']}")
            print(f"Usuário:     {t['usuario']}")
            print(f"Data:        {t['data']}")
            print(f"Status:      {t['status']}")
            print("="*50)
            return t

    print(f"\n✗ Ticket #{ticket_id} não encontrado.")
    return None


def fazer_login():
    """
    Realiza autenticação do usuário usando credenciais centralizadas em config.py.

    Returns:
        bool: True se autenticação bem-sucedida, False caso contrário
    """
    print("\n=== LOGIN ===")
    usuario = input("Usuário: ").strip()
    senha = input("Senha: ").strip()

    if usuario in USUARIOS and USUARIOS.get(usuario) == senha:
        print(f"✓ Login realizado: {usuario}")
        return True
    else:
        print("✗ Usuário ou senha inválidos")
        return False


def main():
    """
    Função principal que controla o fluxo completo do sistema.
    """
    print("\n🎫 Bem-vindo ao SigTicket!")

    if not fazer_login():
        print("Acesso negado. Encerrando...")
        return

    while True:
        menu_principal()

        try:
            opcao = input("\nEscolha uma opção: ")

            if opcao == "1":
                criar_ticket()
            elif opcao == "2":
                listar_tickets()
            elif opcao == "3":
                mudar_status()
            elif opcao == "4":
                try:
                    tid = int(input("\nID do ticket para buscar: "))
                    buscar_ticket(tid)
                except ValueError:
                    print("\n✗ ID inválido!")
            elif opcao == "5":
                print("\nEncerrando sistema... Até logo!")
                break
            else:
                print("\n✗ Opção inválida!")

        except KeyboardInterrupt:
            print("\n\nSistema interrompido pelo usuário.")
            break
        except Exception as e:
            print(f"\n✗ Erro inesperado: {e}")


def carregar_dados_teste():
    """
    Carrega tickets de exemplo com problemas intencionais para demonstração de bugs.
    """
    global contador_id
    tickets.extend([
        {
            "id": 1,
            "titulo": "Impressora não funciona",
            "descricao": "A impressora do 3º andar está offline",
            "usuario": "joao.silva",
            "data": "01/12/2025",
            "status": "aberto"
        },
        {
            "id": 2,
            "titulo": "Senha esquecida",
            "descricao": "Usuário não consegue acessar o sistema",
            "usuario": "maria.santos",
            "data": "32/13/2025",  # Data inválida intencional
            "status": "em analise"  # Status não padronizado
        },
        {
            "id": 3,
            "titulo": "Computador lento",
            "descricao": "Máquina travando constantemente",
            "usuario": "pedro.costa",
            "data": "abc/def/ghij",  # Formato inválido
            "status": "xpto"  # Status absurdo
        }
    ])
    contador_id = 4
    print("✓ Dados de teste carregados (3 tickets com problemas)")


if __name__ == "__main__":
    # Descomente para carregar dados de teste automaticamente
    # carregar_dados_teste()
    main()