from graphviz import Digraph

# Crear un nuevo grafo dirigido
dot = Digraph(comment='Mapa Mental de Arquitectura de Computadoras')

# Tema principal
dot.node("A", "Arquitectura de Computadoras")

# Subtemas
dot.node("B", "Modelos de Computo")
dot.node("C", "Análisis de Componentes")
dot.node("D", "Memoria")
dot.node("E", "Gestión de Entrada/Salida")
dot.node("F", "Buses")
dot.node("G", "Interrupciones")

# Detalles de Modelos de Computo
dot.node("B1", "Von Neumann")
dot.node("B2", "Harvard")
dot.node("B3", "Computación Paralela")

# Detalles de Análisis de Componentes
dot.node("C1", "CPU")
dot.node("C2", "ALU")
dot.node("C3", "Unidad de Control")
dot.node("C4", "Registros")

# Detalles de Memoria
dot.node("D1", "RAM")
dot.node("D2", "ROM")
dot.node("D3", "Memoria Caché")
dot.node("D4", "Memoria Virtual")

# Detalles de Gestión de Entrada/Salida
dot.node("E1", "Dispositivos Periféricos")
dot.node("E2", "Controladores de Dispositivos")
dot.node("E3", "DMA (Acceso Directo a Memoria)")

# Detalles de Buses
dot.node("F1", "Bus de Datos")
dot.node("F2", "Bus de Dirección")
dot.node("F3", "Bus de Control")

# Detalles de Interrupciones
dot.node("G1", "Interrupciones de Hardware")
dot.node("G2", "Interrupciones de Software")
dot.node("G3", "Manejo de Interrupciones")

# Conexiones entre temas principales
dot.edge("A", "B")
dot.edge("A", "C")
dot.edge("A", "D")
dot.edge("A", "E")
dot.edge("A", "F")
dot.edge("A", "G")

# Conexiones de Modelos de Computo
dot.edge("B", "B1")
dot.edge("B", "B2")
dot.edge("B", "B3")

# Conexiones de Análisis de Componentes
dot.edge("C", "C1")
dot.edge("C", "C2")
dot.edge("C", "C3")
dot.edge("C", "C4")

# Conexiones de Memoria
dot.edge("D", "D1")
dot.edge("D", "D2")
dot.edge("D", "D3")
dot.edge("D", "D4")

# Conexiones de Gestión de Entrada/Salida
dot.edge("E", "E1")
dot.edge("E", "E2")
dot.edge("E", "E3")

# Conexiones de Buses
dot.edge("F", "F1")
dot.edge("F", "F2")
dot.edge("F", "F3")

# Conexiones de Interrupciones
dot.edge("G", "G1")
dot.edge("G", "G2")
dot.edge("G", "G3")

# Renderizar el mapa mental
dot.format = 'png'
file_path = '/mnt/data/mapa_mental_arquitectura_computadoras'
dot.render(file_path)

file_path + ".png"
