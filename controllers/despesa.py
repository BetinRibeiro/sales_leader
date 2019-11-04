# -*- coding: utf-8 -*-
# tente algo como
def listar_despesas():
    projeto = db.projeto(request.args(0, cast=int))
    rows = db((db.despesa.projeto == request.args(0, cast=int))).select()
    return locals()

def inserir_desp():
    proj = db.projeto(request.args(0, cast=int))
    db.despesa.projeto.default = proj.id
    db.despesa.projeto.readable = False
    db.despesa.projeto.writable = False
    
    merc = db(db.despesa.projeto==proj.id).select()
    form = SQLFORM(db.despesa).process()
    if form.accepted:
        response.flash = 'Formulario aceito'
        redirect(URL('listar_despesas', args=proj.id))
    elif form.errors:
        response.flash = 'Formulario não aceito'
    else:
        response.flash = 'Preencha o formulario'    
    return locals()

def alterar_desp():
    merc = db.despesa(request.args(0, cast=int))
    proj = db.projeto(merc.projeto)
    db.despesa.id.readable = False
    db.despesa.id.writable = False
    db.despesa.projeto.readable = False
    db.despesa.projeto.writable = False
    form = SQLFORM(db.despesa, request.args(0, cast=int))
    if form.process().accepted:
        session.flash = 'Despesa atualizada'
        redirect(URL('listar_despesas', args=proj.id))
    elif form.errors:
        response.flash = 'Erros no formulário!'
    else:
        if not response.flash:
            response.flash = 'Preencha o formulário!'
    return locals()
