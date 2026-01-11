from typing import List, Optional
from pydantic import BaseModel

class Comment(BaseModel):
    id: int
    content: str
    replies: Optional[List["Comment"]] = None  # Self-referential field/recursive type
Comment.model_rebuild()  # Required to resolve self-references      
comment=Comment(
    id=1,   
    content="first comment",
    replies=[
        Comment(id=2, content="first reply"),
         Comment(id=3, content="second reply",
            replies=[
                Comment(id=4, content="nested reply")
            ]
        )
    ]
)