# Este script conterá todas as funções responsáveis pela criação e plotagem dos gráficos

import config

import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import funcoes

def compara_benchmark(nome):
    fig, ax = plt.subplots(figsize=(15,6))

    fii = funcoes.captura_dados(nome)

    (funcoes.importa_benchmark('fii').IFIX/funcoes.importa_benchmark('fii').IFIX.iloc[0]).plot()
    (funcoes.importa_benchmark('acao').IBOV/funcoes.importa_benchmark('acao').IBOV.iloc[0]).plot()
    (fii.Close/fii.Close.iloc[0]).plot()

    nomes = ['IFIX', 'IBOV', f'{nome}']

    plt.title(f'Comparativo de {nome} com benchmarks')

    plt.savefig(f'comparativo_benchmarks.png')

    plt.legend(nomes)


def annot_max(x,y, ax=None):
    #x = x.strftime('%Y-%m-%d')
    xmax = x[np.argmax(y)]
    ymax = round(y.max(),3)
    xmax2 = xmax.strftime('%d-%m-%Y')
    text= f"Valor máximo =R$ {round(ymax,2)} no dia "+xmax2
    if not ax:
        ax=plt.gca()
    bbox_props = dict(boxstyle="square,pad=0.3", fc="w", ec="k", lw=0.72)
    arrowprops=dict(arrowstyle="->",connectionstyle="angle,angleA=0,angleB=60")
    kw = dict(xycoords='data',textcoords="axes fraction",
              arrowprops=arrowprops, bbox=bbox_props, ha="right", va="top")
    ax.annotate(text, xy=(xmax, round(ymax,3)), xytext=(0.94,0.96), **kw)


def mean_std_daily_ret(dados):
    import plotly.express as px
    media_spread = round(np.mean(dados.Close),3)
    sd1_min_spread = media_spread - round(np.std(dados.Close),3)
    sd1_max_spread = media_spread + round(np.std(dados.Close),3)
    sd2_min_spread = media_spread - (2* (round(np.std(dados.Close),3)))
    sd2_max_spread = media_spread + (2* (round(np.std(dados.Close),3)))

    fig = px.line(dados, x=dados.index, y=dados['Close'])

    fig.add_hline(y=media_spread, line_width=5, line_color="green")

    fig.add_hline(y=sd1_min_spread, line_width=3, line_dash="dash", line_color="orange")
    fig.add_hline(y=sd1_max_spread, line_width=3, line_dash="dash", line_color="orange")
    fig.add_hline(y=sd2_min_spread, line_width=5, line_dash="dash", line_color="red")
    fig.add_hline(y=sd2_max_spread, line_width=5, line_dash="dash", line_color="red")

    fig.update_layout(xaxis_rangeslider_visible=False, title_text='Avaliação da média e desvios-padrão ao redor da média dos retornos diários',template = 'simple_white',width=1000,height=500)
    fig.show()

    fig.write_image("retorno_aoredormedia.png")



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



# GRÁFICO 02

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


# GRÁFICO 03
# Contém a média da razão calculada

def plota_razao_preco_media_marcado(stock, start, mm):

    #import yfinance as yf
    #import pandas as pd

    data = yf.download(stock, start = start, progress= False)

    data['media'] = data.Close.rolling(mm).mean()


    #weg['ret_dia'] = weg.Close.pct_change().rolling(30).mean()

    #weg['vol'] = weg.Close.pct_change().rolling(30).std()

    #weg['razao_ret_vol'] = weg['ret_dia']/weg['vol']

    data['razao'] = data['Close']/data['media']


    vol = data['razao']
    y = vol
    x = pd.to_datetime(vol.index)
    fig, ax = plt.subplots(figsize=(15,6))
    ax.plot(x,y)
    plt.axhline(y=np.mean(y), color='r', linestyle='-')

    titulo = f'Razão Preço/Média de Preço nos últimos 30 dias'
    plt.title(titulo)

    plt.show()