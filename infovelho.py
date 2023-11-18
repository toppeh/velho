from random import choice
from telegram.ext import Updater, MessageHandler, Filters, CallbackContext
from telegram import Update

import config

wizards= [  
'''
  \\\|
   -o-
  / \\\\\\
 /     \\\r
|  \_/  |
|       |
 \     /
  \___/
''',
'''
    \|
   -o-
   / \\\r
  |   |
  | \ |
  |  \|
   \  \\
    \  \\
    |   |
    |   |
    /   \\\r
   |  |  |
   |  |  |
  /    \ \\\r
 /______\ \\\r
/__________\\\r
''',
'''
⠀⠀⠀⠀⠀⠀⣠⣤⣤⣤⣤⣤⣤⣄⣀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⣠⠴⠚⠋⠉⠉⠉⠉⠉⠙⠻⢦⣄⠀⠀⠀
⠀⠀⣠⡴⠋⠀⠀⢀⣀⣤⣴⣶⣶⣦⣀⠀⠈⢳⠀⠀
⠀⠀⠻⣿⣤⣶⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣦⡀
⠀⠀⠀⠙⠻⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠟
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⣰⣿⡿⠟⠋⠉⠉⠉⠉⠉⠉⠉⠉⠻⢿⣦⠀
⠀⢠⣾⡟⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢻⣿⡄
⠀⠘⣿⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⡇
⠀⠀⠈⠻⣦⡀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣴⠟⠋⠀
⠀⠀⠀⠀⠉⠻⣿⣦⣀⣀⣀⣤⣤⣴⠟⠁⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠉⠙⠛⠛⠋⠉⠁⠀
''']
messages = list()

def handleNewMessage(update: Update, context: CallbackContext):
  print(update)
  # Handle only channel posts
  if update.channel_post is None:
    return
  channel_post = update.channel_post

  # Save channel posts of a spesific channel only if such a channel is defined. 
  if config.INFO_CHANNEL_ID != '' and channel_post.chat.id != config.INFO_CHANNEL_ID:
    return 
  
  # Write channel post to a file.
  with open( "tuottajajuttuja.txt", "w" ) as file:
    file.write(f"{channel_post.sender_chat.title} says:\n")
    file.write(f"{channel_post.text}\n")
    file.write(f"{choice(wizards)}")

if __name__ == "__main__":
  updater = Updater(token=config.TOKEN, use_context=True)
  dispatcher = updater.dispatcher
  dispatcher.add_handler(MessageHandler(Filters.text, handleNewMessage))
  updater.start_polling()
