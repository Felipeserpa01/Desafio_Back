Este projeto é um servidor WebSocket que permite a conexão de múltiplos clientes, oferecendo funcionalidades em tempo real, como o envio da data e hora atuais a cada segundo, o cálculo de números de Fibonacci sob demanda e a gestão de usuários conectados. Toda vez que um cliente se conecta ou desconecta, o sistema atualiza um banco de dados PostgreSQL para refletir o status atual dos usuários. O projeto foi desenvolvido utilizando tecnologias modernas e é executado em um ambiente containerizado com Docker e Docker Compose.
---
<p></p>

Tecnologias Utilizadas:

Aqui estão as principais tecnologias usadas no projeto:

Python: Linguagem principal do projeto, escolhida por sua simplicidade e suporte a programação assíncrona.

FastAPI: Framework moderno para criar APIs e WebSockets de forma eficiente.

WebSockets: Protocolo que permite comunicação em tempo real entre clientes e servidores.

PostgreSQL: Banco de dados relacional para armazenar informações sobre os usuários conectados.

Docker: Ferramenta para containerização, facilitando a execução do projeto em qualquer ambiente.

Docker Compose: Usado para orquestrar o servidor e o banco de dados em um único ambiente.

---


Instruções para Rodar o Projeto:
Siga os passos abaixo para configurar e executar o projeto localmente.

<br></br>
Pré-requisitos:
Docker: Instale o Docker em docker.com.

Docker Compose: Geralmente já vem com o Docker. Caso contrário, siga as instruções em docs.docker.com/compose/install.

Passo 1: Clone o Repositório
Clone o repositório do projeto:
```git clone https://github.com/Felipeserpa01/Desafio_Back.git```
```cd Desafio_Back```


<br></br>
Passo 2: Inicie o Projeto com Docker Compose
Execute o seguinte comando para construir e iniciar os contêineres:
```docker-compose up --build```
Isso fará:

Construir a imagem do servidor WebSocket.

Iniciar o banco de dados PostgreSQL.

Iniciar o servidor WebSocket na porta 8000.


<br></br>
Passo 3: Conecte-se ao Servidor WebSocket
Abra um navegador web e acesse:

`localhost:8000`


<br></br>
Passo 4: Teste as Funcionalidades
1. Data e Hora
O servidor envia a data e hora atuais a cada segundo para todos os clientes conectados.

2. Cálculo de Fibonacci
Envie um número n (ex: 10) para o servidor.

O servidor responderá com o valor de Fibonacci(n) (ex: Fibonacci(10) = 55).

3. Gestão de Usuários Conectados
Quando um cliente se conecta ou desconecta, o banco de dados PostgreSQL é atualizado automaticamente.

---

Passo 5: Parar o Projeto
Para parar os contêineres, pressione Ctrl + C e execute:

docker-compose down
