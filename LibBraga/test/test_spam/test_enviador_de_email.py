import pytest

from LibBraga.spam.enviador_de_email import Enviador, EmailInvalido


def test_criar_enviador_de_email():
    enviador = Enviador()
    assert enviador is not None


@pytest.mark.parametrize(
    'destinatario',
    ['jvictor.braga@yahoo.com', 'sooaresraiane@gmail.com', 'jo_elma28@yahoo.com.br']
)
def test_remetente(destinatario):
    enviador = Enviador()
    destinatario
    resultado = enviador.enviar(
        destinatario,
        'jo_elma28@yahoo.com.br',
        'Email de teste para o curso',
        'Oi,so queria testar o envio de email automático.'
    )
    assert destinatario in resultado


@pytest.mark.parametrize(
    'destinatario',
    ['jvictor', 'sooares.com', 'jo_yahoo.']
)
def test_remetente_invalido(destinatario):
    enviador = Enviador()
    with pytest.raises(EmailInvalido):
        enviador.enviar(
            destinatario,
            'jo_elma28@yahoo.com.br',
            'Email de teste para o curso',
            'Oi,so queria testar o envio de email automático.'
        )
