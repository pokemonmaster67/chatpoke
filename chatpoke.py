# This code is based on the following example:
# https://discordpy.readthedocs.io/en/stable/quickstart.html#a-minimal-bot

import discord
import random

client = discord.Client()

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith("$"):
        command = message.content[1:]

        if command == "help":
            await message.channel.send("I can answer your questions and generate creative text formats of text content. Just type in a question or a prompt and I will try my best to answer it or generate something creative.")

        elif command in prompts:
            answer = answers[command]
            await message.channel.send(answer)

        elif command in creative_text_formats:
            await message.channel.send(random.choice(creative_text_formats[command]))

        else:
            await message.channel.send("I don't know how to answer that question.")

prompts = {
    "what is the capital of france?": "Paris",
    "what is the square root of 16?": "4",
    "what is the meaning of life?": "42",
  "is there a mario movie 2 yet?": "no",
    "can you code?": "no",
    "are you a chatbot?": "yes",
  "what can you do?": "a lot",
  "version": "V0.1",
"are you free?": "yes"
  
}

answers = {
    "what is the capital of france?": "Paris is the capital of France.",
    "what is the square root of 16?": "4 is the square root of 16.",
    "what is the meaning of life?": "The meaning of life is a question that has been pondered by philosophers and theologians for centuries. There is no one answer that everyone agrees on, but some possible answers include finding happiness, making a difference in the world, or simply living each day to the fullest.",
 "is there a mario movie 2 yet?": "there is no mario movie 2 yet.",
    "are you a chatbot?": "yes i am a chatbot but i am a small chatbot.",
"can you code?": "no i can't.",
    "what can you do?": "i can answer small questions but some questions doesnt work because i am a really really small language model but i will grow a lot in the future weeks.",
 "version": "right now i am V0.1 but soon it will be V1.0 very soon.",
  "are you free?": "yes i am always free to use i will never cost money."
}

creative_text_formats = {
    "poem": ["Roses are red, violets are blue, I am a large language model, and I can write poems for you."],
    "code": ["`python\nprint('Hello, world!')\n`"],
    "script": ["FADE IN:"],
    "email": ["Dear [RECIPIENT_NAME],"],
    "letter": ["Dear [RECIPIENT_NAME],"],
}

client.run("MTExNzk1NDU0NDI5OTY4Mzg0MA.GBFeOG.qCrcyRfUzS_f9qiOIGsOB26UDjk4ldEx6x_tXw")
