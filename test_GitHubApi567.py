"""
This is a class project for 2024S SSW 567-WS, Software Testing, Quality Assurance and Maintenance
Group members:
Estevan Stowe
Jacob Gelman-Funk
Tawnya Shannon
"""

import requests_mock
from GitHubApi567 import get_repos, get_commits 

def test_get_repos():
    with requests_mock.Mocker() as m:
        m.get('https://api.github.com/users/testuser/repos', json=[{'name': 'repo1'}, {'name': 'repo2'}])
        repos = get_repos('testuser')
        assert repos == [{'name': 'repo1'}, {'name': 'repo2'}]

def test_get_commits():
    with requests_mock.Mocker() as m:
        m.get('https://api.github.com/repos/testuser/repo1/commits', json=[{}, {}, {}])
        commits = get_commits('testuser', 'repo1')
        assert len(commits) == 3