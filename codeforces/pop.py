import matplotlib.pyplot as plt
import matplotlib.patches as patches

# Datos del horario
horario = [
    ("ambiente web", "lunes", 7 + 10/60, 10 + 20/60),
    ("base de datos", "miércoles", 7, 8 + 40/60),
    ("base de datos", "jueves", 7, 8 + 40/60),
    ("seminario", "lunes", 9, 10 + 40/60),
    ("estadística", "martes", 8 + 10/60, 11 + 30/60),
    ("sistemas digitales", "martes", 14 + 20/60, 16 + 50/60),
    ("sistemas digitales", "miércoles", 14 + 20/60, 16),
    ("mate 4", "lunes", 17, 19 + 30/60),
    ("mate 4", "miércoles", 17, 18 + 40/60),
]

# Días de la semana
dias = ["lunes", "martes", "miércoles", "jueves", "viernes", "sábado", "domingo"]
dia_indices = {dia: i for i, dia in enumerate(dias)}

# Crear figura y ejes
fig, ax = plt.subplots(figsize=(10, 7))

# Crear cuadrículas para cada clase
for clase, dia, inicio, fin in horario:
    y = dia_indices[dia]
    rect = patches.Rectangle((inicio, y), fin - inicio, 0.8, edgecolor='black', facecolor='skyblue', alpha=0.6)
    ax.add_patch(rect)
    plt.text(inicio + (fin - inicio) / 2, y + 0.4, clase, ha='center', va='center', fontsize=10)

# Configurar los ejes
ax.set_xlim(7, 20)
ax.set_ylim(-0.5, len(dias) - 0.5)
ax.set_xticks(range(7, 21))
ax.set_yticks(range(len(dias)))
ax.set_yticklabels(dias)
ax.set_xlabel('Hora')
ax.set_ylabel('Día')
ax.grid(True)

# Mostrar el horario
plt.title("Horario de Clases")
plt.show()
