import requests
from bs4 import BeautifulSoup

def scrape_social_media(url, data_type):
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.content, "html.parser")
    
    if "instagram" in url:
        return {"followers": scrape_instagram_followers(soup)}
    elif data_type == "comments":
        return {"comments": scrape_comments(soup)}
    else:
        return {"error": "Unsupported URL or data type"}

def scrape_instagram_followers(soup):
    meta_content = soup.find("meta", property="og:description")
    return meta_content["content"] if meta_content else "No followers found"

def scrape_comments(soup):
    comments = soup.find_all("div", class_="comment")
    return [comment.text for comment in comments]
