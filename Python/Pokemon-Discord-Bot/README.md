# Discord Pokemon Info Bot
This is a simple Discord bot that allows users to request information about a specific Pokemon using the **PokeAPI**. The bot is built using the **discord.py** library, which is a Python wrapper for the Discord API.

## Features
The bot is able to respond to the command "!hello" by sending the message "hello!" in the same channel that the command was sent.
The bot is able to respond to the command "!info [Pokemon name]" by returning the name, type, and an image of the Pokemon, as well as its description. The info is returned in an Embed message.
Usage
To use the bot, you will first need to create a Discord bot and invite it to your server. You can do this by following [these instructions](https://discordpy.readthedocs.io/en/latest/discord.html).

Once the bot is added to your server, you can use the commands as described above.

## Requirements
This code requires the following modules to be installed:

## discord.py
requests
json
You can install these modules using pip by running:
```bash
pip install -r requirements.txt.
```

## Note
You will need to replace the bot token in the client.run() function with the token for your own bot.

## Run the code
You can run the code using python interpreter, if you have python installed in your system:
```bash
python filename.py
```

and then in your discord server you can call the bot commands.
