# Coffee Order Web User Interface

![screenshot](music-box-screenshot.png "screenshot")

_[Python Flask](https://en.wikipedia.org/wiki/Flask_\(web_framework\))_ to serve web pages and provide RESTful APIs

Various scripts are run on system startup from:

``/etc/rc.local``

<details>

```bash
#!/bin/sh -e
#
# rc.local
#
# This script is executed at the end of each multiuser runlevel.
# Make sure that the script will "exit 0" on success or any other
# value on error.
#
# In order to enable or disable this script just change the execution
# bits.
#
# By default this script does nothing.

# Print the IP address
_IP=$(hostname -I) || true
if [ "$_IP" ]; then
  printf "My IP address is %s\n" "$_IP"
fi

sudo /home/trevorde/coffeeServer/index.py &

exit 0
```

</details>
<br />

