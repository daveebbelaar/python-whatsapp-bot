# Airbnb WhatsApp Bot

Follow the instructions here: https://developers.facebook.com/docs/whatsapp/cloud-api/get-started

You can find your bots here: https://developers.facebook.com/apps/?

Here's all the documentation for the WhatsApp API: https://developers.facebook.com/docs/whatsapp

Here's another helpful guide: https://developers.facebook.com/blog/post/2022/10/24/sending-messages-with-whatsapp-in-your-python-applications/

Here's a link to the API docs for sending messages: https://developers.facebook.com/docs/whatsapp/cloud-api/guides/send-messages

Set up WhatsApp app

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
APP_ID: "<YOUR-WHATSAPP-BUSINESS-APP_ID>" # Found at App Dashboard
APP_SECRET: "<YOUR-WHATSAPP-BUSINESS-APP_SECRET>" # Found at App Dashboard

RECIPIENT_WAID: "<YOUR-RECIPIENT-TEST-PHONE-NUMBER>>" # This is your WhatsApp ID (i.e. phone number). Make sure it is added to the account as shown in the send the example test message.

VERSION: "v16.0", # The latest version of the Meta Graph API
ACCESS_TOKEN: "<YOUR-SYSTEM-USER-ACCESS-TOKEN>" # Created in previous step


You can only send a template type message as your first message to a user. That's why you have to send a reply first before we continue. Took me 2 hours to figure this out.


## Configure a Webhook

In the App Dashboard, go to WhatsApp > Configuration, then click the Edit button.

Callback URL: This is the URL Meta will be sending the events to. See the Webhooks, Getting Started guide for information on creating the URL.
Verify Token: This string is set up by you, when you create your webhook endpoint.
You can generate a verify token here ot pick any string you like: https://it-tools.tech/token-generator

After saving, back in the Configuration panel, click the Manage button and subscribe to individual webhook fields. To receive notifications of customer messages, be sure to subscribe to the messages webhook field.


## Start local server with Ngrok

Follow these steps:

https://ngrok.com/docs/integrations/whatsapp/webhooks/

1. Create account: https://dashboard.ngrok.com
2. Claim your free domain: https://dashboard.ngrok.com/cloud-edge/domains
3. Set up authentication token: `ngrok config add-authtoken <YOUR-TOKEN>`

https://developers.facebook.com/docs/graph-api/webhooks/getting-started

Verification Requests
Anytime you configure the Webhooks product in your App Dashboard, we'll send a GET request to your endpoint URL. Verification requests include the following query string parameters, appended to the end of your endpoint URL. They will look something like this:

```
GET https://www.your-clever-domain-name.com/webhooks?
  hub.mode=subscribe&
  hub.challenge=1158201444&
  hub.verify_token=meatyhamhock
```

First run Flask, then Ngrok

Validating Verification Requests
Whenever your endpoint receives a verification request, it must:
- Verify that the hub.verify_token value matches the string you set in the Verify Token field when you configure the Webhooks product in your App Dashboard (you haven't set up this token string yet).
- Respond with the hub.challenge value.

After succesful verification of your Callback URL, you must subscribe to events using the Webhook fields. Click on manage and select all the relevent subscriptions; in our case only `messages`.

## Receive a test message

If your flask app and ngrok are running, you can click on "Test" next to messages to test the subscription. You recieve a test message in upper case. If that is the case, your webhook is set up correctly.

You can now also send a message via whatsapp to you bot and it should reply instantly in upper case to you.


##  Validating Payloads
We sign all Event Notification payloads with a SHA256 signature and include the signature in the request's X-Hub-Signature-256 header, preceded with sha256=. You don't have to validate the payload, but you should.

To validate the payload:

Generate a SHA256 signature using the payload and your app's App Secret.
Compare your signature to the signature in the X-Hub-Signature-256 header (everything after sha256=). If the signatures match, the payload is genuine.

## Running the App
When you want to run the app, just execute the run.py script. It will create the app instance and run the Flask development server.
Lastly, it's good to note that when you deploy the app to a production environment, you might not use run.py directly (especially if you use something like Gunicorn or uWSGI). Instead, you'd just need the application instance, which is created using create_app(). The details of this vary depending on your deployment strategy, but it's a point to keep in mind.
## Phone Numbers
When you’re ready to use your app for a production use case, you need to use your own phone number to send messages to your users. When choosing a phone number, consider the following:

https://developers.facebook.com/docs/whatsapp/phone-numbers/

