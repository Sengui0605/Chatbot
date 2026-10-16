from settings import settings
import discord
from bot_logic import *

intents = discord.Intents.default()
intents.members = True
intents.message_content = True
client = discord.Client(intents=intents)


@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')


@client.event
async def on_member_join(member):
    channel = member.guild.system_channel
    if channel is not None:
        await channel.send(f'¡Bienvenido al servidor, {member.mention}!')


@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('$hola'):
        await message.channel.send('¡Hola! Soy un bot')
    elif message.content.startswith('$risa'):
        await message.channel.send(gen_emodji())
    elif message.content.startswith('$moneda'):
        await message.channel.send(flip_coin())
    elif message.content.startswith('$contraseña'):
        await message.channel.send(gen_pass(10))
    elif message.content.startswith('$unido'):
        miembro = message.mentions[0] if message.mentions else message.author
        fecha = discord.utils.format_dt(miembro.joined_at)
        await message.channel.send(f'{miembro.name} se unió el {fecha}')
    elif message.content.startswith('$dado'):
        await message.channel.send(roll_dice())
    elif message.content.startswith('$chiste'):
        await message.channel.send(get_joke())
    elif message.content.startswith('$mimic'):
        texto = message.content[6:].strip()
        if texto:
            await message.channel.send(texto)
        else:
            await message.channel.send('Escribe un mensaje para repetir.')
    elif message.content.startswith('$ppt'):
        opcion = message.content[4:].strip()
        await message.channel.send(jugar_ppt(opcion))
    elif message.content.startswith('$bola8'):
        pregunta = message.content[6:].strip()
        await message.channel.send(bola_8(pregunta))
    elif message.content.startswith('$ayuda'):
        embed = discord.Embed(title="Lista de Comandos", color=0x3498db)
        embed.add_field(name="Diversión", value="`$hola` - Saludo del bot\n`$risa` - Envía un emoji divertido\n`$mimic <texto>` - Repite lo que dices\n`$chiste` - Cuenta un chiste", inline=False)
        embed.add_field(name="Juegos", value="`$dado` - Lanza un dado\n`$moneda` - Cara o sello\n`$ppt <opción>` - Piedra, papel o tijera\n`$bola8 <pregunta>` - Pregúntale a la bola 8", inline=False)
        embed.add_field(name="Utilidad", value="`$contraseña` - Genera una contraseña\n`$unido [@usuario]` - Fecha de ingreso al servidor\n`$ayuda` - Muestra este menú", inline=False)
        await message.channel.send(embed=embed)
    else:
        await message.channel.send("No puedo procesar este comando. Escribe $ayuda para ver los comandos disponibles.")

client.run(settings["TOKEN"])