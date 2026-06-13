#!/usr/bin/python3
"""
fetching and print posts
"""
import requests
import csv


def fetch_and_print_posts():
    """
    fetch and print posts
    """
    response = requests.get("https://jsonplaceholder.typicode.com/posts")
    print("Status Code: {}".format(response.status_code))

    if response.status_code == 200:
        posts = response.json()
        for post in posts:
            print(post["title"])


def fetch_and_save_posts():
    """
    fetch and save posts
    """
    response = requests.get("https://jsonplaceholder.typicode.com/posts")

    if response.status_code == 200:
        posts = response.json()
        new_list = []

        for post in posts:
            new_list.append({
                "id": post["id"],
                "title": post["title"],
                "body": post["body"]
                })

        with open("posts.csv", "w", newline="") as csvfile:
            fieldnames = ["id", "title", "body"]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(new_list)
