# Proyecto de análisis de datos sobre criptomonedas
![imagen](https://i.imgur.com/nFcpyY4.jpeg)


## Introducción

Las criptomonedas son monedas digitales descentralizadas que han revolucionado el mundo financiero. En este repositorio, exploraremos un análisis de datos relacionados con criptomonedas para obtener una comprensión más profunda de su comportamiento en el mercado. Además, realizaremos una exploración inicial de la calidad de los datos.

## Exploración de Datos

En la fase de exploración de datos, he llevado a cabo una serie de pasos para garantizar la integridad de los datos que utilicé en el análisis:

- **Verificación de Nulos y Duplicados:** Comprobé la presencia de valores nulos y registros duplicados en los datos. Pero no encontré valores faltantes ni duplicados en ninguna de las columnas.

| Columna | Valores Nulos | Valores Duplicados |
|---------|---------------|--------------------|
| date    | 0             |0                   |
| price   | 0             |0                   |

- **Análisis de Outliers:** También investigué la presencia de valores atípicos o outliers en los datos.

![grafico5](https://i.imgur.com/dTDyO4e.png)

- Sin embargo, es importante tener en cuenta que las criptomonedas son conocidas por su alta volatilidad. Considerar los picos como outliers podría introducir un sesgo en el análisis al perder información valiosa sobre los cambios naturales en los precios de las criptomonedas. Por lo tanto decidí no eliminar datos en esta etapa.


## Análisis y Diferencias en la Capitalización del Mercado

A continuación, presento el análisis que realicé utilizando visualizaciones que he preparado.
![grafico](https://i.imgur.com/mPpv4Qw.png)

La conclución más notables que obtuve de este análisis es la diferencia significativa en la capitalización del mercado entre Bitcoin y otras criptomonedas. Bitcoin, como la primera criptomoneda y la más ampliamente reconocida, tiene una capitalización del mercado mucho mayor en comparación con otras criptos.

## Criptomonedas Estables: Volatilidad vs. Estabilidad

### ¿Qué es una Criptomoneda Estable?

Una criptomoneda estable es una forma de criptomoneda diseñada para mantener un valor constante en comparación con una referencia, como una moneda fiduciaria (por ejemplo, el dólar estadounidense) u otros activos estables. A diferencia de las criptomonedas más volátiles como Bitcoin y Ethereum, las criptomonedas estables están diseñadas para minimizar las fluctuaciones en su valor y ofrecer una mayor estabilidad a los usuarios.


### Comparación grafica entre Criptomoneda Estable y Volátil

![grafico2](https://i.imgur.com/zLUfIj7.png)

Aquí se puede observar la diferencia en la volatilidad entre una criptomoneda estable (en celeste) y una criptomoneda volátil (en azul).

## Criptomonedas Destacadas: Últimos 15 Días

En esta sección, mostraré dos criptomonedas que experimentaron los mayores cambios porcentuales en los últimos 15 días, una con un cambio positivo y otra con un cambio negativo. También daré un ejemplo de cuánto hubieras ganado o perdido si hubieras invertido en estas criptomonedas.

### Cambio Positivo: Taraxa

Taraxa es una criptomoneda que ha experimentado un cambio porcentual positivo en los últimos 15 días. A continuación, se detallan los resultados:

- **Inversión inicial:** $1000
- **Cambio en inversión por diferencia porcentual:** $8933.16

![grafico3](https://i.imgur.com/ZZPc5R4.png)

### Cambio Negativo: Dust Protocol

Por otro lado, Dust Protocol es una criptomoneda que ha experimentado un cambio porcentual negativo en los últimos 15 días. A continuación, se detallan los resultados:

- **Inversión inicial:** $1000
- **Cambio en inversión por diferencia porcentual:** $-400.47

![grafico4](https://i.imgur.com/orExMzq.png)

Estos ejemplos resaltan la volatilidad en el mercado de las criptomonedas, donde es posible obtener ganancias significativas o sufrir pérdidas considerables en un corto período de tiempo.

## Conclusión
Cómo conclusión, al explorar el mundo de las criptomonedas, es esencial adoptar un enfoque cauteloso y analítico. A pesar de las emocionantes posibilidades que ofrecen en términos de inversiones y transacciones, las criptomonedas también conllevan una alta volatilidad y riesgos considerables. El análisis de datos presentado subraya la importancia de una evaluación minuciosa de las estrategias de inversión y la toma de decisiones informadas basadas en un conocimiento del mercado. Mantener un equilibrio y una actitud prudente resulta fundamental para aprovechar las oportunidades y atenuar los riesgos asociados a las criptomonedas.

### Tecnologías y Herramientas Utilizadas

Este proyecto de análisis de datos sobre criptomonedas fue desarrollado utilizando estas tecnologías y herramientas:

- **Python:** El lenguaje de programación principal utilizado para la manipulación y análisis de datos.
- **Pandas:** Una biblioteca de Python utilizada para el manejo y análisis de datos estructurados.
- **PyCoingecko:** Una API de Python que proporciona acceso a datos en tiempo real y históricos sobre criptomonedas.
- **NumPy:** Una biblioteca de Python que proporciona soporte para operaciones matemáticas y numéricas.
- **Streamlit:** Una herramienta para la creación de aplicaciones web interactivas con código Python.
- **Plotly:** Una biblioteca de visualización utilizada para crear gráficos interactivos y atractivos.

Estas tecnologías y herramientas desempeñaron un papel crucial en el análisis y la presentación de los resultados obtenidos en este proyecto.
