from flask import Flask, render_template, request
from nltk.chat.util import Chat, reflections

app = Flask(__name__)

# Define a list of questions for user reference
questions_list = [
    "my name is (.*)",
    "what do you do?",
    "what crops should I grow in (.*) season?",
    "how can I improve soil fertility?",
    "how do I conserve water on my farm?",
    "what is crop rotation?",
    "how do I control pests naturally?",
    "what are the benefits of organic farming?",
    "hi|hey|hello",
    "what is your name?|your name|name please",
    "how are you?|how you doing|what about you|how about you?",
    "show questions|list questions",
    "what are some farming techniques?"
]

# List of farming techniques
farming_techniques = [
    "Crop Rotation: Grow different crops in succession to improve soil health.",
    "Drip Irrigation: A method to deliver water directly to the roots.",
    "Organic Fertilizers: Use compost or manure to enhance soil fertility.",
    "Cover Cropping: Plant cover crops to prevent soil erosion.",
    "Integrated Pest Management: Combine biological, cultural, and chemical tools."
]

# Define conversation pairs for the chatbot
pairs = [
    [
        r"my name is (.*)",
        ["Hello %1, How are you today ?",]
    ],
    [
        r"what do you do?",
        ["I am a ChatBot which provides various Farming Techniques for Agricultural encouragement🙌",]
    ],
    [
        r"show questions|list questions",
        ["Here are some questions you can ask me:<br>" + "<br>".join(questions_list),]
    ],
    [
        r"what crops should I grow in (.*) season?",
        ["For %1 season, you might consider growing crops like wheat, barley, and oats if it's winter, or corn, soybeans, and tomatoes if it's summer.",]
    ],
    [
        r"how can I improve soil fertility?",
        ["To improve soil fertility, consider using organic compost, practicing crop rotation, and planting cover crops like clover or rye.",]
    ],
    [
        r"how do I conserve water on my farm?",
        ["You can conserve water by implementing drip irrigation, using mulch to retain soil moisture, and collecting rainwater for irrigation."
         "\nYou can learn more about it here: "
         "<a href='/static/waterconserve.pdf' target='_blank'>Water Conservation PDF</a>.",]
    ],
    [
        r"what is crop rotation?",
        ["Crop rotation involves growing different crops in succession. "
         "You can learn more about it here: "
         "<a href='/static/croprotation.pdf' target='_blank'>Crop Rotation PDF</a>.",]
    ],
    [
        r"how do I control pests naturally?",
        ["For natural pest control, consider integrated pest management (IPM), which includes using beneficial insects, planting pest-repellent plants, and using organic pesticides."
         "You can learn more about it here: "
         "<a href='/static/pestcontrol.pdf' target='_blank'>Pest Control PDF</a>.",]
    ],
    [
        r"what are the benefits of organic farming?",
        ["Organic farming enhances soil fertility, reduces chemical usage, promotes biodiversity, and can increase long-term sustainability of the farm."
         "You can learn more about it here: "
         "<a href='/static/OrganicFarming.pdf' target='_blank'>Organic Farming PDF</a>.",]
    ],
    [
        r"hi|hey|hello",
        ["Hello", "Hey there",]
    ], 
    [
        r"what is your name ?|your name|name please",
        ["I am a Chatbot which suggests various farming techniques!","I am your assistant!"]
    ],
    [
        r"how are you ?|how you doing|what about you|how about you ?",
        ["I'm doing good. How can I help you ?",]
    ],
    [
        r"quit",
        ["Bye take care. See you soon :) ","It was nice talking to you. See you soon :)",]
    ],
    [
        r"what are some farming techniques?",
        ["Here are some farming techniques:<br>" + "<br>".join(farming_techniques)]
    ],
    [
    r"(.*)",
    ["I'm sorry, I didn't understand that. Could you please rephrase or ask another question?"]
    ]
]

# Initialize the chatbot
chatbot = Chat(pairs, reflections)

@app.route("/")
def home():
    return render_template("app.html")  # Serve the HTML template

@app.route("/get")
def get_bot_response():
    userText = request.args.get('msg')  # Get user input from the frontend
    return str(chatbot.respond(userText))  # Return chatbot response

    # Check if the user wants the list of questions
    if "show questions" in userText.lower() or "list questions" in userText.lower():
        response = "Here are some questions you can ask me:<br>" + "<br>".join(questions_list)
        return response
    
    return str(chatbot.respond(userText))  # Get the chatbot's response and send it back

    @app.route("/download/<filename>")
    def download_file(filename):
    # Serve the requested PDF from the 'static/pdfs' directory
        return send_from_directory("static/pdfs", filename, as_attachment=True)
if __name__ == "__main__":
    app.run(debug=True)
