from fastapi import APIRouter, Query
from app.email_manager import manage_email
from app.reddit_bot import automate_reddit
from app.scraper import scrape_social_media

router = APIRouter()

@router.get("/email/read")
def read_email():
    return manage_email("read")

@router.post("/email/send")
def send_email(to: str, subject: str, body: str):
    return manage_email("send", to, subject, body)

@router.post("/reddit/comment")
def post_comment(content: str):
    return automate_reddit("comment", content)

@router.post("/scraper/scrape")
def scrape_data(url: str = Query(...), data_type: str = Query("comments")):
    return scrape_social_media(url, data_type)
