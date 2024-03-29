# -*- coding: utf-8 -*-
# tente algo como
def listar_merc():
    projeto = db.projeto(request.args(0, cast=int))
    rows = db(db.mercadoria.projeto == request.args(0, cast=int)).select()
    return locals()

def inserir_merc():
	proj = db.projeto(request.args(0, cast=int))
	db.mercadoria.projeto.default = proj.id
	db.mercadoria.projeto.writable = False
    
	db.mercadoria.quant_pcs_retorno.readable = False
	db.mercadoria.quant_pcs_retorno.writable = False
    
    
	merc = db(db.mercadoria.projeto==proj.id).select()
	form = SQLFORM(db.mercadoria).process()
	if form.accepted:
		response.flash = 'Formulario aceito'
		redirect(URL('listar_merc', args=proj.id))
	elif form.errors:
		response.flash = 'Formulario não aceito'
	else:
		response.flash = 'Preencha o formulario'
	return locals()

def alterar_merc():
	merc = db.mercadoria(request.args(0, cast=int))
	proj = db.projeto(merc.projeto)
    
	db.mercadoria.id.readable = False
	db.mercadoria.id.writable = False
	db.mercadoria.projeto.readable = False
	db.mercadoria.projeto.writable = False
    
	db.mercadoria.quant_pcs_retorno.readable = False
	db.mercadoria.quant_pcs_retorno.writable = False
    
	form = SQLFORM(db.mercadoria, request.args(0, cast=int))
	if form.process().accepted:
		session.flash = 'atualizada'
		redirect(URL('listar_merc', args=proj.id))
	elif form.errors:
		response.flash = 'Erros no formulário!'
	else:
		if not response.flash:
			response.flash = 'Preencha o formulário!'
	return locals()
def listar_retorno():
    projeto = db.projeto(request.args(0, cast=int))
    rows = db(db.mercadoria.projeto == request.args(0, cast=int)).select()
    return locals()

def alterar_merc_retorno():
    mercadoria = db.mercadoria(request.args(0, cast=int))
    proj = db.projeto(mercadoria.projeto)
    db.mercadoria.id.readable = False
    db.mercadoria.id.writable = False
    
    db.mercadoria.projeto.readable = False
    db.mercadoria.projeto.writable = False
    
    db.mercadoria.quant_pcs_enviada.readable = True
    db.mercadoria.quant_pcs_enviada.writable = False
    
    db.mercadoria.descricao.readable = True
    db.mercadoria.descricao.writable = False
    
    db.mercadoria.preco_unitario.readable = False
    db.mercadoria.preco_unitario.writable = False
    form = SQLFORM(db.mercadoria, request.args(0, cast=int))
    if form.process().accepted:
        session.flash = 'atualizada'
        redirect(URL('listar_retorno', args=proj.id))
    elif form.errors:
        response.flash = 'Erros no formulário!'
    else:
        if not response.flash:
            response.flash = 'Preencha o formulário!'
    return locals()
