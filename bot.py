import discord
from discord.ext import commands
import random
from discord.utils import get
import shutil
import json
import asyncio
import os
from itertools import cycle
import colorsys
from discord import Game, Embed, Color, Status, ChannelType
import datetime
import sqlite3
import math
import sys, traceback
import time
from datetime import timedelta
from collections import OrderedDict, deque, Counter


Bot = commands.Bot(command_prefix = ".")

Bot.remove_command('help')


@Bot.event
async def on_ready():
    print("Даров, бать")

@Bot.event
async def on_command_error(ctx, error):
    pass

@Bot.command(pass_context= True)
@commands.has_permissions(manage_messages =True)
async def clear(ctx, amount = 100):
    await ctx.channel.purge(limit = amount)
 
@Bot.event
async def on_voice_state_update(member,before,after):
    if after.channel.id == 727774763522457640:
        for guild in Bot.guilds:
            maincategory = discord.utils.get(guild.categories, id=727502849172439061)
            channel2 = await guild.create_voice_channel(name=f"{member.display_name}",category = maincategory)
            await channel2.set_permissions(member,connect=True,mute_members=True,move_members=True,manage_channels=True)
            await member.move_to(channel2)
            def check(x,y,z):
                return len(channel2.members) == 0
            await Bot.wait_for('voice_state_update',check=check)
            await channel2.delete()

@Bot.command(pass_context = True)
@commands.has_permissions(administrator = True)

async def kick(ctx, member: discord.Member, *, reason = None):
    await ctx.channel.purge(limit = 1)
    emb = discord.Embed(title = 'Kick', colour = discord.Color.purple())

    await member.kick(reason = reason)
    emb.set_author(name = member.name, icon_url = member.avatar_url)
    emb.add_field(name = 'Kick', value = 'Пинком был изгнан {}'.format(member.mention))
    await ctx.send(embed = emb)
    await member.send(embed = discord.Embed(title = 'Вас выгнали с сервера Dark Side!', colour = discord.Color.purple()))

@Bot.command(pass_context = True)
@commands.has_permissions(administrator = True)

async def ban(ctx, member: discord.Member, *, reason = None):
    await ctx.channel.purge(limit = 1)
    emb = discord.Embed(title = 'Ban', colour = discord.Color.red())
    

    await member.ban(reason = reason)

    emb.set_author(name = member.name, icon_url = member.avatar_url)
    emb.add_field(name = 'Banned', value = 'Великая печать изгнания возложена на {}'.format(member.mention))
    emb.set_footer(text = 'Был забанен администратором {}'.format(ctx.author.name), icon_url = ctx.author_url)
    await ctx.send(embed = emb)
    await member.send(embed = discord.Embed(title = 'Вы были забанены администратором{}'.format(ctx.author.name), icon_url = ctx.author_url, colour = discord.Color.red()))

@Bot.command(pass_context= True)
@commands.has_permissions(administrator = True)

async def unban(ctx, *, member):
    await ctx.channel.purge(limit = 1)

    banned_users = await ctx.guild.bans()


    for ban_entry in banned_users:
        user = ban_entry.user
        emb = discord.Embed(title = 'Unban', colour = discord.Color.green())


        await ctx.guild.unban(user)
        emb.set_author(name = member.name)
        
        await ctx.send(f'Великая печать бана снята с {user.menttion}')

        return

@Bot.command(pass_context = True)
async def vcreate(ctx, *, member):
    await ctx.channel.purge(limit = 1)
    limit = 5
    name = f"{member.name}"
    #category = Bot.get_channel('727502849172439061')
    channel1 = await member.guild.create_text_channel(name)
    await member.move_to(channel1)
    await channel1.set_permissions(Bot.user, connect=True,read_messages=True)
    await channel1.edit(name= name, user_limit = limit)
    await ctx.send(f'{member.mention}, канал создан')

@Bot.command(pass_context= True)
async def help(ctx):
    emb = discord.Embed(title = 'Команды:')

    emb.add_field(name = 'clear', value = 'Очичтка чата')
    emb.add_field(name = 'kick', value = 'Выгнать участника с сервера')
    emb.add_field(name = 'ban', value = 'Забанить участника')
    emb.add_field(name = 'unban', value = 'Розбанить участника')
    emb.add_field(name = 'say', value = 'Отправить сообщение от имени бота')
    emb.add_field(name = 'send', value = 'Отправить личное сообщение от имени бота')
    emb.add_field(name = 'fck', value = 'Послать к трём чертям')
    emb.add_field(name = 'hug', value = 'Обнять')
    emb.add_field(name = 'kiss', value = 'Поцеловать')
    emb.add_field(name = 'kill', value = 'Убить')

    await ctx.send(embed = emb)

@Bot.command()
@commands.has_permissions(manage_messages =True)
async def say(ctx, *, msg):
    await ctx.message.delete()
    await ctx.send("{}".format(msg))

@Bot.command()
async def fck(ctx, member: discord.Member):
    await ctx.message.delete()
    await ctx.send(f"{ctx.author.mention} послал(a) к трём чертям {member.mention}")


@Bot.command()
async def hug(ctx, member: discord.Member):
    await ctx.message.delete()
    await ctx.send(f"{ctx.author.mention} обнял(а) {member.mention}")

@Bot.command()
async def artic(ctx, member: discord.Member):
    await ctx.message.delete()
    await ctx.send(f"{ctx.author.mention} росчленил(а) {member.mention}")

@Bot.command()
async def kiss(ctx, member: discord.Member):
    await ctx.message.delete()
    await ctx.send(f"{ctx.author.mention} поцеловал(а) {member.mention}")

@Bot.command()
async def kill(ctx, member: discord.Member):
    await ctx.message.delete()
    await ctx.send(f"{ctx.author.mention} убил (а) {member.mention}")

@Bot.command()
async def burn(ctx, member: discord.Member):
    await ctx.message.delete()
    await ctx.send(f"{ctx.author.mention} кинул(а) {member.mention} в крематорий")

@Bot.command()
async def sex(ctx, member: discord.Member):
    await ctx.message.delete()
    await ctx.send(f"{ctx.author.mention} подверг(ла) к жесткому сексу {member.mention}")

@Bot.command()
async def suicide(ctx, member: discord.Member):
    vvr = ['утонул(а) в луже', 'умер(ла) на унитазе', 'умер(ла) во время мастурбауии', 'утонул(ла) в луже', 'героически погиб(ла) сражаясь за печеньку', 'умер(ла), причина: кусь']
    await ctx.message.delete()
    await ctx.send(f"{ctx.author.mention}, {random.choice(vvr)}")
 

@Bot.command()
@commands.has_permissions( administrator = True)
async def send(ctx, member: discord.Member, *, msg):
    await ctx.message.delete()
    await member.send('{}'.format(msg))
    await ctx.send('Сообщение отправлено')
    


@Bot.command()
async def ping(ctx):
    await ctx.send("Pong!")

@Bot.command()
async def king(ctx):
    await ctx.send("Kong!")

@ban.error
async def error_command(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.send(embed = discord.Embed(title = '{} у вас недостаточно прав!'.format(ctx.author.name), colour = discord.Color.red()))
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send(embed = discord.Embed(title = '{} укажите аргумент!'.format(ctx.author.name), colour = discord.Color.red()))


@kick.error
async def kick_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.send(embed = discord.Embed(title = '{} у вас недостаточно прав!'.format(ctx.author.name), colour = discord.Color.red()))
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send(embed = discord.Embed(title = '{} укажите аргумент!'.format(ctx.author.name), colour = discord.Color.red()))

token = os.environ.get('BOT_TOKEN')
Bot.run(str(token))
        