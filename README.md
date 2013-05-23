groove-de
=========

Setup:
- [Download Google App Engine SDK for Python](https://developers.google.com/appengine/downloads#Google_App_Engine_SDK_for_Python)
- [Sign up for an Appengine Account](https://appspot.com) and register an
application. Choose any free Application Identifier (AppID).
- Clone this repository
- Edit gae/app.yaml and extension/main.js and replace PUT-YOUR-APPID-HERE with your AppID.
- Upload your App with appcfg.py from the App Engine SDK: `appcfg.py update gae`
- In Chrome open chrome://extensions/ (Tools -> Extensions) enabled Developer
Mode and choose "Load unpacked extension...". Choose the extension folder
from this repository.
- You might have to uninstall any other grooveshark related extensions first.
- Visit grooveshark.com - it should now load over your appengine app.


Too complicated? Just use something like [Deezer](http://goo.gl/SNOlG) instead.
