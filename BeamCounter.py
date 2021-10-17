from h2o_wave import Q, main, app, ui

#listening to events from the UI is to define an @app function:

@app('/counter', mode='broadcast')
async def serve(q: Q):
    bean_count = q.app.bean_count or 0 #information related to the active client(client-technical term for 'browser tab' or 'browser session) & If q.client.bean_count is unavailable (which means this is a new client), we default the bean count to 0.

    if q.args.increment:  #q.args, also a dictionary-like object, carries event arguments
        q.app.bean_count =bean_count=bean_count + 1
    
    if not q.client.initialized:
        q.client.initialized:True 
        q.page['beans'] = ui.form_card(
            box='1 1 1 2',
            items=[
                ui.button(
                    name='increment',
                    label='Click me!',
                    caption=f'{ bean_count } beans',
                    primary=True,
                ),
            ],
        )

    else:
        q.page['beans'].items[0].button.caption = f'{bean_count} beans'

    
    await q.page.save()

    #q.args - request arguments submitted from the browser)
    #q.client - arbitrary information associated with the client
