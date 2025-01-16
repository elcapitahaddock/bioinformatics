# para visualizar gráficos en este notebook
%matplotlib inline

# importamos los módulos necesarios
import matplotlib.pyplot as plt

def generar_pie_chart(datos_biomasa, titulo):
    """
    Genera un gráfico de sectores con los porcentajes de biomasa terrestre por grupos de seres vivos,
    mostrando los nombres en la leyenda.
    """
    labels = list(datos_biomasa.keys())  # Nombres de los grupos de seres vivos
    sizes = list(datos_biomasa.values())  # Biomasa de cada grupo

    # Generamos el gráfico de sectores
    fig, ax = plt.subplots()
    wedges, texts, autotexts = ax.pie(
        sizes,
        labels=labels,  # Mostramos las etiquetas en el gráfico
        autopct='%1.1f%%',  # Añadimos y visibilizamos los porcentajes sobre los sectores
        startangle=90,  # Comenzar desde arriba
        colors=plt.cm.tab10.colors  # Colores distintos para los sectores
    )
    ax.axis('equal')  # Nos aseguramos que sea un círculo

    # Añadimos una leyenda
    ax.legend(
        wedges,  # Asociamos los sectores a la leyenda
        labels,  # Etiquetas de los grupos
        loc="best"  # Ubicación automática para la mejor posición
    )

    # Título del gráfico
    plt.title(titulo)
    plt.show()  # Mostramos el gráfico

# Diccionario con datos de biomasa terrestre por grupos de seres vivos
datos_biomasa = {
    "Animales": 2.589,
    "Bacteria": 70,
    "Fungi": 12,
    "Plantas": 450,
    "Protistas": 4,
    "Virus": 0.2,
    "Arqueas": 7
}

# Generamos el gráfico de sectores usando el diccionario
generar_pie_chart(datos_biomasa, "Distribución de Biomasa Terrestre por Grupos de Seres Vivos (Gt C)")

# Diccionario con datos de biomasa para diferentes tipos de animales
datos_animales = {
    "Artrópodos marinos": 1,
    "Artrópodos terrestres": 0.2,
    "Anélidos": 0.2,
    "Peces": 0.7,
    "Cnidarios": 0.1,
    "Humanos": 0.06,
    "Nemátodos": 0.02,
    "Ganado": 0.1,
    "Aves": 0.002,
    "Mamíferos": 0.007
}

# Generamos el gráfico de sectores usando el diccionario
generar_pie_chart(datos_animales, "Distribución de Biomasa en Animales (Gt C)")