def valor_actual_neto(flujos_caja, r):
    """ calcula el VAN de unos flujos_caja descontados a r """
    
    resultado = 0
    
    for t, flujo in enumerate(flujos_caja):
        resultado += flujo / (1+r)**t
	
    return resultado