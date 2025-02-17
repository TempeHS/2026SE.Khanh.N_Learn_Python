def convert(text: str) -> str:
    return text.replace(":)", "🙂").replace(":(", "🙁")

def main(): 
    aaa = input("enter text: ")
    print(convert(aaa))

main()