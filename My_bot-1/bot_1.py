#Import Discord Package
from asyncio.windows_events import NULL
from pickle import TRUE
from unicodedata import name
import discord
import os

#client(it's our bot yay!)
from code import token

code = token
client = discord.Client()



@client.event
async def on_ready():

    #do stuff

    general_channel = client.get_channel(843385071833972778)

    await general_channel.send('get ready to get awesome pictures')

# @client.event
# async def on_message(message):

#     if message.content == '!!dawn':
#         my_embed = discord.Embed(title="Captured_here", description="Hello there here is the command list.", color=0xffd700)
#         imageURL = "https://media.istockphoto.com/photos/freedom-chains-that-transform-into-birds-charge-concept-picture-id1322104312?b=1&k=20&m=1322104312&s=170667a&w=0&h=VQyPkFkMKmo0e4ixjhiOLjiRs_ZiyKR_4SAsagQQdkk="
#         my_embed = discord.Embed(title="Dawn", description="Beautiful morning with the chirpping birds", color=0xF4C2C2) #creates my_embed
#         my_embed.set_image(url=imageURL)
#         general_channel = client.get_channel(843385071833972778)
#         await general_channel.send(embed = my_embed)



@client.event
async def on_message(message):
    
    if message.content == '!!help':
        
        # file = discord.File("D:\VSCode\discord_bot_project\My_bot-1\help.txt", filename="Need_help.txt")
        embed = discord.Embed(title="Captured_here", description="Hello there here is the command list.", color=0xffd700)
        embed.add_field(name="!!dawn",value="gives picture of dawn",inline=False)
        embed.add_field(name="!!tiger",value="gives picture of tiger",inline=False)
        embed.add_field(name="!!armour",value="gives picture of armour",inline=False)
        embed.add_field(name="!!cat",value="gives picture of cat",inline=False)
        embed.add_field(name="!!kitten",value="gives picture of kitten",inline=False)
        embed.add_field(name="!!monroe",value="gives picture of Marllin Monroe",inline=False)
        embed.add_field(name="!!dodinsky",value="gives picture of quote by dodinsky",inline=False)
        general_channel = client.get_channel(843385071833972778)
        await general_channel.send(embed = embed)

    if message.content == '!!dawn':
        imageURL = "https://media.istockphoto.com/photos/freedom-chains-that-transform-into-birds-charge-concept-picture-id1322104312?b=1&k=20&m=1322104312&s=170667a&w=0&h=VQyPkFkMKmo0e4ixjhiOLjiRs_ZiyKR_4SAsagQQdkk="
        embed = discord.Embed(title="Dawn", description="Beautiful morning with the chirpping birds", color=0xF4C2C2) #creates embed
        embed.set_image(url=imageURL)
        general_channel = client.get_channel(843385071833972778)
        await general_channel.send(embed = embed)
    
    if message.content == '!!tiger':
        imageURL = "https://images.unsplash.com/photo-1641236247216-1c3ab02c9e57?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHx0b3BpYy1mZWVkfDR8SnBnNktpZGwtSGt8fGVufDB8fHx8&auto=format&fit=crop&w=600&q=60"
        embed = discord.Embed(title="Tiger", description="Be the Tiger", color=0xF4C2C2) #creates embed
        embed.set_image(url=imageURL)
        general_channel = client.get_channel(843385071833972778)
        await general_channel.send(embed = embed)
    
    if message.content == '!!armour':
        imageURL = "https://images.unsplash.com/photo-1642603437713-29c53824023c?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHx0b3BpYy1mZWVkfDE3fGRpanBidzk5a1FRfHxlbnwwfHx8fA%3D%3D&auto=format&fit=crop&w=600&q=60"
        embed = discord.Embed(title="Armour", description="relic of the past the armour", color=0xF4C2C2) #creates embed
        embed.set_image(url=imageURL)
        general_channel = client.get_channel(843385071833972778)
        await general_channel.send(embed = embed)

    if message.content == '!!cat':
        imageURL = "https://images.unsplash.com/photo-1615789591457-74a63395c990?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxzZWFyY2h8MXx8ZG9tZXN0aWMlMjBjYXR8ZW58MHx8MHx8&w=1000&q=80"
        embed = discord.Embed(title="Cat", description="Dedicated to  MI_LADY", color=0xF4C2C2) #creates embed
        embed.set_image(url=imageURL)
        general_channel = client.get_channel(843385071833972778)
        await general_channel.send(embed = embed)

    if message.content == '!!kitten':
        imageURL = "https://hips.hearstapps.com/hmg-prod.s3.amazonaws.com/images/cat-quotes-1543599392.jpg?crop=1.00xw:0.759xh;0,0&resize=980:*"
        embed = discord.Embed(title="Kitten", description="Loaded with cuteness", color=0xF4C2C2) #creates embed
        embed.set_image(url=imageURL)
        general_channel = client.get_channel(843385071833972778)
        await general_channel.send(embed = embed)
    
    if message.content == '!!monroe':
        imageURL = "https://images.gr-assets.com/quotes/1511992603p8/8630.jpg"
        embed = discord.Embed(title="Marlin_Monroe", description="Queen's Here", color=0xF4C2C2) #creates embed
        embed.set_image(url=imageURL)
        general_channel = client.get_channel(843385071833972778)
        await general_channel.send(embed = embed)

    if message.content == '!!dodinsky':
        imageURL = "http://www.reckontalk.com/wp-content/uploads/2014/12/10-Inspirational-Quotes-To-Enrich-Your-Life-1.jpg"
        embed = discord.Embed(title="Dodinsky", description="In the garden of thoughts", color=0xF4C2C2) #creates embed
        embed.set_image(url=imageURL)
        general_channel = client.get_channel(843385071833972778)
        await general_channel.send(embed = embed)

    
        

#run the client the server
client.run(give the token here)


 