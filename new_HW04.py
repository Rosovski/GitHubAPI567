import requests
import json
api_base = "https://api.github.com"


def get_repos(username):
    url = "{}/users/{}/repos".format(api_base, username)
    res = requests.get(url)

    if res.status_code != 200:
        return "Request Failed"

    return json.loads(res)


def get_commits(username, repo):
    url = "{}/repos/{}/{}/commits".format(api_base, username, repo)
    res = requests.get(url)

    if res.status_code != 200:
        return "Request Failed"

    return json.loads(res)


def get_summary(username):
    repos = get_repos(username)

    if repos == "Request Failed":
        return "Request Failed"

    result = "User: {}\n".format(username)

    for repo in repos:
        commits = get_commits(username, repo["name"])
        if commits == "Request Failed":
            return "Request Failed"
        result += "Repo: {} Number of commits: {}\n".format(
            repo["name"], len(commits))

    return result[:-1]


if __name__ == '__main__':
    print(get_repos("Rosovski"))
