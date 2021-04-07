import re

regS = '\#(.\n)*'
txt = '''# \t # ? | string a =  "ayush \n agarwal"; '''


print(re.fullmatch(regS,txt))
# txt = '# ayush'

# if(re.search(regS,txt)):
#     print("matched")
# else:
#     print("notMatched")

# import re

# txt = "The rain in Spain"
# x = re.fullmatch("The rai in Spain", txt)
# print(x)