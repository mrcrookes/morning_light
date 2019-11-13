# morning_light

# make python file executable
chmod a+x /home/pi/morning_light.py

# to start up every morning...
# put file in /etc/cron.daily

# to check if added to cron.daily
run-parts --test /etc/cron.daily 
