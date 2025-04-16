from square import Square
from square.environment import SquareEnvironment
from square.core.api_error import ApiError
from dotenv import load_dotenv
import os

load_dotenv()

client = Square(
    environment=SquareEnvironment.SANDBOX,
    token=os.environ['SQUARE_ACCESS_TOKEN']
)

try:
    response = client.locations.list()
    for location in response.locations:
        print(f"{location.id}: ", end="")
        print(f"{location.name}, ", end="")
        print(f"{location.address}, ", end="")

except ApiError as e:
    for error in e.errors:
        print(error.category)
        print(error.code)
        print(error.detail)