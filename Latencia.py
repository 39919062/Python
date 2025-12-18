def latencia_estimada(x):
  return x * 1.20

print(f"La latencia real de 200 miliseguntos es de {latencia_estimada(200)}")
print(f"La latencia real de 149 miliseguntos es de {round(latencia_estimada(149),2)}")
print(f"La latencia real de 74 miliseguntos es de {latencia_estimada(74)}")
