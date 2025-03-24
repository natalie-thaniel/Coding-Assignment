import random

class WordScramble:
  def __init__(self, words):
    self.words = words
    self.word = random.choice(words)
    self.scrambled_word = self.scramble_word(self.word)
    self.score = 0
    self.attempts = 0
    self.high_score = self.load_high_score()
    

  def scramble_word(self, word):
    word_list = list(word)
    random.shuffle(word_list)
    word_str = "".join(word_list)
    return word_str
  
  def check_guess(self, guess):
    self.attempts +=1
    if guess == self.word:
      self.score = (len(self.word)*10) - (self.attempts*5)
      return True
    else: 
      return False

  def give_hint(self):
      return self.word[0]

  def load_high_score(self):
    with open("high_score.txt", "r") as f:
      high_score = int(f.read())
      return high_score

  def update_high_score(self):
    if self.score > self.high_score:
      self.high_score = self.score
      with open("high_score.txt", "w") as f:
        f.write(str(self.high_score))

wordscramble = WordScramble("words.txt")

wordscramble = WordScramble(words)

while True:
  print("Unscramble the following word: "+wordscramble.scrambled_word)
  guess = input("What is your guess? ")
  if guess == "hint":
    print("The first letter of the word is "+wordscramble.give_hint())
  is_guess_true = wordscramble.check_guess(guess)
  if is_guess_true == True:
    wordscramble.update_high_score()
    print("Good Job your score is: "+str(wordscramble.score))
    break
  else:
    print("You wrong try again")
