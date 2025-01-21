import re

class Dinosaurio:
    def __init__(self, especie, peso, cadera, ubicacion, periodo):
        self.especie = especie  # Atributo: especie de dinosaurio
        self.peso = peso  # Atributo: peso en kilogramos
        self.cadera = cadera  # Atributo: tipo de cadera
        self.ubicacion = ubicacion  # Atributo: país actual en el que vivió
        self.periodo = periodo  # Atributo: período geológico en el que vivió

    def __str__(self):
        """Método que devuelve la información del dinosaurio como una cadena."""
        return (f"{self.especie}:\n"
                f" - Peso: {self.peso} kilogramos\n"
                f" - Cadera: {self.cadera}\n"
                f" - Ubicación: {self.ubicacion}\n"
                f" - Período: {self.periodo}\n")

    def info_dinosaurio(self):
        """Método que imprime la información del dinosaurio."""
        return str(self)


# Subclase Saurisquio
class Saurisquio(Dinosaurio):
    def __init__(self, especie, peso, ubicacion, periodo, longitud):
        super().__init__(especie, peso, "saurisquio", ubicacion, periodo)  # Llama al constructor de Dinosaurio
        self.longitud = longitud  # Longitud específica del sauropodo

    def __str__(self):
        """Método que devuelve la información del sauropodo como una cadena."""
        return super().__str__() + f" - Longitud: {self.longitud} metros\n"


# Subclase Teropodo
class Teropodo(Saurisquio):
    def __init__(self, especie, peso, ubicacion, periodo, dieta):
        super().__init__(especie, peso, ubicacion, periodo)  # Llama al constructor de Saurisquio
        self.dieta = dieta  # Atributo específico para terópodos

    def __str__(self):
        """Método que devuelve la información del terópodo como una cadena."""
        return super().__str__() + f" - Dieta: {self.dieta}\n"


# Crear una "enciclopedia" de dinosaurios
enciclopedia = {
    "Tyrannosaurus rex": Teropodo("Tyrannosaurus rex", 8000, "Estados Unidos", "Cretácico", "carnívora"),
    "Brachiosaurus": Saurisquio("Brachiosaurus", 56000, "Estados Unidos", "Jurásico", 25),
    "Stegosaurus": Dinosaurio("Stegosaurus", 2000, "Estados Unidos", "Jurásico"),
    "Concavenator": Teropodo("Concavenator", 500, "España", "Cretácico", "carnívora"),
    "Turiasaurus": Saurisquio("Turiasaurus", 46000, "España", "Jurásico", 35),
    "Eocursor": Dinosaurio("Eocursor", 3, "Sudáfrica", "Jurásico"),
    "Lusotitan": Saurisquio("Lusotitan", 26000, "Portugal", "Jurásico", 25),
    "Velociraptor": Teropodo("Velociraptor", 15, "Mongolia", "Cretácico", "carnívora"),
    "Baryonyx": Teropodo("Baryonyx", 1200, "Inglaterra", "Cretácico", "carnívora"),
    "Pelicanimimus": Teropodo("Pelicanimimus", 50, "España", "Cretácico", "carnívora"),
    "Yi qi": Teropodo("Yi qi", 0.38, "China", "Jurásico", "insectívora"),
    "Majungasaurus": Teropodo("Majungasaurus", 1100, "Madagascar", "Cretácico", "carnívora"),
    "Dilophosaurus": Teropodo("Dilophosaurus", 400, "Estados Unidos", "Jurásico", "carnívora"),
    "Herrerasaurus": Teropodo("Herrerasaurus", 250, "Argentina", "Triásico", "carnívora"),
    "Pachycephalosaurus": Dinosaurio("Pachycephalosaurus", 450, "Estados Unidos", "Cretácico"),
    "Triceratops": Dinosaurio("Triceratops", 6000, "Estados Unidos", "Cretácico"),
    "Losillasaurus": Saurisquio("Losillasaurus", 25000, "España", "Jurásico", 20),
    "Ceratosaurus": Teropodo("Ceratosaurus", 980, "Estados Unidos", "Jurásico", "carnívora"),
    "Carnotaurus": Teropodo("Carnotaurus", 1400, "Argentina", "Cretácico", "carnívora"),
    "Diplodocus": Saurisquio("Diplodocus", 15000, "Estados Unidos", "Jurásico", 27),
    "Parasaurolophus": Dinosaurio("Parasaurolophus", 2500, "Canadá", "Cretácico"),
    "Microraptor": Teropodo("Microraptor", 1, "China", "Cretácico", "carnívora"),
    "Deinonychus": Teropodo("Deinonychus", 70, "Estados Unidos", "Cretácico", "carnívora"),
    "Troodon": Teropodo("Troodon", 50, "Estados Unidos", "Cretácico", "omnivora"),
    "Torvosaurus": Teropodo("Torvosaurus", 2000, "Estados Unidos", "Jurásico", "carnívora"),
    "Tarbosaurus": Teropodo("Tarbosaurus", 5000, "Mongolia", "Cretácico", "carnívora"),
    "Cryolophosaurus": Teropodo("Cryolophosaurus", 465, "Antártida", "Jurásico", "carnívora"),
    "Compsognathus": Teropodo("Compsognathus", 3, "Alemania", "Jurásico", "carnívora"),
    "Archaeopteryx": Teropodo("Archaeopteryx", 0.5, "Alemania", "Jurásico", "insectívora"),
    "Iberomesornis": Teropodo("Iberomesornis", 0.07, "España", "Cretácico", "insectívora"),
    "Meraxes": Teropodo("Meraxes", 4000, "Argentina", "Cretácico", "carnívora"),
    "Stygimoloch": Dinosaurio("Stygimoloch", 80, "Estados Unidos", "Cretácico"),
    "Abditosaurus": Saurisquio("Abditosaurus", 14000, "España", "Cretácico", 18),
    "Titanosaurus": Saurisquio("Titanosaurus", 10000, "India", "Cretácico", 12),
    "Argentinosaurus": Saurisquio("Argentinosaurus", 80000, "Argentina", "Cretácico", 35),
    "Aragosaurus": Saurisquio("Aragosaurus", 22000, "España", "Jurásico", 20),
    "Giganotosaurus": Teropodo("Giganotosaurus", 7600, "Argentina", "Cretácico", "carnívora"),
    "Abelisaurus": Teropodo("Abelisaurus", 3000, "Argentina", "Cretácico", "carnívora"),
    "Spinosaurus": Teropodo("Spinosaurus", 9000, "Egipto", "Cretácico", "carnívora"),
    "Carcharodontosaurus": Teropodo("Carcharodontosaurus", 6500, "Egipto", "Cretácico", "carnívora"),
    "Vallibonavenatrix": Teropodo("Vallibonavenatrix", 2500, "España", "Cretácico", "carnívora"),
    "Passer domesticus": Teropodo("Passer domesticus", 0.03, "Mundial", "Holoceno", "granívora"),
    "Carduelis carduelis": Teropodo("Carduelis carduelis", 0.02, "Mundial", "Holoceno", "granívora")
}

# Función para buscar información sobre un dinosaurio
def buscar_dinosaurio(nombre):
    """Busca un dinosaurio en la enciclopedia y devuelve su información."""
    try:
        # Validación básica para evitar caracteres no deseados (solo letras, espacios y guiones permitidos)
        if not re.match(r'^[a-zA-Z\s\-]+$', nombre):
            return "Entrada no válida. Por favor, introduce un nombre de dinosaurio válido."

        dino = enciclopedia.get(nombre)
        if dino:
            return dino.info_dinosaurio()
        else:
            return "Dinosaurio no encontrado."
    except Exception as e:
        return f"Se produjo un error: {e}"

# Ejemplo de uso
if __name__ == "__main__":
    while True:
        nombre_dino = input("¿De qué dinosaurio quieres saber más? (escribe 'salir' para terminar): ")
        if nombre_dino.lower() == 'salir':
            break
        print(buscar_dinosaurio(nombre_dino))