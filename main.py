from fastapi import FastAPI

from routers.friends import router as friends_router
from routers.rooms import router as rooms_router
from routers.users import router as users_router
from routers.websockets.sockets import router as websocket_rooms_router


app = FastAPI()


app.include_router(friends_router, prefix="/api/friends", tags=["friends"])
app.include_router(rooms_router, prefix="/api/rooms", tags=["rooms"])
app.include_router(users_router, prefix="/api/users", tags=["users"])

app.include_router(websocket_rooms_router, prefix="/ws/room")
