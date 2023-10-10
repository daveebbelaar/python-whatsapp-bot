# Airbnb WhatsApp Bot

Follow the instructions here: https://developers.facebook.com/docs/whatsapp/cloud-api/get-started

You can find your bots here: https://developers.facebook.com/apps/?

Here's all the documentation for the WhatsApp API: https://developers.facebook.com/docs/whatsapp

Here's another helpful guide: https://developers.facebook.com/blog/post/2022/10/24/sending-messages-with-whatsapp-in-your-python-applications/

Set up WhatsApp

Select the business account

You start with a test number that you can use to send messages to up to 5 numbers

Go to API Setup and find your test number that you will be sending from

Here you can also add numbers to send to. Put in your own number.

You'll receive a code on your phone via WhatsApp to verify your number

In the API access you have a 24 hour access token that you can use to send messages via the API

It will show an example of how to send messages using a curl command which can be send from the terminal or with a tool like Postman.

Let's convert that into a Python function with the request library.

You should receive the following message on WhatsApp:

```text
**Hello World**
Welcome and congratulations!! This message demonstrates your ability to send a WhatsApp message notification from the Cloud API, hosted by Meta. Thank you for taking the time to test with us.
```

There can be a 60-120 second delay in receiving the message

Create a system user at the Meta Business account level. Here we can create another access token that will work for longer than the 24 hours access token.

Here you select the app, and then for how long the access token will be valid. you can choose 60 days or never expire.

Select all the permissions as I was running into errors when I just selected the WhatsApp ones.

Confirm and copy the access code

On the System Users page, configure the assets to your System User, assigning your WhatsApp app with full control. Don’t forget to click the Save Changes button.


Now we have to find the following information:

These can be found at the app page:
APP_ID: "<<YOUR-WHATSAPP-BUSINESS-APP_ID>>" # Found at app page
APP_SECRET: "<<YOUR-WHATSAPP-BUSINESS-APP_SECRET>>" # Found at app page

RECIPIENT_WAID: "<<YOUR-RECIPIENT-TEST-PHONE-NUMBER>>" # This is your WhatsApp ID (i.e. phone number). Make sure it is added to the account as shown in the send the example test message.

VERSION: "v16.0", # The latest version of the Meta Graph API
ACCESS_TOKEN: "<<YOUR-SYSTEM-USER-ACCESS-TOKEN>>" # Created in previous step

## Adding Phone Numbers
https://developers.facebook.com/docs/whatsapp/phone-numbers/
