

def situación_pda():
    import pandas as pd
    import numpy as np
    import matplotlib.pyplot as plt


    import matplotlib.pyplot as plt
    import seaborn as sns

    #plotly
    import plotly.express as px
    from plotly.subplots import make_subplots
    import plotly.graph_objects as go

    #leo csv
    derecho_2020=pd.read_csv('/Users/rube/Documents/ironhack/proyecto final/data_limpia/derecho2020.csv')

    derecho_pivot = derecho_2020.pivot_table(index='mes', columns=['ST_TIT_FAM'], values = 'TOT_CASOS', aggfunc=sum)

    
    
    #con pyplot titular vs famaliar
    fig = make_subplots(rows=2, cols=2,subplot_titles=("titular", "familiar", 'ambos', 'total'))

    #graficas
    fig.add_trace(go.Scatter(x=derecho_pivot.index, y=derecho_pivot['Titular']), row=1,col=1)
    fig.add_trace(go.Scatter(x=derecho_pivot.index, y=derecho_pivot['beneficiario']), row=1,col=2)

    fig.add_trace(go.Scatter(x=derecho_pivot.index, y=derecho_pivot['Titular']), row=2,col=1)
    fig.add_trace(go.Scatter(x=derecho_pivot.index, y=derecho_pivot['beneficiario']), row=2,col=1)

    fig.add_trace(go.Scatter(x=derecho_pivot.index, y=(derecho_pivot['Titular']+derecho_pivot['beneficiario'])), row=2,col=2)
     

    #ejes
    fig.update_yaxes(title_text="asegurados", row=1, col=1)
    fig.update_xaxes(title_text="mes", row=1, col=1)
        
    fig.update_yaxes(title_text="asegurados", row=1, col=2)
    fig.update_xaxes(title_text="mes", row=1, col=2)

    fig.update_yaxes(title_text="asegurados", row=2, col=1)
    fig.update_xaxes(title_text="mes", row=2, col=1)

    fig.update_yaxes(title_text="asegurados", row=2, col=2)
    fig.update_xaxes(title_text="mes", row=2, col=2)

    #tamaño
    fig.update_layout(height=600, width=1000, title_text="situación derechohabientes",showlegend=False)
  
    return fig.show()
    
    
def clinicas_mas_pda():
    import pandas as pd
    import numpy as np
    import matplotlib.pyplot as plt

    import matplotlib.pyplot as plt
    import seaborn as sns

    #plotly
    import plotly.express as px
    from plotly.subplots import make_subplots
    import plotly.graph_objects as go

    #leo csv
    derecho_2020=pd.read_csv('/Users/rube/Documents/ironhack/proyecto final/data_limpia/derecho2020.csv')

    derecho_2020_UMF=derecho_2020.pivot_table(index='NOMBRE_UMF_RP', columns='mes', values='TOT_CASOS',aggfunc=sum, margins=True)

    derecho_2020_UMF_des=(derecho_2020_UMF.sort_values('All', ascending=False))

    top_UMF=((derecho_2020_UMF_des[1:11]).drop('All', axis=1)).T

    top_UMF.columns = ['UMF 007 Tlalpan', 'UMF 035 Pantitlan', 'UMF 031 Iztapalapa', 'UMF 015 ermita', 'UMF 028 Gabriel Mancera', 'UMF 041 Fortuna','UMF 009 San Pedro de los Pinos', 'UMF 020 Vallejo', 'UMF 094 Aragon', 'UMF 021 Balbuena']



    #clinicas con mas Derechohabientes
    fig = make_subplots(rows=1, cols=1)
    #graficas

    for i in range(0,8):
        fig.add_trace(go.Bar(x=top_UMF.index, y=top_UMF[top_UMF.columns[i]],name=top_UMF.columns[i],), row=1,col=1)

    #ejes
    fig.update_yaxes(title_text="derechohabientes", row=1, col=1)
    fig.update_xaxes(title_text="mes", row=1, col=1)

    #tamaño
    fig.update_layout(height=600, width=1000, title_text="clínicas con mas derechohabientes",showlegend=True)

    return fig.show()


   
def edad_sexo():
    import pandas as pd
    import numpy as np
    import matplotlib.pyplot as plt

    import matplotlib.pyplot as plt
    import seaborn as sns

    #plotly
    import plotly.express as px
    from plotly.subplots import make_subplots
    import plotly.graph_objects as go
    

    #leo csv
    derecho_2020=pd.read_csv('/Users/rube/Documents/ironhack/proyecto final/data_limpia/derecho2020.csv')

    #filtro por edad y sexo
    derecho_2020_edad= derecho_2020.pivot_table(index='mes',columns=['CVE_RANGO_EDAD','CVE_SEXO'], values = 'TOT_CASOS', aggfunc = sum)
    derecho_2020_edad = derecho_2020_edad[['(<25)','(26-40)','(40-65)',('(>65)')]]

    #lista guía para el for
    edades=np.array(derecho_2020_edad.columns)
    edades_2=edades.reshape(2,2,2)

    #derechohabientes por edad y sexo
    #truena mi chrome con estas gráficas
    fig = make_subplots(rows=2, cols=2,subplot_titles=("menor 25", "26-40", '41-65', 'mayor a 65'))

    for i in range(0,2):
        for j in range(0,2):
            #sexos
            fig.add_trace(go.Scatter(x=derecho_2020_edad.index, y=derecho_2020_edad[edades_2[i][j][0]],name='F'), row=i+1,col=j+1)
            fig.add_trace(go.Scatter(x=derecho_2020.index, y=derecho_2020_edad[edades_2[i][j][1]],name='M'), row=i+1,col=j+1)

            #ejes
            fig.update_yaxes(title_text="asegurados", row=i+1, col=j+1)
            fig.update_xaxes(title_text="mes", row=i+1, col=j+1)
            
    #tamaño
    fig.update_layout(height=600, width=1000, title_text="derechohabientes por edad y sexo")

    return fig.show()
  

    
