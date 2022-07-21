# READ ME
# Este código contém as funções que são utilizadas na criação do relatório

import yfinance as yf
import pandas as pd

# Retorna a data de criação do relatório
def def_data():
    import datetime
    today = datetime.date.today()

    des_data = str(today.strftime('Relatório criado no dia %d de %b de %Y'))

    return des_data


def razao_preco_media(stock, start, mm):
    
    #import yfinance as yf
    #import pandas as pd

    data = yf.download(stock, start = start)

    data['media'] = data.Close.rolling(mm).mean()
    

    #weg['ret_dia'] = weg.Close.pct_change().rolling(30).mean()

    #weg['vol'] = weg.Close.pct_change().rolling(30).std()

    #weg['razao_ret_vol'] = weg['ret_dia']/weg['vol']

    data['razao'] = data['Close']/data['media']

    return data['razao']


def plota_razao_preco_media(stock, start, mm):

    #import yfinance as yf
    #import pandas as pd

    data = yf.download(stock, start = start, progress= False)

    data['media'] = data.Close.rolling(mm).mean()


    #weg['ret_dia'] = weg.Close.pct_change().rolling(30).mean()

    #weg['vol'] = weg.Close.pct_change().rolling(30).std()

    #weg['razao_ret_vol'] = weg['ret_dia']/weg['vol']

    data['razao'] = data['Close']/data['media']

    return data['razao'].plot();