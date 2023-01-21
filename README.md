# chatGPT Discord Bot
- Send/receive messages to/from chatGPT via Discord. 

### Configure your Discord settings
- Go to https://discord.com/developers/applications > New Application
- Settings > Bot > Reset Token 
- Copy this token. U will need it for the python script.
- Privileged Gateway Intents > turn on all 3 intents
- Concurrently, go to your Discord app and create a server for yourself.
- Using Discord Developer Portal > select OAUTH2 > URL Generator > Scopes (Bot) > Bot Permissions > select everything related to messages and threads 
- Use the generated url > select your newly created server > authorize access 

### Configure your chatGPT settings
- Go to https://beta.openai.com/overview > Personal > View API keys > create new secret key 
- Copy this API key. U will need it for the python script

### Install or Update 
- pip3 install discord

### Using the python script
- Enter your chatGPT API key and Discord Token into the relevant fields stated in python script.
- Run `python3 chatgpt_bot.py`
- Now you can send/receive messages to/from chatGPT via Discord (even discord mobile app).

### Additional Notes
- Consider using a raspberry pi to run the python script.
- Credit goes to chatGPT for helping me refine this python script :P
