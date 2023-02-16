# Badger Rockets

Script for the Badger series of e-ink board from [Pimoroni](https://shop.pimoroni.com/search?q=badger) to display the the list of rocket launches that are due to occur.

Both boards will support it but it will be a lot easier with the Badger 2040 W as it's built around the PicoW which has on board WiFi.

Download the files into the examples folder and then look for rockets on the menu. Make sure you have the correct WiFi details.

Connection will be made to the [SpaceDevs](https://lldev.thespacedevs.com/docs/) API service for data. At the moment it connects to the development endpoint which has stale data but not subject to any rate limits. 

At the moment it will display the Mission Name and Description for the first record in the missions tree.
