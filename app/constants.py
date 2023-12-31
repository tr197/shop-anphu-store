import environ
from enum import Enum
import boto3


env = environ.Env()
environ.Env.read_env()


class PathUploadImg:
    CATEGORY=env('PATH_IMG_CATEGORY')
    PRODUCT_MAIN=env('PATH_IMG_PRODUCT_MAIN')
    PRODUCT_OTHER=env('PATH_IMG_PRODUCT_MAIN')


class AWSS3Info(Enum):
    USING = bool(int(env('MEDIA_S3')))
    AWS_ACCESS_KEY_ID=env('AWS_ACCESS_KEY_ID')
    AWS_SECRET_ACCESS_KEY=env('AWS_SECRET_ACCESS_KEY')
    AWS_STORAGE_BUCKET_NAME=env('AWS_STORAGE_BUCKET_NAME')
    AWS_S3_REGION_NAME=env('AWS_S3_REGION_NAME')
    AWS_S3_CUSTOM_DOMAIN = env('AWS_S3_CUSTOM_DOMAIN')
    DEFAULT_FILE_STORAGE = env('DEFAULT_FILE_STORAGE')


S3 = boto3.resource('s3',
                    aws_access_key_id = AWSS3Info.AWS_ACCESS_KEY_ID.value,
                    aws_secret_access_key = AWSS3Info.AWS_SECRET_ACCESS_KEY.value,
                    region_name = AWSS3Info.AWS_S3_REGION_NAME.value)

BUCKET = S3.Bucket(AWSS3Info.AWS_STORAGE_BUCKET_NAME.value)


class CmpInfo:
    PHONE_NUMBER = "0941.145.689"
    DOMAIN_NAME = "phukienanphu.com"
    NAME = "CÔNG TY TNHH THIẾT BỊ ĐIỆN NƯỚC AN PHÚ"
    SHORT_INTRO = "Nhà cung cấp phụ kiện vật tư ngành nước"
    LONG_DESCRIPTION = """Luôn trú trọng vào chất lượng sản phẩm vì 
                        sự hài lòng của khác hàng là niềm vui của chúng tôi"""