from Bot import Bot
n= input("Login oracle academy and Open the Course and type (Yes/Y/y) to continue : ")
bot = Bot()

#bot.login()
#bot.openChannel()
#bot.openLearningModuleN(2)
while True:
    incomplete = bot.getFirstIncomplete()
    if incomplete:
        bot.completeOne(incomplete)
        bot.play()
        bot.goBackToLearningPath()
    else:
        break

bot.close()
#OA1535666953