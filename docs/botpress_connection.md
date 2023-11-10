# Connecting Botpress to WhatsApp

You can check out [this video from Botpress](https://www.youtube.com/watch?v=LQd1iGJLj58&) for a video walkthrough of the following steps. If you have never used WhatsApp for business, please refer to [this page]((https://developers.facebook.com/docs/whatsapp/cloud-api/get-started)). This tutorial will use a WhatsApp test number that will be automatically created for you. I believe, you cannot have two Test numbers under one Meta business account.

## Steps
1. Create bot in Botpress
2. Make sure the bot is published
4. Go to your [Meta Developers](https://developers.facebook.com/apps/) account
5. Create App, Other, Business, Name your app, Select WhatsApp as the integration
6. In Botpress, go to integration and click "Browse in Hub"
7. Select WhatsApp and install to your Botpress project
8. Now you have to fill Verify Token, Access Token, and default number
   - Verify Token: a string that you can select (e.g., 12345)
   - Access Token: In the Meta App dashboard, to API Setup and copy your temporary Access Token (valid for 24 hours)
   - Default Number: On the API Setup page, you can also copy the Phone number ID for your test number
9. Press save and enable intergration
10. Now on the same page, copy the Webhook URL from the Botpress WhatsApp integration page
11. Go back to your Meta app, select Configuration, and edit the Callback URL
12. Paste the Webhook URL and your same Verify Token that you just came up with (e.g., Again, 12345)
13. Now click verify and save
14. Now on the same page, got to Webhook fields, Manage and Subscribe to messages
15. Now go back to API Setup and select your test phone number (or add if it's your first time). This should be your own number that you have access to.
16. Next, click send test message wait for your message to appear in WhatsApp (this can take 60-120 seconds).
17. Your connection with Botpress should now be live and you can start chatting!
