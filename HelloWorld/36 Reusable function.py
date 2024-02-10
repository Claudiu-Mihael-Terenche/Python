def emoji_converter(message_sms):
    words = message_sms.split(' ')
    emojis = {
        ':)': '😊',
        ':(': '😒'
    }
    output = ''
    for word in words:
        output += emojis.get(word, word) + ' '
    return output


message = input('>')
print(emoji_converter(message))
