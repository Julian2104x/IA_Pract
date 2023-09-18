colores = input('Introduce un color:\n')
tupla_colores = ('Lila', 'Turquesa', 'Naranja', 'Magenta')

if colores in tupla_colores[0]:
	print('El color Lila está admitido')
elif colores in tupla_colores[1]:
	print('El color Turquesa está admitido')
elif colores in tupla_colores[2]:
	print('El color Naranja está admitido')
elif colores in tupla_colores[3]:
	print('El color Magenta está admitido')
else:
	print('Color no admitido')
