import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from datetime import timedelta
import numpy as np
#
def leer_csv(nombre):
    df = pd.read_csv(f'datos_csv/{nombre}_coin.csv')
    return df

# Monedas a utilizar
bitcoin = leer_csv('bitcoin')
ethereum = leer_csv('ethereum')
tether = leer_csv('tether')
bnb = leer_csv('binancecoin')
xrp = leer_csv('ripple')
usd_coin = leer_csv('usd-coin')
dai = leer_csv('dai')
polygon = leer_csv('matic-network')
grove = leer_csv('grove')
dogecola = leer_csv('dogecola')#asdasd
wall_street_baby = leer_csv('wall-street-baby')
cryn = leer_csv('cryn')
taraxa = leer_csv('taraxa')
taraxa['date'] = pd.to_datetime(taraxa['date'])
taraxa['date'] = taraxa['date'].dt.date
taraxa = taraxa.drop_duplicates(subset=['date'])
dust_protocol = leer_csv('dust-protocol')
dust_protocol['date'] = pd.to_datetime(taraxa['date'])
dust_protocol['date'] = dust_protocol['date'].dt.date
dust_protocol = dust_protocol.drop_duplicates(subset=['date'])


bitcoin['date'] = pd.to_datetime(bitcoin['date'], format='%Y-%m-%d')
ethereum['date'] = pd.to_datetime(ethereum['date'], format='%Y-%m-%d')
tether['date'] = pd.to_datetime(tether['date'], format='%Y-%m-%d')
bnb['date'] = pd.to_datetime(bnb['date'], format='%Y-%m-%d')
xrp['date'] = pd.to_datetime(xrp['date'], format='%Y-%m-%d')
usd_coin['date'] = pd.to_datetime(usd_coin['date'], format='%Y-%m-%d')
dai['date'] = pd.to_datetime(dai['date'], format='%Y-%m-%d')
polygon['date'] = pd.to_datetime(polygon['date'], format='%Y-%m-%d')
grove['date'] = pd.to_datetime(grove['date'], format='%Y-%m-%d')
dogecola['date'] = pd.to_datetime(dogecola['date'], format='%Y-%m-%d')
wall_street_baby['date'] = pd.to_datetime(wall_street_baby['date'], format='%Y-%m-%d')
cryn['date'] = pd.to_datetime(cryn['date'], format='%Y-%m-%d')
taraxa['date'] = pd.to_datetime(taraxa['date'], format='%Y-%m-%d')
dust_protocol['date'] = pd.to_datetime(dust_protocol['date'], format='%Y-%m-%d')

st.title('Visualización de Criptomonedas')

# Botón Home
if st.sidebar.button('Home'):
    st.text("")
    
#-----Top criptomonedas según capitalización del mercado
capitalizacion_mercado = st.button('Top criptomonedas mas capitalizadas según el mercado')
if capitalizacion_mercado:
    #-----Grafico de lineas
    st.write('Estas son las 5 criptomonedas con mayor capitalización de mercado. Esto quiere decir que son las que mayor valor tienen y son las mas reconocidas en el mercado.')
    criptomonedas = [bitcoin, ethereum, tether, bnb, xrp]
    nombres_criptomonedas = ['Bitcoin', 'Ethereum', 'Tether', 'Binance Coin', 'XRP']
    
    fig_line = go.Figure()
    
    for i, cripto in enumerate(criptomonedas):
        fig_line.add_trace(go.Scatter(x=cripto['date'], y=cripto['price'], mode='lines', name=nombres_criptomonedas[i]))
    
    fig_line.update_layout(xaxis_title='Fecha', yaxis_title='Precio', title='Comparación de precios')
    fig_line.update_layout(legend=dict(orientation='h', yanchor='bottom', y=1.02, xanchor='right', x=1))

    st.plotly_chart(fig_line)
    st.write('En este gráfico, notamos que Bitcoin mantiene un valor significativamente alto en comparación con las otras criptomonedas, destacando su posición predominante. Ethereum también es notable, aunque se encuentra a distancia de Bitcoin en términos de valor.')

    #-----Grafico de Torta
    coin_names = ['Bitcoin', 'Ethereum', 'Tether', 'Binance Coin', 'XRP']
    coin_values = [bitcoin['price'].iloc[-1], ethereum['price'].iloc[-1], tether['price'].iloc[-1], bnb['price'].iloc[-1], xrp['price'].iloc[-1]]
    
    otros_value = sum(coin_values[2:])
    coin_names = ['Bitcoin', 'Ethereum', 'Otros']
    coin_values = [coin_values[0], coin_values[1], otros_value]
    
    fig_pie = px.pie(names=coin_names, values=coin_values, title='Precios actuales de diferentes criptos', color=coin_names, color_discrete_sequence=['#FF9900', '#8A2BE2', '#00FFFF'])
    
    st.plotly_chart(fig_pie)
    st.write('El gráfico presentado se aprecia que Bitcoin lidera en capitalización de mercado, seguido por Ethereum con una diferencia considerable. Las demás criptomonedas, como Tether, Binance Coin y XRP, tienen una menor participación.')
    #st.write('En resumen, estos gráficos reflejan la dominancia de Bitcoin y Ethereum en el mercado de criptomonedas, con otras monedas teniendo un impacto menor en la capitalización total.')
    
    #-----Grafico cambio porcentual
    st.write("## Cambio Porcentual")
    nombres_criptomonedas = ['Bitcoin', 'Ethereum', 'Tether', 'Binance Coin', 'XRP']
    
    for rango_seleccionado in ['Ultimos 7 días', 'Ultimos 30 días', 'Ultimo año']:
        if rango_seleccionado == 'Ultimos 7 días':
            fecha_inicio = bitcoin['date'].iloc[-1] - timedelta(days=7)
        elif rango_seleccionado == 'Ultimos 30 días':
            fecha_inicio = bitcoin['date'].iloc[-1] - timedelta(days=30)
        elif rango_seleccionado == 'Ultimo año':
            fecha_inicio = bitcoin['date'].iloc[-1] - timedelta(days=365)
        
        fig_cambio = go.Figure()
        fecha_fin = bitcoin['date'].iloc[-1]

        for i, cripto in enumerate([bitcoin, ethereum, tether, bnb, xrp]):
            cripto_filtrada = cripto[(cripto['date'] >= fecha_inicio) & (cripto['date'] <= fecha_fin)]
            cambio_porcentual = ((cripto_filtrada['price'].iloc[-1] - cripto_filtrada['price'].iloc[0]) / cripto_filtrada['price'].iloc[0]) * 100
            fig_cambio.add_trace(go.Bar(x=[nombres_criptomonedas[i]], y=[cambio_porcentual], name=nombres_criptomonedas[i]))

        fig_cambio.update_layout(title=f'{rango_seleccionado}')

        st.plotly_chart(fig_cambio)
        
#-----Monedas estables
estables = st.button('Top criptomonedas mas estables')
if estables:
    st.write('Una moneda estable en el mundo de las criptomonedas es como una versión digital de dinero real. A diferencia de otras criptomonedas que pueden cambiar mucho de valor en poco tiempo, una moneda estable trata de mantener un valor constante, similar al dinero que usamos en la vida diaria. Esto la hace más adecuada para transacciones y ahorro sin preocuparse tanto por los cambios bruscos en su valor.')
    #-----Grafico de lineas
    criptomonedas = [tether, usd_coin, dai]
    nombres_criptomonedas = ['Tether', 'USD Coin', 'Dai']
    
    fig_line = go.Figure()
    
    for i, cripto in enumerate(criptomonedas):
        fig_line.add_trace(go.Scatter(x=cripto['date'], y=cripto['price'], mode='lines', name=nombres_criptomonedas[i]))
    
    fig_line.update_layout(xaxis_title='Fecha', yaxis_title='Precio', title='Comparación entre monedas estables')
    fig_line.update_layout(legend=dict(orientation='h', yanchor='bottom', y=1.02, xanchor='right', x=1))

    st.plotly_chart(fig_line)
    st.write('Estas criptomonedas tienen una cotización bastante estable, pero es importante resaltar ciertos picos de baja que se han experimentado en su historial. Estos picos de baja fueron causados por situaciones como el cierre de bancos que están vinculados a estas criptomonedas. Sin embargo, con el paso del tiempo, el precio de estas volvió a estabilizarse.')
    #-----Grafico de lineas comparativo
    criptos = [tether, polygon]
    nombres_criptos = ['Tether', 'Polygon']
    
    fig_line = go.Figure()
    
    for i, cripto in enumerate(criptos):
        fig_line.add_trace(go.Scatter(x=cripto['date'], y=cripto['price'], mode='lines', name=nombres_criptos[i]))
    
    fig_line.update_layout(xaxis_title='Fecha', yaxis_title='Precio', title='Comparación entre una moneda estable y una volatil')
    fig_line.update_layout(legend=dict(orientation='h', yanchor='bottom', y=1.02, xanchor='right', x=1))

    st.plotly_chart(fig_line)
    #-----Grafico de volatilidad
    fig_volatility_bar = go.Figure()

    for i, cripto in enumerate(criptos):
        daily_returns = [((price - cripto['price'][j - 1]) / cripto['price'][j - 1]) * 100
                         for j, price in enumerate(cripto['price']) if j > 0]

        volatility = np.std(daily_returns)
        fig_volatility_bar.add_trace(go.Bar(x=[nombres_criptos[i]], y=[volatility], name=nombres_criptos[i]))

    fig_volatility_bar.update_layout(xaxis_title='Criptomoneda', yaxis_title='Volatilidad', title='Comparación de Volatilidad')

    st.plotly_chart(fig_volatility_bar)
    st.write('Al comparar estas dos criptomonedas, una de las cuales es una criptomoneda estable respaldada por el precio del dólar y la otra que presenta una mayor volatilidad, se puede observar claramente que Tether representa una inversión más segura en comparación con Polygon. La estabilidad hace de Tether una opción más confiable en contraste con la fluctuación de Polygon')
    
    
# -----Mejores y peores
mejores_peores = st.button('Mejor y peor de los últimos 15 días')
if mejores_peores:
    st.write('Las criptomonedas que experimentaron los mayores o menores cambios porcentuales en el último período resaltan la oportunidad de obtener ganancias significativas al comprar y vender en momentos estratégicos. Sin embargo, también subrayan el riesgo de perder toda tu inversión si no logras identificar el momento adecuado para salir de una criptomoneda.')
    # -----Grafico de lineas mejores
    criptomonedas_mejores = [taraxa]
    nombres_criptomonedas_mejores = ['Taraxa']
    
    fig_line = go.Figure()

    for i, cripto in enumerate(criptomonedas_mejores):
        fig_line.add_trace(go.Scatter(x=cripto['date'], y=cripto['price'], mode='lines', name=nombres_criptomonedas_mejores[i]))

    fig_line.update_layout(xaxis_title='Fecha', yaxis_title='Precio', title='Mejor de los últimos 15 días')
    fig_line.update_layout(legend=dict(orientation='h', yanchor='bottom', y=1.02, xanchor='right', x=1))
    
    st.plotly_chart(fig_line)

    # -----Análisis de las monedas
    initial_investment = 1000

    for i, cripto in enumerate(criptomonedas_mejores):
        max_price = max(cripto['price'])
        min_price = min(cripto['price'])

        price_difference_percent = ((max_price - min_price) / min_price) * 100  # Diferencia porcentual entre precio máximo y mínimo
        investment_change = (price_difference_percent / 100) * initial_investment  # Cambio en la inversión en relación con la diferencia porcentual

        if len(cripto['price']) > 0:
            final_price = cripto['price'].iloc[-1]
            investment_gain = final_price - initial_investment
            st.write(f"Para {nombres_criptomonedas_mejores[i]}:")
            st.write(f'Inversión inicial: ${initial_investment}')
            st.write(f"Cambio en inversión por diferencia porcentual: ${investment_change:.2f}")
        else:
            st.write(f"No hay datos de precios disponibles para {nombres_criptomonedas_mejores[i]}")
            
            
    #-----Grafico de lineas comparativo entre las peores monedas del año
    # -----Grafico de lineas peores
    criptomonedas_peores = [dust_protocol]
    nombres_criptomonedas_peores = ['Dust Protocol']

    fig_line = go.Figure()

    for i, cripto in enumerate(criptomonedas_peores):
        fig_line.add_trace(go.Scatter(x=cripto['date'], y=cripto['price'], mode='lines', name=nombres_criptomonedas_peores[i]))

    fig_line.update_layout(xaxis_title='Fecha', yaxis_title='Precio', title='Peor de los últimos 15 días')
    fig_line.update_layout(legend=dict(orientation='h', yanchor='bottom', y=1.02, xanchor='right', x=1))

    st.plotly_chart(fig_line)

    # -----Análisis de las peores monedas
    initial_investment = 1000

    for i, cripto in enumerate(criptomonedas_peores):
        price_values = cripto['price']
        
        if len(price_values) > 0:
            initial_price = price_values.iloc[0]
            final_price = price_values.iloc[-1]
            
            price_difference_percent = ((final_price - initial_price) / initial_price) * 100
            investment_change = (price_difference_percent / 100) * initial_investment
            
            st.write(f"Para {nombres_criptomonedas_peores[i]}:")
            st.write(f'Inversión inicial: ${initial_investment}')
            st.write(f"Cambio en inversión por diferencia porcentual: ${investment_change:.2f}")
        else:
            st.write(f"No hay datos de precios disponibles para {nombres_criptomonedas_peores[i]}")
