

## Building a WhatsApp Bot

Follow the instructions here: https://developers.facebook.com/docs/whatsapp/cloud-api/get-started

You can find your bots here: https://developers.facebook.com/apps/?

Here's all the documentation for the WhatsApp API: https://developers.facebook.com/docs/whatsapp

Here's another helpful guide: https://developers.facebook.com/blog/post/2022/10/24/sending-messages-with-whatsapp-in-your-python-applications/

Here's a link to the API docs for sending messages: https://developers.facebook.com/docs/whatsapp/cloud-api/guides/send-messages


### Get Started

#### Step 1: Select phone numbers

Select the business account

You start with a test number that you can use to send messages to up to 5 numbers

Go to API Setup and find your test number that you will be sending from

Here you can also add numbers to send to. Put in your own number.

You'll receive a code on your phone via WhatsApp to verify your number

#### Step 2: Send messages with the API

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


#### Step 3: Configure webhooks to receive messages

In the App Dashboard, go to WhatsApp > Configuration, then click the Edit button.

Callback URL: This is the URL Meta will be sending the events to. See the Webhooks, Getting Started guide for information on creating the URL.
Verify Token: This string is set up by you, when you create your webhook endpoint.
You can generate a verify token here ot pick any string you like: https://it-tools.tech/token-generator

After saving, back in the Configuration panel, click the Manage button and subscribe to individual webhook fields. To receive notifications of customer messages, be sure to subscribe to the messages webhook field.


#### Step 4: Test with a local server

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

Receive a test message

If your flask app and ngrok are running, you can click on "Test" next to messages to test the subscription. You recieve a test message in upper case. If that is the case, your webhook is set up correctly.

You can now also send a message via whatsapp to you bot and it should reply instantly in upper case to you.


Validating Payloads
We sign all Event Notification payloads with a SHA256 signature and include the signature in the request's X-Hub-Signature-256 header, preceded with sha256=. You don't have to validate the payload, but you should.

To validate the payload:

Generate a SHA256 signature using the payload and your app's App Secret.
Compare your signature to the signature in the X-Hub-Signature-256 header (everything after sha256=). If the signatures match, the payload is genuine.

#### Step 5: Learn about the API and build your app
Review the developer documentation to learn how to build your app and start sending messages. [See documentation](https://developers.facebook.com/docs/whatsapp/cloud-api).

#### Step 6: Add a phone number

When you’re ready to use your app for a production use case, you need to use your own phone number to send messages to your users.
To start sending messages to any WhatsApp number, add a phone number. To manage your account information and phone number, [see the Overview page.](https://business.facebook.com/wa/manage/home/) and the [WhatsApp docs](https://developers.facebook.com/docs/whatsapp/phone-numbers/).

If you want to use a number that is already being used in the WhatsApp customer or business app, you will have to fully migrate that number to the business platform. Once the number is migrated, you will lose access to the WhatsApp customer or business app. [See Migrate Existing WhatsApp Number to a Business Account for information](https://developers.facebook.com/docs/whatsapp/cloud-api/get-started/migrate-existing-whatsapp-number-to-a-business-account).

Once you have chosen your phone number, you have to add it to your WhatsApp Business Account. [See Add a Phone Number](https://developers.facebook.com/docs/whatsapp/cloud-api/get-started/add-a-phone-number).

When dealing with WhatsApp Business API and wanting to experiment without affecting your personal number, you have a few options:

1. **Buy a New SIM Card**: 
    - This is the most straightforward way. Purchase a cheap prepaid SIM card. Insert it into your phone or another device, activate WhatsApp, and then use this number with the WhatsApp Business API.
    - **Pros**: Full control over the number, easy to replace.
    - **Cons**: Costs associated with purchasing a new SIM, managing another phone number.

2. **Virtual Phone Numbers**: 
    - Services like Twilio, Nexmo, or Burner offer virtual phone numbers that you can use for WhatsApp.
    - **Pros**: No need for physical SIM cards, easy to set up, and some platforms might offer integration with the WhatsApp Business API directly.
    - **Cons**: Costs associated with maintaining a virtual number, some numbers might not be supported by WhatsApp.

3. **Dual SIM Phones**: 
    - If you have a dual SIM phone, you can use the second SIM slot for an experimental number without affecting your primary number.
    - **Pros**: Use one device for both numbers, easy to switch.
    - **Cons**: Costs associated with purchasing a new SIM, might not be feasible if you don't have a dual SIM device.

4. **Use a Different Device**: 
    - If you have an old smartphone lying around, you can use it exclusively for this purpose. This way, your primary device and number remain unaffected.
    - **Pros**: Completely isolated environment, no disturbances to the primary number.
    - **Cons**: Need an additional device.

5. **Temporary Number Services**: 
    - Some online services offer temporary phone numbers to receive SMS. They might work for activating WhatsApp, but there's a risk involved.
    - **Pros**: No costs, online-based.
    - **Cons**: Not secure, numbers are public (others can see your activation code), WhatsApp might block these numbers if detected.

6. **Dedicated Devices for Development**: 
    - In a professional setting, developers sometimes use dedicated devices for development and testing purposes. These are kept separate from personal devices.
    - **Pros**: Consistent environment, isolated from personal data.
    - **Cons**: Costs associated with maintaining separate devices.

**Recommendation**: If this is for a more prolonged or professional purpose, using a virtual phone number service or purchasing a new SIM card for a dedicated device is advisable. For quick tests, a temporary number might suffice, but always be cautious about security and privacy. Remember that once a number is associated with WhatsApp Business API, it cannot be used with regular WhatsApp on a device unless you deactivate it from the Business API and reverify it on the device.