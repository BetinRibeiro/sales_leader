# -*- coding: utf-8 -*-
# tente algo como
@auth.requires_login()
def listar_projetos():
    a = auth.user
    rows = db(db.projeto.created_by == auth.user).select()
    return locals()


def criar_projeto():
    conteudo = db.projeto(request.args(0, auth.user))

    form = SQLFORM(db.projeto).process()
    if form.accepted:
        response.flash = 'Formulario aceito'
        redirect(URL('listar_projetos'))
    elif form.errors:
        response.flash = 'Formulario não aceito'
    else:
        response.flash = 'Preencha o formulario'
    return locals()


def alterar_projeto():
    projeto = db.projeto(request.args(0, cast=int))

    db.projeto.id.readable = False
    db.projeto.id.writable = False

    form = SQLFORM(db.projeto, request.args(0, cast=int))
    if form.process().accepted:
        session.flash = 'Filme atualizado'
        redirect(URL('listar_projetos'))
    elif form.errors:
        response.flash = 'Erros no formulário!'
    else:
        if not response.flash:
            response.flash = 'Preencha o formulário!'
    return locals()

def acesso_geral_projeto():
    projeto = db.projeto(request.args(0, cast=int))
    return locals()
