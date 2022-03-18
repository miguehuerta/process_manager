# process_manager
project to maage any linux process


Just add your processes to constants.py file like the example and manage them

#!/bin/python

SERVICES=[
    {
        'name':'example',
        'filter':["ps -eaf | grep example | grep -v grep | awk '{print $2}'"],
        'start_commands': 'nohup /opt/app/example.sh &',
        'category':'utils'
    },
    {
        'name':'process',
        'filter':["ps -eaf | grep process | grep -v grep | awk '{print $2}'"],
        'start_commands': 'python /opt/app2/process.py &',
        'category':'utils'
    }
]
