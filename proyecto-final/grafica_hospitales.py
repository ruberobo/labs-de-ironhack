
def hospitales(url):
    import pandas as pd
    import numpy as np
    import matplotlib.pyplot as plt

    import numpy as np
    import pandas as pd
    import matplotlib.pyplot as plt
    import seaborn as sns

    #plotly
    import plotly.express as px
    from plotly.subplots import make_subplots
    import plotly.graph_objects as go

    #leo csv
    cdmx= pd.read_csv(url)

    #filtro por imss
    imsscdmx = cdmx[cdmx['LUGAR DE TRASLADO'].apply(lambda x:x.startswith('IMSS'))]

    #paso a fecha el indice
    imsscdmx['Fecha']= pd.to_datetime(imsscdmx['Fecha'])
    imsscdmx.index = pd.DatetimeIndex(imsscdmx['Fecha'])
    imsscdmx.drop(['Fecha'], axis=1, inplace=True)


    #limpio columna hospitales
    def limpio_h(x):
        y= x.replace('IMSS ','')
        z= y.replace('.','')
        return z.strip()


    imsscdmx['LUGAR DE TRASLADO']= imsscdmx['LUGAR DE TRASLADO'].apply(limpio_h)

    top10_hospitales=imsscdmx['LUGAR DE TRASLADO'].value_counts().head(10)

    #por hospital
    imss_dia=pd.get_dummies(imsscdmx['LUGAR DE TRASLADO']).groupby(imsscdmx.index).agg(sum)
    imss_mes=pd.get_dummies(imsscdmx['LUGAR DE TRASLADO']).groupby(imsscdmx.index.month).agg(sum)

    imss_dia['Total']=imss_dia.sum(axis=1)

    #hospitales con mas pacientes asociados a covid
    fig = make_subplots(rows=2, cols=1,subplot_titles=("por mes","por día"))
    #graficas
    for i in range(0,10):
        #por mes
        fig.add_trace(go.Bar(x=imss_mes.index, y=imss_mes[top10_hospitales.index[i]],name=top10_hospitales.index[i],), row=1,col=1)

    #por día
    fig.add_trace(go.Scatter(x=imss_dia.index, y=imss_dia['Total'],name='Total',), row=2,col=1)

    #ejes
    fig.update_yaxes(title_text="hospitalizados", row=1, col=1)
    fig.update_xaxes(title_text="mes", row=1, col=1)
    fig.update_yaxes(title_text="hospitalizados", row=2, col=1)
    fig.update_xaxes(title_text="día", row=2, col=1)


    #tamaño
    fig.update_layout(height=800, width=1000,showlegend=True,
                 legend=dict(orientation="h",yanchor="bottom",y=1.02,xanchor="right",x=1))

    
    
    return fig.show()
    
    
  
   
