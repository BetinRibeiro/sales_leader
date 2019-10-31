# -*- coding: utf-8 -*-
# tente algo como

def listar_vendedor():
    projeto = db.projeto(request.args(0, cast=int))
    rows = db(db.vendedor.projeto == request.args(0, cast=int)).select()
    return locals()


def inserir_vendedor():
    proj = db.projeto(request.args(0, cast=int))
    db.vendedor.projeto.default = proj.id
    db.vendedor.projeto.readable = False
    db.vendedor.projeto.writable = False

    db.vendedor.comissao_venda.readable = True
    db.vendedor.comissao_venda.writable = True
    db.vendedor.vale_saida.readable = True
    db.vendedor.vale_saida.writable = True

    merc = db(db.vendedor.projeto==proj.id).select()
    form = SQLFORM(db.vendedor).process()
    if form.accepted:
        response.flash = 'Formulario aceito'
        redirect(URL('listar_vendedor', args=proj.id))
    elif form.errors:
        response.flash = 'Formulario não aceito'
    else:
        response.flash = 'Preencha o formulario'
    return locals()
def listar_venda():
    vendedor = db.vendedor(request.args(0, cast=int))
    rows = db(db.venda.vendedor).select()
    return locals()
