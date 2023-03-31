# Prayer_Times_Email
This pulls the Islamic times of prayer from a website using selenium, then formats and sends it in an email.

Selenium is utilized by navigating to the website islamicfinder.org and copies the html elements that contain the prayer times, those prayer times are then formatted.

The formatted prayer times along with some additional information is sent in an email to a recipient of your choosing. 

The script requires that you authenticate the sender address, this requires the sender email address to have it's security settings adjusted accordingly and it is recommended that 2FA or MFA is not enabled. In this case it is best to use a throwaway email as a sender.

NOTE: Make sure you have selenium and the appropriate driver installed for whicheever browser you want selenium to use. you can find all the installation and setup info here: https://pypi.org/project/selenium/

Make sure both python files are in the same directory as one imports variables from the other.
