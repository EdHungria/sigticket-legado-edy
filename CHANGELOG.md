# Changelog
Todas as mudanças notáveis do projeto SigTicket serão documentadas aqui.
O formato é baseado em [Keep a Changelog](https://keepachangelog.com/pt-
BR/1.0.0/).
---
## [1.0.0] - 2025-12-20
### Adicionado
- Sistema completo de gerenciamento de tickets
- Autenticação de usuários
- Criação de tickets com validação
- Listagem de todos os tickets
- Alteração de status com validação
- Sistema de relatórios
---
## [0.3.0] - 2025-12-18
### Adicionado
- Arquivo CHANGELOG.md para documentar mudanças
### Melhorado
- Mensagens de erro mais descritivas (code review)
- Constantes movidas para topo do arquivo
- Comentários adicionais no código
- Refatoração baseada em sugestões do code review
---
## [0.2.0] - 2025-12-17
### Adicionado
- Arquivo .gitignore para ignorar arquivos temporários
- Arquivo config.py para configurações centralizadas
- README.md com documentação completa do projeto
### Mudado
- Credenciais movidas de hardcoded para arquivo de configuração
- Suporte para múltiplos usuários (admin e suporte)
### Segurança
- Remoção de senhas hardcoded do código principal
---
## [0.1.1] - 2025-12-16
### Corrigido
- Bug #2: Validação de data na criação de tickets
- Formato DD/MM/AAAA obrigatório
- Rejeita datas futuras
- Rejeita datas inválidas (ex: 32/13/2025)
- Limita tentativas de entrada
- Bug #1: Validação de status de tickets
- Lista de status válidos implementada
- Validação antes de alterar status
- Mensagens de erro claras
- Tratamento de exceções
---
## [0.1.0] - 2025-12-15
### Adicionado
- Auditoria técnica completa do sistema legado
- Issues criadas para bugs identificados
- Board Kanban no GitHub Projects
- Documentação inicial dos problemas encontrados
### Identificado
- Issue #1: Falta validação de status
- Issue #2: Falta validação de data
- Issue #3: Senha hardcoded no código
- Issue #4: Ausência de .gitignore
- Issue #5: README incompleto
---
## Legendas
- **Adicionado** - Novas funcionalidades
- **Mudado** - Mudanças em funcionalidades existentes
- **Descontinuado** - Funcionalidades que serão removidas
- **Removido** - Funcionalidades removidas
- **Corrigido** - Correção de bugs
- **Segurança** - Correções de vulnerabilidades