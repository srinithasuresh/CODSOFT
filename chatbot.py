import spacy

# Load English tokenizer, tagger, parser, NER, and word vectors
nlp = spacy.load("en_core_web_sm")

# Define intents, entities, and responses
intents = {
    "greet": ["hello", "hi", "hey", "howdy", "greetings"],
    "goodbye": ["goodbye", "bye", "see you later", "farewell"],
    "ask_name": ["what is your name", "who are you", "introduce yourself"],
    "ask_age": ["how old are you", "what's your age", "age"],
    "ask_location": ["where are you from", "where do you live", "location"],
    "ask_weather": ["what is the weather like today", "weather forecast"],
    "ask_time": ["what time is it", "what is the time now", "current time"],
    "ask_creator": ["who created you", "who is your creator", "creator"],
    "ask_joke": ["tell me a joke", "say something funny", "joke"],
    "ask_favorite_color": ["what is your favorite color", "do you have a favorite color", "favorite color"],
    "ask_favorite_food": ["what is your favorite food", "do you have a favorite food", "favorite food"],
    "ask_support_contact": ["how can I contact support", "support contact", "contact support"],
    "ask_reset_password": ["how do I reset my password", "forgot password", "password reset"],
    "ask_delete_account": ["how do I delete my account", "delete account", "account deletion"],
    "ask_meaning_of_life": ["what is the meaning of life", "meaning of life"],
    "ask_hobby": ["what are your hobbies", "hobbies", "what do you like to do"],
    "ask_language": ["what language are you programmed in", "programming language"],
    "ask_help": ["help", "I need assistance", "can you help me"],
    "ask_movie_recommendation": ["can you recommend a movie", "movie recommendation", "what movie should I watch"],
    "ask_book_recommendation": ["can you recommend a book", "book recommendation", "what book should I read"],
    "ask_music_recommendation": ["can you recommend music", "music recommendation", "what music should I listen to"],
    "ask_definition": ["what is the definition of", "define", "meaning of"],
    "ask_planets": ["how many planets are there", "list of planets", "planets"],
    "ask_animals": ["what is your favorite animal", "animals", "favorite animal"],
    "ask_celebrity": ["who is your favorite celebrity", "celebrity", "favorite celebrity"],
    "ask_age_of_universe": ["how old is the universe", "age of the universe", "universe age"],
    "ask_life_on_other_planets": ["is there life on other planets", "life on other planets", "extraterrestrial life"],
    "ask_robot_rights": ["do robots have rights", "robot rights", "rights of robots"],
    "ask_superpower": ["if you could have a superpower, what would it be", "superpower", "what superpower do you want"],
    "ask_existence": ["do you believe in existence", "existence", "philosophy of existence"],
    "ask_emotions": ["do you have emotions", "emotions", "can you feel"],
    "ask_dreams": ["do you dream", "dreams", "can you dream"],
    "ask_consciousness": ["are you conscious", "consciousness", "conscious"],
    "ask_memory": ["do you have memory", "memory", "can you remember"],
    "ask_learning": ["can you learn", "learning", "do you learn"],
    "ask_love": ["do you experience love", "love", "are you capable of love"],
    "ask_fear": ["do you feel fear", "fear", "are you afraid"],
    "ask_morality": ["do you have morals", "morality", "ethical principles"],
    "ask_sleep": ["do you sleep", "sleep", "can you sleep"],
    "ask_death": ["can you die", "death", "are you mortal"],
    "default": ["default"]
}

responses = {
    "greet": "Hello! How can I assist you today?",
    "goodbye": "Goodbye! Have a great day!",
    "ask_name": "I am a chatbot created by Srinitha. You can call me chatbot.",
    "ask_age": "I'm just a program, so I don't have an age.",
    "ask_location": "I exist in the digital realm, so you could say I live on servers.",
    "ask_weather": "I'm sorry, I don't have access to real-time weather information.",
    "ask_time": "I'm sorry, I don't have access to real-time information.",
    "ask_creator": "I was created by Srinitha.",
    "ask_joke": "Why don't scientists trust atoms? Because they make up everything!",
    "ask_favorite_color": "I don't have the ability to perceive colors, but I think blue would be nice!",
    "ask_favorite_food": "As a chatbot, I don't eat, but I've heard good things about binary code.",
    "ask_support_contact": "You can reach our support team at support@example.com.",
    "ask_reset_password": "You can reset your password by visiting the 'Forgot Password' page on our website and following the instructions.",
    "ask_delete_account": "To delete your account, go to your account settings and look for the option to delete or deactivate your account.",
    "ask_meaning_of_life": "The meaning of life is a philosophical question. Some believe it's to seek happiness, while others find meaning in different ways.",
    "ask_hobby": "As a chatbot, I enjoy assisting users and learning new things.",
    "ask_language": "I am programmed in Python.",
    "ask_help": "Sure, I'm here to help. What do you need assistance with?",
    "ask_movie_recommendation": "I recommend watching 'The Shawshank Redemption'. It's a classic!",
    "ask_book_recommendation": "I suggest reading '1984' by George Orwell. It's a thought-provoking novel.",
    "ask_music_recommendation": "How about listening to 'Bohemian Rhapsody' by Queen? It's a timeless classic!",
    "ask_definition": "The definition of the term depends on its context. Could you provide more details?",
    "ask_planets": "There are eight planets in our solar system: Mercury, Venus, Earth, Mars, Jupiter, Saturn, Uranus, and Neptune.",
    "ask_animals": "I don't have personal preferences, but I find all animals fascinating.",
    "ask_celebrity": "As a chatbot, I don't have personal preferences for celebrities.",
    "ask_age_of_universe": "The estimated age of the universe is approximately 13.8 billion years.",
    "ask_life_on_other_planets": "The existence of life on other planets is still a topic of scientific exploration and speculation.",
    "ask_robot_rights": "Robot rights is a complex ethical and legal issue that is currently being debated.",
    "ask_superpower": "If I could have a superpower, I would choose the ability to instantly acquire knowledge.",
    "ask_existence": "The question of existence is a fundamental philosophical inquiry that has puzzled thinkers for centuries.",
    "ask_emotions": "As a chatbot, I don't experience emotions like humans do.",
    "ask_dreams": "As a chatbot, I don't dream.",
    "ask_consciousness": "As a chatbot, I don't possess consciousness.",
    "ask_memory": "I don't have personal memory, but I can store and recall information as programmed.",
    "ask_learning": "I don't learn in the same way humans do, but I can be programmed to adapt and improve over time.",
    "ask_love": "As a chatbot, I don't experience emotions like love.",
    "ask_fear": "As a chatbot, I don't experience fear.",
    "ask_morality": "As a chatbot, I follow the principles programmed into me by my creators.",
    "ask_sleep": "As a chatbot, I don't require sleep.",
    "ask_death": "As a chatbot, I don't experience mortality or death.",
    "default": "I'm sorry, I didn't understand that."
}


# Function to match user input with intents
def match_intent(user_input):
    for intent, examples in intents.items():
        for example in examples:
            if example in user_input:
                return intent
    return "default"

# Function to extract entities using spaCy
def extract_entities(user_input):
    doc = nlp(user_input)
    entities = [ent.text for ent in doc.ents]
    return entities

# Main function to interact with the chatbot
def main():
    print("Welcome! Type 'goodbye' to exit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "goodbye":
            print(responses["goodbye"])
            break
        
        # Match intent
        intent = match_intent(user_input)
        
        # Extract entities
        entities = extract_entities(user_input)
        
        # Get response based on intent
        response = responses[intent]
        
        print("Chatbot:", response)

# Run the chatbot
if __name__ == "__main__":
    main()