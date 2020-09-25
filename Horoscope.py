#An application which tells future based upon the zodiac sign

next=True
while next==True:
     print(''' From all the mentioned zoadic signs
     1) Aries
     2) Tauras
     3) Gemini
     4) Cancer
     5) Leo
     6) Virgo
     7) Libra
     8) Scorpio
     9) Sagittarius
    10) Capricon
    11) Aquarius
    12) Pisces
    ''')

     s=int(input("Pick your zoadiac sign and Press Enter to know your future:"))

     if s==1:
         print('''
     All eyes may be on you today — for your looks, skills, or even your funky bag! Make hay while 
     the sun shines, " "and charge your batteries with all that attention.You can get some decent 
     work done with that energy, says Ganesha.''')

     elif s==2:
       print('''
     Spontaneity yet sincerity will be the ruling emotions of the day. Keep your eyes and ears open,
     advises Ganesha, as trouble might be headed your way." " Make it a point to read the print well 
     before you sign any legal contract today. Prevention is better than cure, reminds Ganesha.''')

     elif s==3:
       print('''
     Today, your enthusiasm for sports and outdoor activities is palpable. According to you, variety is
     the spice of life. You will keep on jumping from one venture to another. " "You will establish a 
     good rapport with your bosses and colleagues. It's time to taste success in your immediate and 
     interim objectives.''')

     elif s==4:
       print('''
     It is likely that you will reach an important milestone in life today. Keep in mind that your success
     may be a cause of envy for a few people, some of whom may want to harm you. You are left with two 
     choices: either try to help them out of their troubles and miseries, or prepare for a battle.''')

     elif s==5:
       print('''
     Forget the weather. Today, the only thing shining bright are your chances of spending some quality 
     time with your near and dear ones. Going along these lines, Ganesha wonders how long has it been since you 
     last did the same. So, make the most of this lucky day. Chances are that you shall make
     new friends, who might turn out to be very supportive in the future. Ganesha wishes you the very best
     on this eventful day.''')

     elif s==6:
       print('''
     Business acumen is natural to you. Your management skills are immaculate. Move with imagination, 
     innovation and motivation to further your enterprise, advises Ganesha. Feel free to express and exercise
     your sense of judgement, says Ganesha.''')

    elif s==7:
       print('''
     The whole point of being a Libran is that you always have the tendency to be two separate things put 
     together on a pair of scales that somehow balance. Ganesha feels that today, you'll bring to the scales the
     stability of being your own master and servant. It's a fine balance to maintain. But only you are capable 
     of doing that, thanks to your extremely high-power status today.''')

     elif s==8:
       print('''
     Retail therapy with your loved ones is a perfect recipe to have a good time! You will be more than willing 
     to buy things of their choice. Haggling will be a trait you have closeted today as you go about being lavish 
     in your expenses, says Ganesha.''')

     elif s==9:
       print('''
     You may have women swooning over you today; such is your charm and way with them, says Ganesha. But friends 
     are highly valuable to you, and you shall spend much time with them cherishing their company and reliving 
     amazing times spent together.''')

    elif s==10:
       print('''
     You love the people around you unconditionally and such emotions will be more visible now than ever. Today,
     you will want to keep yourself surrounded with your loved ones, make them happy and have a good time, 
     says Ganesha. Your honesty and sincerity will give depth to your existing relationships.''')

     elif s==11:
       print('''
     God helps those who help themselves. You have experienced this plenty of times as your efforts have been paid 
     off. While your colleagues at work may pass negative comments at your work, your boss will not have any complains
     with you. For investments purposes, real estate and construction seem to be a wise option, suggests Ganesha''')

     elif s==12:
       print('''
     You will be able to come up trumps against the competition today. You should be wary of hidden enemies, for 
     they might be involved in slandering you. It is best to reach out to others and make friends before they take it
     upon themselves to hinder your progress. Apart from this, no other significant event is indicated today, says Ganesha.''')

     else:
       print("Hey You sure about the number? This is not in the horoscope  ")

     print()
     if input("Shall we do it again? (Y/N) ")=="Y":
         next=True
     else:
         next=False
