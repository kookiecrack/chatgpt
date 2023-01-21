import discord
import requests
import json


# Initialize the Discord client
intents = discord.Intents.all()
client = discord.Client(intents=intents)

# Set the OpenAI API key
api_key = '<YOUR APIKEY HERE>'

@client.event
async def on_message(message):
    # Check if the message is from the bot
    if message.author == client.user:
        return

    # Send the message to the OpenAI API and get the response
#    response = requests.post('https://api.openai.com/v1/engines/davinci-codex/completions',
    response = requests.post('https://api.openai.com/v1/engines/text-davinci-003/completions',
                             headers={'Content-Type': 'application/json',
                                     'Authorization': f'Bearer {api_key}'},
                             json={'prompt': message.content,
                                   'temperature': 0, 'max_tokens':2000})
    block_size = 2000
    response_text = response.json()['choices'][0]['text']
    if len(response_text) < 2000:
        # Send the response back to the channel
        await message.channel.send(response_text)
    else:
        for i in range(0, len(response_text), block_size):
            await message.channel.send(response_text[i:i+block_size])

# Run the Discord client
client.run('<YOUR TOKEN HERE>')
