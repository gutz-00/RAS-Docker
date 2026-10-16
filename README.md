# 🐳 Trabalho de Recuperação Paralela 3º Bimestre - RASI (Docker + Flask)

Instituto Federal de Educação, Ciência e Tecnologia de São Paulo (IFSP) - Campus Campos do Jordão

Curso: Técnico em Informática Integrado ao Ensino Médio

Disciplina: Redes e Administração de Sistemas (RASI)

Professor: Cesar Augusto de Moraes Costa

Aluno: [Pablo Augusto de Moura Rocha]

Prontuário: [CJ3027988]

Data de Entrega: 23/10/2026

# 📌 1. Sobre o Projeto

Este repositório contém a implementação prática da containerização de uma aplicação web em Python/Flask utilizando o Docker. O projeto faz parte do Trabalho de Recuperação Paralela do 3º Bimestre da disciplina de RASI e toma como referência base o repositório do professor: CesarAugusto88/RAS-Docker.

# 🎯 Objetivos Concluídos:

[x] Provisionamento de VM Ubuntu Server no VirtualBox.

[x] Configuração da interface de rede e acesso remoto via SSH.

[x] Instalação e teste de funcionamento do Docker Engine.

[x] Criação do Dockerfile utilizando a imagem obrigatória python:3.14-slim.

[x] Expansão da aplicação Flask para conter 4 rotas distintas (/, /sobre, /contato, /aluno) com layouts e temas visuais personalizados via CSS.

[x] Rebuild, mapeamento de porta (5000:5000) e teste no navegador da máquina hospedeira.

# 🛠️ 2. Estrutura do Repositório

```text
├── app.py              # Aplicação principal em Flask com as rotas customizadas
├── Dockerfile          # Especificação da imagem Docker (python:3.14-slim)
├── requirements.txt    # Lista de dependências Python (Flask)
└── README.md           # Documentação e instruções de execução
```


🚀 3. Como Executar o Projeto no Docker

Passo 1: Clonar o Repositório na VM Ubuntu Server

Conecte-se à VM via SSH e clone este repositório:

git clone https://github.com/[seu-usuario]/RAS-Docker-Aluno.git
cd RAS-Docker-Aluno



Passo 2: Construir a Imagem Docker

Execute o comando de build para criar a imagem local nomeada flask-app:

```text
docker build -t flask-app .
```


Passo 3: Subir o Container

Inicie o container em segundo plano (detached) mapeando a porta 5000:
```text
docker run -d -p 5000:5000 --name meu-flask flask-app
```


Passo 4: Verificar a Execução

Certifique-se de que o container está ativo:
```text
docker ps
```


Para visualizar os logs da aplicação:
```text
docker logs meu-flask
```


# 🌐 4. Rotas da Aplicação

Após subir o container, acesse pelo navegador da máquina hospedeira (substituindo [IP_DA_VM] pelo IP do seu servidor):

Home: http://[IP_DA_VM]:5000/

Sobre: http://[IP_DA_VM]:5000/sobre

Contato: http://[IP_DA_VM]:5000/contato

Aluno: http://[IP_DA_VM]:5000/aluno

# 📚 5. Referências

Documentação Oficial do Docker

Documentação do Flask

Repositório Base - Prof. Cesar Augusto
