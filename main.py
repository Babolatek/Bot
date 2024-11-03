import discord
import random

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)
emojis = "🫨🩷🩵🩶🫷🫸🫎🫏🪽🪿🪼🪻🫚🫛🪭🪮🪇🪈🪯🛜🫠🫢🫣🫡🫥🫤🥹🫱🫲🫴🫰🫵🫶🫦🫅🫃🫄🧌🪸🪷🪹🪺🫘🫗🫙🛝🛞🛟🪩🪫🩼🩻🫧🪬🪪🟰🥲🥸🤌🫀🫁🥷🦬🦣🦫🦤🪶🦭🪲🪰🪱🪴🫐🫒🫑🫓🫔🫕🫖🧋🪨🪵🛖🛻🛼🪄🪅🪆🪡🪢🩴🪖🪗🪘🪙🪃🪚🪛🪝🪜🛗🪞🪟🪠🪤🪣🪥🪦🪧🥱🤎🤍🤏🦻🧏🧍🧎🦧🦮🦥🦦🦨🦩🧄🧅🧇🧆🧈🦪🧃🧉🧊🛕🦽🦼🛺🪂🪐🤿🪀🪁🦺🥻🩱🩲🩳🩰🪕🪔🪓🦯🩸🩹🩺🪑🪒🟠🟡🟢🟣🟤🟥🟧🟨🟩🟦🟪😀😁😂🤣😃😄😅😆😉😊😋😎😍🥰😘😗😙😚🙂🤗🤩🤔🤨😐😑😶🙄😏😣😥😮🤐😯😪😫😴😌😛😜😝🤤😒😓😔😕🙃🤑😲☹️🙁😖😞😟😤😢😭😦😧😨😩🤯😬😰😱😳🤪😵😡😠🤬😷🤒🤕🤢🤮🤧😇🤠🤡🤥🤫🤭🧐🤓🥳🥴🥺🥵🥶😈👿👹👺👾💀👻👽🤖💩😺😹😻😼😽🙀😿😾👶👧🧒👦👩🧑👨👵🧓👴👲👳‍♀️👳‍♂️🧕🧔👱‍♂️👱‍♀️👮‍♀️👮‍♂️👷‍♀️👷‍♂️💂‍♀️💂‍♂️🕵️‍♀️🕵️‍♂️👩‍⚕️👨‍⚕️👩‍🌾👨‍🌾👩‍🍳👨‍🍳👩‍🎓👨‍🎓👩‍🎤👨‍🎤👩👨‍🏫👩‍🏭👨‍🏭👩‍💻👨‍💻👩‍💼👨‍💼👩‍🔧👨‍🔧👩‍🔬👨‍🔬👩‍🎨👨‍🎨👩‍🚒👨‍🚒👩‍✈️👨‍✈️👩‍🚀👨‍🚀👩‍⚖️👨‍⚖️👰🤵👸🤴🤶🎅🧙‍♀️🧙‍♂️🧝‍♀️🧝‍♂️🧛‍♀️🧛‍♂️🧟‍♀️🧟‍♂️🧞‍♀️🧞‍♂️🧜‍♀️🧜‍♂️🧚‍♀️🧚‍♂️👼🤰🤱🙇‍♀️🙇‍♂️💁‍♀️💁‍♂️🙅‍♀️🙅‍♂️🙆‍♀️🙆‍♂️🙋‍♀️🙋‍♂️🤦‍♀️🤦‍♂️🤷‍♀️🤷‍♂️🙎‍♀️🙎‍♂️🙍‍♀️🙍‍♂️💇‍♀️💇‍♂️💆‍♀️💆‍♂️🧖‍♀️🧖‍♂️🦹‍♀️🦹‍♂️🦸‍♀️🦸‍♂️👨‍🦰👩‍🦰👨‍🦱👩‍🦱👨‍🦳👩‍🦳👨‍🦲👩‍🦲🦰🦱🦲🦳💅🤳💃🕺👯‍♂️👯‍♀️👯🕴🚶‍♀️🚶‍♂️🏃‍♀️🏃‍♂️👫👭👬💑👩‍❤️‍👩👨‍❤️‍👨💏👩‍❤️‍💋‍👩👨‍❤️‍💋‍👨👪👨‍👩‍👧👨‍👩‍👧‍👦👨‍👩‍👦‍👦👨‍👩‍👧‍👧👩‍👩‍👦👩‍👩‍👧👩‍👩‍👧‍👦👩‍👩‍👦‍👦👩‍👩‍👧‍👧👨‍👨‍👦👨‍👨‍👧👨‍👨‍👧‍👦👨‍👨‍👦‍👦👨‍👨‍👧‍👧👩‍👦👩‍👧👩‍👧‍👦👩‍👦‍👦👩‍👧‍👧👨‍👦👨‍👧👨‍👧‍👦👨‍👦‍👦👨‍👧‍👧🤲👐🙌👏🤝👍👎👊✊🤛🤜🤞✌️🤟🤘👌👈👉👆👇☝️✋🤚🖐🖖👋🤙💪🖕✍️🙏💍💄💋👄👅👂👃👣🦵🦾🦿🦶🦴🦷👁👀🧠🗣👤👥🫂🐶🐱🐭🐹🐰🦊🐻🐼🐨🐯🦁🐮🐷🐽🐸🐵🙈🙉🙊🐒🐔🐧🐦🐤🐣🐥🦆🦅🦉🦇🐺🐗🐴🦄🐝🐛🦋🐌🐚🐞🐜🦗🕷🕸🦂🐢🐍🦎🦖🦕🐙🦑🦐🦀🐡🐠🐟🐬🐳🐋🦈🐊🐅🐆🦓🦍🐘🦏🐪🐫🦒🐃🐂🐄🐎🐖🐏🐑🐐🦌🐕🐩🐈🐓🦃🕊🐇🐁🐀🐿🦔🐾🐉🐲🦝🦘🦡🦚🦜🦢🦠🦟🦧🦛🦙🦞🌵🎄🌲🌳🌴🌱🌿☘️🍀🎍🎋🍃🍂🍁🍄🌾💐🌷🌹🥀🌺🌸🌼🌻🌞🌝🌛🌜🌚🌕🌖🌗🌘🌑🌒🌔🌙🌎🌍🌏💫⭐️🌟✨⚡️☄️💥🔥🌪🌈☀️🌤⛅️🌥☁️🌦🌧⛈🌩🌨❄️☃️⛄️🌬💨💧💦☔️☂️🌊🌫🟫"
message_number = 0
next_message = 0
special_command = 0
bot_cards = []
user_cards = []
the_top_card = 0
talia = []
prefix = "!"
def losowe_emoji(lista_l,ilosc):
    wiadomosc = ""
    dlugosc = len(lista_l) - 1
    print(dlugosc)
    for i in (range(ilosc)):
        numer = random.randint(0,dlugosc)
        emoji = emojis[numer]
        print(numer)
        wiadomosc += emoji
        print(len(wiadomosc))
    return wiadomosc

@client.event
async def on_ready():
    print(f'Zalogowaliśmy się jako {client.user}')

@client.event
async def on_message(message):
    global message_number
    global next_message
    global special_command
    global user_cards
    global bot_cards
    global the_top_card
    global talia
    message_number += 1
    print("numer wiadomości",message_number)
    
    if message.author == client.user:
        return
    if special_command == 1 and message.content.startswith(prefix) and next_message == message_number:
        lista = "papier","kamień","nożyce"
        wiadomosc = lista[random.randint(0,2)]
        await message.channel.send(wiadomosc)
        if message.content == prefix + "papier":
            if wiadomosc == "papier":
                await message.channel.send("Remis")
            elif wiadomosc == "kamień":
                await message.channel.send("Wygrałeś")
            else:
                await message.channel.send("Wygrałem")
        elif message.content == prefix + "kamień":
            if wiadomosc == "kamień":
                await message.channel.send("Remis")
            elif wiadomosc == "papier":
                await message.channel.send("Wygrałeś")
            else:
                await message.channel.send("Wygrałem")
        elif message.content == prefix + "nożyce":
            if wiadomosc == "nożyce":
                await message.channel.send("Remis")
            elif wiadomosc == "papier":
                await message.channel.send("Wygrałeś")
            else:
                await message.channel.send("Wygrałem")
        else:
            await message.channel.send("Nie znam odpowiedzi")
    elif special_command == 2 and message.content.startswith(prefix) and next_message == message_number:
        message_without_prefix = ""
        for i in range(len(prefix),len(message.content)):
            if i == len(message.content):
                break
            message_without_prefix += message.content[i]
            print("x")
        print(message_without_prefix)
        able_cards = {"1" : ["1","2"],"2" : ["2","3"],"3" : ["3","4"],"4" : ["4","5"],"5" : ["5","6"],"6" : ["6","bzz"],"bzz" : ["bzz","1"]} 
        if message_without_prefix in user_cards:
            if able_cards[str(the_top_card)][0] == message_without_prefix or able_cards[str(the_top_card)][1] == message_without_prefix:
                user_cards.remove(message_without_prefix)
                the_top_card = message_without_prefix
                await message.channel.send("To są Twoje karty" + str(user_cards))
                await message.channel.send("Karta na stole to :" + str(the_top_card)) 
            else:
                number = random.randint(0,len(talia) - 1)
                user_cards.append(talia.pop(number))   
                await message.channel.send("To są Twoje karty" + str(user_cards))
                await message.channel.send("Karta na stole to :" + str(the_top_card)) 
        else:
            number = random.randint(0,len(talia) - 1)
            user_cards.append(talia.pop(number))   
            await message.channel.send("To są Twoje karty" + str(user_cards))
            await message.channel.send("Karta na stole to :" + str(the_top_card))
        if the_top_card in bot_cards:
            bot_cards.remove(the_top_card)
            await message.channel.send("Zagrałem :" + the_top_card)
            await message.channel.send("Karta na stole to :" + str(the_top_card))
            next_message = message_number + 1
        elif able_cards[str(the_top_card)][1]:
            bot_cards.remove(able_cards[str(the_top_card)][1])
            await message.channel.send("Zagrałem :" + able_cards[str(the_top_card)][1])
            the_top_card = able_cards[str(the_top_card)][1]
            await message.channel.send("Karta na stole to :" + str(the_top_card))
            next_message = message_number + 1
        else:
            number = random.randint(0,len(talia) - 1)
            bot_cards.append(talia.pop(number))
            await message.channel.send("Dobrałem kartę")
            await message.channel.send("Karta na stole to :" + str(the_top_card))
            next_message = message_number + 1
        print(next_message)

    elif message.content.startswith(prefix + 'hello'):
        await message.channel.send(f'Cześć, jestem bot {client.user}!')
    elif  message.content.startswith(prefix + 'heh'):
        if len(message.content) > 4:
            count_heh = int(message.content[4:])
        else:
            count_heh = 5
        await message.channel.send("he" * count_heh)
    elif message.content.startswith(prefix + "emoji"):
        if len(message.content) > 6:
            count_emoji = int(message.content[6:])
        else:
            count_emoji = 1
        wiadomosc = losowe_emoji(emojis,count_emoji)
        print(count_emoji)
        await message.channel.send(wiadomosc)
    elif message.content.startswith(prefix + "gra pkn"):
        special_command = 1
        next_message = message_number + 2
        print("message_number :",message_number)
        print("next_message :",next_message)
        await message.channel.send("Zagrajmy")
    elif message.content.startswith(prefix + "gra komary"):
        special_command = 2
        next_message = message_number + 3
        talia = []
        for i in range(6):
            for j in range(8):
                talia.append(str(i + 1))
        for i in range(7):
            talia.append("bzz")      
        print(talia)
        bot_cards = []
        user_cards = []
        for i in(range(6)):
            number_bot = random.randint(0,len(talia)-1)
            bot_cards.append(talia.pop(number_bot))
            number_user = random.randint(0,len(talia)-1)
            user_cards.append(talia.pop(number_user))
        await message.channel.send("To są Twoje karty :" + str(user_cards))
        the_top_card = talia[random.randint(0,len(talia)-1)]
        await message.channel.send("Karta na stole to :" + str(the_top_card))
        print(bot_cards)
        print(talia)
client.run("TOKEN")
