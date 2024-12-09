import discord
from discord.ext import commands
from model import get_class


intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Hi! I am a bot {bot.user}!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

@bot.command()
async def checker(ctx):
    if ctx.message.attachments:
        for attachment in ctx.message.attachments:
            file_name = attachment.filename
            file_url = attachment.url
            await ctx.send("Archivo guardado...")
            await attachment.save(f"./{file_name}")

            try:
                class_name = get_class("keras_model.h5", "labels.txt", file_name)
                if class_name[0] == "Fuente":
                    await ctx.send("Esta es la fuente de un computador, puede ir ubicada en la parte superior o inferior del gabinete")

                elif class_name[0] == "Fuente":
                    await ctx.send("Esta es la fuente de un computador, puede ir ubicada en la parte superior o inferior del gabinete")

                elif class_name[0] == "Cooler":
                    await ctx.send("Esto es un cooler, el enfriamiento del computador. Puede ir ubicado en la parte superior del gabinete, en la parte frontal del gabinete, en la parte inferior del gabinete, en la parte trasera del gabinete o en el disipador del CPU")

                elif class_name[0] == "Procesador":
                    await ctx.send("Esto es un procesador, la mente de toda computadora. Va ubicado en el socket indicado en la placa madre")

                elif class_name[0] == "Placa madre":
                    await ctx.send("Esta es una placa madre, va ubicada dentro de la base del gabinete")

                elif class_name[0] == "Tarjeta grafica":
                    await ctx.send("Esta es una tarjeta grafica, va ubicada en la ranura PCle de la placa madre")

                elif class_name[0] == "Tarjeta de audio":
                    await ctx.send("Esta es la tarjeta de audio del computador, es la base sonora del pc. Va ubicada en la parte externa del gabinete asi como en la parte interna del gabinete.")

                elif class_name[0] == "Memoria RAM":
                    await ctx.send("Esta es una memoria RAM, la memoria temporal del ordenador. Van ubicadas en las ranuras DIMM (Dual Inline Memory Module) de la placa madre.")

                elif class_name[0] == "Disco duro":
                    await ctx.send("Esto es un disco duro, el espacio y almacenamiento de archivos del pc. Van ubicados en las bahías del gabinete del PC.")

                elif class_name[0] == "Puertos USB":
                    await ctx.send("Esto son los puertos USB, un tipo de puerto para diferentes periféricos. Estos pueden ir ubicados en la parte frontal del gabinete, en la parte trasera del gabinete y en los laterales del gabinete.")

                elif class_name[0] == "Unidad óptica":
                    await ctx.send("Esta es una unidad optica, el lector de cds de los pcs. Va ubicada en la parte frontal del gabinete.")

                elif class_name[0] == "Gabinete":
                    await ctx.send("Este es el gabinete, la base que soporta todo el computador. Por lo tanto es la estructura del pc.")

            except:
                await ctx.send("Ha ocurrido un error, usaste una imagen?...")
    else:
        await ctx.send("Olvidaste subir una imagen...")

bot.run("TU TOKEN")