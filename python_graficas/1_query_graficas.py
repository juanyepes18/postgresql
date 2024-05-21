import matplotlib.pyplot as plt

# Datos proporcionados
job_titles = [
    "Data Analyst",
    "Director of Analytics",
    "Associate Director- Data Insights",
    "Data Analyst, Marketing",
    "Data Analyst (Hybrid/Remote)",
    "Principal Data Analyst (Remote)",
    "Director, Data Analyst - HYBRID",
    "Principal Data Analyst, AV Performance Analysis",
    "Principal Data Analyst",
    "ERM Data Analyst"
]

salaries = [
    650000.0,
    336500.0,
    255829.5,
    232423.0,
    217000.0,
    205000.0,
    189309.0,
    189000.0,
    186000.0,
    184000.0
]

# Crear la gráfica de barras
plt.figure(figsize=(12, 8))
plt.barh(job_titles, salaries, color='skyblue')
plt.xlabel('Salario Anual Promedio ($)',fontsize=12)
plt.ylabel('Título del Trabajo',fontsize=12)
plt.title('Average Annual Salaries by Job Title', fontsize=14)
plt.gca().invert_yaxis()  # Invertir el eje Y para que los salarios más altos estén arriba
plt.grid(axis='x', linestyle='--', alpha=0.7)
plt.yticks(fontsize=10)
plt.tight_layout()
plt.show()
