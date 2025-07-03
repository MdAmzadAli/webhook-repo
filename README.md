This is a setup for checking webhook events of github basically merge, pull_request and push

Requirements

- MongoDB_uri
- One Repo for testing event
- ngrok(for exposing localhost url to a public url) 
- Python
- Node 


Follow the steps below:


- Clone the repo  
- Add `MONGO_URI` in `webhook-repo/app/config.py` file  
- Create another GitHub repo (say `action-repo`) for testing events  
- Configure Webhook setting in `action-repo` to accept ngrok URL which you will get by running the following commands  
- Open the `webhook-repo` in terminal (better to create a virtual environment)


```bash
pip install -r requirements.txt
python run.py
ngrok http 5000
```
- Add the ngrok forwarding url into github repo and configure it to accept pull_request and push
- Create a new terminal
- Go inside the frontend folder , then run the following command

```bash
npm install
npm run dev
```


Now you are ready to test events in the action-repo and watch every action displayed in the frontend UI


