import discord
import random

TOKEN = input("Enter your bot token: ")
RANDOM_EMOJIS = [':ok_hand:', ':100:', ':banana:', ':monkey_face:', ':sunglasses:', ':thinking:', ':yum:', ':weary:', ':poop:', ':smiling_imp:', ':scream_cat:']

client = discord.Client()

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('!memify'):
        params = message.content.split()
        memes = [random.choice(RANDOM_EMOJIS) for param in params[1:]]
        meme_text = []
        for meme, param in zip(memes, params[1:]):
            meme_text.append(meme)
            meme_text.append(param)
        meme_text = ' '.join(meme_text)
        await client.send_message(message.channel, meme_text)

@client.event
async def on_ready():
    print(f'Logged in as: {client.user.name}')

client.run(TOKEN)