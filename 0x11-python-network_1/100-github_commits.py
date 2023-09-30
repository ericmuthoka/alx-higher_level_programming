#!/usr/bin/python3
"""
Module for interacting with the GitHub API and extracting information.
"""

import requests
from requests.auth import HTTPBasicAuth
from sys import argv


def main(argv):
    """
    Lists the 10 most recent commits in a repository.
    Usage: ./script.py <repository_name> <owner_name>
    """

    def print_commits(i, commit_list):
        """
        Prints commit details for up to 10 commits.
        """
        sha = commit_list[i].get('sha')
        commit = commit_list[i].get('commit')
        author = commit.get('author')
        name = author.get('name')
        print('{}: {}'.format(sha, name))

    repo = argv[1]
    owner = argv[2]
    headers = {"Accept": "application/vnd.github.v3+json"}
    url = f'https://api.github.com/repos/{owner}/{repo}/commits'
    response = requests.get(url, headers=headers)
    commit_list = response.json()
    size = len(commit_list)
    if size < 10:
        for i in range(size):
            print_commits(i, commit_list)
    else:
        for i in range(10):
            print_commits(i, commit_list)


if __name__ == "__main__":
    main(argv)
