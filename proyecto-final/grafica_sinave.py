

def sector_salud(url):
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
    sinave= pd.read_csv(url)

    fig= px.pie(values = sinave['sector'].value_counts().head(10), names= (sinave['sector'].value_counts().head(10)).index)
    
    
    return fig.show()
    
    
  
   
def casos_mes(url):
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
    sinave= pd.read_csv(url)

    sinave_imss = sinave[sinave['sector'].apply(lambda x: x.startswith('IMSS'))]
    sinave_imss

    
    sinave_imss.drop(['origen', 'sector', 'cve_entidad_unidad_medica','municipio_residencia',
       'entidad_unidad_medica', 'delegacion_unidad_medica', 'fecha_de_registro','entidad_residencia',
                 'localidad_residencia','clave_localidad_residencia','evolucion_caso',
       'fecha_defuncion', 'semana_defuncion','nacionalidad','es_indigena',
       'habla_lengua_indigena','fecha_inicio_sintomas','antiviral',
       'fecha_inicio_tratamiento_antiviral','contacto_aves', 'contacto_cerdos', 'contacto_animales',
                 'fecha_estimada_vacunacion', 'toma_muestra', 'laboratorio',
       'folio_laboratorio','es_migrante',
       'pais_nacionalidad', 'pais_origen', 'fecha_ingreso_pais', 'puerperio',
       'dias_puerperio', 'antipireticos', 'unidad_cuidados_intensivos',
       'linaje_influenza_tipo_b', 'viaje_1', 'viaje_2', 'viaje_3', 'viaje_4',
       'viaje_5', 'rango_de_edad'], axis=1, inplace=True)

    sinave_imss2= sinave_imss.copy()
    sinave_imss2.drop(['recibio_tratamiento_antibiotico', 'unidad_medica','contacto_infeccion_viral','intubado'], axis=1, inplace=True)

    #lleno nulos con ceros
    sinave_imss2.fillna(0, inplace=True)

    #cambio formato a fecha
    #importo
    import locale
    locale.setlocale(locale.LC_ALL,'es_ES.UTF-8')
    from datetime import datetime as dt

    #asigno índice
    sinave_imss2['fecha_ingreso']= pd.to_datetime(sinave_imss2['fecha_ingreso'])
    sinave_imss2.index =sinave_imss2['fecha_ingreso']

    sinave_imss3=sinave_imss2.sort_index()

    #lleno con cero y uno
    comorbolidades = ['diagnostico_clinico_neumonia','esta_emabarazada',
    'fiebre', 'tos', 'odinofagia',
       'disnea', 'irritabilidad', 'diarrea', 'dolor_toracico', 'calofrios',
       'cefalea', 'mialgias', 'artralgias', 'ataque_al_estado_general',
       'rinorrea', 'polipnea', 'vomito', 'dolor_abdominal', 'conjuntivitis',
       'cianosis', 'inicio_subito_sintomas', 'diabetes', 'epoc', 'asma',
       'inmunosupresivo', 'hipertension', 'VIH_SIDA', 'otra_condicion',
       'enfermedad_cardiaca', 'obesidad', 'insuficiencia_renal_cronica',
       'tabaquismo', 'recibio_tratamiento', 'recibio_tratamiento_antiviral',
       'vacunado']

    for i in comorbolidades:
        sinave_imss3[i]=np.where(sinave_imss3[i]=='SI',1,0)

    sinave_imss3['Masculino']=np.where(sinave_imss3['sexo']=='Masculino',1,0)
    sinave_imss3['Femenino'] = np.where(sinave_imss3['sexo']=='Femenino',1,0)
    sinave_imss3['Ambulatorio']= np.where(sinave_imss3['tipo_paciente']=='AMBULATORIO',1,0)
    sinave_imss3['HOSPITALIZADO']=np.where(sinave_imss3['tipo_paciente']=='HOSPITALIZADO',1,0)
    sinave_imss3['tiene_covid19']=np.where(sinave_imss3['resultado_definitivo']=='SARS-CoV-2',1,0)
    sinave_imss3['negativo_covid19']=np.where(sinave_imss3['resultado_definitivo']!='SARS-CoV-2',1,0)

    #funcion para saber si es urgencia
    def urgencias(x):
        import re
        return bool(re.search('URGENCIA',x))


    import re
    sinave_imss3['urgencia']=np.where(sinave_imss3['servicio_ingreso'].apply(urgencias),1,0)

    #borrar fecha que no es indice, sexo, tipo de paciente, diagnostico probable y resultado definitivo
    sinave_imss4=sinave_imss3.copy()

    sinave_imss4.drop(['sexo','tipo_paciente', 'resultado_definitivo', 'diagnostico_probable', 'fecha_ingreso',
                   'servicio_ingreso', 'ocupacion'],
                 axis =1, inplace=True)

    #agrupo por fecha
    sinave_imss5= sinave_imss4.groupby(sinave_imss4.index).agg('sum')

    #borro columnas categoricas
    sinave_imss5.drop(['cve_entidad_residencia', 'cve_municipio_residencia','edad','meses_embarazo'],axis =1, inplace=True)

    #agrego mes
    import datetime
    sinave_imss5['mes']=sinave_imss5.index.month


    sinave_mes=sinave_imss5.groupby('mes').agg({'tiene_covid19':'sum','negativo_covid19':'sum',
                                 'HOSPITALIZADO':'sum','Ambulatorio':'sum'})

    
    #grafica
    fig = make_subplots(rows=1, cols=2,subplot_titles=('positivos vs negativos', 'hospitalización'))

    #agrego graficas
    fig.add_trace(go.Scatter( x=sinave_mes.index, y=sinave_mes['tiene_covid19'],name='positivo'), row=1,col=1)
    fig.add_trace(go.Scatter( x=sinave_mes.index, y=sinave_mes['negativo_covid19'], name='negativo'), row=1,col=1)

    fig.add_trace(go.Scatter( x=sinave_mes.index, y=sinave_mes['HOSPITALIZADO'],name='hospitalizado'), row=1,col=2)
    fig.add_trace(go.Scatter( x=sinave_mes.index, y=sinave_mes['Ambulatorio'], name='ambulatorio'), row=1,col=2)

    #ejes
    fig.update_yaxes(title_text="pacientes", row=1, col=1)
    fig.update_yaxes(title_text="pacientes", row=1, col=2)
    fig.update_xaxes(title_text="mes", row=1, col=2)
    fig.update_xaxes(title_text="mes", row=1, col=1)

    #titulo
    fig.update_layout(height=600, width=1000, title_text="pacientes al 28 septiembre 2020 IMSS",)
    
    return fig.show()






    
    





    
    



    





    

    
