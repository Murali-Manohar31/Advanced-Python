letter = ''' 
Dear <|Name|>,
You are selected!
<|Date|>
'''
print(letter.replace("<|Name|>","Murali").replace("<|Date|>", "30.06.2025"))