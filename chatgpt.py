#!/usr/bin/python3
#creater:
#_________[ IMPORTING MODULES ]______>>
import os, json, openai
#_______[ BASIC COLORS ]_____>>
white = '\033[1;37m'
rad = '\033[1;31m'
green = '\033[1;32m'
#_______[ LOGO ]_____>>
def logo():
    os.system("clear")
    print(f"""{white}
          d888b      d8888b   d888888b 
          88  Y8b    88   8D     88
          88         88oodD      88    
          88  ooo    88          88    
          88   8     88          88    
          Y888P      88          YP 
-----------------------------------------------{white}""")
#_________[ MAIN MENU ]__________>>
def main():
    logo()
    while True:
        openai.api_key = "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"
        content = input(f" User : ")
        completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "user", 
                "content": content
            }
        ]
        )
        response = json.loads(str(completion.choices[0].message))
        print(f" ChatGPT : {str(response['content'])}")

if __name__=="__main__":
    main()
