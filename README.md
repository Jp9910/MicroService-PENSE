# Servidor:  Pense - Processor Executando Neste SErvidor

## Autor: _João Paulo Secundo_

## Como funciona
Depois de iniciado, o servidor atenderá requisições GET HTTP de qualquer subrota de `/`, e responderá com uma tabela informando os processos que estão atualmente em execução no servidor. Para isso, é criado um subprocesso `ps`, e seu output é montado dinamicamente em uma tabela html.

##  Porta do servidor:

> 55504

## Exemplo de uso:

> Em um terminal linux, digitar: "wget localhost:55504"

> No firefox, digitar "localhost:55504/teste" (ou qualquer subrota de / )
