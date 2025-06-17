from fastapi import APIRouter

router = APIRouter(prefix="/products", tags=["Products"])

@router.get("/")
def list_products():
    return [
        {
            "name": "Logitech MX Master 3",
            "price": 89.99,
            "store": "Amazon",
            "link": "https://www.amazon.es/dp/B07WQ4M5TS"
        }
    ]
