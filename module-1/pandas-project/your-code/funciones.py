#funciones pandas

#función para actividad
def activity(x):
    try:
        y = x.split()
        for z in y:
            if z.endswith('ing'):
                return z
    except:
        pass


#funcion para la edad

def age(x):
    try:
        y = x.split()
        for i in y:
            if i.isnumeric():
                return float(i)
    except:
        return x


#funcion para la edad

def time (x):
    try:
        if x.startswith(('06','07','08','09','10','11','Shortly before', 'Early', 'A.M.', 'Just', 'Daytime', 'AM')):
            y ='Morning'
            return y
        elif x.startswith(('12','13','14','15','16','17','18', '19', 'Mid','Sunset', 'Eve','Late','After', 'P.M.','noon', 'Lunch', 'Dawn' )):
            y = 'Afternoon'
            return y
        elif x.startswith(('2','00','01','02','03','04','05','Dusk', 'Dark','dusk','night', '"Night"')):
            y = 'Night'
            return y
        else:
            return x
    except:
        return x


