from unittest.mock import Mock


import pytest
from LibBraga.spam.main import EnviadorDeSpam
from LibBraga.spam.modelos import Usuario


@pytest.mark.parametrize(
    'usuarios',
    [
        [
            Usuario(nome='htjoao', email='jvictor.braga@yahoo.com'),
            Usuario(nome='raiane', email='sooaresraiane@gmail.com')
        ],
        [
            Usuario(nome='htjoao', email='sooaresraiane@gmail.com')
        ]
    ]
)
def test_qde_de_spam(sessao, usuarios):
    for usuario in usuarios:
        sessao.salvar(usuario)
    enviador = Mock()
    enviador_de_spam = EnviadorDeSpam(sessao, enviador)
    enviador_de_spam.enviar_emails(
        'jvictor.braga@yahoo.com',
        'teste de curso',
        'Teste com sucesso, Email foi enviado'
    )
    assert len(usuarios) == enviador.enviar.call_count


def test_pareametros_de_spam(sessao):
    usuario = Usuario(nome='htjoao', email='jvictor.braga@yahoo.com')
    sessao.salvar(usuario)
    enviador = Mock()
    enviador_de_spam = EnviadorDeSpam(sessao, enviador)
    enviador_de_spam.enviar_emails(
        'sooaresraiane@gmail.com',
        'teste de curso',
        'Teste com sucesso, Email foi enviado'
    )
    enviador.enviar.assert_called_once_with(
        'sooaresraiane@gmail.com',
        'jvictor.braga@yahoo.com',
        'teste de curso',
        'Teste com sucesso, Email foi enviado'
    )
