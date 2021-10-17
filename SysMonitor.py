# Node. js is an open-source cross-platform JavaScript run-time environment built on Chrome's JavaScript engine that 
# allows server-side execution of JavaScript code and npm on Raspberry Pi. 

import time
import psutil
from h2o_wave import site, ui, data

page = site['/monitor']

cpu_card = page.add('cpu_stats', ui.small_series_stat_card(
    box='1 1 1 1',
    title='CPU',
    value='={{usage}}%',
    data=dict(usage=0.0),
    plot_data=data('tick usage', -15), # Our buffer holds at most 15 rows(Width streched to 15 values of ticks), and has exactly two columns: tick (a one-up integer) and usage (the CPU usage).
                                      #To display information on the card, you only need to send it new values (and not all the data rows all over again)
    plot_category='tick',
    plot_value='usage',
    plot_zero_value=0,
    plot_color='$red',
))

mem_card = page.add('mem_stats', ui.small_series_stat_card(
    box='1 2 1 1',
    title='Memory',
    value='={{usage}}%',
    data=dict(usage=0.0),
    plot_data=data('tick usage', -15),
    plot_category='tick',
    plot_value='usage',
    plot_zero_value=0,
    plot_color='$blue',
))


tick = 0
while True:
    tick += 1

    cpu_usage = psutil.cpu_percent(interval=1)
    cpu_card.data.usage = cpu_usage
    cpu_card.plot_data[-1] = [tick, cpu_usage] #we measure CPU usage every second and append a new row to the end of card's data buffer
                                               #displays a value and a time series visualization

    
    mem_usage = psutil.virtual_memory().percent
    mem_card.data.usage = mem_usage
    mem_card.plot_data[-1] = [tick, mem_usage]
    
    page.save()
    time.sleep(1)
