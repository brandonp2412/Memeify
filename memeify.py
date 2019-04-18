import discord
import random

token = input("Enter your bot token: ")
RANDOM_EMOJIS = [':ok_hand:', ':100:', ':banana:', ':monkey_face:', ':sunglasses:', ':thinking:', ':yum:', ':weary:', ':poop:', ':smiling_imp:', ':scream_cat:']

client = discord.Client()

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('!memeify'):
        params = message.content.split()
        memes = [random.choice(RANDOM_EMOJIS) for param in params[1:]]
        meme_text = []
        for meme, param in zip(memes, params[1:]):
            meme_text.append(meme)
            meme_text.append(param)
        meme_text = ' '.join(meme_text)
        log(message, meme_text)
        await client.send_message(message.channel, meme_text)

@client.event
async def on_ready():
    print(f'[INFO] -- Logged in as: {client.user.name}')

def log(message, meme_text):
    print(f"[INFO] -- User: {message.author} inputted: {message.content}")
    print(f"[INFO] -- User: {message.author} got output: {meme_text}")

client.run(token)
