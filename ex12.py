while True:
    try:
        score = float(input("Enter your score:"))
        break
    except ValueError:
        print("Enter number only")
if score >= 50:
    print("Display 'Pass'")
else:
    print("Display 'Fail'")