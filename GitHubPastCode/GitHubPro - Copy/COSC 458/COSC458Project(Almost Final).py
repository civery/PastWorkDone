import webbrowser

a1 = open("ch1.1.txt","r")
b1 = open("ch1.2.txt","r")
c1 = open("ch1.3.txt","r")

a2 =open("ch2.1.txt","r")
b2 =open("ch2.2.txt","r")
c2 =open("ch2.3.txt","r")
d2 =open("ch2.4.txt","r")

a3 =open("ch3.1.txt","r")
b3 =open("ch3.2.txt","r")
c3 =open("ch3.3.txt","r")
d3 =open("ch3.4.txt","r")

a4 =open("ch4.1.txt","r")
b4 =open("ch4.2.txt","r")
c4 =open("ch4.3.txt","r")
d4 =open("ch4.4.txt","r")
e4 =open("ch4.5.txt","r")
f4 =open("ch4.6.txt","r")

a5 =open("ch5.1.txt","r")
b5 =open("ch5.2.txt","r")
c5 =open("ch5.3.txt","r")
d5 =open("ch5.4.txt","r")
e5 =open("ch5.5.txt","r")

a6 =open("ch6.1.txt","r")
b6 =open("ch6.2.txt","r")
c6 =open("ch6.3.txt","r")
d6 =open("ch6.4.txt","r")
x=0
while(x!=6):
  print("*********************")
  print("1 - Chapter 1(Introduction)")
  print("2 - Chapter 2 (Software Processes)")
  print("3 - Chapter 3(Agile Software Development)")
  print("4 - Chapter 4(Requirements Engineering)")
  print("5 - Chapter 5(System Modeling)")
  print("6 - Chapter 6(Architectural Design)")
  print("7 - Feedback Form")
  print("8 - Exit Program")
  x=int(input(" Enter your choice and press return:"))
  if(x==1):
  
    print("1 - Professional software development")
    print("2 - Software engineering ethics")
    print("3 - Case studies")
    print("4 - Chapter 1 review Quiz")
    y=int(input("pick a chap(deep):"))
    if(y==1):
      print(a1.read())
    if(y==2):
      print(b1.read())
    if(y==3):
      print(c1.read())
    if(y==4):
      webbrowser.open("https://quizlet.com/103245277/quiz-on-software-engineering-code-of-ethics-and-professional-practice-flash-cards/")
  if(x==2):
    print("1 - Software process models")
    print("2 - Process activities")
    print("3 - Coping with change") 
    print("4 - Process improvement")
    print("5 - Chapter 2 review Quiz")
    y=int(input("pick a chap(deep):"))
    if(y==1):
      print(a2.read())
    if(y==2):
      print(b2.read())
    if(y==3):
      print(c2.read())
    if(y==4):
      print(d2.read())
    if(y==5):
      webbrowser.open("https://quizlet.com/93684622/software-engineering-chapter-2-software-processes-flash-cards/")      
  if(x==3):
    print("1 - Agile methods")
    print("2 - Agile developement techniques")
    print("3 - Agile project management")
    print("4 - Scaling agile methods")
    print("5 - Chapter 3 review Quiz")
    y=int(input("pick a chap(deep):"))
    if(y==1):
      print(a3.read())
    if(y==2):
      print(b3.read())
    if(y==3):
      print(c3.read())
    if(y==4):
      print(d3.read())
    if(y==5):
      webbrowser.open("https://quizlet.com/12875613/test")      
  if(x==4):
    print("1 - Functional and non-functional requirements")
    print("2 - Requirements engineering processes")
    print("3 - Requirements elicitation")
    print("4 - Requirements specification")
    print("5 - Requirements validation")
    print("6 - Requirements change")
    print("7 - Chapter 4 review Quiz")
    y=int(input("pick a chap(deep):"))
    if(y==1):
      print(a4.read())
    if(y==2):
      print(b4.read())
    if(y==3):
      print(c4.read())
    if(y==4):
      print(d4.read())
    if(y==5):
      print(e4.read())
    if(y==6):
      print(f4.read())   
    if(y==7):
      webbrowser.open("https://quizlet.com/102697571/chapter-4-requirements-engineering-flash-cards/")      
  if(x==5):
    print("1 - Context models")
    print("2 - interaction models")
    print("3 - Structural models")
    print("4 - Behavioral models")
    print("5 - Model-driven engineering")
    print("6 - Chapter 5 review Quiz")
    y=int(input("pick a chap(deep):"))
    if(y==1):
      print(a5.read())
    if(y==2):
      print(b5.read())
    if(y==3):
      print(c5.read())
    if(y==4):
      print(d5.read())
    if(y==5):
      print(e5.read())   
    if(y==6):
      webbrowser.open("https://quizlet.com/102703814/chapter-5-system-modeling-flash-cards/")      

  if(x==6):
    print("1 - Architectural design decisions")
    print("2 - Architectural views")
    print("3 - Architectural patterns")
    print("4 - Application architectures")
    print("5 - Chapter 6 review Quiz")
    y=int(input("pick a chap(deep):"))
    if(y==1):
      print(a6.read())
    if(y==2):
      print(b6.read())
    if(y==3):
      print(c6.read())
    if(y==4):
      print(d6.read())
    if(y==5):
      webbrowser.open("https://quizlet.com/102705169/chapter-6-architectural-design-flash-cards/")               
  if(x==7):
    webbrowser.open("https://docs.google.com/spreadsheets/d/1L8n7G1OFJ6Z5uzdU3j0NyEJM1uuyXEJd4WWiDXunSw8/edit?usp=sharing")
  if(x==8):
    print("End of Program.")
    break
  if(x>6):
    print("Invalid choice Please Try Again.")

