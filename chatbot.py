from flask import Flask, render_template, request
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
from chatterbot.trainers import ListTrainer

app = Flask(__name__)

with open('file.txt', 'r') as file:
    conversation = file.read()

botname = "PetroBot"
bot = ChatBot(
    botname,
    logic_adapters=["chatterbot.logic.MathematicalEvaluation",
                    "chatterbot.logic.BestMatch"
                    ])

weather = [
    "What's the weather today?",
    "So hot!!",
    "Bila nak hujan",
    "Tahla, esok kot",
    "Mana masjid?",
    "Dekat tasik"
]
cafe = [
    "What's the weather today?",
    "So hot!!",
    "Bila nak hujan",
    "Tahla, esok kot",
    "Mana masjid?",
    "Dekat tasik"
]
sport_facility = [
    "badminton",
    "At block A",
    "swimming",
    "In front mosque"
]

trainer = ListTrainer(bot)
for items in (weather, cafe, sport_facility, conversation):
    trainer.train(items)

# corpus_trainer = ChatterBotCorpusTrainer(bot)
# corpus_trainer.train("chatterbot.corpus.english")

trainer.export_for_training('./my_export.json')


@app.route("/")
def home():
    return render_template("home.html", botname=botname)


@app.route("/get")
def get_bot_response():
    userText = request.args.get('msg')
    return str(bot.get_response(userText))


if __name__ == "__main__":
    app.run(port=5500)
