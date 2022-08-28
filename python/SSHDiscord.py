

    
# import discord
# from discord.ext import commands
# import asyncio
# import paramiko
# import time


# client = commands.Bot(command_prefix = '.')

# @client.event
# async def on_ready():
#     print('Bot is ready')


# @client.command()
# async def ping(ctx):
#     await ctx.send(f'Pong! {round(client.latency * 1000)}ms')


# @client.command()
# @commands.is_owner()
# async def connect(ctx):

#     #Connect to the server using paramiko and SSHClient()

#     ssh = paramiko.SSHClient()
#     ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
#     ssh.connect('192.168.2.64', username='root', password='bhSuperNukeCat06')

#     #Send a message to the user that they are connected

#     await ctx.send('Connected!')

#     #Wait for the user to type in a command and then send it to the server

#     while True:
#         msg = await client.wait_for('message')
#         if msg.content == 'exit':
#             break
#         else:
#             stdin, stdout, stderr = ssh.exec_command(msg.content)
#             output = stdout.readlines()
#             await ctx.send(output)

#     #Close the connection when the user types exit

#     ssh.close()

#     await ctx.send('Disconnected!')



import discord
from discord.ext import commands
import asyncio
import paramiko
import time
import sys


client = commands.Bot(command_prefix = '!')


@client.event
async def on_ready():
    print ("\n Ready to make some connections, yaknow? \n")


@client.command()
async def ping(ctx):
    await ctx.send(f'Pong! {round(client.latency * 1000)}ms')


@client.command()
async def connect(ctx, ip, username, password):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    try:
        ssh.connect(ip, username=username, password=password)

        channel = ctx.message.channel

        while True:
            await channel.send('Enter a command')

            def check(m):
                return m.author == ctx.message.author and m.channel == channel

            msg = await client.wait_for('message', check=check)

            if msg is not None:
                command = msg.content

                if command == 'exit':
                    break

                stdin, stdout, stderr = ssh.exec_command(command)

                result = stdout.read().decode('utf-8') + stderr.read().decode('utf-8')

                await channel.send(result)

    except Exception as e:
        print('Connection Failed')
        print(e)



token = ""
client.run(token, bot=False)

