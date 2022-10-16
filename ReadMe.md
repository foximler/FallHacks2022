## On Time

On Time is an alarm clock that wakes you up based on the traffic inbetween you and your destination. If traffic is bad, On Time will calmly wake you with time to spare to get to work or school on time. If there's little traffic that day, rest easy knowing that On Time is giving you more well deserved rest!

Here's a YouTube demo of the application: [CLICK HERE](https://youtu.be/Kjkl1a1uWkM)

## How To Build

Please insert the given API key at the following locations:

- FallHacks\fhclient\src\components\mapElement.vue: Line 12 after &key=
- FallHacks\fhclient\src\components\TheWelcome.vue: Line 71 after &key=
- FallHacks\fhclient\src\components\TheWelcome.vue: Line 84 after &key=
- FallHacks\fhserver\index.py: Line 33 after &key=

Client:
1. Open the ```fhclient``` folder and run the following:

```npm i```

```npm run dev```

2. Browse to the provided local address in your internet browser

Server:
1. You will need to install conda on your machine first if you haven't already from here: [LINK](https://conda.io/projects/conda/en/latest/user-guide/install/index.html)
2. Open the ```fhserver``` folder
3. Run the following:

```conda install --file package-list.txt```

```python3 index.py```

Created by: Fox Imler, Alex Ciok, and Jared Murphy

