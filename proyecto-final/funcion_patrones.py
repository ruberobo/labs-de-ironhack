
def limpia_patrones(ubi):
    import pandas as pd
    import numpy as np
    
    asegurados_mes = pd.read_csv(ubi, sep='|',engine='python')
    
    #asegurados cdmx
    asegurados_cdmx_mes =(asegurados_mes[asegurados_mes['cve_entidad']==9]).reset_index(drop=True)
    
    
    #renombro de acuerdo a glosario del imss
    asegurados_cdmx_mes.rename(columns= {'ta':'ta_puestos_trabajo', 'teu':'teu_eventual_urbano', 
                                            'tec':'tec_eventual_campo',
                                            'tpu':'tpu_permanente_urbano', 'tpc':'tpc_permanente_campo'})
    
    #actualizo sexo
    asegurados_cdmx_mes['sexo']=np.where(asegurados_cdmx_mes['sexo']==1,'M','F')
    
    #borro columnas que no sirven 
    asegurados_cdmx_mes.drop(['cve_delegacion', 'cve_subdelegacion', 'cve_entidad', 'cve_municipio','rango_uma',
                                'sector_economico_2', 'sector_economico_4'], axis=1, inplace=True)
    
    
    #los vacíos son dificiles de interpretar por lo que se borran
    asegurados_cdmx_mes.dropna(axis=0, inplace=True)
    asegurados_cdmx_mes_2=asegurados_cdmx_mes.reset_index(drop=True)
    
    #actualizo variables de rango salarial
    menor_a_6 =['W1','W2','W3','W4','W5']
    de_6_a_12 = ['W6','W7','W8','W9','W10','W11']
    mayor_a_12= ['W12','W13','W14','W15','W16','W17', 'W18', 'W19', 'W20','W21','W22','W23','W24','W25']
    
    for i in menor_a_6:
        asegurados_cdmx_mes_2['rango_salarial']=asegurados_cdmx_mes_2['rango_salarial'].replace(i,'menor 6')
    
    for i in de_6_a_12:
        asegurados_cdmx_mes_2['rango_salarial']=asegurados_cdmx_mes_2['rango_salarial'].replace(i,'6 a 12')
    
    for i in mayor_a_12:
        asegurados_cdmx_mes_2['rango_salarial']=asegurados_cdmx_mes_2['rango_salarial'].replace(i,'mayor a 12')
    
    #Actualizo tamaño de patron
    menor_a_5 = ['S1','S2']
    de_6_a_50 = ['S3']
    de_51_a_500= ['S4','S5']
    mayor_500= ['S6','S7']
    
    for i in menor_a_5:
        asegurados_cdmx_mes_2['tama�o_patron']=asegurados_cdmx_mes_2['tama�o_patron'].replace(i,'S1-S2(<5)')
    
    
    for i in de_6_a_50:
        asegurados_cdmx_mes_2['tama�o_patron']=asegurados_cdmx_mes_2['tama�o_patron'].replace(i,'S3(<50)')
    
    
    for i in de_51_a_500:
        asegurados_cdmx_mes_2['tama�o_patron']=asegurados_cdmx_mes_2['tama�o_patron'].replace(i,'S4-S5(51-500)')
        
    for i in mayor_500:
        asegurados_cdmx_mes_2['tama�o_patron']=asegurados_cdmx_mes_2['tama�o_patron'].replace(i,'>S6(>500)')
        
    #actualizo edad
    menor_de_25_años=['E1','E2','E3']
    de_25_a_40= ['E4','E5','E6']
    de_40_a_65 = ['E7','E8','E9','E10','E11']
    mas_de_65 = ['E12','E13','E14']
    
    for i in menor_de_25_años:
        asegurados_cdmx_mes_2['rango_edad']=asegurados_cdmx_mes_2['rango_edad'].replace(i,'E1-E3(<25)')
    
    for i in de_25_a_40:
        asegurados_cdmx_mes_2['rango_edad']=asegurados_cdmx_mes_2['rango_edad'].replace(i,'E4-E6(26-40)')
    
    for i in de_40_a_65:
        asegurados_cdmx_mes_2['rango_edad']=asegurados_cdmx_mes_2['rango_edad'].replace(i,'E7-E11(40-65)')
    
    for i in mas_de_65:
        asegurados_cdmx_mes_2['rango_edad']=asegurados_cdmx_mes_2['rango_edad'].replace(i,'E12-E14(>65)')
        
        


    
    #funcion para sector
    def sec(x):
        sector={0:'agricultura',1:'extractiva',3:'transformación',4:'construcción',5:'energía_agua',6:'comercio',7:'transporte',8:'servicios_lucrativos', 9:'servicios_sociales'}

        return sector[x]

    
        
    #actualizo sector economico
    asegurados_cdmx_mes_2['sector_economico_1']=asegurados_cdmx_mes_2['sector_economico_1'].apply(sec)

    #quito simbolo raro
    asegurados_cdmx_mes_2.rename(columns = ({'tama�o_patron':'tamano_patron'}), inplace=True) 
    
    #regreso data frame
    return asegurados_cdmx_mes_2
    
    
  
   
