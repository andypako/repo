import streamlit as st
import pandas as pd

def cargar_datos(archivo_excel):
    datos = pd.read_excel(archivo_excel, engine='openpyxl')
    return datos

def mostrar_tabla(datos):
    st.table(datos)

def buscar_y_filtrar(datos):
    busqueda = st.text_input('Buscar')

    columnas = list(datos.columns)
    columna_seleccionada = st.selectbox('Selecciona una columna', columnas)

    opciones_filtro = datos[columna_seleccionada].unique()
    opcion_seleccionada = st.selectbox('Selecciona un filtro', opciones_filtro)

    datos_filtrados = datos[datos[columna_seleccionada] == opcion_seleccionada]

    if busqueda:
        datos_filtrados = datos_filtrados[datos_filtrados[columna_seleccionada].str.contains(busqueda)]

    return datos_filtrados

def main():
    st.title('Mi aplicación')

    archivo_excel = st.file_uploader('Cargar archivo de Excel', type=['xlsx'])
    if archivo_excel is not None:
        datos = cargar_datos(archivo_excel)

        mostrar_tabla(datos)

        datos_filtrados = buscar_y_filtrar(datos)

        mostrar_tabla(datos_filtrados)

if __name__ == '__main__':
    main()
