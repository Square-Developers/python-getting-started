# Get Started
[Install Python](https://www.python.org/downloads/) - If you don't have dotnet already installed on your machine.

[Square Python SDK Guide](https://developer.squareup.com/docs/sdks/python/using-python-sdk) - details on how to use / configure the Square client.

[Python Quickstart Guide](https://developer.squareup.com/docs/sdks/python/quick-start) - The quickstart directory is based off of this document.


## Quickstart Instructions

Change into the `quickstart` directory

copy `.env.example` to `.env` and replace with your access token
```
SQUARE_ACCESS_TOKEN=yourSandboxAccessToken
```

Create a virtual environment
```
$ python3 -m venv env
```

Activate the environment
```
$ source env/bin/activate
```

Install dependencies
```
$ pip install -r requirements.txt
```

Set your Access Token in your Environment Variables
```
$ export SQUARE_ACCESS_TOKEN=yourSandboxAccessToken
```

Run the code
```
$ python ./quickstart.py
```

You should see your `Square Sandbox Seller account's` location logged in the console.