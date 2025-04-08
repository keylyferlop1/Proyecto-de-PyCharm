import pandas as pd
import matplotlib.pyplot as plt
#from mpl_toolkits.mplot3d.axes3d import Axes3D

file_path = "./Data/pen Sales Data.xlsx"
df_pen_sales = pd.read_excel(file_path, sheet_name="Pen Sales")

#print(df_pen_sales)

#Analisis de Costos de envio
df_avg_pen_costos = df_pen_sales.groupby("Item")["Shipping Cost"].mean()
# print(df_avg_pen_costs)

plt.figure(figsize = (10,5))
df_avg_pen_costs.plot(kind="barh", color = "green")
plt.title("Costo de envio Promedio por Producto")
plt.xlabel("Costo medio de envio")
plt.ylabel("Tipo de Producto")
plt.show()

#RanKing de Popularidad de Leos Boligrafos
#Tarea: Identificar el tipo de Boligrafo que se Compra con mas frecuencias
#Pasos: Cuente el numero de compras por articulos.
#Ordenar en orden descendiente
# Trazae un Grafico de Barras Horizontales para mayor Claridad.
#Visializacion Graficos de barras Horizontales(Boligrafos mas Vendidos)