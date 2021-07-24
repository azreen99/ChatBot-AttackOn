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
cafeQ = [
    "How many cafes are there in UTP?",
    "There are 11 cafes available in UTP such as V1 V2 V3 V4 V5 V6 Cafe Sayang Pocket C Al-Marjan TEEPEE Cafe Pocket D",
    "Usual operation hours for cafes?",
    "Most cafes are available starting from 7:00AM till 12:00PM",
    "V1 cafe",
    "V1 cafe is located near UTP bus station",
    "V4 cafe location",
    "V4 cafe is located near UTP post office station",
    "V2 cafe menu for today",
    "There are roti canai, nasi lemak, mee goreng and more!",
    "The nearest cafe around Block K?",
    "Nearest cafe around Block K are Cafe Sayang & Al-Marjan",
    "Cafe that sell pizza?",
    "V1 cafe are selling various types of pizza Lets give a visit!"
]
sport_facility = [
    "badminton",
    "At block A",
    "swimming",
    "In front mosque"
]

trainer = ListTrainer(bot)
for items in (weather, cafeQ, sport_facility, conversation):
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
