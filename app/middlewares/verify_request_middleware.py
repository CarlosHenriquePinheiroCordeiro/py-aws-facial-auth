from fastapi.routing import APIRoute
from fastapi import Request

class VerifyRequestMiddleware(APIRoute):
    def get_route_handler(self):
        original_route_handler = super().get_route_handler()

        async def custom_route_handler(request: Request):
            #some validation
            return await original_route_handler(request)

        return custom_route_handler
