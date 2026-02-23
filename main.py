import random
print("Welcome to Mad Libs!Please choose the number to pick the story:")
print("1. The Hospital,")
print("2. The Camping,")
print("3. The Castle in an Enchanted Forest.")
print("4. Surprise Me!")

choice = input("Please,enter 1, 2, 3 or 4 in order to pick the story!")
if choice == "4":
    choice = str(random.randint(1, 3))
    print(f" The computer chose story number {choice}")
if choice == "1":
    print("You chose 'The Hospital' story!")
    hospital_words = []
    hospital_words.append(input("Enter a Number:"))
    hospital_words.append(input("Enter a Measure of time:"))
    hospital_words.append(input("Enter a Mode of transportation:"))
    hospital_words.append(input("Enter an Adjective:"))
    hospital_words.append(input("Enter an Adjective:"))
    hospital_words.append(input("Enter a Noun(plural):"))
    hospital_words.append(input("Enter a Color:"))
    hospital_words.append(input("Enter a Part of the Body:"))
    hospital_words.append(input("Enter a Verb:"))
    hospital_words.append(input("Enter a Number:"))
    hospital_words.append(input("Enter a Noun:"))
    hospital_words.append(input("Enter a Noun:"))
    hospital_words.append(input("Enter a Part of the body:"))
    hospital_words.append(input("Enter a Verb:"))
    hospital_words.append(input("Enter a Noun:"))
    hospital_words.append(input("Enter an Adjective:"))
    hospital_words.append(input("Enter a Silly Word:"))
    hospital_words.append(input("Enter a Noun:"))
    print(f"""It was about {hospital_words[0]} {hospital_words[1]} ago
    when I arrived at the hospital in a {hospital_words[2]}.
    The hospital is a/an {hospital_words[3]} place, there are a lot of {hospital_words[4]}
    {hospital_words[5]} here. There are nurses here who have {hospital_words[6]} {hospital_words[7]}.
    If someone wants to come into my room I told them that they have to {hospital_words[8]}
    first. I’ve decorated my room with {hospital_words[9]} {hospital_words[10]}.Today I talked to
    a doctor and they were wearing a {hospital_words[11]} on their {hospital_words[12]}.
    I heard that all doctors {hospital_words[13]} {hospital_words[14]} every day for breakfast.The most
    {hospital_words[15]} thing about being in the hospital is the {hospital_words[16]}
    {hospital_words[17]}!""")
elif choice == "2":
    print("You chose 'The Camping' story!")
    camping_words = []
    camping_words.append(input("Enter a Proper Noun(Person Name):"))
    camping_words.append(input("Enter a Noun:"))
    camping_words.append(input("Enter an Adjective(Feeling):"))
    camping_words.append(input("Enter a Verb:"))
    camping_words.append(input("Enter an Adjective(Feeling):"))
    camping_words.append(input("Enter an Animal:"))
    camping_words.append(input("Enter a Verb:"))
    camping_words.append(input("Enter a Color:"))
    camping_words.append(input("Enter a Verb(ending in ing):"))
    camping_words.append(input("Enter an Adverb(ending in ly):"))
    camping_words.append(input("Enter a Number:"))
    camping_words.append(input("Enter a Measure of Time:"))
    camping_words.append(input("Enter a Color:"))
    camping_words.append(input("Enter an Animal:"))
    camping_words.append(input("Enter a Noumber:"))
    camping_words.append(input("Enter a Silly Word:"))
    camping_words.append(input("Enter a Noun:"))
    print(f"""This weekend I am going camping with {camping_words[0]}.
    I packed my lantern, sleeping bag, and {camping_words[1]}. I am so {camping_words[2]} 
    to {camping_words[3]} in a tent. I am {camping_words[4]} we might see a(n) {camping_words[5]},
    I hear they’re kind of dangerous. While we’re camping, we are going to hike,
    fish, and {camping_words[6]}. I have heard that the {camping_words[7]} lake is great for {camping_words[8]}.
    Then we will {camping_words[9]} hike through the forest for {camping_words[10]} 
    {camping_words[11]}. If I see a {camping_words[12]} {camping_words[13]} while hiking, I am going to bring
    it home as a pet! At night we will tell {camping_words[14]} {camping_words[15]} stories and roast
    {camping_words[16]} around the campfire!! """)
elif choice == "3":
    print("You chose 'The Castle in an Enchanted Forest' story!")
    castle_words = []
    castle_words.append(input("Enter a Proper Noun(Person Name):"))
    castle_words.append(input("Enter an Adjective:"))
    castle_words.append(input("Enter a Color:"))
    castle_words.append(input("Enter an Animal:"))
    castle_words.append(input("Enter a Place:"))
    castle_words.append(input("Enter an Adjective:"))
    castle_words.append(input("Enter a Magical Creature(plural):"))
    castle_words.append(input("Enter an Adjective:"))
    castle_words.append(input("Enter a Magical Creature(plural):"))
    castle_words.append(input("Enter a Room in a House:"))
    castle_words.append(input("Enter a Noun:"))
    castle_words.append(input("Enter a Noun:"))
    castle_words.append(input("Enter a Noun(plural):"))
    castle_words.append(input("Enter an Adjective:"))
    castle_words.append(input("Enter a Noun(plural):"))
    castle_words.append(input("Enter a Number:"))
    castle_words.append(input("Enter a Measure of Time:"))
    castle_words.append(input("Enter a Verb(ending in ing):"))
    castle_words.append(input("Enter an Adjective:"))
    castle_words.append(input("Enter a Noun:"))
    print(f"""Dear {castle_words[0]}, I am writing to you from a 
    {castle_words[1]} castle in an enchanted forest. I found myself here one day after
    going for a ride on a {castle_words[2]} {castle_words[3]} in {castle_words[4]}. There are {castle_words[5]} 
    {castle_words[6]} and {castle_words[7]} {castle_words[8]} 
    here! In the {castle_words[9]} there is a pool full of {castle_words[10]}. I fall asleep 
    each night on a {castle_words[11]} of {castle_words[12]} and dream of {castle_words[13]} {castle_words[14]}.
    It feels as though I have lived here for {castle_words[15]} {castle_words[16]}. I hope one
    day you can visit, although the only way to get here now is {castle_words[17]}
    on a {castle_words[18]} {castle_words[19]}!!""")
else:
    print("Invalid choice!Please restart!")
