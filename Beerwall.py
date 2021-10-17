import time
from h2o_wave import site, ui

page = site['/beer']

beer_card1 = page.add('wall', ui.markdown_card(
    box='1 1 4 2',
    title='10 Bottles of Beer',
    content='', #Initialised with empty string
))


#set the content to an expression (or formula) & An expression is a string that starts with = 
beer_verse = """= {{before}} bottles of beer on the wall, {{before}} bottles of beer.

    Take one down, pass it around, {{after}} bottles of beer on the wall...
    """

beer_cardnew = page.add('wall', ui.markdown_card(
    box='1 3 4 2',
    title='20 Bottles of Beer',
    content=beer_verse, #set to a variable
    data = dict(before='20', after='19'), #we set the card's data attribute to a Python dictionary containing values for the placeholders before and after:

))

for i in range(10,0,-1): # Every iteration the content has been overwritten & f""" -> formatted string 
    beer_card1.content = f"""  
    {i} bootles of beer on the wall, {i} bottles of beer.

    Take one down, pass it around, {i-1} bottles of beer on the wall...
    
    """

    beer_cardnew.data.before = str(i) #if no str It won't be concatinated
    beer_cardnew.data.after = str(i - 1)

    page.save()
    time.sleep(1)
    #Python time sleep function is used to add delay in the execution of a program. 
    #We can use python sleep function to halt the execution of the program for given time in seconds. 
    #Notice that python time sleep function actually stops the execution of current thread only, not the whole program.


