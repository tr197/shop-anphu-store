import environ
from enum import Enum

env = environ.Env()
environ.Env.read_env()


class PathUploadImg:
    CATEGORY=env('PATH_IMG_CATEGORY')
    PRODUCT_MAIN=env('PATH_IMG_PRODUCT_MAIN')
    PRODUCT_OTHER=env('PATH_IMG_PRODUCT_MAIN')


class AWSS3Info(Enum):
    AWS_ACCESS_KEY_ID=env('AWS_ACCESS_KEY_ID')
    AWS_SECRET_ACCESS_KEY=env('AWS_SECRET_ACCESS_KEY')
    AWS_STORAGE_BUCKET_NAME=env('AWS_STORAGE_BUCKET_NAME')
    AWS_S3_REGION_NAME=env('AWS_S3_REGION_NAME')
    AWS_S3_CUSTOM_DOMAIN = env('AWS_S3_CUSTOM_DOMAIN')
    DEFAULT_FILE_STORAGE = env('DEFAULT_FILE_STORAGE')


class CmpInfo:
    PHONE_NUMBER = "0941.145.689"
    NAME = "CÔNG TY TNHH THIẾT BỊ ĐIỆN NƯỚC AN PHÚ"
    LONG_DESCRIPTION = """Luôn trú trọng vào chất lượng sản phẩm vì 
                        sự hài lòng của khác hàng là niềm vui của chúng tôi"""