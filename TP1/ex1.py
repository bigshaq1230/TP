color = input("give a color: ")
match color:
    case "Red":
        print("#ff0000")
    case "Blue":
        print("#00ff00")
    case "Green":
        print("#0000ff")
    case _:
        print("unknown")