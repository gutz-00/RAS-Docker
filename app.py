from flask import Flask

app = Flask(__name__)

# Estilo global para padronização visual das páginas
CSS_BASE = """
    <style>
        * { box-sizing: border-box; }
        body { 
            font-family: 'Segoe UI', Roboto, Helvetica, Arial, sans-serif; 
            margin: 0; 
            padding: 40px 20px; 
            text-align: center; 
            color: #2c3e50; 
            min-height: 100vh;
            display: flex;
            align-items: center;
            justify-content: center;
        }
        .card { 
            background-color: #ffffff; 
            border-radius: 12px; 
            padding: 40px; 
            box-shadow: 0 10px 25px rgba(0,0,0,0.12); 
            max-width: 650px; 
            width: 100%; 
            transition: all 0.3s ease;
        }
        h1 { 
            color: #1a5276; 
            margin-top: 0;
            margin-bottom: 15px; 
            font-size: 1.8rem;
        }
        p { 
            font-size: 1.1rem; 
            line-height: 1.6; 
            color: #566573;
        }
        .info-box {
            background-color: #f8f9f9;
            border-left: 4px solid #2980b9;
            padding: 15px;
            margin: 20px 0;
            text-align: left;
            border-radius: 0 8px 8px 0;
        }
        nav { 
            margin-top: 30px; 
            padding-top: 20px; 
            border-top: 2px solid #eaeded; 
        }
        nav a { 
            margin: 0 12px; 
            color: #2980b9; 
            text-decoration: none; 
            font-weight: 600; 
            font-size: 1.05rem;
            display: inline-block;
            padding: 6px 12px;
            border-radius: 6px;
            transition: background 0.2s;
        }
        nav a:hover { 
            background-color: #ebf5fb; 
            color: #1b4f72;
        }
    </style>
"""

def render_page(title, content, bg_color="#f4f6f7"):
    """
    Função auxiliar para renderizar páginas HTML com layout e cores dinâmicas.
    """
    nav = """
    <nav>
        <a href="/">Home</a>
        <a href="/sobre">Sobre</a>
        <a href="/contato">Contato</a>
        <a href="/aluno">Aluno</a>
    </nav>
    """
    return f"""
    <!DOCTYPE html>
    <html lang="pt-br">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>{title}</title>
        {CSS_BASE}
    </head>
    <body style="background-color: {bg_color};">
        <div class="card">
            <h1>{title}</h1>
            <div>{content}</div>
            {nav}
        </div>
    </body>
    </html>
    """

@app.route('/')
def home():
    content = """
    <p>Bem-vindo à aplicação web containerizada rodando no Docker!</p>
    <div class="info-box">
        <strong>Status do Sistema:</strong> Ativo e operando dentro do container Python 3.14-slim.<br>
        <strong>Servidor Web:</strong> Flask WSGI Server em execução na porta 5000.
    </div>
    """
    return render_page("Página Inicial - RASI Docker", content, "#eaedd0")

@app.route('/sobre')
def sobre():
    content = """
    <p>Projeto de Recuperação Paralela do 3º Bimestre da disciplina de <strong>Redes e Administração de Sistemas (RASI)</strong>.</p>
    <div class="info-box">
        <strong>Objetivo:</strong> Migrar a infraestrutura de testes para um ambiente modernizado utilizando virtualização leve via Docker.
    </div>
    """
    return render_page("Sobre o Projeto", content, "#d0ece7")

@app.route('/contato')
def contato():
    content = """
    <p>Entre em contato com o administrador do sistema ou com a instituição de ensino:</p>
    <div class="info-box">
        <strong>E-mail Institucional:</strong> aluno@aluno.ifsp.edu.br<br>
        <strong>Instituição:</strong> Instituto Federal de SP - Campus Campos do Jordão<br>
        <strong>Docente Responsável:</strong> Prof. Cesar Augusto de Moraes Costa
    </div>
    """
    return render_page("Canais de Contato", content, "#fdebd0")

@app.route('/aluno')
def aluno():
    content = """
    <p>Dados de identificação do aluno responsável pela execução da atividade:</p>
    <div class="info-box">
        <strong>Nome do Aluno:</strong> [Seu Nome Completo Aqui]<br>
        <strong>Prontuário:</strong> [Seu Prontuário]<br>
        <strong>Curso:</strong> Técnico em Informática Integrado ao Ensino Médio<br>
        <strong>Turma:</strong> RASI - 3º Bimestre / 2026
    </div>
    """
    return render_page("Perfil do Aluno", content, "#f5eedc")

if __name__ == '__main__':
    # Define o host como '0.0.0.0' para permitir acesso fora do container
    app.run(host='0.0.0.0', port=5000)