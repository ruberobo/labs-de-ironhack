def derecho_hab(ubi): #ubicacion del csv en local
    import pandas as pd
    import numpy as np
    
    data = pd.read_csv(ubi, sep='|',engine='python')
    
    #filtro solo cdmx
    derecho_cdmx=(data[(data['ID_DELEG_RP']==39)|(data['ID_DELEG_RP']==40)])[['NOMBRE_UMF_RP','ST_TIT_FAM','CVE_SEXO','CVE_RANGO_EDAD','TOT_CASOS']]
    derecho_mes= derecho_cdmx.reset_index(drop=True)
    
    derecho_mes2=derecho_mes[derecho_mes['CVE_RANGO_EDAD']!='ND']
    derecho_mes2.reset_index(drop=True)
    
    #limpio edad
    derecho_mes2['CVE_RANGO_EDAD']=derecho_mes2['CVE_RANGO_EDAD'].apply(lambda x:x.strip())
    
    #actualizo edad
    d_menor_de_25_años=['E0','E1','E2','E3','E4','E5','E6','E7','E8','E9','E10','E11','E12','E13','E14','E15']
    d_de_25_a_40= ['E16','E17','E18']
    d_de_40_a_65 = ['E19','E20','E21','E22','E23']
    d_mas_de_65 = ['E24','E25','E26','E27','E28']
    
    
    for i in d_menor_de_25_años:
        derecho_mes2['CVE_RANGO_EDAD']=derecho_mes2['CVE_RANGO_EDAD'].replace(i,'(<25)')
    
    for i in d_de_25_a_40:
        derecho_mes2['CVE_RANGO_EDAD']=derecho_mes2['CVE_RANGO_EDAD'].replace(i,'(26-40)')
    
    for i in d_de_40_a_65:
        derecho_mes2['CVE_RANGO_EDAD']=derecho_mes2['CVE_RANGO_EDAD'].replace(i,'(40-65)')
    
    for i in d_mas_de_65:
        derecho_mes2['CVE_RANGO_EDAD']=derecho_mes2['CVE_RANGO_EDAD'].replace(i,'(>65)')
        
     #actualizo sexo

    derecho_mes2['CVE_SEXO']=np.where(derecho_mes2['CVE_SEXO']==1,'M','F') 
    
    #actualizo ST_TIT_FAM
    derecho_mes2['ST_TIT_FAM']=np.where(derecho_mes2['ST_TIT_FAM']==1,'Titular','beneficiario')
    
    return derecho_mes2
    
    
