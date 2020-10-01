

def trabajo_eventual_permanente():
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
    p_2020= pd.read_csv('/Users/rube/Documents/ironhack/proyecto final/data_limpia/p_2020.csv')

    p_meses=p_2020.groupby(['mes']).agg({'asegurados':'sum','teu_sal':'sum', 'tpu_sal':'sum',})


    #trabajo eventual vs permanente
    #con plotly
    fig = make_subplots(rows=1, cols=2,subplot_titles=("trabajo eventual", "trabajo permanente"))

    #graficas
    fig.add_trace(go.Scatter( x=p_meses.index, y=p_meses["teu_sal"],name='teu_sal'), row=1,col=1)
    fig.add_trace(go.Scatter( x=p_meses.index, y=p_meses["tpu_sal"]), row=1,col=2)

    #eje y
    fig.update_yaxes(title_text="asegurados", row=1, col=1)
    fig.update_yaxes(title_text="asegurados", row=1, col=2)

    #ejex
    fig.update_xaxes(title_text="mes",range=[0,9], row=1, col=1)
    fig.update_xaxes(title_text="mes", row=1, col=2)
                 
    #titulo
    fig.update_layout(height=600, width=1000, title_text="trabajo eventual y permanente",showlegend=False)
    
    return fig.show()
  

def asegurados_tamano_patron():
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
    p_2020= pd.read_csv('/Users/rube/Documents/ironhack/proyecto final/data_limpia/p_2020.csv')

    #tamaño patron
    p_pivot_2020=p_2020.pivot_table(index='mes', columns='tamano_patron', values='asegurados', aggfunc=sum)
    #ordeno columnas
    p_pivot_2020= p_pivot_2020[['S1-S2(<5)','S3(<50)','S4-S5(51-500)','>S6(>500)']]



    #con plotly
    fig = make_subplots(rows=2, cols=2,subplot_titles=("menor a 5 trabajadores", "de 5 a 50 trabajadores",
                                                   'de 51 a 500 trabajadores','mayor a 500 trabajadores'))

    #graficas
    fig.add_trace(go.Scatter( x=p_pivot_2020.index, y=p_pivot_2020['S1-S2(<5)'],name='S1-S2(<5)'), row=1,col=1)
    fig.add_trace(go.Scatter( x=p_pivot_2020.index, y=p_pivot_2020['S3(<50)']), row=1,col=2)
    fig.add_trace(go.Scatter( x=p_pivot_2020.index, y=p_pivot_2020['S4-S5(51-500)']), row=2,col=1)
    fig.add_trace(go.Scatter( x=p_pivot_2020.index, y=p_pivot_2020['>S6(>500)']), row=2,col=2)
           
    #eje y
    fig.update_yaxes(title_text="asegurados", row=1, col=1)
    fig.update_yaxes(title_text="asegurados", row=1, col=2)
    fig.update_yaxes(title_text="asegurados", row=2, col=1)
    fig.update_yaxes(title_text="asegurados", row=2, col=2)  
              
    #ejex
    fig.update_xaxes(title_text="mes",range=[0,9], row=1, col=1)
    fig.update_xaxes(title_text="mes", row=1, col=2)
    fig.update_xaxes(title_text="mes", row=2, col=1)
    fig.update_xaxes(title_text="mes", row=2, col=2)             
                 
    #titulo
    fig.update_layout(height=800, width=1000, title_text="asegurados por tamaño de patron",showlegend=False)

    return fig.show()

def asegurados_sector():
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
    p_2020= pd.read_csv('/Users/rube/Documents/ironhack/proyecto final/data_limpia/p_2020.csv')


    #por sector economico
    p_ec_pivot_2020=p_2020.pivot_table(index='mes', columns='sector_economico_1', values='asegurados', aggfunc=sum)

    sector =list(p_ec_pivot_2020.columns)
    #lo cambio a array para que funcione mi doble for
    sector_array = (np.array(sector)).reshape(3,3)

    #con plotlib
    fig = make_subplots(rows=3, cols=3,subplot_titles=(sector))

    for i in range(0,3):
        for j in range(0,3):
            #graficas
            fig.add_trace(go.Scatter(x=p_ec_pivot_2020.index, y=p_ec_pivot_2020[sector_array[i,j]]), row=i+1,col=j+1)
        
            #ejes
            fig.update_yaxes(title_text="asegurados", row=i+1, col=j+1)
            fig.update_xaxes(title_text="mes", row=i+1, col=j+1)
        
    fig.update_layout(height=800, width=1050, title_text="asegurador por sector",showlegend=False)
    return fig.show()

def asegurados_salarios_minimos():
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
    p_2020= pd.read_csv('/Users/rube/Documents/ironhack/proyecto final/data_limpia/p_2020.csv')


    
    #por salarios minimos
    p_sal_pivot_2020=p_2020.pivot_table(index='mes', columns=['rango_salarial'], values='asegurados', aggfunc=sum)
    p_sal_pivot_2020= p_sal_pivot_2020[['menor 6','6 a 12', 'mayor a 12']]


    #con plotlib
    fig = make_subplots(rows=2, cols=2,subplot_titles=('menor 6', '6 a 12', 'mayor a 12', 'juntos'))

    #graficas
    fig.add_trace(go.Scatter(x=p_sal_pivot_2020.index, y=p_sal_pivot_2020['menor 6']), row=1,col=1)
    fig.add_trace(go.Scatter(x=p_sal_pivot_2020.index, y=p_sal_pivot_2020['6 a 12']), row=1,col=2)
    fig.add_trace(go.Scatter(x=p_sal_pivot_2020.index, y=p_sal_pivot_2020['mayor a 12']), row=2,col=1)

    fig.add_trace(go.Scatter(x=p_sal_pivot_2020.index, y=p_sal_pivot_2020['menor 6']), row=2,col=2)
    fig.add_trace(go.Scatter(x=p_sal_pivot_2020.index, y=p_sal_pivot_2020['6 a 12']), row=2,col=2)
    fig.add_trace(go.Scatter(x=p_sal_pivot_2020.index, y=p_sal_pivot_2020['mayor a 12']), row=2,col=2)      

    #ejes
    fig.update_yaxes(title_text="asegurados", row=1, col=1)
    fig.update_xaxes(title_text="mes", row=1, col=1)
        
    fig.update_yaxes(title_text="asegurados", row=1, col=2)
    fig.update_xaxes(title_text="mes", row=1, col=2)

    fig.update_yaxes(title_text="asegurados", row=2, col=1)
    fig.update_xaxes(title_text="mes", row=2, col=1)

    fig.update_yaxes(title_text="asegurados", row=2, col=2)
    fig.update_xaxes(title_text="mes", row=2, col=2)
        
    fig.update_layout(height=600, width=1000, title_text="asegurados por salarios minimos",showlegend=False)
    return fig.show()



def masa_salarial_sector():

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
    p_2020= pd.read_csv('/Users/rube/Documents/ironhack/proyecto final/data_limpia/p_2020.csv')


    #Masa salarial por sector
    p_2020_salarios =p_2020.pivot_table(index = 'mes', columns='sector_economico_1', values='masa_sal_ta', aggfunc='sum')

    sector = list(p_2020_salarios.columns)
    sector_array = (np.array(sector)).reshape(3,3)


    #con plotlib
    fig = make_subplots(rows=3, cols=3,subplot_titles=(sector))

    for i in range(0,3):
        for j in range(0,3):
            #graficas
            fig.add_trace(go.Scatter(x=p_2020_salarios.index, y=p_2020_salarios[sector_array[i,j]]), row=i+1,col=j+1)
        
            #ejes
            fig.update_yaxes(title_text="masa salarial ($)", row=i+1, col=j+1)
            fig.update_xaxes(title_text="mes", row=i+1, col=j+1)
        
    fig.update_layout(height=800, width=1050, title_text="masa salarial por sector en MXN",showlegend=False)
    return fig.show() 

def masa_salarial_tamano_patron():

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
    p_2020= pd.read_csv('/Users/rube/Documents/ironhack/proyecto final/data_limpia/p_2020.csv')

    
    #masa salarial por tamaño de patron

    p_2020_sal_pat =p_2020.pivot_table(index = 'mes', columns='tamano_patron', values='masa_sal_ta', aggfunc='sum')
    p_2020_sal_pat= p_2020_sal_pat[['S1-S2(<5)','S3(<50)','S4-S5(51-500)','>S6(>500)']]


    fig = make_subplots(rows=2, cols=2,subplot_titles=("menor a 5 trabajadores", "de 5 a 50 trabajadores",'de 51 a 500 trabajadores','mayor a 500 trabajadores'))

    #graficas
    fig.add_trace(go.Scatter( x=p_2020_sal_pat.index, y=p_2020_sal_pat['S1-S2(<5)'],name='S1-S2(<5)'), row=1,col=1)
    fig.add_trace(go.Scatter( x=p_2020_sal_pat.index, y=p_2020_sal_pat['S3(<50)']), row=1,col=2)
    fig.add_trace(go.Scatter( x=p_2020_sal_pat.index, y=p_2020_sal_pat['S4-S5(51-500)']), row=2,col=1)
    fig.add_trace(go.Scatter( x=p_2020_sal_pat.index, y=p_2020_sal_pat['>S6(>500)']), row=2,col=2)

              
    #eje y
    fig.update_yaxes(title_text="masa salarial ($)", row=1, col=1)
    fig.update_yaxes(title_text="masa salarial ($)", row=1, col=2)
    fig.update_yaxes(title_text="masa salarial ($)", row=2, col=1)
    fig.update_yaxes(title_text="masa salarial ($)", row=2, col=2)  
              
    #ejex
    fig.update_xaxes(title_text="mes",range=[0,9], row=1, col=1)
    fig.update_xaxes(title_text="mes", row=1, col=2)
    fig.update_xaxes(title_text="mes", row=2, col=1)
    fig.update_xaxes(title_text="mes", row=2, col=2)             
                 
    #titulo
    fig.update_layout(height=800, width=1000, title_text="masa salarial por tamaño de patron",showlegend=False)
    return fig.show()
    

    



    

    
