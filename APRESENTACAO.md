# Roteiro de Apresentação - SigTicket

**Data:** 20/12/2025  
**Grupo:** 7  
**Membros:**
- Edimar Hungria – Líder / Desenvolvimento principal / Documentação
- Emerson Souza – Correções de bugs / Refatorações / Code Review
- Paulo Araújo – Auditoria inicial / Testes / Suporte
- Alex Craveiro – Documentação final / Apresentação / Suporte

**Tempo total:** 10 minutos

---

## Estrutura da Apresentação

### 1. Introdução (1 min)
**Apresentador:** Edimar Hungria  
**Pontos:**
- Apresentação da equipe
- Nome do projeto: SigTicket
- Objetivo: Sistema de gerenciamento de tickets de suporte
- Contexto: Evolução de um sistema legado durante a semana

---

### 2. Sistema Original e Auditoria (1,5 min)
**Apresentador:** Emerson Souza  
**Pontos:**
- Funcionalidades básicas do legado
- Problemas identificados na auditoria (ATV5)
- Principais bugs e dívidas técnicas (senha hardcoded, falta de validações)
- Demonstração rápida do board Kanban inicial com issues

---

### 3. Correções de Bugs (2 min)
**Apresentador:** Emerson Souza  
**Pontos:**
- Bug #1: Validação de status
- Bug #2: Validação de data (formato, futura, tentativas)
**Demo ao vivo:**
- Tentar status inválido → erro
- Tentar data inválida/futura → erro com tentativas
- Criar ticket com dados válidos → sucesso

---

### 4. Refatorações (2 min)
**Apresentador:** Paulo Araújo  
**Pontos:**
- Remoção de senha hardcoded → config.py
- Criação de .gitignore
- Melhoria completa do README.md
- Centralização de configurações
**Demo:**
- Mostrar arquivo config.py
- Mostrar README.md atualizado

---

### 5. Code Review e Melhorias (1,5 min)
**Apresentador:** Alex Craveiro  
**Pontos:**
- Revisão mútua com buddy group
- Melhorias implementadas (limpeza de código, constantes, docstrings)
- Aprendizados do code review

---

### 6. Documentação Final (1,5 min)
**Apresentador:** Edimar Hungria  
**Pontos:**
- Comentários e docstrings completas no código
- DOCS.md: documentação técnica detalhada
- CHANGELOG.md atualizado até versão 1.0.0
**Demo:**
- Mostrar exemplo de função comentada em tickets.py
- Mostrar estrutura do projeto (arquivos finais)

---

### 7. Conclusão (1 min)
**Apresentador:** Todos (Edimar Hungria fecha)  
**Pontos:**
- Resultados alcançados: sistema funcional, seguro e bem documentado
- Principais aprendizados da semana
- Trabalho em equipe (presencial + remoto)
- Agradecimentos ao professor e à turma

---

## Divisão de Responsabilidades
- **Edimar Hungria:** Introdução, Documentação Final, Conclusão, Demo principal do sistema
- **Emerson Souza:** Sistema Original/Auditoria, Correções de Bugs, Demo de validações
- **Paulo Araújo:** Refatorações, Demo de config.py e README
- **Alex Craveiro:** Code Review e Melhorias

---

## Checklist Pré-Apresentação
- [ ] Testar o sistema completo antes da apresentação
- [ ] Abrir repositório GitHub em aba (PRs, board Kanban)
- [ ] Abrir Codespace pronto para demo ao vivo
- [ ] README.md, DOCS.md e CHANGELOG.md abertos
- [ ] Cronometrar tempo total (máximo 10 min)
- [ ] Todos ensaiaram sua parte
- [ ] Prints de backup caso internet falhe

---

## Demonstração ao Vivo (3-4 minutos)
**Ordem:**
1. Login (tentar senha errada → erro)
2. Criar ticket (tentar data inválida/futura → erro com tentativas → sucesso)
3. Listar tickets
4. Mudar status (tentar inválido → erro → sucesso)
5. Mostrar código comentado (exemplo de função com docstring)

---

## Falas Sugeridas

**Abertura (Edimar):**
"Bom dia/tarde! Somos o grupo 7: Edimar Hungria, Emerson Souza, Paulo Araújo e Alex Craveiro. Hoje vamos apresentar a evolução do SigTicket, um sistema de gerenciamento de tickets que começamos como legado e transformamos em uma versão robusta e documentada."

**Transição para demo (Emerson):**
"Agora vamos demonstrar o sistema funcionando, destacando as validações que implementamos..."

**Encerramento (Edimar):**
"Concluindo, evoluímos um sistema legado corrigindo bugs críticos, refatorando o código, realizando code review e documentando completamente o projeto. Obrigado pela atenção!"

---

## Perguntas Possíveis
**P: Por que usaram config.py em vez de variáveis de ambiente?**  
R: Para manter simplicidade no escopo educacional. Em produção usaríamos variáveis de ambiente ou secrets.

**P: Os dados são persistidos?**  
R: Não, ficam em memória. Está documentado como melhoria futura no DOCS.md.

**P: Como foi o trabalho em equipe?**  
R: Híbrido: parte presencial (Edimar e Emerson) e remoto via WhatsApp (Paulo e Alex). Funcionou bem com divisão clara de tarefas.

---

**Última atualização:** 19/12/2025