class Random:
    def __init__(self, seed):
        self.seed = seed
       

    def next(self):
         self.seed = (16807 * self.seed) % (2147483647)
         return self.seed

    def choose(self, limit):
        return self.next() % limit

class Rule:
    def __init__(self, left, right):
        self.left = left
        self.right = right
        self.count = 1
    
    def __repr__(self):
        s = str(self.count) + " " + self.left + " -> " + str(self.right)
        return s
 
class Grammar:
    def __init__(self,seed):
        self.rand = Random(seed)
        self.dict = {}
    def rule(self,left, right):
        if(left in self.dict):
            self.dict[left] += (Rule(left,right),)
        else:
            self.dict[left] = (Rule(left,right),)
    def generate(self):
        if('Start' in self.dict):
            return self.generating(('Start',))
        else:
            raise Exception("No Start in dictionary")
    def generating(self,strings):
        result = ''
        for i in strings:
            if i not in self.dict:
                result += i + ' '
            else:
                result += self.generating(self.select(i))
        return result

    def select(self,left):
        rules = self.dict[left]
        total = self.summ(rules)
        index = self.rand.choose(total)
        for rule in rules:
            index -= rule.count
            chosen = rule
            if index <= 0:
                break
        for x in rules:
            if(x != chosen):
                x.count += 1
        return chosen.right
        
        
        
        
    def summ(self, rules):
        total = 0
        for x in rules:
            total += x.count
        return total
        
        
        
        
           
        
        
        
        
        
        
G = Grammar(101) 
G.rule('Noun',   ('cat',))                                #  01 
G.rule('Noun',   ('boy',))                                #  02 
G.rule('Noun',   ('dog',))                                #  03 
G.rule('Noun',   ('girl',))                               #  04 
G.rule('Verb',   ('bit',))                                #  05 
G.rule('Verb',   ('chased',))                             #  06 
G.rule('Verb',   ('kissed',))                             #  07 
G.rule('Phrase', ('the', 'Noun', 'Verb', 'the', 'Noun'))  #  08 
G.rule('Story',  ('Phrase',))                             #  09 
G.rule('Story',  ('Phrase', 'and', 'Story'))              #  10 
G.rule('Story',  ('Phrase', 'but', 'Story'))              #  11 
G.rule('Start',  ('Story', '.'))                          #  12
 
for x in range(30): 
    print (" ")
    print ("Test " + str(x + 1) + " With Seed 101")
    for y in range(10): 
        print (G.generate())

G = Grammar(200) 
G.rule('Noun',   ('cat',))                                #  01 
G.rule('Noun',   ('boy',))                                #  02 
G.rule('Noun',   ('dog',))                                #  03 
G.rule('Noun',   ('girl',))                               #  04 
G.rule('Verb',   ('bit',))                                #  05 
G.rule('Verb',   ('chased',))                             #  06 
G.rule('Verb',   ('kissed',))                             #  07 
G.rule('Phrase', ('the', 'Noun', 'Verb', 'the', 'Noun'))  #  08 
G.rule('Story',  ('Phrase',))                             #  09 
G.rule('Story',  ('Phrase', 'and', 'Story'))              #  10 
G.rule('Story',  ('Phrase', 'but', 'Story'))              #  11 
G.rule('Start',  ('Story', '.')) 

for x in range(30): 
    print(" ")
    print ("Test " + str(x + 1) + " With Seed 200")
    for y in range(10): 
        print (G.generate())