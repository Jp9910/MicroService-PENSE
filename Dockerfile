FROM python:2.7

LABEL version="0.1" description="Servidor web em Python" maintainer="Joao Paulo Secundo <joao.secundo@dcomp.ufs.br>"

WORKDIR /

COPY ./servidor.py .

#expose serve apenas para documentacao. usar -p 55504:80 quando for iniciar o container
EXPOSE 80

CMD ["python", "servidor.py"]
