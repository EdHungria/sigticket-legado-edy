---
name: ♻️ Refatoração / Dívida Técnica
about: Identificar código que precisa ser melhorado
title: '[REFACTOR] '
labels: refactor
assignees: ''
---

## 📋 Problema Identificado

Descreva qual parte do código tem problema de qualidade.

**Exemplo:** "Senha de administrador está hardcoded na linha 8 do arquivo `tickets.py`."

---

## ⚠️ Por Que Isso é um Problema?

Explique o impacto dessa dívida técnica.

**Exemplo:** "Qualquer pessoa com acesso ao código-fonte consegue ver a senha. Isso é uma falha grave de segurança."

---

## ✅ Solução Proposta

Como melhorar esse código?

**Exemplo:** 
"Mover a senha para variável de ambiente usando arquivo `.env`:
from dotenv import load_dotenv
import os

load_dotenv()
SENHA_ADMIN = os.getenv('SENHA_ADMIN')

---

## 📊 Impacto

Qual área do sistema será afetada?

- [ ] Segurança
- [ ] Manutenibilidade
- [ ] Performance
- [ ] Legibilidade

---

## 🏷️ Classificação

- [ ] `refactor` - Melhorar código existente
- [ ] `security` - Segurança
- [ ] `docs` - Documentação
- [ ] `architecture` - Estrutura do código
