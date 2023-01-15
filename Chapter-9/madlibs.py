with open('madibs.txt', 'w') as txt_fw :
    txt_fw.write('The ADJECTIVE panda walked to the NOUN and then VERB. \nA nearby NOUN was unaffected by these events.')
    txt_fw.close()

adj = input('\033[1m'+'Enter an adjective : \n' + '\033[0m')
noun = input('\033[1m'+'Enter an noun : \n' + '\033[0m')
adverb = input('\033[1m'+'Enter an adverb : \n' + '\033[0m')
verb = input('\033[1m'+'Enter an verb : \n' + '\033[0m')

with open('madibs.txt', 'r') as txt_f :
    data = txt_f.read()
    txt_f.close()
with open('madibs.txt', 'w') as txt_fwr :
    data = data.replace('ADJECTIVE' , adj)
    data = data.replace('NOUN' , noun)
    data = data.replace('VERB' , verb)
    data = data.replace('ADVERB' , adverb)
    txt_fwr.write(data)
    txt_fwr.close()


        


    

    
    

    