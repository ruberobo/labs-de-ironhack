

def coronavirus():

    import pickle
    import pandas as pd
    import numpy as np


    # Load from file
    with open('coronavirus', 'rb') as file:
        modelo = pickle.load(file)

    #inputs
    neumonia=input('¿diagonostico neumonía?')
    edad=input('edad con numeros entero')
    embarazo=input('¿esta embarazada?')
    meses=input('si esta embarazada inserte meses en número entero, de otra forma coloque cero')
    fiebre=input('¿fiebre?')
    tos=input('¿tos?')
    odinofagia=input('¿dolor de garganta?')
    disnea=input('¿dificultad para respirar?')
    irritabilidad=input('¿irritabilidad?')
    diarrea=input('¿diarrea?')
    dolor_t=input('¿dolor toracico?')
    calofrios= input('¿escalofrios?')
    cefalea=input('¿dolor de cabeza?')
    mialgia=input('¿dolor muscular?')
    artralgia=input('¿dolor en articulaciones?')
    ataque=input('¿se siente mal en general?')
    rinorrea=input('¿escurrimiento nasal?')
    polipnea=input('¿respiración acelerada?')
    vomito=input('¿vómito?')
    dolor_ab=input('¿dolor abdominal?')
    conjuntivitis = input('¿irritación de ojos?')
    cianosis=input ('¿cambio de color en piel?')
    inicio_subito=input('¿sus sintomas iniciaron de manera súbita?')
    diabetes=input('¿diabetes?')
    epoc=input('¿enfermedad pulmonar obstructiva crónica?')
    asma=input('¿asma?')
    inmunosupresivo = input('¿inmunosupresivo?')
    hipertension=input('¿hipertension?')
    vih=input('¿Es VIH positivo?')
    otra=input('¿alguna otra condición?')
    enfermedad_cardiaca=input('¿enfermedad cárdiaca?')
    obesidad=input('¿sobrepeso u obesidad?')
    renal=input('¿padece insuficiencia renal?')
    tabaquismo=input('¿fuma?')
    tratamiento=input('¿recibió tratamiento para su padecimiento?')
    antiviral=input('¿tomo antivirales?')
    vacunado=input('¿se vacuno contra influenza?')
    masculino=input('Si se considera masculino escriba si,si es femenino escriba no y responda si la siguiente pregunta')
    femenino=input('Si se considera femenino escriba si')
    ambulatorio=input('¿tratamiento ambulatorio?')
    hospitalizado=input('¿requirió hospitalización?')
    urgencia=input('¿fue servicio de urgencia?')

    array=np.array([
        neumonia,edad,embarazo,meses,fiebre,tos,odinofagia,disnea,irritabilidad,diarrea,dolor_t,calofrios,
    cefalea,mialgia,artralgia,ataque,rinorrea,polipnea,vomito,dolor_ab,conjuntivitis,cianosis,inicio_subito,
    diabetes,epoc,asma,inmunosupresivo,hipertension,vih,otra,enfermedad_cardiaca,obesidad,renal,
    tabaquismo,tratamiento,antiviral,vacunado,masculino,femenino,ambulatorio,hospitalizado,urgencia
    ])

    #limpio respuestas
    lista=[]
    for i in array:
        if i.isnumeric()==True:
            lista.append(int(i))
        
        else:
            x=i.lower()
            if x=='si':
                y=x.replace('si','1')
            if x=='no':
                y=x.replace('no','0')
        
            lista.append(int(y))


    coronavirus=modelo.predict(np.array([lista]))

    if coronavirus[0]==0:
        return 'lo más probable es que usted no tenga coronavirus'
    else:
        return 'Puede que usted tenga coronavirus, cuidese mucho y quedese en casa'







    
    





    
    



    





    

    
