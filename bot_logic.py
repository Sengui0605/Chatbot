import random


def gen_pass(pass_length):
    elements = "+-/*!&$#?=@<>"
    password = ""

    for i in range(pass_length):
        password += random.choice(elements)

    return password


def gen_emodji():
    emodji = ["\U0001f600", "\U0001f642", "\U0001F606", "\U0001F923"]
    return random.choice(emodji)


def flip_coin():
    flip = random.randint(0, 2)
    if flip == 0:
        return "CARA"
    else:
        return "SELLO"


def roll_dice():
    num = random.randint(1, 6)
    mensajes = {
        1: "🎲 Sacaste un 1. ¡Todo comienzo tiene su magia, que tengas un bonito día!",
        2: "🎲 Sacaste un 2. ¡Poco a poco se llega lejos, sonríe que hoy será un buen día!",
        3: "🎲 Sacaste un 3. ¡Punto medio perfecto, sigue adelante con tu buena energía!",
        4: "🎲 Sacaste un 4. ¡Muy buena tirada, la suerte te está acompañando!",
        5: "🎲 Sacaste un 5. ¡Casi el máximo, qué linda racha llevas!",
        6: "🎲 ¡Sacaste un 6! ¡La mejor tirada posible, hoy el día te sonríe con todo!"
    }
    return mensajes[num]


def get_joke():
    jokes = [
        "¿Qué le dice un bit al otro? Nos vemos en el bus.",
        "¿Por qué los pájaros no usan Facebook? Porque ya tienen Twitter.",
        "¿Qué hace una abeja en el gimnasio? ¡Zum-ba!",
        "Hay 10 tipos de personas en el mundo: las que entienden binario y las que no.",
        "¿Qué le dice una impresora a otra? ¿Esa hoja es tuya o es una impresión mía?"
    ]
    return random.choice(jokes)


def jugar_ppt(opcion):
    opcion = opcion.lower().strip()
    opciones = {
        "piedra": "🪨",
        "papel": "📄",
        "tijera": "✂️",
        "tijeras": "✂️"
    }
    if opcion not in opciones:
        return "Debes elegir: piedra, papel o tijera. Ejemplo: $ppt piedra"

    if opcion == "tijeras":
        opcion = "tijera"

    bot_opcion = random.choice(["piedra", "papel", "tijera"])
    icono_user = opciones[opcion]
    icono_bot = opciones[bot_opcion]

    if opcion == bot_opcion:
        mensajes_empate = [
            f"¡Empate! Ambos sacamos {icono_bot} {bot_opcion}. ¿Acaso leemos la mente?",
            f"Empate con {icono_bot} {bot_opcion}. Gran duelo, intentémoslo otra vez.",
            f"{icono_bot} contra {icono_bot}. ¡Empate técnico!"
        ]
        return random.choice(mensajes_empate)

    victorias = {
        "piedra": "tijera",
        "papel": "piedra",
        "tijera": "papel"
    }

    if victorias[opcion] == bot_opcion:
        mensajes_ganaste = [
            f"Tú: {icono_user} {opcion} | Bot: {icono_bot} {bot_opcion}. ¡Me ganaste limpiamente!",
            f"Tú sacaste {icono_user} y yo {icono_bot}. ¡Victoria para ti! Bien jugado.",
            f"¡Ganaste! Tu {icono_user} destruyó mi {icono_bot}. Tuviste suerte esta vez..."
        ]
        return random.choice(mensajes_ganaste)
    else:
        mensajes_perdiste = [
            f"Tú: {icono_user} {opcion} | Bot: {icono_bot} {bot_opcion}. ¡Punto para mí! Suerte a la próxima.",
            f"Saqué {icono_bot} y tú {icono_user}. ¡Te gané! La máquina sigue invicta.",
            f"¡Perdiste! Mi {icono_bot} venció a tu {icono_user}. Mejor suerte en la siguiente ronda."
        ]
        return random.choice(mensajes_perdiste)


def bola_8(pregunta):
    pregunta = pregunta.strip()
    if not pregunta:
        return "🎱 Debes hacerme una pregunta. Ejemplo: $bola8 ¿Voy a aprobar el examen?"

    respuestas = [
        "🎱 Totalmente seguro.",
        "🎱 Es decididamente así.",
        "🎱 Sin lugar a dudas, sí.",
        "🎱 Mis fuentes dicen que sí.",
        "🎱 Todo apunta a que sí, celébralo.",
        "🎱 Sí, definitivamente.",
        "🎱 Las perspectivas son buenas.",
        "🎱 Pregunta de nuevo más tarde, el universo está ocupado.",
        "🎱 Mejor no te lo digo ahora...",
        "🎱 Concéntrate y vuelve a preguntar.",
        "🎱 Mis circuitos están indecisos, prueba otra vez.",
        "🎱 No cuentes con ello.",
        "🎱 Mi respuesta es un rotundo no.",
        "🎱 Mis fuentes dicen que ni de chiste.",
        "🎱 Las perspectivas no son nada buenas.",
        "🎱 Ni lo sueñes.",
        "🎱 La probabilidad es casi cero."
    ]
    return f"Pregunta: *{pregunta}*\n{random.choice(respuestas)}"