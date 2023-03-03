# comunicação chat GPT
URL = 'https://api.openai.com/v1/engines/davinci-codex/completions'
CONTENT_TYPE = "application/json"
AUTHORIZATION = "Bearer sua_chave_token_de_acesso_a_api_do_chatgpt"
MAX_TOKENS = 100
TEMPERATURE = 0.7


# falas
FALA_INICIAR = 'SAFIRA'
FALA_SAUDACAO = 'Pois não ?'
FALA_ESTOU_OUVINDO = 'Pode falar, estou ouvindo'
FALA_FINALIZAR_AUXILIO = 'Espero ter ajudado em algo. Se precisar é só me chamar'
FALA_FINALIZAR_PROGRAMA = 'Irei me retirar no momento. Caso precise do meu auxílio, é só executar o programa novamente'

FALA_ERRO_GENERICO = 'Aconteceu um erro inesperado, verifique o log gerado, por gentileza'
FALA_ERRO_CONEXAO = 'Erro de conexão com o serviço de reconhecimento de voz. Por esse motivo estarei desativada temporariamente, até que o sistema volte a funcionar'
FALA_ERRO_REQUISICAO = 'Não consegui resposta para o que você falou' + FALA_ERRO_GENERICO

# lista de falas não compreendida
FALA_NAO_COMPREENDIDA_1 = 'Não consegui entender o que você falou'
FALA_NAO_COMPREENDIDA_2 = 'Você está falando alguma coisa?'
FALA_NAO_COMPREENDIDA_3 = 'Meu irmão, fala alguma coisa pra mim responder e ir embora, por favor'
FALA_NAO_COMPREENDIDA_4 = 'Pode repetir?'
FALA_NAO_COMPREENDIDA_5 = 'Não entendi foi nada, cara. Repete'

LISTA_FALAS_INCOMPREENDIDAS = [
    FALA_NAO_COMPREENDIDA_1,
    FALA_NAO_COMPREENDIDA_2,
    FALA_NAO_COMPREENDIDA_3,
    FALA_NAO_COMPREENDIDA_4,
    FALA_NAO_COMPREENDIDA_5
]
