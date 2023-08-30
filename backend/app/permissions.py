from fastapi import Request, HTTPException


async def is_authenticated(request: Request):
    user = request.session.get('user')
    if user is None:
        raise HTTPException(status_code=401, detail="Sign in for access")
    return user
