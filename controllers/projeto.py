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
        redirect(URL('acesso_geral_projeto', args=projeto.id))
    elif form.errors:
        response.flash = 'Erros no formulário!'
    else:
        if not response.flash:
            response.flash = 'Preencha o formulário!'
    return locals()

def acesso_geral_projeto():
    projeto = db.projeto(request.args(0, cast=int))
    return locals()

def alterar_vale_saida():
    projeto = db.projeto(request.args(0, cast=int))

    db.projeto.id.readable = False
    db.projeto.id.writable = False
    
    db.projeto.nome.readable = True
    db.projeto.nome.writable = False

    db.projeto.nome_chefe.readable = True
    db.projeto.nome_chefe.writable = False

    db.projeto.primeira_cidade.readable = True
    db.projeto.primeira_cidade.writable = False

    db.projeto.adiantamento_dinh_venda.readable = True
    db.projeto.adiantamento_dinh_venda.writable = False

    db.projeto.data_saida_venda.readable = True
    db.projeto.data_saida_venda.writable = False

    db.projeto.data_cobranca.readable = True
    db.projeto.data_cobranca.writable = False
    form = SQLFORM(db.projeto, request.args(0, cast=int))
    if form.process().accepted:
        session.flash = 'Filme atualizado'
        redirect(URL('acesso_geral_projeto', args=projeto.id))
    elif form.errors:
        response.flash = 'Erros no formulário!'
    else:
        if not response.flash:
            response.flash = 'Preencha o formulário!'
    return locals()
