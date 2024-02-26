import requests

def salvar_arquivo_no_github(nome_arquivo, conteudo_arquivo, nome_repositorio, nome_usuario, token_acesso):
    url = f'https://api.github.com/repos/{nome_usuario}/{nome_repositorio}/contents/{nome_arquivo}'
    
    headers = {
        'Authorization': f'token {token_acesso}',
        'Content-Type': 'application/json',
    }
    
    dados = {
        'message': 'Adicionando arquivo via API',
        'content': conteudo_arquivo,
    }
    
    response = requests.put(url, headers=headers, json=dados)
    
    if response.status_code == 201:
        print(f'Arquivo {nome_arquivo} salvo com sucesso no repositório {nome_repositorio}.')
    else:
        print(f'Erro ao salvar o arquivo. Código de status: {response.status_code}')
        print(response.text)

# Exemplo de uso
nome_arquivo = 'exemplo.txt'
conteudo_arquivo = 'Conteúdo do arquivo de exemplo.'
nome_repositorio = 'seu-repositorio'
nome_usuario = 'seu-usuario'
token_acesso = 'seu-token-de-acesso'

salvar_arquivo_no_github(nome_arquivo, conteudo_arquivo, nome_repositorio, nome_usuario, token_acesso)
