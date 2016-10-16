# Make a program that will return the meaning of 
# a tarot card after asking for the suit and then 
# asking for the number / face of the card
#(thought - use date time in library to pull card for the day...use it to help randomize the card for the day?)

#force each string input to automatically be lowercase to make string evaluation easier

# // Set an array (2D) of the values of each suit and face of the cards
#     // Earth, Pentacles = {}
earthArray = ["Material Force - Prosperity - Practicality - Trust","Juggling - Flexibility - Fun","Teamwork - Planning - Competence","Possessiveness - Control - Blocked Change","Hard Times - Ill Health - Rejection","Having/Not Having:- Resources - Knowledge - Power","Assessment - Reward - Direction Change","Diligence - Knowledge - Detail","Discipline - Self-Reliance - Refinement","Affluence - Permanence - Convention","Have an Effect - Be Practical - Be Prosperous - Be Trusting/Trustworthy","Unwavering - Cautious - Thorough - Realistic - Hardworking","Stubborn - Unadventurous - Obsessive - Pessimistic - Grinding","Nurturing - Bighearted - Down-to-Earth - Resourceful - Trustworthy","Enterprising, Adept, Reliable, Supporting, Steady"]

#     // Fire, Wands = {}
fireArray = ["Creative Force - Enthusiasm - Confidence - Courage", "Personal Power - Boldness - Originality","Exploration - Foresight - Leadership","Celebration - Freedom - Excitement","Disagreement - Competition - Hassles","Triumph - Acclaim - Pride","Aggression - Defiance - Conviction","Quick Action - Conclusion - News","Defensiveness - Perseverance - Stamina","Overextending - Burdens - Struggle","Be Creative - Be Enthusiastic - Be Courageous - Be Confident","Charming - Self-Confident - Daring - Adventurous - Passionate","Superficial - Cocky - Foolhardy - Restless - Hot-Tempered", "Attractive - Wholehearted - Energetic - Cheerful - Self-Assured","Creative - Inspiring - Forceful - Charismatic - Bold"]
#     // Air, Swords = {}
airArray = ["Mental Force - Truth - Justice - Fortitude","Blocked Emotions - Avoidance - Stalemate","Heartbreak - Loneliness - Betrayal","Rest - Contemplation - Quiet - Preperation","Self-Interest - Discord - Open Dishonor","The Blues - Recovery - Travel","Running Away - Lone-Wolf Style - Hidden - Dishonor","Restriction - Confusion - Powerlessness","Worry - Guilt - Anguish","Bottoming Out - Victim - Mentality - Martyrdom","Use Your Mind - Be Truthful - Be Just - Have Fortitutde","Direct - Authoritative - Incisive - Knowledgeable - Logical","Blunt - Overbearing - Cutting - Opinionated - Unfeeling","Honest - Astute - Forthright - Witty - Experienced", "Intellectual - Analytical - Articulate - Just - Ethical"]
#     // Water, Cups = {}
waterArray = [ "Emotional Force - Intuition - Intamacy - Love","Connection - Truce - Attraction","Exuberance - Friendship - Community", "Self-Absorption - Apathy - Going Within","Loss - Bereavement - Regret","Good Will - Innocence - Childhood","Wishful Thinking - Options - Dissipation","Deeper Meaning - Moving On - Weariness","Wish Fulfillment - Satisfaction - Sensual Pleasure","Joy - Peace - Family","Be Emotional - Be Intutive - Be Intimate - Be Loving","Romantic - Imaginative - Sensitive - Refined - Introspective", "Overemotional - Fanciful - Temperamental - Overrefined - Introverted","Loving - Tenderhearted - Intutitive - Psychic - Spiritual","Wise - Calm - Diplomatic - Caring - Tolerant"]
#     // Major Arcana = {}
majorArray = ["Beginning - Spontaneity - Faith - Appartent Folly","Action - Concious Awareness - Concentration - Power","NonAction - Unconcious Awareness - Potential - Mystery","Motherhood - Abundance - Senses - Nature","Fatherhood - Structure - Authority - Regulation","Education - Belief Systems - Conformity - Group Identification","Relationship - Sexuality - Personal Beliefs - Values","Victory - Will - Self-Assertion - Hard Control","Strength - Patience - Compassion - Soft Control","Introspection - Searching - Guidance - Solitude","Destinty - Turning Point - Movement - Personal Vision","Justice - Responsibility - Decision - Cause and Effect","Letting Go - Reversal - Suspension - Sacrafice","Ending - Transition - Elimination - Inexporaable Forces","Temperance - Balance - Health - Combination","Bondage - Materialism - Ignorance - Hopelessness","Sudden Change - Release - Downfall - Revelation","Hope - Inspiration - Generosity - Serenity","Fear - Illusion - Imagination - Bewilderment","Enlightenment - Greatness - Vitality - Assurance","Judgment - Rebirth - Inner Calling - Absolution","Integration - Accomplishment - Involvement - Fulfillment"]
# // First function ask if the card is a major arcana/trump card
def askPath():
#   (Take all numerical values as a string)
      arcana = raw_input('Type [major] for Major Arcana or [minor] for Minor Aracana: ')
#     // If it is then ask which number it is
      while arcana == 'major':
        majorArcanaNumber = raw_input('What is the number on the card? : ')
#         // Take value and convert to position in array to find meaning
        majorArcanaNumber = int(majorArcanaNumber)-1
        print majorArray[majorArcanaNumber]
#             //Return what that major arcana card means

# #         // Ask if user would like to try again
#         decisionToContinue = raw_input('Try Again? (Y or N): ')
# #             // If yes then run the first fuction again
#         if (decisionToContinue == 'Y') or (decisionToContinue =='y') or (decisionToContinue == 'Yes') or (decisionToContinue == 'yes'):
#             # majorArcanaNumber = raw_input('What is the number on the card? : ')
#             arcana = ""
#             askPath();
# #             // Else espcape the program 
#         else:
#           exit()
        decisionToContinue();
        pass
#     // Else call the function that will ask the suit
      while arcana == 'minor':
        minorArcanaSuit = raw_input('What is suit of the card? Type in [pentacles], [swords], [cups], [wands]: ')
        minorArcanaFace = raw_input('What is the face of the card? [ex: Ace, 2, ... , Queen, King] : ')
        findCardSuit(minorArcanaSuit, minorArcanaFace);
        #         // Ask if user would like to try again
        decisionToContinue(); 
        pass


def findCardSuit(minorArcanaSuit,minorArcanaFace):

    if minorArcanaFace == 'ace':
      minorArcanaFace = 1
      findCardMeaning(minorArcanaSuit, minorArcanaFace);
    elif minorArcanaFace == 'page':
      minorArcanaFace = 11
      findCardMeaning(minorArcanaSuit, minorArcanaFace);
    elif minorArcanaFace == 'knight':
      minorArcanaFace = 12
      findCardMeaning(minorArcanaSuit, minorArcanaFace);
    elif minorArcanaFace == 'queen':
      minorArcanaFace = 13
      findCardMeaning(minorArcanaSuit, minorArcanaFace);
    elif minorArcanaFace == 'king':
      minorArcanaFace = 14
      findCardMeaning(minorArcanaSuit, minorArcanaFace);
    else:
      findCardMeaning(minorArcanaSuit, minorArcanaFace);


def findCardMeaning (minorArcanaSuit,minorArcanaFace):

    if (minorArcanaSuit == 'pentacles') or (minorArcanaSuit == 'Pentacles'):
      print ("The influence of this suit is " + earthArray[0])
      print ("The influence of this card is " +earthArray[minorArcanaFace])
    elif (minorArcanaSuit == 'swords') or (minorArcanaSuit == 'Swords'):
      print ("The influence of this suit is " + airArray[0])
      print ("The influence of this card is " +airArray[minorArcanaFace])
    elif (minorArcanaSuit == 'cups') or (minorArcanaSuit == 'Cups'):
      print ("The influence of this suit is " + waterArray[0])
      print ("The influence of this card is " +waterArray[minorArcanaFace])
    elif (minorArcanaSuit == 'wands') or (minorArcanaSuit == 'Wands'):
      print ("The influence of this suit is " + fireArray[0])
      print ("The influence of this card is " +fireArray[minorArcanaFace])
    pass

    decisionToContinue();

def decisionToContinue():
        keepGoing = raw_input('Try Again? (Y or N): ')
#             // If yes then run the first fuction again
        if (keepGoing == 'Y') or (keepGoing =='y') or (keepGoing == 'Yes') or (keepGoing == 'yes'):
            # majorArcanaNumber = raw_input('What is the number on the card? : ')
            arcana = ""
            askPath();
#             // Else espcape the program 
        else:
          exit()
        pass

askPath();











# // Function that asks what suit it is

#     // Ask user to enter the suit

#     // Ask for the number or face

#         // Take value and call specific suit array
#               then convert to position in array to find meaning

#             // Return the meaning based on entry

#             // Ask user if they would like to try again

#                 // If yes then call first function

#                 // Else escape the program


# // Function that calls a card randomly

#     // Create a function that randomly generates a number between 1 & 5 (or 0 & 4)

#     // Assign speicic values to the suits (or set an array of suits)

#         // If the suit is the major arcana value 

#             // Run random number generator between 1 & 22 (or 0 & 21)

#                 // Return the meaning of the card via array

#             // Ask if user would like to select another random card or input a card, or neither

#                 // If random

#                     // Run random card function

#                 // Else if input card

#                     // Run first card function

#                 // Else escape the program

#         // Else if the suit is minor arcana

#             // Run random number generator between 1 & 12 (or 0 & 11)

#                 // Return meaning of card via array


#         // Ask if user would like to select another random card or input a card, or neither

#             // If random

#                 // Run random card function

#             // Else if input card

#                 // Run first card function

#             // Else escape the program



