## Code Challenge: Ransom Note
There is a kidnapper who wrote a ransom note, but found a magazine and wants to know if he can cut out whole words from it and use them to create an untraceable replica of his ransom note. 
Words in the ransom note are **case-sensitive** and *must* use only whole words available in the magazine. He *cannot* use substrings or concatenation to create the words he neds.

Given words in the magazine and words in the ransom note, print `yes` or return `True` if he can replicate ransom note **exactly** using whole words from the magazine; otherwise, print `no` or return `False`. 

#### Example Explanation:
Ransom note is "Attack at dawn". The magazine contains only "attack at daw". The magazine has all the right words, but there's case mismatch. The answer is `False` or `no`. 

#### Example 1:
```
Input: 
    magazine = "give me one grand today night"
    ransom = "give one grand today"
Output:
    True
```

#### Example 2:
```
Input:
    magazine = "ive Got a Lovely Bunch of Coconuts"
    note = "ive got some coconuts"
Output: 
    False
```

Souce: HackerRank