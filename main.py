from Bot import Bot

bot = Bot()

bot.login()
bot.openChannel()
bot.openLearningModule2()
while True:
    incomplete = bot.getFirstIncomplete()
    if incomplete:
        bot.completeOne(incomplete)
        bot.play()
        bot.goBackToLearningPath()
    else:
        break

bot.close()