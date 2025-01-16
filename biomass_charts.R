# Cargar las bibliotecas necesarias
library(ggplot2)
library(ggrepel)

# Crear los datos de biomasa terrestre por grupos de seres vivos
datos_biomasa <- data.frame(
  grupo = c("Animales", "Bacteria", "Fungi", "Plantas", "Protistas", "Virus", "Arqueas"),
  biomasa = c(2.589, 70, 12, 450, 4, 0.2, 7)
)

# Crear el gráfico de sectores
ggplot(datos_biomasa, aes(x = "", y = biomasa, fill = grupo)) +
  geom_bar(stat = "identity", width = 1) +
  coord_polar("y", start = 0) +
  geom_text_repel(aes(label = paste0(grupo, " - ", biomasa, " Gt C")),
                  position = position_stack(vjust = 0.5),
                  size = 4) +
  theme_void() +
  theme(legend.position = "none") +
  labs(title = "Distribución de Biomasa Terrestre por Grupos de Seres Vivos (Gt C)")

# Crear los datos de biomasa para diferentes tipos de animales
datos_animales <- data.frame(
  grupo = c("Artrópodos marinos", "Artrópodos terrestres", "Anélidos", "Peces", "Cnidarios", "Humanos", "Nemátodos", "Ganado", "Aves", "Mamíferos"),
  biomasa = c(1, 0.2, 0.2, 0.7, 0.1, 0.06, 0.02, 0.1, 0.002, 0.007)
)

# Crear el gráfico de sectores
ggplot(datos_animales, aes(x = "", y = biomasa, fill = grupo)) +
  geom_bar(stat = "identity", width = 1) +
  coord_polar("y", start = 0) +
  geom_text_repel(aes(label = paste0(grupo, " - ", biomasa, " Gt C")),
                  position = position_stack(vjust = 0.5),
                  size = 4) +
  theme_void() +
  theme(legend.position = "none") +
  labs(title = "Distribución de Biomasa en Animales (Gt C)")