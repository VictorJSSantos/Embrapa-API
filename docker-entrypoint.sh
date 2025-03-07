#!/bin/sh
set -e 

if [ -z "$SECRET_KEY" ]; then
    echo "Erro ao inicializar: A variável de ambiente SECRET_KEY não foi definida."
    echo "É preciso definir as variáveis SECRET_KEY, USERNAME e PASSWORD"
    exit 1
fi

if [ -z "$USERNAME" ]; then
    echo "Erro ao inicializar: A variável de ambiente USERNAME não foi definida."
    echo "É preciso definir as variáveis SECRET_KEY, USERNAME e PASSWORD"
    exit 1
fi

if [ -z "$PASSWORD" ]; then
    echo "Erro ao inicializar: A variável de ambiente PASSWORD não foi definida."
    echo "É preciso definir as variáveis SECRET_KEY, USERNAME e PASSWORD"
    exit 1
fi

exec "$@"