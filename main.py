import discord
from discord.ext import commands
from discord.ext.commands import CommandNotFound
from discord.ext.commands import has_permissions, MissingPermissions
from discord import Member


bot = commands.Bot(command_prefix='-')

@bot.command()
@has_permissions(manage_roles=True, ban_members=True)
async def am(ctx):
    if ctx.message.author.guild_permissions.administrator:
        tmp = ctx.message.content.split(" ",1)


   

    if len(tmp) == 1:
        await ctx.message.channel.send("error:Cannot send an empty message")
    else:
        await ctx.message.channel.send(tmp[1])


bot.run('TOKEN') 