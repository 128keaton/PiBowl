# PiBowl
A simple python script to use with Instapush to determine if your cat food bowl is empty/full.
## Setup

1. Make an Instapush account.

2. Create two events with the event titles as "Empty" and "Full"

3. For both of them, make the tracker`message` and the handler `{message}`

4. Save your secret and id.

5. Edit the Python script with your secret, id, and GPIO pin of your light sensor.

6. Attach light sensor to power, ground, and GPIO pin. Affix light sensor to inside of bowl.

7. Edit your crontab to include `0,30 * * * * yourScriptPath`

### Party on

(probably) IOT certified!

## Demo:
[Album](http://imgur.com/a/zHI0D)
