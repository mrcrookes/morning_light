# morning_light

### make python file executable
chmod a+x ~/morning_light.py

### to start up every morning put python file in /etc/cron.daily folder
sudo cp ~/morning_light.py /etc/cron.daily/

### to check if added to cron.daily
run-parts --test /etc/cron.daily 
