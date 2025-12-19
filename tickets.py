"""
SigTicket - Sistema de Gestão de Tickets de Suporte
Versão Legado 0.1 (Contém bugs conhecidos) – Melhorias do Code Review Dia 18

ATENÇÃO: Este é um sistema legado com problemas intencionais para fins educacionais.
"""

from datetime import datetime

# Configurações e constantes do sistema
SENHA_ADMIN = "admin123"
USUARIOS_AUTORIZADOS = ["admin", "suporte"]

# Constantes para validações
MAX_TENTATIVAS_DATA = 3

# Base de dados em memória
tickets = []
contador_id = 1


def validar_data(data: str) -> bool:
    """
    Valida se a string 'data' está no formato DD/MM/AAAA e representa uma data válida,
    não futura e com ano a partir de 2000.
    
    Imprime mensagens de erro específicas e retorna True apenas se válida.
    """
    data = data.strip()
    
    # Verificações básicas de formato
    if len(data) != 10:
        print("✗ Erro: A data deve ter exatamente 10 caracteres (DD/MM/AAAA).")
        return False
    
    if data[2] != '/' or data[5] != '/':
        print("✗ Erro: A data deve usar '/' como separador (ex: 18/12/2025).")
        return False
    
    try:
        dia, mes, ano = map(int, data.split('/'))
    except ValueError:
        print("✗ Erro: Dia, mês e ano devem ser números.")
        return False
    
    # Validação com datetime
    try:
        data_obj = datetime(ano, mes, dia)
    except ValueError:
        print("✗ Erro: Data inválida! Verifique dia/mês (ex: 31/04 não existe).")
        return False
    
    # Rejeita datas futuras
    if data_obj.date() > datetime.now().date():
        print("✗ Erro: Data não pode ser futura.")
        return False
    
    # Rejeita anos muito antigos
    if ano < 2000:
        print("✗ Erro: Ano deve ser 2000 ou posterior.")
        return False
    
    return True


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
    Cria um novo ticket com validação completa de dados, incluindo data.
    Usa loop de tentativas para data inválida.
    """
    global contador_id
    
    print("\n--- CRIAR NOVO TICKET ---")
    titulo = input("Título do problema: ").strip()
    descricao = input("Descrição detalhada: ").strip()
    usuario = input("Usuário solicitante: ").strip()
    
    # Loop de tentativas para entrada de data válida
    for tentativa in range(MAX_TENTATIVAS_DATA):
        print(f"Tentativa {tentativa + 1} de {MAX_TENTATIVAS_DATA}")
        data = input("Data (DD/MM/AAAA): ").strip()
        
        if validar_data(data):
            ticket = {
                "id": contador_id,
                "titulo": titulo,
                "descricao": descricao,
                "usuario": usuario,
                "data": data,
                "status": "aberto"
            }
            tickets.append(ticket)
            contador_id += 1
            print(f"\n✓ Ticket #{ticket['id']} criado com sucesso!")
            return ticket
        
        tentativas_restantes = MAX_TENTATIVAS_DATA - tentativa - 1
        if tentativas_restantes > 0:
            print(f"✗ Data inválida! Tentativas restantes: {tentativas_restantes}")
        # Mensagem final tratada fora do loop
    
    print("\n✗ Número máximo de tentativas excedido. Criação de ticket cancelada.")
    return None


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
    
    if usuario in USUARIOS_AUTORIZADOS and senha == SENHA_ADMIN:
        print(f"\n✓ Bem-vindo, {usuario}!")
        return True
    else:
        print("\n✗ Credenciais inválidas!")
        return False


def main():
    """Função principal que executa o sistema"""
    print("\n🎫 Bem-vindo ao SigTicket!")
    
    if not autenticar():
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
                listar_tickets()
                try:
                    tid = int(input("\nID do ticket: "))
                    novo_status = input("Novo status: ")
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
            "data": "32/13/2025",
            "status": "em analise"
        }
    ])
    contador_id = 3
    print("✓ Dados de teste carregados")


if __name__ == "__main__":
    # Descomente para carregar dados de teste
    # carregar_dados_teste()
    main()
