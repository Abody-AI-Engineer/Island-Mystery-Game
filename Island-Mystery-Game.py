print ("❚█══☠══█❚")

print ("Welcome to my island 🏝️ 🏝️")

print ("There are tow doors\nA Red door🟥 🚪 and a blue door🟦 🚪.")

enter_door = input ("Which door do you want to open?:\n🚪").upper ()

if enter_door == "RED" :
    print ("Great 🟥! Now you entered a room you found three boxes 📦📦📦:\n(White box ⬜,Green box 🟩 and black box ⬛)")
    three_boxes = input ("Which box do you want to open?:\n⬜ 🟩 ⬛").lower ()
     
    if three_boxes == "white" :
        print ("Oops 🟦! You opened a box filled with Snakes 🐍🐍🐍\nGame over 🎲👾🎲")
    
    elif three_boxes == "green" :
        print ("Congratulation you found the treasure!💰🥳🏆")
    
    elif three_boxes == "black" :
        print ("Oops! You opened a box filled with Spiders 🕷️ 🕸️ 🕷️\nGame over🎲👾🎲")

    else :
        print ("Invaild choice 🤷‍♀️👺")

elif enter_door == "BLUE" :
    print ("Oops!,You chose the crocodile door 🐊🐊🐊\nGame over 🎲👾🎲") 

else :
    print ("Invaild choice 🤷‍♀️👺") 