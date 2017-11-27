import json
import sys

from core.rules import validate_game


def lambda_handler(event):
    print("Event: %s" % event)

    game = json.loads(event)
    return validate_game(game)


result = lambda_handler(sys.argv[1])
print(result)
