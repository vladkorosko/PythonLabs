import os


def client_request(request: str) -> None:
    with open("lab5/classes/requests.txt", "a+") as requests:
        requests.write(request + "\n")


def client_responses() -> str:
    with open("lab5/classes/responses.txt", "r") as responses:
        while True:
            line = responses.readline()
            if not line:
                break
            print(line)

    os.remove("lab5/classes/responses.txt")
