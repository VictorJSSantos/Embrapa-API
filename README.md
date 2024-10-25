# Visão Geral | Overview 
Essa é um projeto de uma API que está sendo construída para acessar os dados referentes ao processo produtivo (E outras informações também, consulte o link para saber exatamente quais) de uvas no Estado do Rio Grande do SUl (http://vitibrasil.cnpuv.embrapa.br/).
O projeto é feito para a entrega do primeiro módulo do curso de pós-graduação da FIAP em Machine Learning Engineering.

Este projeto é fruto do aprendizado do primeiro módulo da pós-graduação, que envolvia, entre outros tópicos:
* Fundamentos de Python;
* Criação de módulos e bibliotecas;
* Orientação a objetos;
* Estruturas de memórias
* API's e frameworks de ML;

Este projeto foi criado pelo time de dois engenheiros de dados estudantes: Victor Santos e Tatiana Haddad. Também teve o apoio de dois professores do curso para tirar eventuais dúvidas, Leonardo Pena e Ioannis Eleftheriou.
Pela ajuda, professores, nosso muito obrigado! 

# Objetivos | Objectives 

O objetivo deste projeto consiste em criar uma API com o escopo que deve incluir as seguintes áreas de interesse:
* Produção.
* Processamento.
* Comercialização.
* Importação.
* Exportação.

Com as áreas e dados delimitados, devemos garantir que este projeto seja capaz de fazer as seguintes atividades:
* Criar uma Rest API em Python que faça a consulta no site da Embrapa. -                                               ✔                   
* Sua API deve estar documentada. -                                                                                    ✔
* É recomendável (não obrigatório) a escolha de um método de autenticação (JWT, por exemplo). -                        ✔
* Criar plano para fazer o deploy da API. -                                                                            ✔
* Fazer um MVP realizando o deploy com um link compartilhável e um repositório no github. -                            ✔

# Diretórios do Projeto

O projeto foi feito tentando manter uma organização próxima ao indicado para projetos da vida real, de modo que facilite tanto a manutenção quanto o entendimento por qualquer pessoa interessada neste projeto.

O projeto tem os arquivos principais, relacionados ao próprio funcionamento dentro da pasta "app", que irá conter algumas informações importantes, a seguir iremos explicar os arquivos e uma breve descrição do conteúdo:
* main.py - Arquivo principal da aplicação sendo responsável pela chamada da aplicação;
* models.py - Arquivo constituído de todas as classes (modelos) que simbolizam os parâmetros da consulta, tais como área e subárea, para realizar a consulta de forma correta;
* schemas.py - Arquivo constituído dos schemas de validação, tanto para Input quanto para Output de cada requisição da API;
* requisicao_http.py - Arquivo constituído da classe Requisition, criada de forma a facilitar a manutenção e execução das ações http;
* transformar.py - Arquivo constituído da classe Transform, que irá servir para maiores manipulações de um resultado após a requisição http;
* utils.py - Arquivo constituído de funções generalistas, que podem ser acessadas em outras partes do programa, com o foco de centralizar o uso e facilitar a manutenabilidade;

Por fim, temos também a pasta "routes", esta pasta contém os arquivos que simbolizam todas as rotas. Cada rota foi separada em um arquivo com o motivo de facilitar a manutenção e a tornar fácil a identificação de quais rotas são tratadas em cada arquivo.

# Fluxo da API

![Fluxo desta API](https://github.com/VictorJSSantos/Modulo-1/blob/main/Module%201%20-%20API%20Architeture%20Design.jpg)

# Desenho de arquitetura do projeto


