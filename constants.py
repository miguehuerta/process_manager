
SERVICES = [
    {
        'name': 'example',
        'filter': ["ps -eaf | grep example-service | grep -v grep | awk '{print $2}'"],
        'start_commands':'nohup /opt/example-service.sh &> /var/log/example.log &',
        'category':'common'
    },


]
