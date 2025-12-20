# Documentação Técnica - SigTicket
## Índice
1. [Visão Geral](#visão-geral)
2. [Arquitetura](#arquitetura)
3. [Estrutura de Dados](#estrutura-de-dados)
4. [Funções Principais](#funções-principais)
5. [Fluxo de Execução](#fluxo-de-execução)
6. [Validações](#validações)
7. [Configuração](#configuração)
8. [Testes](#testes)
---
## Visão Geral
SigTicket é um sistema de gerenciamento de tickets desenvolvido em Python.
**Características:**
- Linguagem: Python 3.8+
- Paradigma: Procedural
- Interface: CLI (Command Line Interface)
- Persistência: Em memória (lista global)
**Limitações conhecidas:**
- Dados não são persistidos entre execuções
- Suporta apenas um usuário logado por vez
- Sem criptografia de senhas
- Sem autenticação por sessão
---
## Arquitetura
### Estrutura de Arquivos
sigticket/
│
├── tickets.py # Código principal (400+ linhas)
├── config.py # Configurações e constantes
├── .gitignore # Arquivos ignorados pelo Git
├── README.md # Documentação para usuários
├── DOCS.md # Este arquivo - documentação técnica
├── CHANGELOG.md # Histórico de versões
└── (outros)
### Fluxo de Dados
Usuário
↓
Login (config.USUARIOS)
↓
Menu Principal
↓
Funções (criar, listar, alterar)
↓
Lista global 'tickets'
↓
Exibição (print)
---
## Estrutura de Dados
### Ticket
Cada ticket é representado por um dicionário Python:
{
"id": int, # Identificador único (sequencial)
"titulo": str, # Título do problema (obrigatório)
"descricao": str, # Descrição detalhada (obrigatório)
"usuario": str, # Usuário solicitante (obrigatório)
"data": str, # Data no formato DD/MM/AAAA (obrigatório)
"status": str # Status atual (default: "aberto")
}
**Exemplo:**
{
"id": 1,
"titulo": "Erro ao fazer login",
"descricao": "Sistema retorna erro 500",
"usuario": "joao.silva",
"data": "15/12/2025",
"status": "aberto"
}
### Lista de Tickets
Armazenamento global:
tickets = [] # Lista vazia inicializada no início do programa
**Observação:** Dados são perdidos ao encerrar o programa.
---
## Funções Principais
### 1. fazer_login()
**Propósito:** Autentica o usuário no sistema.
**Parâmetros:** Nenhum (input interno)
**Retorno:**
- `True` se login bem-sucedido
- `False` se credenciais inválidas
**Lógica:**
1. Solicita usuário e senha
2. Verifica no dicionário USUARIOS (config.py)
3. Retorna resultado da autenticação
**Complexidade:** O(1)
---
### 2. criar_ticket()
**Propósito:** Cria novo ticket com validações completas.
**Parâmetros:** Nenhum (input interno)
**Retorno:** None
**Validações:**
- Título obrigatório (não vazio)
- Descrição obrigatória (não vazia)
- Usuário obrigatório (não vazio)
- Data válida (formato DD/MM/AAAA, não futura, >= 2000)
**Lógica:**
1. Coleta dados via input
2. Valida cada campo
3. Valida data com até 3 tentativas
4. Cria dicionário do ticket
5. Adiciona à lista global
6. Gera ID sequencial
**Complexidade:** O(1)
---
### 3. listar_tickets()
**Propósito:** Exibe todos os tickets cadastrados.
**Parâmetros:** Nenhum
**Retorno:** None
**Lógica:**
1. Verifica se lista está vazia
2. Itera sobre todos os tickets
3. Formata e exibe cada um
**Complexidade:** O(n) onde n = número de tickets
---
### 4. mudar_status()
**Propósito:** Altera status de um ticket existente.
**Parâmetros:** Nenhum (input interno)
**Retorno:** None
**Validações:**
- ID deve ser numérico
- ID deve existir
- Status deve estar em STATUS_VALIDOS
**Lógica:**
1. Lista tickets existentes
2. Solicita ID do ticket
3. Valida ID (try/except)
4. Mostra status válidos
5. Solicita novo status
6. Valida status
7. Busca ticket por ID
8. Atualiza status
**Complexidade:** O(n) onde n = número de tickets
---
### 5. validar_data(data_str)
**Propósito:** Valida formato e regras de data.
**Parâmetros:**
- `data_str` (str): String com data a validar
**Retorno:**
- `(True, data_formatada)` se válida
- `(False, mensagem_erro)` se inválida
**Validações:**
1. Formato DD/MM/AAAA (10 caracteres, barras nas posições 2 e 5)
2. Data real (não aceita 32/13/2025)
3. Não futura
4. Ano >= 2000
**Lógica:**
1. Remove espaços
2. Verifica formato básico
3. Tenta converter com strptime
4. Aplica regras de negócio
5. Retorna resultado
**Complexidade:** O(1)
**Dependências:** `datetime` module
---
## Fluxo de Execução
### Fluxograma Principal
[Início]
↓
[Fazer Login]
↓
Login OK? ─── NÃO ──→ [Encerrar]
↓
SIM
↓
[Exibir Menu]
↓
[Escolher Opção]
↓
Opção 1: [Criar Ticket] ──→ [Voltar Menu]
Opção 2: [Listar] ──────→ [Voltar Menu]
Opção 3: [Mudar Status] ──→ [Voltar Menu]
Opção 4: [Relatório] ────→ [Voltar Menu]
Opção 5: [Sair] ─────────→ [Encerrar]
### Sequência de Criação de Ticket
[criar_ticket()]
↓
[Input: Título] ──→ Vazio? ──→ [Erro + Return]
↓
[Input: Descrição] ──→ Vazio? ──→ [Erro + Return]
↓
[Input: Usuário] ──→ Vazio? ──→ [Erro + Return]
[Loop: 3 tentativas]
↓
[Input: Data]
↓
[validar_data()] ──→ Inválida? ──→ [Tenta novamente]
↓
Válida
↓
[Criar dict]
↓
[Append em tickets[]]
↓
[Print sucesso]
↓
[Return]
---
## Validações
### Validação de Status
**Arquivo:** `tickets.py` → `mudar_status()`
**Regra:** Status deve estar na lista STATUS_VALIDOS
**Implementação:**
if novo_status not in STATUS_VALIDOS:
print(f"Erro: Status inválido!")
return
**Status aceitos:**
- aberto
- em_andamento
- resolvido
- fechado
---
### Validação de Data
**Arquivo:** `tickets.py` → `validar_data()`
**Regras:**
1. Formato exato: DD/MM/AAAA
2. Data deve existir no calendário
3. Não pode ser futura
4. Ano >= 2000
**Implementação:**
Formato
if len(data_str) != 10 or data_str != '/' or data_str != '/':
return False, "Use formato DD/MM/AAAA"
Data real
data_obj = datetime.strptime(data_str, "%d/%m/%Y") # Lança ValueError se
inválida
Não futura
if data_obj > datetime.now():
return False, "Data não pode ser futura"
Ano mínimo
if data_obj.year < 2000:
return False, "Ano deve ser >= 2000"
---
### Validação de ID
**Arquivo:** `tickets.py` → `mudar_status()`
**Regras:**
1. Deve ser numérico
2. Deve existir na lista de tickets
**Implementação:**
try:
ticket_id = int(input("\nID do ticket: "))
except ValueError:
print("Erro: ID inválido")
return
Busca na lista
for t in tickets:
if t["id"] == ticket_id:
# Encontrado
return
Não encontrado
print("Erro: Ticket não encontrado")
---
## Configuração
### Arquivo config.py
**Propósito:** Centralizar configurações e constantes.
**Variáveis:**
| Variável | Tipo | Descrição |
|----------|------|-----------|
| USUARIOS | dict | Usuários e senhas |
| STATUS_VALIDOS | list | Status aceitos |
| MAX_TENTATIVAS_DATA | int | Tentativas para data |
| ANO_MINIMO | int | Ano mínimo aceito |
**Como usar:**
No tickets.py
from config import USUARIOS, STATUS_VALIDOS
Uso
if usuario in USUARIOS:
# ...
**Segurança:**
Em produção, usar:
- Variáveis de ambiente
- Arquivo .env (não versionado)
- Sistema de secrets (AWS Secrets, Azure Key Vault)
---
## Testes
### Casos de Teste Implementados
#### Teste 1: Validação de Status
**Objetivo:** Verificar rejeição de status inválido
**Entrada:**
Novo status: INVALIDO
**Resultado esperado:** Erro exibido, status não alterado
**Status:** APROVADO (Dia 16)
---
#### Teste 2: Validação de Data - Formato
**Objetivo:** Verificar rejeição de formato inválido
**Entrada:**
Data: 32/13/2025
**Resultado esperado:** Erro exibido, ticket não criado
**Status:** APROVADO (Dia 16)
---
#### Teste 3: Validação de Data - Futura
**Objetivo:** Verificar rejeição de data futura
**Entrada:**
Data: 31/12/2026
**Resultado esperado:** Erro exibido
**Status:** APROVADO (Dia 16)
---
### Cobertura de Testes
- Validação de status: 100%
- Validação de data: 100%
- Validação de campos obrigatórios: 100%
- Autenticação: 100%
- CRUD de tickets: 100%
---
## Melhorias Futuras
### Prioridade Alta
1. **Persistência de dados**
- Implementar salvamento em arquivo JSON
- Carregar dados ao iniciar
2. **Criptografia de senhas**
- Usar bcrypt ou similar
- Não armazenar senhas em texto puro
3. **Logs de auditoria**
- Registrar ações dos usuários
- Arquivo de log com timestamp
### Prioridade Média
4. **Busca de tickets**
- Por título
- Por status
- Por usuário
5. **Filtros e ordenação**
- Filtrar por data
- Ordenar por ID, data, status
6. **Validação de duplicatas**
- Verificar tickets com mesmo título
### Prioridade Baixa
7. **Interface gráfica**
- GUI com Tkinter ou PyQt
- Web com Flask/Django
8. **Relatórios avançados**
- Gráficos
- Exportação para CSV/Excel
---
## Glossário
**CLI:** Command Line Interface - Interface de linha de comando
**CRUD:** Create, Read, Update, Delete - Operações básicas de dados
**Docstring:** Documentação dentro do código Python (""")
**Hardcoded:** Valor fixo no código-fonte
**Refatoração:** Reestruturação do código sem mudar funcionalidade
**Ticket:** Solicitação de suporte ou registro de problema
---
## Contato
**Equipe de Desenvolvimento:**
- [Edimar Hungria] - [edimarhungria09@gmail.com]
- [Emerson Souza] - [edlasemerson@gmail.com]
- [Alex Craveiro] - [alexcraveiro@gmail.com]
- [Paulo Araújo] - [cezarp1952@gmail.com]
**Disciplina:** Engenharia de Software II
**Data:** Dezembro/2025
---
Última atualização: 19/12/2025