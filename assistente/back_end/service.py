import requests
from utils import constantes


def enviar_pergunta(pergunta):
    # Envio da pergunta para o ChatGPT
    try:
        # criação do cabeçalho da requisição
        headers = {
            "Content-Type": constantes.CONTENT_TYPE,
            "Authorization": constantes.AUTHORIZATION
        }

        # criação do corpo da requisição
        body = {
            "prompt": pergunta,
            "max_tokens": constantes.MAX_TOKENS,
            "temperature": constantes.TEMPERATURE
        }

        response = requests.post(constantes.URL, headers=headers, json=body)
        resultado_retornado = response.json()

        # pegando informação exata da resposta retornada
        resposta = resultado_retornado["choices"][0]["text"]

        return resposta

    except Exception as e:
        print(f"Erro: {e}")

        return constantes.FALA_ERRO_REQUISICAO
