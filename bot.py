import discord
import os

client = discord.Client()

@client.event
async def on_ready():
    print("Даров, бать")

@client.event
async def on_raw_reaction_add(payload):
    message_id = payload.message_id
    if message_id == 711260552592359555:
        guild_id = payload.guild_id
        guild = discord.utils.find(lambda g : g.id == guild_id, client.guilds)

        if payload.emoji.name == 'r6':
            role = discord.utils.get(guild.roles, name='r6')
        elif payload.emoji.name == 'minecraft':
            role = discord.utils.get(guild.roles, name='minecraft')
        elif payload.emoji.name == 'farcry':
            role = discord.utils.get(guild.roles, name='farcry')
        elif payload.emoji.name == 'gmod':
            role = discord.utils.get(guild.roles, name='gmod')
        elif payload.emoji.name == 'payday2':
            role = discord.utils.get(guild.roles, name='payday2')
        elif payload.emoji.name == 'apex':
            role = discord.utils.get(guild.roles, name='apex')
        elif payload.emoji.name == 'gta5':
            role = discord.utils.get(guild.roles, name='gta5')
        elif payload.emoji.name == 'pubg':
            role = discord.utils.get(guild.roles, name='pubg')
        else:
            role = discord.utils.get(guild.roles, name = payload.emoji.name)

        if role is not None:
            member = discord.utils.find(lambda m : m.id == payload.user_id, guild.members)
            if member is not None:
                await member.add_roles(role)
                print('Done')
            else:
                print('Member not found')
        else:
            print('Role not found')

@client.event
async def on_raw_reaction_remove(payload):
    message_id = payload.message_id
    if message_id == 711260552592359555:
        guild_id = payload.guild_id
        guild = discord.utils.find(lambda g : g.id == guild_id, client.guilds)

        if payload.emoji.name == 'r6':
            role = discord.utils.get(guild.roles, name='r6')
        elif payload.emoji.name == 'minecraft':
            role = discord.utils.get(guild.roles, name='minecraft')
        elif payload.emoji.name == 'farcry':
            role = discord.utils.get(guild.roles, name='farcry')
        elif payload.emoji.name == 'gmod':
            role = discord.utils.get(guild.roles, name='gmod')
        elif payload.emoji.name == 'payday2':
            role = discord.utils.get(guild.roles, name='payday2')
        elif payload.emoji.name == 'apex':
            role = discord.utils.get(guild.roles, name='apex')
        elif payload.emoji.name == 'gta5':
            role = discord.utils.get(guild.roles, name='gta5')
        elif payload.emoji.name == 'pubg':
            role = discord.utils.get(guild.roles, name='pubg')
        else:
            role = discord.utils.get(guild.roles, name = payload.emoji.name)

        if role is not None:
            member = discord.utils.find(lambda m : m.id == payload.user_id, guild.members)
            if member is not None:
                await member.remove_roles(role)
                print('Done')
            else:
                print('Member not found')
        else:
            print('Role not found')

token = os.environ.get('BOT_TOKEN')
run.bot(str(token))
        