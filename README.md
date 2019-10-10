# doorbell
A [raspend](https://github.com/jobe3774/raspend) based application to switch on/off my doorbell. Therefore it exposes two methods of the **GPIOSwitch** class, which is included in this project, two switch on/off a GPIO pin. This GPIO pin controls a relay, which in turn controls the power supply of my bell transformer. Using the command interface of [raspend](https://github.com/jobe3774/raspend) I can call these methods via HTTP POST or GET requests.

# License
MIT. See LICENSE file.
