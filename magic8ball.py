from yattag import Doc
import random

def lambda_handler(event, context):
    
    answers = [
        "It is certain",
   "It is decidedly so",
"Without a doubt",
"Yes definitely",
"You may rely on it",
"As I see it, yes",
"Most likely",
"Outlook good",
"Yes",
"Signs point to yes",
"Reply hazy try again",
"Ask again later",
"Better not tell you now",
"Cannot predict now",
"Think and ask again",
"Don't count on it",
"My reply is no",
"My sources say no",
"Outlook not so good",
"Very doubtful"
        ]
    
    shake = ""
    if "queryStringParameters" in event:
        if event["queryStringParameters"] is not None:
            if "shake" in event["queryStringParameters"]:
                shake = event["queryStringParameters"]["shake"]

    doc, tag, text = Doc().tagtext()

    with tag('html'):
        with tag('body'):
            with tag('form', action = "magic8ball"):
                with tag('div', name='center', style="margin-top: 150"):
                    with tag('div', name='circle', style="background: #black; border-radius: 50%; height:300px; width:300px; position: relative; box-shadow: 0 0 0 120px black; margin: auto;"):
                        with tag('div', name='text', style="position: relative; float: left; top: 50%; left: 50%; transform: translate(-50%, -50%);"):

                            if shake == "":
                                doc.stag('font', style="font-weight: bold; font-size: 110px; font-family: verdana; ")  
                                text("8")
                            else:
                                with tag('div', name='triangle', style="width: 0; height: 0; border-style: solid; margin-top: -60px; border-width: 0 120px 210px 120px; border-color: transparent transparent #007bff transparent;"):
                                    with tag('div', style="width: 120px; text-align: center;  margin-left: -60px; bottom: 0;"):
                                        doc.stag('font', style="color: white; font-weight: bold; font-size: 22px; font-family: verdana; text-align: center")  
                                        doc.stag('br')
                                        doc.stag('br')
                                        doc.stag('br')
                                        doc.stag('br')
                                        text(random.choice(answers))
                    
                    with tag('div', name='text', style="position: relative; float: left; top: 50%; left: 50%; transform: translate(-50%, -50%);"):
                        
                        doc.input(name = "shake", type = 'hidden', value = "true")
                        doc.stag('input', type = "submit", value = "Shake!", style="width: 200px; margin-top: 350px; background-color: black; border: none; color: white; padding: 15px 32px; text-align: center; text-decoration: none; display: inline-block; font-size: 16px; display: flex; justify-content: center; cursor: pointer;")
                
    htmlResult = doc.getvalue()

    return {
            'statusCode': "200",
            'body': htmlResult,
            'headers': {
                'Content-Type': 'text/html',
            }
        }
