# -*- coding: utf-8 -*-
db.define_table('projeto',
				#info_antes_venda
                Field('nome', 'string', notnull=True, label="Nome Projeto"),
				Field('nome_chefe', 'string', label="Nome Chefe"),
                Field('primeira_cidade', 'string', label="Primeira Cidade"),
				Field('vale_saida_chefe', 'double', label="Vale Chefe",notnull=True, default=0),
				Field('adiantamento_dinh_venda', 'double', label="Adiant Dinh Venda",notnull=True, default=0),
                Field('comissao_chefe_venda', 'double',  label="% Comissao Ven Chefe",notnull=True, default=3),
                Field('data_saida_venda', 'date', label="Data Saida Venda"),
                Field('data_cobranca', 'date', label="Data Cobrança"),
                #info_chegada_Venda
				Field('devolucao_dinh_venda', 'double', label="Devol Dinh Venda",notnull=True, default=0),
                
				Field('total_valor_depesa_venda', 'double', writable=False, readable=False, notnull=True, default=0),
                
				#informações Mercadoria (informação vem da tabela de Mercadoria)
				Field('total_quant_pcs_envio', 'integer', writable=False, readable=False, notnull=True, default=0),
				Field('total_preco_envio', 'double', writable=False, readable=False, notnull=True, default=0),
                
				Field('total_quant_pcs_retorno', 'integer', writable=False, readable=False, notnull=True, default=0),
				Field('total_preco_retorno', 'double', writable=False, readable=False, notnull=True, default=0),
                
                
				Field('total_quant_pcs_devolucao', 'integer', writable=False, readable=False, notnull=True, default=0),
				Field('total_preco_devolucao', 'double', writable=False, readable=False, notnull=True, default=0),

				#informações Funcionario (informação vem da tabela de Funcionario)
				Field('total_salario', 'double', writable=False, readable=False, notnull=True, default=0),
				Field('total_vale_saida_funcionario', 'double', writable=False, readable=False, notnull=True, default=0),
				Field('total_vale_caderno_funcionario', 'double', writable=False, readable=False, notnull=True, default=0),
                Field('total_recebido_chegada_funcionario', 'double', writable=False, readable=False, notnull=True, default=0),

                #informações vendedor (informação que vem da tabela de vendedor)
				Field('total_vale_saida_vendedor', 'double', writable=False, readable=False, notnull=True, default=0),
				Field('total_vale_caderno_vendedor', 'double', writable=False, readable=False, notnull=True, default=0),
				Field('total_venda', 'double', writable=False, readable=False, notnull=True, default=0),
				Field('total_entradas_venda', 'double', writable=False, readable=False, notnull=True, default=0),
				Field('total_quant_fichas', 'integer', writable=False, readable=False, notnull=True, default=0),
				Field('total_comis_venda_vendedor', 'double', writable=False, readable=False, notnull=True, default=0),
                
                Field('total_venda_vista', 'double', writable=False, readable=False, notnull=True, default=0),
                auth.signature)

db.define_table('despesa',
				Field('projeto','reference projeto', label='Equipe', writable=True, readable=True),
				Field('descricao', 'string', notnull=True, default="Valor Gasto"),
				Field('valor', 'double', notnull=True, default=0),
				Field('tipo_desp','string', writable=False, readable=False,notnull=True, default=""),
				auth.signature)

db.define_table('mercadoria',
				Field('projeto','reference projeto', label='Equipe', writable=True, readable=True),
				Field('quant_pcs_enviada', 'integer', notnull=True, default=0),
				Field('descricao', 'string', notnull=True),
				Field('preco_unitario', 'double', notnull=True, default=0),
				Field('quant_pcs_retorno', 'integer', default=0, notnull=True),
				auth.signature)
db.define_table('funcionario',
				Field('projeto','reference projeto', label='Equipe'),
				Field('nome_funcionario', 'string'),
				Field('funcao', 'string'),
				Field('salario_funcionario', 'double',  notnull=True, default=1000),
				Field('vale_saida_funcionario', 'double', notnull=True, default=0),
				Field('vale_caderno_funcionario', 'double',  notnull=True, default=0),
				auth.signature)

db.define_table('vendedor',
				Field('projeto','reference projeto', label='Equipe', writable=True, readable=True),
				Field('nome_vendedor', 'string'),
				Field('vale_saida', 'double', writable=False, readable=False, notnull=True, default=0),
				Field('vale_caderno', 'double', writable=False, readable=False, notnull=True, default=0),
				Field('vendapraso', 'double', writable=False, readable=False, notnull=True, default=0),
                Field('vendavista', 'double', writable=False, readable=False, notnull=True, default=0),
				Field('entradas_venda', 'double', writable=False, readable=False, notnull=True, default=0),
				Field('quant_fichas', 'integer', writable=False, readable=False, notnull=True, default=0),
				Field('comissao_venda', 'double', writable=False, readable=False, notnull=True, default=7),
				auth.signature)


db.define_table('venda',
				Field('vendedor','reference vendedor', label='Vendedor', writable=True, readable=True),
                Field('data_venda', 'date', label="Data"),
				Field('vale_caderno', 'double', notnull=True, default=0),
				Field('quant_fichas', 'integer', notnull=True, default=0),
				Field('vendapraso', 'double', notnull=True, default=0),
				Field('entradas_venda', 'double', notnull=True, default=0),
				Field('vendavista', 'double', notnull=True, default=0),
				auth.signature)
