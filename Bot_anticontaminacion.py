import discord
from discord.ext import commands
import random

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="$", intents=intents)

consejos = [
    "Utiliza transporte público, bicicleta o camina en lugar de usar el coche.",
    "Recicla correctamente y separa los residuos.",
    "Reduce el consumo de plásticos de un solo uso.",
    "Ahorra energía apagando las luces cuando no las necesites.",
    "Usa productos reutilizables como botellas y bolsas.",
    "Compra productos locales para reducir la huella de carbono.",
    "Planta árboles o cuida de las áreas verdes cercanas.",
    "Evita desperdiciar agua, cierra el grifo cuando no lo uses.",
    "Opta por energías renovables si es posible.",
    "Participa en limpiezas de espacios públicos como playas o parques."
]





@bot.event
async def on_ready():
    print(f'Hemos iniciado sesión como {bot.user}')

@bot.command()
async def consejo(ctx):
    consejo = random.choice(consejos)
    await ctx.send(consejo)
@bot.command()
async def meme_comparacion(ctx):
    with open('images/Drakememe.jpg', 'rb') as f:
        
        picture = discord.File(f)
    await ctx.send(file=picture)
@bot.command()
async def meme_aliens(ctx):
    with open('images/memealiens.jpg', 'rb') as f:
        
        picture = discord.File(f)
    await ctx.send(file=picture)
@bot.command()
async def quiz(ctx):
    preguntas = [
        ("¿Reciclas las botellas de plastico?"),
        ("¿Usas transporte público o bicicleta regularmente?"),
        ("¿Apagas las luces cuando sales de una habitación?"),
        ("¿Cierras el grifo cuando te lavas los dientes?"),
    ] 
    puntaje = 0
    for pregunta in preguntas: 
        await ctx.send(pregunta)   
        try:
            mensaje = await bot.wait_for('message', timeout=30.0)
            if mensaje.content.lower() in ["sí", "si"]:
                puntaje += 1
        except TimeoutError:
            await ctx.send("Tiempo agotado para responder.")
    await ctx.send(f"Felicidades, realizas {puntaje} acciones que ayudan al medio ambiente.")
        
bot.run('Token')

