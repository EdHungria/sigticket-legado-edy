#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Arquivo de Configuração - SigTicket
Versão: 1.0.0

Este arquivo centraliza todas as configurações e constantes do sistema.

ATENÇÃO DE SEGURANÇA:
Em ambiente de produção, as credenciais devem ser armazenadas em:
- Variáveis de ambiente
- Arquivos .env (não versionados)
- Sistemas de gerenciamento de secrets

Este arquivo com credenciais está aqui apenas para fins educacionais.
"""

# ================================================================
# CREDENCIAIS DE ACESSO
# ================================================================
# Dicionário de usuários e senhas
# Chave: nome de usuário
# Valor: senha em texto plano (apenas para fins educacionais)
USUARIOS = {
    "admin": "admin123",    # Usuário administrador
    "suporte": "suporte123" # Usuário de suporte
}

# ================================================================
# CONFIGURAÇÕES DE VALIDAÇÃO
# ================================================================
# Status válidos que um ticket pode ter
# Ordem representa fluxo típico de atendimento
STATUS_VALIDOS = [
    "aberto",         # Ticket recém-criado
    "em_andamento",   # Ticket sendo analisado/trabalhado
    "resolvido",      # Problema solucionado, aguardando confirmação
    "fechado"         # Ticket finalizado
]

# Número máximo de tentativas para entrada de data válida
MAX_TENTATIVAS_DATA = 3

# Ano mínimo aceito para datas (evita datas muito antigas)
ANO_MINIMO = 2000