from typing import List

from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from .. import database, oauth2, schemas
from ..repository import blog

router = APIRouter(
    prefix="/blog",
    tags=['Blogs']
)
get_db = database.get_db


@router.get('', response_model=List[schemas.ShowBlog])
def all_blog(db: Session = Depends(get_db),
             current_user: schemas.User = Depends(
                oauth2.get_current_user)):
    return blog.get_all(db)


@router.post('', status_code=status.HTTP_201_CREATED)
def create_blog(request: schemas.Blog, db: Session = Depends(get_db)):
    return blog.create(db, request)


@router.get('/{id}', status_code=status.HTTP_200_OK,
            response_model=schemas.ShowBlog)
def show(id: int, db: Session = Depends(get_db)):
    return blog.show(id, db)


@router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT)
def destroy(id: int, db: Session = Depends(get_db)):
    return blog.destroy(id, db)


@router.put('/{id}', status_code=status.HTTP_202_ACCEPTED)
def update(id: int, request: schemas.Blog, db: Session = Depends(get_db)):
    return blog.update(id, db, request)
