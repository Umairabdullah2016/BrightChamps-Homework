import time
import subprocess
import sys
print("Loading gameplay.uaserver.io/Online/UAserver_Story_Game/")
time.sleep(5)
print("<gameplay.uaserver.io> Online , UAserver Headquaretes Controlled")
print("Hi, welcome to the story maker game")
time.sleep(1)
while True:
  msg1 = input("Is Today Sunny Or Rainy?: ")
  if msg1 ==  "Sunny":
      print("I can put my trainers on on \n")
      break
  elif msg1 == "Rainy":
      print("I Have to put my boots on")
      break
  else:
      print("Invalid Input")

msg2 = input("Do I have school today?: ")
while True:
    if msg2 == "Yes":
      print("I Guess I have to,go, 🥱")
      timeb = 8.500
      print("Waiting For School To Be Over")
      time.sleep(16)
      print("ahh, I'm done with school")
      break
    elif msg2 == "No":
      print("Yay, I can sleep in") 
      print("ahh, I'm done with school")
      break
    else:
      print("Invalid Input")
while True:
  msg3 = input("Ok , What do I do now? \nOptions: \n 1. Go to the park \n 2. Go to the mall: ")
  if msg3 in ["Shopping Mall", "2", "Go to the mall", "Mall", "shop"]:
    print("Ok, I'm going to the mall")
    break
  elif msg3 in ["Park", "1", "Go to the park", "play"]:
    print("Ok, I'm going to the park")
    break
  else:
      print("Invalid option")
while True:
  msg4 = input("OK, I am Back Home, I need to relax, chose one of the following options: \n -1. Play Video Games \n -2. Read A Book \n -3. Watch TV \n -4. Go Over To My Friends House \n\n Choose: ")
  if msg4 in ["1", "Play Video Games", "Video Games", "Play Digital Games", "Digital Games", "Play Games", "Play"]:
    print("Ok, I'm going to play video games")
    print('''______________________________________________________________________________|
             | MENU  VID HD               ROBLOX                                           |                                                                             
             |      ____                                                                   |
             |    |     |                                                                  |
             |    |   :)|                                                                  |
             |    |  ___|                                                                  |
             |     |                                                                       |
             |    //|\\                                                                    |
             |   // | \\                                                                   |
             |     |                                                                       |
             |    |  |                                                                     |
             |   |     |                                                                   |
             ------------------------------------------------------------------------------|
             ''')
    time.sleep(10)
    break
  elif msg4 in ["2", "Read A Book", "Book", "Read", "Read Book", "Read a book"]:
    print("KK, i will read my book")
    print("📖")
    time.sleep(5)
    break
  elif msg4 in ["3", "Watch TV", "TV", "Watch", "Watch TV", "Watch a TV"]:
   print("Yay, Time to Watch itseystreem battle against kawaii_kunicon \n 👦⚔👧") 
   for i in range(2):
     print("📺🔊Clin, Chon Clang Cling, Cha, Chilgh, Boom")
     time.sleep(1)
   print("📺--- kawaii_kunicorn was slayed by itseystreem")
   print("Outcomes: \n Health: \n-- itseystreem: 34% \n-- kawaii_kunicorn: Killed / -17% \n Battle \n-- itseystreem: won \n-- kawaii_kunicorn: defeated")
   break
  elif msg4 in ["4", "Go Over To My Friends House", "Friends House", "Friends", "Friend", "Go Over To My Friends House", "Go Over To My Friends House", "Go Over To My Friends House"]:
    print("Ok, I'm going to my friends house")
    print("🏠")
    time.sleep(5)
    break
  
  else:
    print("Invalid option")
while True:
  msg5 = input("I am Done Relaxing, What Do I Do Now? \n Options: \n 1. Go To Bed To Rest \n 2. Go To The Kitchen To Have Dinner\n\n Choose: ")
  if msg5 in ["1", "Go To Bed To Rest", "Bed", "Rest", "Go To Bed", "Sleep"]:
     print("Ok, I'm going to bed")
     print("🛌")
     print('''      
                    z
                  z
                z
              z
            z
          z
        🛌
     ''')
     print("<Rooster> Cock-a-doodle-doo")
     print("<Alarm Clock> Beep Beep Beep, Beep Beep Beep")
     break
  elif msg5 in ["2", "Go To The Kitchen To Have Dinner", "Kitchen", "Dinner", "Have Dinner", "Go To The Kitchen", "Eat"]:
     print("Ok, I'm going to the kitchen")
     print("🍽")
     print("Nam Nam Nam")
     time.sleep(1)
     print("Nam Nam Nam")
     time.sleep(5)
     break
  else:
     print("Invalid option")
print("Ahh, I am Done With my Day, I am going to bed")
print("<UAserver Messenger> Thank you for playing the story maker game")
req = input("Do you want to play again? (Y/n)?: ")
while True:
    if req == "Y":
      subprocess.run(["python", "Make_A_Story/main.py"], capture_output=True, text=True)
      break
    if req == "n":
      print("Bye :)")
      sys.exit(1)
      
     
    else:
      print("Invalid Input")