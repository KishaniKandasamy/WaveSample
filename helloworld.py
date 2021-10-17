from h2o_wave import site, ui

# Grab a reference to the page at route '/hello'
page = site['/hello']  #site - script

# Add a markdown card to the page.
page['quote'] = ui.markdown_card(
    box='1 1 2 2',
    title='Hello World',
    content='"The Internet? Is that thing still around?" - *Homer Simpson*',
)

# Finally, save the page.
page.save()

#Python REPL : REPL stands for read-eval-print loop and basically provides a programmer with an interactive programming environment

#Reference to our card 
quote = page['quote']
quote.title = 'Hello Again!'
quote.content = "It is my hello world wave script!"
page.save()

#Create  a new card
quote2= page.add('quote2',ui.markdown_card(
    box='1 2 2 2',
    title='Hello World',
    content='"The Internet? Is that thing still around?" - *Homer Simpson*',
))
page.save()

#Quit the REPL
quit()
