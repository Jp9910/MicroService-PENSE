# Servidor:  PENSE - Processos Executando Neste SErvidor

## Autor: _João Paulo Secundo_

## Como funciona
Depois de iniciado, o servidor atenderá requisições GET HTTP de qualquer subrota de `/`, e responderá com uma tabela informando os processos que estão atualmente em execução no servidor. Para isso, é criado um subprocesso `ps`, e seu output é montado dinamicamente em uma tabela html.

##  Porta do servidor:

> 55504

## Exemplo de uso:

### Para iniciar o servidor:

- (Etapas sem container)
    - Deve-se executar o servidor, com o comando "python servidor.py". 

- (Etapas com container)
    - Primeiro deve-se buildar a imagem do container a partir do Dockerfile, com o comando 
    > docker image build -t servidorweb-jp:0.1 .

    - Em seguida deve-se pôr o container para executar fazendo bind da porta 80 do container com a 55504 do host, usando o comando 
    > docker container run -d -p 55504:80 -it --name servidorweb-jp servidorweb-jp:0.1

### Para acessar o serviço:

- Usa-se um cliente web:

    - Em um terminal com wget instalado, digitar: "wget localhost:55504"
    
    Ou

    - No firefox, digitar "localhost:55504/teste" (Pode ser qualquer subrota de / )
