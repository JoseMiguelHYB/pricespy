from fastapi import APIRouter
from app.services.scraper import scrape_amazon

router = APIRouter(prefix="/products", tags=["Products"])

@router.get("/")
def list_products(q: str = "Logitech MX Master 3"):
    return scrape_amazon(q)
