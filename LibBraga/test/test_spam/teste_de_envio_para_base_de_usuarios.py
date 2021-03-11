import pytest

from LibBraga.spam.enviador_de_email import Enviador
from LibBraga.spam.main import EnviadorDeSpam
from LibBraga.spam.modelos import Usuario


@pytest.mark.parametrize(
    'usuarios',
    [
        [
            Usuario(nome='htjoao', email='sooaresraiane@gmail.com'),
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
    enviador = Enviador()
    enviador_de_spam = EnviadorDeSpam(sessao, enviador)
    enviador_de_spam.enviar_emails(
        'jvictor.braga@yahoo.com',
        'teste de curso',
        'Teste com sucesso, Email foi enviado'
    )
    assert len(usuarios) == enviador.qde_email_enviados
