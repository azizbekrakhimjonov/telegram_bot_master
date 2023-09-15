from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

btnMain = KeyboardButton('⬅ Main Menu')
btnOtherMain = KeyboardButton('⬅ Back')
btnFoodMain = KeyboardButton('⬅ Back')

# Main Menu :
btnRandom = KeyboardButton('♦ Random Number')
btnFood = KeyboardButton('🍕 Random String')
btnOther = KeyboardButton('➡ Other')
mainMenu = ReplyKeyboardMarkup(resize_keyboard = True).add(btnRandom, btnFood, btnOther)


# Other Menu :
btnInfo = KeyboardButton('📚 Information')
btnMoney = KeyboardButton('📈 Exchange Rate')
otherMenu = ReplyKeyboardMarkup(resize_keyboard = True).add(btnInfo, btnMoney, btnMain)

# Sub Other Menu:
subOtherMenu = ReplyKeyboardMarkup(resize_keyboard = True).add(btnOtherMain)

# Food Menu:
subFoodMenu = ReplyKeyboardMarkup(resize_keyboard = True).add(btnFoodMain)
