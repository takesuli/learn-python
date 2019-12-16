# -*- coding: utf-8 -*-
import random

def get_answer(answer_number):
      if answer_number == 1:
          return '確かにそうだ'
      elif answer_number == 2:
          return '間違いなくそうだ'
      elif answer_number == 3:
           return 'はい'
      elif answer_number == 4:
          return 'なんとも。もう一度やってみて'
      elif answer_number == 5:
           return 'あとでもう一度聞いてみて'
      elif answer_number == 6:
          return '集中'
      elif answer_number == 7:
           return 'ノー'
      elif answer_number == 8:
          return 'それほど良くない'
      elif answer_number == 9:
           return 'とても疑わしい'

r = random.randint(1, 9)
fortune = get_answer(r)
print(fortune)

