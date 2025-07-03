This is a setup for checking webhook events of github basically merge, pull_request and push

Requirements
`
MongoDB_uri
One Repo for testing event
ngrok(for exposing localhost url to a public url) 
python
`

Follow the steps below

`
-clone the repo
-add MONGO_URI in webhook-repo/app/config.py file
-create another github repo say action-repo for testing events 
-configure Webhook setting in action-repo to accept ngrok url which you will get by running following commands
-open the webhook-repo in terminal(Better to create a virtual environment)

```bash
pip install -r requirements.txt
python run.py
ngrok http 5000
```
-add the ngrok forwarding url into github repo and configure it to accept pull_request and push
-create a new terminal
-go inside the frontend folder , then run the following command

```bash
npm install
npm run dev
```
`

Now you are ready to test events in the action-repo and watch every action displayed in the frontend UI


