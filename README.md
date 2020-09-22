# Coffee Order Web User Interface <img src="icon-coffee-24-icon.jpg" style="width:10%;height:10%" />
A very large hammer to crack a very small nut!

## Background
I'm an early riser and always bring my wife a coffee when she wakes up.
Instead of her calling out for one, or even ringing a bell, what better
way than to employ one of my Raspberry Pi Zeros 
(and a tacky, £1.50 plastic palm tree with LED lights)?

The RPi0 serves up a webpage with two buttons:
* order a coffee
* acknowledge receipt of coffee

When the _Order_ button is pressed, it lights up the palm tree;
and the _Receive_ button turns it off - simples!

## Photos and Screenshots
<details>
  <summary>Photos</summary>

  ![CoffeeServer01](images/CoffeeServer01.jpg "Ready")<p />
  ![CoffeeServer02](images/CoffeeServer02.jpg "Order received")<p />
  ![CoffeeServer03](images/CoffeeServer03.jpg "Overview")<p />
  ![CoffeeServer04](images/CoffeeServer04.jpg "Details")<p />

</details>
<p />

<details>
  <summary>Screenshots</summary>

  ![Screen01](images/Screen01.png "Ready")<p />
  ![Screen02](images/Screen02.png "Order pending")<p />
  ![Screen03](images/Screen03.png "Order still pending")<p />
  ![Screen04](images/Screen04.png "Order received")<p />

</details>
<p />

## Architecture

_[Python Flask](https://en.wikipedia.org/wiki/Flask_\(web_framework\))_ is used to serve a web page
and provide RESTful APIs.

The single web page uses _Javascript_ to call various APIs to _order_ and _receive_ a coffee.

_[Python GPIO](https://pypi.org/project/RPi.GPIO/)_ is used to turn on/off power to the LEDs.

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

# prevent wifi going to sleep
iw wlan0 set power_save off

sudo /home/trevorde/coffeeServer/index.py &

exit 0
```

</details>
<br />

## Further work
* order status is held on a _per session_ basis but this information
  is used to control a **single** output.  This is incorrect and the
  order status should be held globally, typically in something like
  _Redis_.
* sometimes it takes up to 20s (!) after clicking the _Receive_ button
  for the LEDs to turn on.  This is why the web page has a 'progress bar'
  (_UpdatePlacingOrder_) to show that something is happening.
  I suspect that the _Python Flask_ server shuts down threads after a
  period of inactivity, as subsequent API requests (clicks on _Send_ or _Receive_)
  are very fast.

