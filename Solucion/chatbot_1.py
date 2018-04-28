# Crear Variable con preguntas por defecto

preguntas = {
    'hola':'Hola bienvenido a Flisol',
    'de que color es el cielo':'El cielo es azul',
    'como te llamas':'yo soy fli'
}

despedidas = [
    'adios',
    'chao',
    'hasta pronto',
    'bye',
    'nos vemos'
]

# Repetir hasta que el usuario se despida
while True:
    # Preguntar al usuario su pregunta
    pregunta_usuario = input('¿que quieres saber? \n')

    # Si se despide debemos cerrar
    if pregunta_usuario in despedidas:
        print('Hasta luego')
        break

    # Si conocemos la respuesta debemos responder
    elif pregunta_usuario in preguntas:
        print(preguntas[pregunta_usuario])

    # Si no conocemos la respuesta debemos aprender
    else:
        respuesta_nueva = input('No se la respuesta, '
                                '¿Que deberia decir?')
        preguntas[pregunta_usuario] = respuesta_nueva