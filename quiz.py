questions={ "what is 2+2":"4", "what is the capital of the USA":"Washington DC", "what color is grass":"green", "what is longer, km or mile":"mile", "what is 5x5":"25"}
score=0

for question in questions:
  print(question)
  
  if(input("answer: ")==questions[question]):
    print("correct")
    score+=1
  else:
    print(f"incorrect! Correct answer is {questions[question]}")

print(f"you scored {score} out of 5")
