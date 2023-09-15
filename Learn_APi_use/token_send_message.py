# import requests
#
# url = "https://api.telegram.org/5351490636:AAEI4-V03agUU80kmg5ymmkvGu15hnxEYcU/sendMessage/salom"
#
# payload = {
#     "text": "Required",
#     "parse_mode": "Optional",
#     "disable_web_page_preview": False,
#     "disable_notification": False,
#     "reply_to_message_id": None
# }
# headers = {
#     "Accept": "application/json",
#     "User-Agent": "Telegram Bot SDK - (https://github.com/irazasyed/telegram-bot-sdk)",
#     "Content-Type": "application/json"
# }
#
# response = requests.post(url, json=payload, headers=headers)
#
# print(response.text)



# import requests
#
# url = "https://api.telegram.org/bot5351490636:AAEI4-V03agUU80kmg5ymmkvGu15hnxEYcU/sendMessage?chat_id=-1001661816517$text=Hello+world"
#
# headers = {
#     "Accept": "application/json",
#     "User-Agent": "Telegram Bot SDK - (https://github.com/irazasyed/telegram-bot-sdk)"
# }
#
# response = requests.post(url, headers=headers)
# #hop
# print(response.text)


# import requests
#
# url = "https://api.telegram.org/5351490636:AAEI4-V03agUU80kmg5ymmkvGu15hnxEYcU/forwardMessage"
#
# payload = {
#     "message_id": None,
#     "disable_notification": False
# }
# headers = {
#     "Accept": "application/json",
#     "User-Agent": "Telegram Bot SDK - (https://github.com/irazasyed/telegram-bot-sdk)",
#     "Content-Type": "application/json"
# }
#
# response = requests.post(url, json=payload, headers=headers)
#
# print(response.text)

# for example
# https://api.telegram.org/bot123456:ABC-DEF1234ghIkl-zyx57W2v1u123ew11/sendMessagets
import requests
token = '5375176127:AAG-BAeAEYR2EAS96zl7CtrV3CS9hmleNvk'
method = 'sendMessagets'
response = requests.post(
    url='https://api.telegram.org/bot{0}/{1}'.format(token, method),
    data={'chat_id': -1001661816517, 'text': 'hello friend'}
).json()

print(response)