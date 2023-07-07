from app.constants import AWSS3Info, BUCKET



def delete_file_object(file_url):
    '''delete aws s3 file object'''

    if not AWSS3Info.USING:
        return True
    try:
        BUCKET.delete_objects(Delete={'Objects': [{'Key': file_url}]})
        print(f'action: delete {file_url}')
        return True
        
    except Exception as e:
        print(f'error: can not delete {file_url}')
        print(f'error detail: {e}')
        return False
    