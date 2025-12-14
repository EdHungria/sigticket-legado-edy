"""
SigTicket - Sistema de Gestão de Tickets de Suporte
Versão Legado 0.1 (Contém bugs conhecidos)

ATENÇÃO: Este é um sistema legado com problemas intencionais para fins educacionais.
"""

# Configurações (PROBLEMA: Senha hardcoded!)
SENHA_ADMIN = "admin123"
usuarios_autorizados = ["admin", "suporte"]

# Base de dados em memória
tickets = []
contador_id = 1


def menu_principal():
    """Exibe o menu principal do sistema"""
    print("\n" + "="*50)
    print("       SIGTICKET - Sistema de Tickets")
    print("="*50)
    print("1. Criar novo ticket")
    print("2. Listar todos os tickets")
    print("3. Mudar status de um ticket")
    print("4. Buscar ticket por ID")
    print("5. Sair")
    print("="*50)


def criar_ticket():
    """
    Cria um novo ticket no sistema
    BUG #2: Não valida o formato da data
    """
    global contador_id
    
    print("\n--- CRIAR NOVO TICKET ---")
    titulo = input("Título do problema: ")
    descricao = input("Descrição detalhada: ")
    usuario = input("Usuário solicitante: ")
    data = input("Data (DD/MM/AAAA): ")  # BUG #2: Aceita qualquer coisa!
    
    # Cria o ticket sem validações adequadas
    ticket = {
        "id": contador_id,
        "titulo": titulo,
        "descricao": descricao,
        "usuario": usuario,
        "data": data,
        "status": "aberto"  # Sempre inicia como aberto
    }
    
    tickets.append(ticket)
    contador_id += 1
    
    print(f"\n✓ Ticket #{ticket['id']} criado com sucesso!")
    return ticket


def listar_tickets():
    """Lista todos os tickets cadastrados"""
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


def mudar_status(ticket_id, novo_status):
    """
    Altera o status de um ticket
    BUG #1: Aceita qualquer string como status (sem validação!)
    """
    for t in tickets:
        if t["id"] == ticket_id:
            # BUG #1: Não valida se o status é válido!
            # Aceita "xpto", "qualquercoisa", etc.
            t["status"] = novo_status
            print(f"\n✓ Status do ticket #{ticket_id} alterado para: {novo_status}")
            return True
    
    print(f"\n✗ Ticket #{ticket_id} não encontrado.")
    return False


def buscar_ticket(ticket_id):
    """Busca e exibe detalhes de um ticket específico"""
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


def autenticar():
    """
    Sistema básico de autenticação
    PROBLEMA: Senha está hardcoded no início do arquivo!
    """
    print("\n--- AUTENTICAÇÃO ---")
    usuario = input("Usuário: ")
    senha = input("Senha: ")
    
    if usuario in usuarios_autorizados and senha == SENHA_ADMIN:
        print(f"\n✓ Bem-vindo, {usuario}!")
        return True
    else:
        print("\n✗ Credenciais inválidas!")
        return False


# Função principal
def main():
    """Função principal que executa o sistema"""
    print("\n🎫 Bem-vindo ao SigTicket!")
    
    # Autenticação simples
    if not autenticar():
        print("Acesso negado. Encerrando...")
        return
    
    # Loop principal do menu
    while True:
        menu_principal()
        
        try:
            opcao = input("\nEscolha uma opção: ")
            
            if opcao == "1":
                criar_ticket()
            
            elif opcao == "2":
                listar_tickets()
            
            elif opcao == "3":
                listar_tickets()
                try:
                    tid = int(input("\nID do ticket: "))
                    novo_status = input("Novo status: ")  # BUG #1: Sem validação!
                    mudar_status(tid, novo_status)
                except ValueError:
                    print("\n✗ ID inválido!")
            
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


# Dados de exemplo para teste (opcional - descomentar para usar)
def carregar_dados_teste():
    """Carrega alguns tickets de exemplo"""
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
            "data": "32/13/2025",  # BUG #2: Data inválida!
            "status": "em analise"  # BUG #1: Status não padronizado!
        },
        {
            "id": 3,
            "titulo": "Computador lento",
            "descricao": "Máquina travando constantemente",
            "usuario": "pedro.costa",
            "data": "abc/def/ghij",  # BUG #2: Data completamente inválida!
            "status": "xpto"  # BUG #1: Status absurdo aceito!
        }
    ])
    
    contador_id = 4
    print("✓ Dados de teste carregados (3 tickets com problemas)")


if __name__ == "__main__":
    # Descomente a linha abaixo para carregar dados de teste
    carregar_dados_teste()
    
    main()
