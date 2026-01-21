def main():
    user_input=input()
    print(convert(user_input))

def convert(str):
    converted=str.replace(":)", "🙂")
    converted=converted.replace(":(","🙁")
    return converted


main()

