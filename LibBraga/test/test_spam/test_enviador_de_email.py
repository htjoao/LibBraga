import pytest

from LibBraga.spam.enviador_de_email import Enviador, EmailInvalido


def test_criar_enviador_de_email():
    enviador = Enviador()
    assert enviador is not None


@pytest.mark.parametrize(
    'remetente',
    ['jvictor.braga@yahoo.com', 'sooaresraiane@gmail.com', 'jo_elma28@yahoo.com.br']
)
def test_remetente(remetente):
    enviador = Enviador()
    remetente
    resultado = enviador.enviar(
        remetente,
        'jo_elma28@yahoo.com.br',
        'Email de teste para o curso',
        'Oi,so queria testar o envio de email automático.'
    )
    assert remetente in resultado


@pytest.mark.parametrize(
    'remetente',
    ['jvictor', 'sooares.com', 'jo_yahoo.']
)
def test_remetente_invalido(remetente):
    enviador = Enviador()
    with pytest.raises(EmailInvalido):
        enviador.enviar(
            remetente,
            'jo_elma28@yahoo.com.br',
            'Email de teste para o curso',
            'Oi,so queria testar o envio de email automático.'
        )
