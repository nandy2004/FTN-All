from fastapi import APIRouter

router=APIRouter()

@router.get('/users')
def Hello():
    return "Hello"