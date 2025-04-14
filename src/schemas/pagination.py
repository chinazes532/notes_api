from typing import Annotated

from fastapi import Depends
from pydantic import BaseModel, Field


class PaginationParams(BaseModel):
    limit: int = Field(5, ge=0, le=100, description="Количество элементов на странице")
    offset: int = Field(0, ge=0, description="Смещение от начала")


PaginationDep = Annotated[PaginationParams, Depends(PaginationParams)]