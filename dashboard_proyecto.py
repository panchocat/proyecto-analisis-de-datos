import pandas as pd #es una librería de Python especializada en el manejo y análisis de estructuras de datos.
import xlwings as xw #es una librería de Python que  permite comunicarse con excel para intercambiar informacion y compartir funcionalidades.
#Plotly es una biblioteca de visualización de datos en Python que permite crear gráficos interactivos y personalizados para explorar y representar datos de manera efectiva.
import plotly.express as px# sub libreripermite visualizar nuestros gráficos de forma inmediata
import plotly.graph_objects as go#proporciona objetos que contribuyen hacer trazos en los gráficos. Permite personalizar los gráficos.
#import matplotlib.pyplot as plt# llamamos las librerias que vamos a necesitar para analizar y graficar datos.
#import matplotlib.patheffects as pa



#df = pd.read_csv('D:\Cursos\Analisis de datos y graficos con python\PARAMETROS BROCA 8.5_RB2004H.csv', sep=';')# se crea la variable df leyendo la información de un archivo .csv
df = pd.read_excel('D:\Cursos\Analisis de datos y graficos con python\parametros de perforación ejercicio.xlsx')# se crea la variable df leyendo la información de un archivo .xlsx
#df1 = df.set_index("DEPTH")# cremos un nuevo dataframe cambiando el indice del df que se generó por defecto al leer el archivo por uno presonalizado que en este caso va a ser "DEPTH"
#df.set_index("DEPTH", inplace=True)
dfl = len(df["MD"])# Calculamos y almacenamos el valor de la longitud de la serie MD del df en la variable dfl.
dmax = df["MD"].max()# almacenamos en una variable el valor minimo de la columna DEPTH.
dmin = df["MD"].min()# almacenamos en una variable el valor maximo de la columna DEPTH.
#mwl = df["MW"].head().isnull()# muestra si los primeros 5 valores de la columna MW esta vacios.
#mwl1 = df.loc[[0],['MW']]# muestra el valor de una celda con el nombre de la columna y el numero de la fila.
#mwl2 = df.at[0,'MW']# muestra el valor de una celda.
#dfs = df.shape# método que permite consultar la dimensión que tiene el data frame y lo entrega en una tubla,se almacena la consulta en la variable dfs.


#print(columnas)
print(df)
#print(dfl)
print(dmin)
print(dmax)
#print(mwl)
#print(mwl1)
#print(mwl2)

# Bloque de codigo que permite leer el nombre de las columnas de un df y almacenarlos en una lista
coldf = []
for i in df:
    coldf.append(i)
print(coldf)

def check (ncol, list):
    if ncol in list:
        return True
    else:
        return False
    
colnec = ['MD','SPP','CAUDAL','MW']


for j in colnec:
    eval1 = j != "MW"
    eval2 = check(j,coldf) == False
    if eval2 & eval1:
        print(f'El dataframe no contiene los datos de {j}, por favor revise los datos de origen y vuelva a correr el programa.')
        break
    if j == "MW":
        print('El dataframe no contiene los datos de "MW", ingrese esa información:')
        while(True):# Bucle infinito
            try:# Excepción.
                mw = float(input("Ingrese el valor del peso del lodo: "))
                break# rompe el bucle infinito.
            except ValueError:# si el error es debido al dato que ingreso, lo informa.
                print('Debe ingresar un número')

        while(True):
            try:
                intermin = int(input(f"Ingrese el valor de profundidad(este valor no puede estar por debajo de {dmin} y ni por encima de {dmax}) donde empieza este peso de lodo: "))
                break
            except ValueError:# si el error es debido al dato que ingreso, lo informa.
                print('Debe ingresar un número')
            
        while(True):    
            try:
                intermax = int(input(f"Ingrese el valor de profundidad(este valor no puede estar por debajo de {dmin} y ni por encima de {dmax}) donde finaliza este peso de lodo: "))
                break
            except ValueError:# si el error es debido al dato que ingreso, lo informa.
                print('Debe ingresar un número')
                    
        df.set_index("MD", inplace=True)# cambiamos el indice del df que se generó por defecto en pandas por uno presonalizado que en este caso va a ser "DEPTH"
        for i in range (intermin,intermax+1):
            df.at[i,'MW'] = mw # Almacenamos en una celda especifica el valor mw.
        while (True):
            consultar = input("Quieres ingresar mas valores de MW? S/N: ")
            if consultar == "N":
                print("Gracia por ingresar la información!!!")
                break
            elif consultar == "S":
                
                while(True):
                    try:
                        mw = float(input("Ingrese el valor del peso del lodo: "))
                        break
                    except ValueError:# si el error es debido al dato que ingreso, lo informa.
                        print('Debe ingresar un número')
                        
                while(True):
                    try:
                        intermin = int(input(f"Ingrese el valor de profundidad(este valor no puede estar por debajo de {dmin} y ni por encima de {dmax}) donde empieza este peso de lodo: "))
                        break
                    except ValueError:# si el error es debido al dato que ingreso, lo informa.
                        print('Debe ingresar un número')
                while(True):    
                    try:
                        intermax = int(input(f"Ingrese el valor de profundidad(este valor no puede estar por debajo de {dmin} y ni por encima de {dmax}) donde finaliza este peso de lodo:"))
                        break
                    except ValueError:# si el error es debido al dato que ingreso, lo informa.
                        print('Debe ingresar un número')       
                    
                
                        
                df.at[i,'MW'] = mw#guarda el valor mw en la posición que se encuentra en la fila con nombre fila y la columna de con nombre columna del DataFrame df.
                        
            else:
                print("No seleccionó una de las opciones validas")
        
        break
        
    # else:
    #     continue

print('La información del dataframe está completa, a continuación se generará la gráfica de correlación de presiones')      
df.reset_index(inplace=True)# cambiamos el indice del df que personalizamos por el que estaba por defecto.
print(df)
    

        


'''
print(f"El dataframe no tiene la columna MW, por favor introduzca esta información basado en el intervalo de profudidad del pozo que va desde {dmin} hasta {dmax}")

# Bloque de codigo que pide ingresar datos para completar información faltante en el dataframe, también si el dato ingresado no es el correcto lo informa.
while(True):# Bucle infinito
    try:# Excepción.
        mw = float(input("Ingrese el valor del peso del lodo: "))
        break# rompe el bucle infinito.
    except ValueError:# si el error es debido al dato que ingreso, lo informa.
        print('Debe ingresar un número')

while(True):
    try:
        intermin = int(input(f"Ingrese el valor de profundidad(este valor no puede estar por debajo de {dmin} y ni por encima de {dmax}) donde empieza este peso de lodo: "))
        break
    except ValueError:# si el error es debido al dato que ingreso, lo informa.
        print('Debe ingresar un número')
    
while(True):    
    try:
        intermax = int(input(f"Ingrese el valor de profundidad(este valor no puede estar por debajo de {dmin} y ni por encima de {dmax}) donde finaliza este peso de lodo: "))
        break
    except ValueError:# si el error es debido al dato que ingreso, lo informa.
        print('Debe ingresar un número')



#bloque de codigo que permite ingresar en el dataframe los valores faltantes de la columna MW
df.set_index("MD", inplace=True)# cambiamos el indice del df que se generó por defecto en pandas por uno presonalizado que en este caso va a ser "DEPTH"
print(df)
for i in range (intermin,intermax+1):
    df.at[i,'MW'] = mw # Almacenamos en una celda especifica el valor mw.
while (True):
    consultar = input("Quieres ingresar mas valores de MW? S/N: ")
    if consultar == "N":
        print("Gracia por ingresar la información!!!")
        break
    elif consultar == "S":
        
        while(True):
            try:
                mw = float(input("Ingrese el valor del peso del lodo: "))
                break
            except ValueError:# si el error es debido al dato que ingreso, lo informa.
                print('Debe ingresar un número')
                
        while(True):
            try:
                intermin = int(input(f"Ingrese el valor de profundidad(este valor no puede estar por debajo de {dmin} y ni por encima de {dmax}) donde empieza este peso de lodo: "))
                break
            except ValueError:# si el error es debido al dato que ingreso, lo informa.
                print('Debe ingresar un número')
        while(True):    
            try:
                intermax = int(input(f"Ingrese el valor de profundidad(este valor no puede estar por debajo de {dmin} y ni por encima de {dmax}) donde finaliza este peso de lodo:"))
                break
            except ValueError:# si el error es debido al dato que ingreso, lo informa.
                print('Debe ingresar un número')       
            
        #intermin = int(input("Ingrese el valor de profundidad donde empieza este peso de lodo: "))
        #intermax = int(input("Ingrese el valor de profundidad donde finaliza este peso de lodo: "))
        #df.set_index("DEPTH", inplace=True)# cambiamos el indice del df que se generó por defecto por uno presonalizado que en este caso va a ser "DEPTH"
        for i in range (intermin,intermax+1):
            df.at[i,'MW'] = mw#guarda el valor mw en la posición que se encuentra en la fila con nombre fila y la columna de con nombre columna del DataFrame df.
    else:
        print("No seleccionó una de las opciones validas")
    #consultar = input("Quieres ingresar mas valores de MW? S/N: ")
df.reset_index(inplace=True)# cambiamos el indice del df que personalizamos por el que estaba por defecto.
#SPPT = []# se crea una variable con una lista vacia.
print(df)
#df.to_excel('D:\Cursos\Analisis de datos y graficos con python\PARAMETROS BROCA_6892_FT_A_8145_FT_CASTILLA_358.xlsx', index=False)# guarda el datframe sin el indice creado por pandas en un archivo excel.



#
#Este bloque de codigo me permitira permite leer archivos Excel y escribir en ellos usando la libreria openpyxl. 
wb = openpyxl.load_workbook('D:\Cursos\Analisis de datos y graficos con python\TGT REPORTE DIARIO INGENIERIA 02 QUIFA 931H 23-04-2023.xlsx', data_only=True)#parametro data_only se usa para que cargue los valores de la hoja y no las formulas
ws = wb['REP ING 1']
ws['C20'] = df.at[2,"SPMT"]
wb.save('D:\Cursos\Analisis de datos y graficos con python\output\TGT REPORTE DIARIO INGENIERIA 02 QUIFA 931H 23-04-2023.xlsx')


# Bloque de codigo que permite compartir información con un archivo excel para crear una nueva columna llamada "SPPT" y generar los valores de la columna.
wb = xw.Book('D:\Cursos\Analisis de datos y graficos con python\TGT REPORTE DIARIO INGENIERIA 03 QUIFA 931H 24-04-2023.xlsx')
ws = wb.sheets['REP ING 1']
for i in range(0,dfl):
    ws['G6'].value = df.at[i,"MD"]
    ws['D22'].value = df.at[i,"CAUDAL"]
    ws['C224'].value = df.at[i,"MW"]
    df.at[i,'SPPT'] = ws['D215'].value
    
#Bloque de codigo que crea dos nuevas columnas ('SPPT5%+' y 'SPPT5%-') en el dataframe con sus respctivos valores.
for j in range(0,dfl):
    df.at[j,'SPPT5%+']  = df.at[j,'SPPT']*5/100 + df.at[j,'SPPT']
    df.at[j,'SPPT5%-']  = df.at[j,'SPPT'] - df.at[j,'SPPT']*5/100 

print(df)
print(df['SPPT'].dtype)# muestra que tipo de dato esta almacenado la columna.
print(df['SPP'].dtype)
#
fig = px.line(df, x = df.MD, y = df.SPPT, title="sample figure")
fig.show()


# Bloque de codigo que permite crear un grafica para visualizar información del df.
fig = go.Figure()
fig.add_trace(go.Scatter(x=df.MD, y=df.SPP, mode='lines', line_color='green'))
fig.add_trace(go.Scatter(x=df.MD, y=df.SPPT,mode='lines', line_color='indigo'))

fig.show()
'''