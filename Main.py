"""Programa para um bot de discord

Autor:
@Celio Ludwig Slomp
Instagram: celio.ls
Twitter: celio_ls_
Github: https://github.com/CelioSlomp
"""

import discord
from discord.ext import commands
import random
import youtube_dl
from invisivel import token

# Foi criado o objeto 'cliente' para setar os eventos e comandos 
# usados posteriormente.
usuario = commands.Bot(command_prefix=":")

# Quando rodar o programa, o bot estará funcionando a partir 
# do momento que printar 'Bot está online.' no cmd/terminal.
@usuario.event
async def on_ready():
    print("Bot está online.")

@usuario.command()
async def xingar(ctx, user):
    await ctx.send(f"Aí, de boa, vai tomar no cu {user}")

# É para mostrar todos os comandos que o bot possui. Por enquanto
# contando com os de placeholder, possuem 4 comandos.
@usuario.command()
async def commands(ctx):
    await ctx.send("Por enquanto não temos comandos T-T")

# Dá clear no chat, comando muito útil porém perigoso.
@usuario.command()
async def clear(ctx, quantidade=5): # Adicionar uma certa restrição para
    await ctx.channel.purge(limit=quantidade) # quem pode utilizar isso.

# Caso o usuário digite 'salve' no chat, o bot irá responder com alguma
# frase da lista 'lista_salve'.
@usuario.event
async def on_message(message):
    if message.author == usuario.user:
        return
    
    if message.content.lower() == 'salve':
        lista_salve = ["Salve man", "Nem sempre mando salve tlgd", 
                       "SALVEEEEE FMLL", "qqpegazé, salve aí irmão"]
        response = random.choice(lista_salve)
        await message.channel.send(response)

# Fará com que o bot entre dentro do canal em que o usuário está.
@usuario.command(pass_context=True)
async def entrar(ctx):
    canal = ctx.author.voice.channel
    await canal.connect()
    
# Fará com que o bot desconecte do canal que está.
@usuario.command(pass_context=True)
async def sair(ctx):
    await ctx.voice_client.disconnect()

# Aqui irá 'linkar' o código com o bot do Discord.
usuario.run(token)