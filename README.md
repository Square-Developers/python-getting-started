# Square Python SDK Quickstart

This quickstart sample creates a Square client instance with your Square access token and then lists the locations in your account.
The sample is based on the [Python SDK Quickstart guide](https://developer.squareup.com/docs/sdks/python/quick-start).

## Setup
[Install Python](https://www.python.org/downloads/) - If you don't have dotnet already installed on your machine.

## Quickstart Instructions

1. Change into the `quickstart` directory

1. copy `.env.example` to `.env` and replace with your access token
    ```
    SQUARE_ACCESS_TOKEN=yourSandboxAccessToken
    ```

1. Create a virtual environment
    ```
    $ python3 -m venv env
    ```

1. Activate the environment
    ```
    $ source env/bin/activate
    ```

1. Install dependencies
    ```
    $ pip3 install -r requirements.txt
    ```

1. Install the latest Square SDK
    ```
    $ pip3 install squareup
    ```

1. Run the code
    ```
    $ python3 ./quickstart.py
    ```

1. You should see output similar to this in your console
    ```
    LHJ1ZXP3YSV8X: Default Test Account, 1600 Pennsylvania Ave NW, Washington
    ```

## Resources
[Square Python SDK Guide](https://developer.squareup.com/docs/sdks/python/using-python-sdk) - details on how to use / configure the Square client.

[Pip repository for Square](https://pypi.org/project/squareup/) - Where the package files are hosted

[Python SDK Source Code](https://github.com/square/square-python-sdk) - Github repo with sdk source code