import requests


def handler(event, context):
    resp = requests.get("https://dev.classmethod.jp")
    print(resp.text[:200])


if __name__ == "__main__":
    handler(None, None)
