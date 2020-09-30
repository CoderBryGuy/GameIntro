
urName = "fucky"

urNameInASentence = "hello {}".format(urName)

print(urNameInASentence)

count = urNameInASentence.count("l")

print(count)

print(urNameInASentence.upper())

print(urNameInASentence)

urNameInASentence_CAPs = urNameInASentence.upper()

print(urNameInASentence_CAPs)
print(urNameInASentence_CAPs.lower())

print(urNameInASentence.title())

print("1234".isdigit())

print(urNameInASentence.index("u"))

print(urNameInASentence.find("fuc"))

isFucky = True

while isFucky:
    isUrName = input("is ur name really fucky?")
    # isUrName = isUrName.lower()
    for word in isUrName.split(" "):
         if word == "yes":
            isFucky = False
            print("success")
