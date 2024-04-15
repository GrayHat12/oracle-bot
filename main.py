from Bot import Bot
n= input("Login oracle academy and Open the Course and type (Yes/Y/y) to continue : ")
bot = Bot()

#bot.login()
#bot.openChannel()
#bot.openLearningModuleN(2)s
while True:
    incomplete = bot.getFirstIncomplete()
    if incomplete:
        quizSkip=bot.completeOne(incomplete)
        
        if quizSkip==True:
            bot.play()  
            bot.goBackToLearningPath()
        else:
            
            pass
    else:
        break

#OA1535666953