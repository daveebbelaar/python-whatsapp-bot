# Building a WhatsApp Bot

This guide will walk you through the process of creating a WhatsApp bot using the Meta (formerly Facebook) Cloud API. We'll also integrate webhook events to receive messages in real-time.

## Prerequisites

1. Access to Meta's developer platform: [developers.facebook.com](https://developers.facebook.com/)
2. Familiarity with Python for some examples.
3. A registered WhatsApp Business account.

## Table of Contents

- [Building a WhatsApp Bot](#building-a-whatsapp-bot)
  - [Prerequisites](#prerequisites)
  - [Table of Contents](#table-of-contents)
  - [Get Started](#get-started)
    - [Step 1: Select Phone Numbers](#step-1-select-phone-numbers)
    - [Step 2: Send Messages with the API](#step-2-send-messages-with-the-api)
    - [Step 3: Configure Webhooks to Receive Messages](#step-3-configure-webhooks-to-receive-messages)
    - [Step 4: Test with a Local Server](#step-4-test-with-a-local-server)
    - [Step 5: Learn about the API and Build Your App](#step-5-learn-about-the-api-and-build-your-app)
    - [Step 6: Add a Phone Number](#step-6-add-a-phone-number)
  - [Choosing the Right Phone Number for Your Bot](#choosing-the-right-phone-number-for-your-bot)

## Get Started

1. **Overview & Setup**: Begin your journey [here](https://developers.facebook.com/docs/whatsapp/cloud-api/get-started).
2. **Locate Your Bots**: Your bots can be found [here](https://developers.facebook.com/apps/).
3. **WhatsApp API Documentation**: Familiarize yourself with the [official documentation](https://developers.facebook.com/docs/whatsapp).
4. **Helpful Guide**: Here's a [Python-based guide](https://developers.facebook.com/blog/post/2022/10/24/sending-messages-with-whatsapp-in-your-python-applications/) for sending messages.
5. **API Docs for Sending Messages**: Check out [this documentation](https://developers.facebook.com/docs/whatsapp/cloud-api/guides/send-messages).

### Step 1: Select Phone Numbers

- Choose your business account.
- Start with a test number: It can send messages to up to 5 numbers.
- Access the API Setup to find your test number.
- Add your phone number for testing and verify it via a code sent to WhatsApp.

### Step 2: Send Messages with the API

- Obtain a 24-hour access token from the API access section.
- Follow the given example to send messages using `curl`.
- Convert this into a Python function if desired.
- You will receive a "Hello World" message.

> Note: Expect a 60-120 second delay for the message.

### Step 3: Configure Webhooks to Receive Messages

- Edit the configuration in the App Dashboard.
- Set up the Callback URL and Verify Token.
- Save changes and manage webhook field subscriptions.
  
### Step 4: Test with a Local Server

- Register on [ngrok](https://dashboard.ngrok.com) and set up a domain.
- Configure the authentication token.
- Review the [Webhooks Getting Started Guide](https://developers.facebook.com/docs/graph-api/webhooks/getting-started).
- Ensure Flask and Ngrok are running, and then test your webhook.

### Step 5: Learn about the API and Build Your App

- Dive into the [developer documentation](https://developers.facebook.com/docs/whatsapp/cloud-api).

### Step 6: Add a Phone Number

- Add a production phone number when ready.
- Migrate an existing number if needed.
  
## Choosing the Right Phone Number for Your Bot

There are various methods to get a phone number for your bot:

1. **New SIM Card**
2. **Virtual Phone Numbers**
3. **Dual SIM Phones**
4. **Use a Different Device**
5. **Temporary Number Services**
6. **Dedicated Devices for Development**

Choose wisely based on your needs. For long-term or professional usage, a virtual number or a new SIM card is recommended.


