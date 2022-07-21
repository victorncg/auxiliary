import yfinance as yf

def soma(f, x):
    a = f + x
    return a


def importa_benchmark(tipo):
    if tipo == 'fii':
        fii = captura_dados(nome_fii)

        search_results = investpy.search_quotes(text = 'IFIX', products= ['indices'], countries= ['brazil'], n_results = 50)

        for search_result in search_results[0:1]:
            search_result

        benchmark = search_result.retrieve_historical_data(from_date = '01/01/2014', to_date = '04/07/2022')

    if tipo == 'acao':
        benchmark = yf.download("^BVSP",start = '2019-01-01',progress=False)

    else:
        print('ativo nao reconhecido')
        
    return benchmark
    
    

