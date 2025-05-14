def decode_blog(doc) -> dict:
    return {
        "_id": str(doc.get("_id")),
        "title": doc.get("title"),
        "sub_title": doc.get("sub_title", ""),  
        "content": doc.get("content"),
        "author": doc.get("author"),
        "tags": doc.get("tags", []),  
        "date": doc.get("date")
    }


def decode_blogs(docs) -> list:
    return [decode_blog(doc) for doc in docs]