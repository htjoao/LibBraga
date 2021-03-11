from LibBraga.spam.modelos import Usuario


def test_salvar_usuario(sessao):
    usuario = Usuario(nome='htjoao', email='sooaresraiane@gmail.com')
    sessao.salvar(usuario)
    assert isinstance(usuario.id, int)


def test_listar_usuario(sessao):
    usuarios = [
        Usuario(nome='htjoao', email='sooaresraiane@gmail.com'),
        Usuario(nome='raiane', email='sooaresraiane@gmail.com')
    ]
    for usuario in usuarios:
        sessao.salvar(usuario)
    assert usuarios == sessao.listar()
