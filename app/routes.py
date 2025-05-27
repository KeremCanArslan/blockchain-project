from fastapi import APIRouter, UploadFile, File, HTTPException
from app.utils import calculate_hash
from app.database import insert_certificate, find_certificate_by_hash

router = APIRouter()

@router.post("/upload/")
async def upload_certificate(file: UploadFile = File(...)):
    file_content = await file.read()
    hash_value = calculate_hash(file_content)
    insert_certificate(file.filename, hash_value)
    return {"message": "Certificate uploaded", "hash": hash_value}

@router.post("/verify/")
async def verify_certificate(file: UploadFile = File(...)):
    file_content = await file.read()
    hash_value = calculate_hash(file_content)
    cert = find_certificate_by_hash(hash_value)
    if cert:
        return {"message": "Certificate is valid", "file": cert['name']}
    else:
        raise HTTPException(status_code=404, detail="Certificate not found")
