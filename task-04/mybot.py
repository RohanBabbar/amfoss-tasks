import os
import telebot
import requests
import json
import csv

# TODO: 1.1 Get your environment variables 
yourkey = os.getenv("90a54d43")
bot_id = os.getenv("5865267013:AAEIrin3FaL5wD8rVqSkDHG4QORYm1IGApA")


bot = telebot.TeleBot("5865267013:AAEIrin3FaL5wD8rVqSkDHG4QORYm1IGApA")
print("HEllo")
@bot.message_handler(commands=['start', 'hello'])
def greet(message):
    global botRunning
    botRunning = True
    bot.reply_to(
        message, 'Hello there! I am a bot that will show movie information for you and export it in a CSV file')
    
@bot.message_handler(commands=['stop', 'bye'])
def goodbye(message):
    global botRunning
    botRunning = False
    bot.reply_to(message, 'Bye!\nHave a good time')
    


@bot.message_handler(func=lambda message: botRunning, commands=['help'])
def helpProvider(message):
    bot.reply_to(message, '1.0 You can use \"/movie MOVIE_NAME\" command to get the details of a particular movie. For eg: \"/movie The Shawshank Redemption\"\n\n2.0. You can use \"/export\" command to export all the movie data in CSV format.\n\n3.0. You can use \"/stop\" or the command \"/bye\" to stop the bot.')


@bot.message_handler(func=lambda message: botRunning, commands=['movie'])
def getMovie(message):
    global botRunning
    botRunning = True
    name_id = message.text
    z = name_id.lstrip("/movie ")
    # print(message)
    bot.reply_to(message, 'Getting movie info...')       
    # TODO: 1.2 Get movie information from the API
    # TODO: 1.3 Show the movie information in the chat window
    # TODO: 2.1 Create a CSV file and dump the movie information in it
    # https://www.omdbapi.com/?apikey=90a54d43&t={}
    # print(message.text)
    bot.send_message(message.chat.id, 'Here it is')
    
    print("Welcome")
    URL = "https://www.omdbapi.com/?apikey=90a54d43&t="+z
    response = requests.get(URL)
    
    json1 = response.json()
    line="Title: "+json1['Title']+"\nReleased: "+json1['Released']+"\nimdbRating: "+json1['imdbRating']+"\n"+json1['Poster']
    bot.send_message(message.chat.id, line)
    
    

@bot.message_handler(func=lambda message: botRunning, commands=['export'])
def getList(message):
    global botRunning
    name_id = message.text
    z = name_id.lstrip("/export ")

    bot.reply_to(message, 'Generating file...')
    #TODO: 2.2 Send downlodable CSV file to telegram chat
    URL = "https://www.omdbapi.com/?apikey=90a54d43&t="+z
    response = requests.get(URL)
    y=z+'.csv'
    json1 = response.json()
    line="Title: "+json1['Title']+"\nReleased: "+json1['Released']+"\nimdbRating: "+json1['imdbRating']+"\n"+json1['Poster']
    l1=['Title',json1['Title']]
    l2=['Released',json1['Released']]
    l3=['imdbRating',json1['imdbRating']]    
    with open(y, 'w') as csvfile:
        spamwriter = csv.writer(csvfile, delimiter=' ', quotechar='|', quoting=csv.QUOTE_MINIMAL)
        spamwriter.writerow(l1)
        spamwriter.writerow(l2)
        spamwriter.writerow(l3)
        print('yess')
    with open(y, 'r') as file:
       csvreader = csv.reader(file)
       for row in csvreader:
          print(row)
    gigs=open(y,'r')
    bot.send_document(message.chat.id,gigs)
              


            
    
    
    

    

@bot.message_handler(func=lambda message: botRunning)
def default(message):
    bot.reply_to(message, 'I did not understand '+'\N{confused face}')
    
bot.infinity_polling()
