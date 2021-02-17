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
from invisivel import token

# Foi criado o objeto 'cliente' para setar os eventos e comandos 
# usados posteriormente.
cliente = commands.Bot(command_prefix="&")

# Quando rodar o programa, o bot estará funcionando a partir 
# do momento que printar 'Bot está online.' no cmd/terminal.
@cliente.event
async def on_ready():
    print("Bot está online.")

# @Placeholder, serve apenas para teste de comandos.
@cliente.command()
async def ping(ctx):
    await ctx.send("Pong!")

# @Placeholder, serve apenas para teste de comandos.
@cliente.command()
async def pong(ctx):
    await ctx.send("Não cara, deu, tá chatão já")

# É para mostrar todos os comandos que o bot possui. Por enquanto
# contando com os de placeholder, possuem 4 comandos.
@cliente.command()
async def commands(ctx):
    await ctx.send("Por enquanto nós temos os seguintes comandos: \n\
&ping - Irá ter uma resposta legal - \n\
&pong - Irá ter outra resposta legal -")

# Dá clear no chat, comando muito útil porém perigoso.
@cliente.command()
async def clear(ctx, quantidade=5): # Adicionar uma certa restrição para
    await ctx.channel.purge(limit=quantidade) # quem pode utilizar isso.

# Aqui irá 'linkar' o código com o bot do Discord.
cliente.run(token)
             