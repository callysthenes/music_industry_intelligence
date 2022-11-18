import requests
import os
import json

# To set your enviornment variables in your terminal run the following line:
# export 'BEARER_TOKEN'='AAAAAAAAAAAAAAAAAAAAAPEbiQEAAAAAuuFvB9xcB%2FR4J2RXWNApbAWQ3PY%3DVqvJvvr5WlYDYSfMq5GcZqGGu2gapcfF0ezvJzCWfDaodqSE4L'
bearer_token = "AAAAAAAAAAAAAAAAAAAAAPEbiQEAAAAAuuFvB9xcB%2FR4J2RXWNApbAWQ3PY%3DVqvJvvr5WlYDYSfMq5GcZqGGu2gapcfF0ezvJzCWfDaodqSE4L"


def bearer_oauth(r):
    """
    Method required by bearer token authentication.
    """

    r.headers["Authorization"] = f"Bearer {bearer_token}"
    r.headers["User-Agent"] = "v2FilteredStreamPython"
    return r


def get_rules():
    response = requests.get(
        "https://api.twitter.com/2/tweets/search/stream/rules", auth=bearer_oauth
    )
    if response.status_code != 200:
        raise Exception(
            "Cannot get rules (HTTP {}): {}".format(response.status_code, response.text)
        )
    print(json.dumps(response.json()))
    return response.json()


def delete_all_rules(rules):
    if rules is None or "data" not in rules:
        return None

    ids = list(map(lambda rule: rule["id"], rules["data"]))
    payload = {"delete": {"ids": ids}}
    response = requests.post(
        "https://api.twitter.com/2/tweets/search/stream/rules",
        auth=bearer_oauth,
        json=payload
    )
    if response.status_code != 200:
        raise Exception(
            "Cannot delete rules (HTTP {}): {}".format(
                response.status_code, response.text
            )
        )
    print(json.dumps(response.json()))


def set_rules(delete):
    # You can adjust the rules if needed
    sample_rules = [
        {"value": "#badbunny" , "tag": "#badbunny positive", "keyword": "badbunny", "place_country":"US", "lang":"en"},
        {"value": "#harrystyles" , "tag": "#harrystyles positive", "keyword": "harrystyles", "place_country":"US", "lang":"en"},
        {"value": "#onerepublic" , "tag": "#onerepublic", "keyword": "onerepublic", "place_country":"US", "lang":"en"},
        {"value": "#johnlegend" , "tag": "#johnlegend", "keyword": "johnlegend", "place_country":"US", "lang":"en"},
        {"value": "#jcole" , "tag": "#jcole", "keyword": "jcole", "place_country":"US", "lang":"en"}
    ]
    payload = {"add": sample_rules}
    response = requests.post(
        "https://api.twitter.com/2/tweets/search/stream/rules",
        auth=bearer_oauth,
        json=payload,
    )
    if response.status_code != 201:
        raise Exception(
            "Cannot add rules (HTTP {}): {}".format(response.status_code, response.text)
        )
    print(json.dumps(response.json()))


def get_stream(set):
    response = requests.get(
        "https://api.twitter.com/2/tweets/search/stream", auth=bearer_oauth, stream=True,
    )
    print(response.status_code)
    if response.status_code != 200:
        raise Exception(
            "Cannot get stream (HTTP {}): {}".format(
                response.status_code, response.text
            )
        )
    for response_line in response.iter_lines():
        if response_line:
            json_response = json.loads(response_line)
            print(json.dumps(json_response, indent=4, sort_keys=True))
            

def main():
    rules = get_rules()
    delete = delete_all_rules(rules)
    set = set_rules(delete)
    get_stream(set)

if __name__ == "__main__":
    main()
