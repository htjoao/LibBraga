from LibBraga.spam.enviador_de_email import Enviador
from LibBraga.spam.main import EnviadorDeSpam


def test_envio_de_spam(sessao):
    enviador_de_spam = EnviadorDeSpam(sessao, Enviador())
    enviador_de_spam.enviar_emails(
        'jvictor.braga@yahoo.com',
        'teste de curso',
        'Teste com sucesso, Email foi enviado'
    )
