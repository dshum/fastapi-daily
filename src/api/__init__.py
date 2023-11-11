from api import meal, weighting, user

__all__ = ["routers"]

routers = [
    user.router,
    weighting.router,
    meal.router,
]
