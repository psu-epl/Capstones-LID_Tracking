### Using the Station Module:

![Station Module in Enclosure](https://github.com/psu-epl/Capstones-LID_Tracking/blob/master/SM/img/enc.png)

#### Normal Login
When a registered user swipes a card, the SM sends a request to the database, if the user is authorized, the SM light a green LED and send power to the external relay. The database logs the entry with a timestamp. It can take up to 4 seconds to recieve a reply from the server.
If the user is unauthorized, the SM will emit a beep and remain off.
If it takes 15s or more to get a reply, this indicates that the SM is timing out with the server. Debugging info is available on the serial port of the SM.

#### Logout
Pushing the attached button causes the relay to be shut off and a logout command to be sent to the database. A logout timestamp is added to the last login entry.

#### Double Scanning
If a user is logged in, and another user badges in on top of them, the module will stay logged in under the new user.
If an unauthorized user tries to login over an existing session, the SM will end the session.

#### Add user
For a manager to add a user, they will hold down the button and scan their badge. The SM will blink alternating red and green for 10 seconds. The new user will scan their badge and the info is sent to the database.  If the add is successful, the SM will log in.
