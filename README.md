# Get Started
[Install Python](https://www.python.org/downloads/) - If you don't have dotnet already installed on your machine.

[Square Python SDK Guide](https://developer.squareup.com/docs/sdks/python/using-python-sdk) - details on how to use / configure the Square client.

[Python Quickstart Guide](https://developer.squareup.com/docs/sdks/python/quick-start) - The quickstart directory is based off of this document.

[Pip repository for Square](https://pypi.org/project/squareup/) - Where the package files are hosted

[Python SDK Source Code](https://github.com/square/square-python-sdk) - Github repo with sdk source code


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
$ pip3 install -r requirements.txt
```

Install the latest Square SDK
```
$ pip3 install squareup
```

Run the code
```
$ python3 ./quickstart.py
```

You should see output similar to this in your console

```
LHJ1ZXP3YSV8X: Default Test Account, 1600 Pennsylvania Ave NW, Washington
```