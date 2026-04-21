import random
def get_input(prompt, is_numeric=False):
    while True:
        user_val = input(prompt).strip()
        if not user_val:
            print("ERROR: FIELD CAN NOT BE EMPPTY!!!")
            continue
        if is_numeric:
            if user_val.isdigit():
                return user_val
            else:
                print("ERROR.PLEASE ENTER A VALID NUMBER!!!")
            continue
        else:
            if user_val.replace("","").isalpha():
                return user_val
            else:    
                print("ERROR: PLEASE ENTER WORDS ONLY(NO NUMBERS)!!!")
                continue
        return user_val
print("Welcome to Mad Libs!Please choose the number to pick the story:")
print("1. The Hospital")
print("2. The Camping")
print("3. The Castle in an Enchanted Forest")
print("4. Surprise Me!")
choice = input("\nPlease pick a story (1-4): ")
if choice == "4":
    choice = str(random.randint(1, 3))
    print(f"The computer chose story number {choice}!")
if choice == "1":
    print("\nYou chose 'The Hospital'!")
    words = [
        get_input("Enter a Number: ", is_numeric=True),
        get_input("Enter a Measure of time: "),
        get_input("Enter a Mode of transportation: "),
        get_input("Enter an Adjective: "),
        get_input("Enter an Adjective: "),
        get_input("Enter a Noun (plural): "),
        get_input("Enter a Color: "),
        get_input("Enter a Part of the Body: "),
        get_input("Enter a Verb: "),
        get_input("Enter a Number: ", is_numeric=True),
        get_input("Enter a Noun: "),
        get_input("Enter a Noun: "),
        get_input("Enter a Part of the body: "),
        get_input("Enter a Verb: "),
        get_input("Enter a Noun: "),
        get_input("Enter an Adjective: "),
        get_input("Enter a Silly Word: "),
        get_input("Enter a Noun: ")
    ]
    print(f"\nIt was about {words[0]} {words[1]} ago when I arrived at the hospital in a {words[2]}. "
          f"The hospital is a/an {words[3]} place; there are a lot of {words[4]} {words[5]} here. "
          f"The nurses have {words[6]} {words[7]}. If someone wants to come into my room, I tell them "
          f"they have to {words[8]} first. I’ve decorated my room with {words[9]} {words[10]}. "
          f"Today I talked to a doctor; they were wearing a {words[11]} on their {words[12]}. "
          f"I heard that all doctors {words[13]} {words[14]} every day for breakfast. "
          f"The most {words[15]} thing about being here is the {words[16]} {words[17]}!")
elif choice == "2":
    print("\nYou chose 'The Camping'!")
    words = [
        get_input("Enter a Person's Name: "),
        get_input("Enter a Noun: "),
        get_input("Enter an Adjective (Feeling): "),
        get_input("Enter a Verb: "),
        get_input("Enter an Adjective (Feeling): "),
        get_input("Enter an Animal: "),
        get_input("Enter a Verb: "),
        get_input("Enter a Color: "),
        get_input("Enter a Verb (ending in 'ing'): "),
        get_input("Enter an Adverb (ending in 'ly'): "),
        get_input("Enter a Number: ", is_numeric=True),
        get_input("Enter a Measure of Time: "),
        get_input("Enter a Color: "),
        get_input("Enter an Animal: "),
        get_input("Enter a Number: ", is_numeric=True),
        get_input("Enter a Silly Word: "),
        get_input("Enter a Noun: ")
    ]
    print(f"\nThis weekend I am going camping with {words[0]}. I packed my lantern, sleeping bag, and {words[1]}. "
          f"I am so {words[2]} to {words[3]} in a tent. I am {words[4]} we might see a(n) {words[5]}; "
          f"I hear they’re dangerous. We are going to hike, fish, and {words[6]}. "
          f"The {words[7]} lake is great for {words[8]}. Then we will {words[9]} hike for {words[10]} {words[11]}. "
          f"If I see a {words[12]} {words[13]}, I'm bringing it home! At night we will tell {words[14]} {words[15]} "
          f"stories and roast {words[16]} around the campfire!!")
elif choice == "3":
    print("\nYou chose 'The Castle'!")
    words = [
        get_input("Enter a Person's Name: "),
        get_input("Enter an Adjective: "),
        get_input("Enter a Color: "),
        get_input("Enter an Animal: "),
        get_input("Enter a Place: "),
        get_input("Enter an Adjective: "),
        get_input("Enter a Magical Creature (plural): "),
        get_input("Enter an Adjective: "),
        get_input("Enter a Magical Creature (plural): "),
        get_input("Enter a Room in a House: "),
        get_input("Enter a Noun: "),
        get_input("Enter a Noun: "),
        get_input("Enter a Noun (plural): "),
        get_input("Enter an Adjective: "),
        get_input("Enter a Noun (plural): "),
        get_input("Enter a Number: ", is_numeric=True),
        get_input("Enter a Measure of Time: "),
        get_input("Enter a Verb (ending in 'ing'): "),
        get_input("Enter an Adjective: "),
        get_input("Enter a Noun: ")
    ]
    print(f"\nDear {words[0]}, I am writing from a {words[1]} castle. I arrived here after "
          f"riding a {words[2]} {words[3]} in {words[4]}. There are {words[5]} {words[6]} and {words[7]} {words[8]} here! "
          f"In the {words[9]} there is a pool of {words[10]}. I sleep on a {words[11]} of {words[12]} "
          f"and dream of {words[13]} {words[14]}. I have lived here for {words[15]} {words[16]}. "
          f"The only way to get here is {words[17]} on a {words[18]} {words[19]}!!")
else:
    print("Invalid choice! Please restart the program and enter 1, 2, 3, or 4.")
    
