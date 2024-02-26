#!/bin/python3

import requests

def gitHub_parser(username):
    repos = get_repos(username)
    for repo in repos:
        commits = get_commits(username, repo['name'])
        print(f"Repo: {repo['name']} Number of commits: {len(commits)}")

def get_repos(username):
    url = f'https://api.github.com/users/{username}/repos'
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return None

def get_commits(username, repo_name):
    url = f'https://api.github.com/repos/{username}/{repo_name}/commits'
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return None

if __name__ == "__main__":
    username = input("Enter GitHub username: ")
    gitHub_parser(username)