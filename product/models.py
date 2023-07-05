import cv2
import os
from django.core.files import File
from io import BytesIO
from PIL import Image
import uuid
from django.utils.text import slugify
from django.db import models
from product.services import processing_image
import numpy as np

from PIL import Image, ImageDraw, ImageFont
import sys
from django.core.files.uploadedfile import InMemoryUploadedFile 

class Category(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=200, unique=True, null=False, blank=True)
    image = models.ImageField(upload_to="category")
    parent = models.ForeignKey('self', related_name='childrens', 
                               on_delete=models.CASCADE, null=True, blank=True)
    create_date = models.DateField(auto_now_add=True)
    update_date = models.DateField(auto_now=True)


    class Meta:
        db_table = 'category'

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)

        if self.image:
            # Đọc hình ảnh và chuyển đổi thành định dạng NumPy array
            image = Image.open(self.image)
            image_array = np.array(image)

            # Xử lý hình ảnh bằng hàm processing_image
            processed_image_array = processing_image(image_array)

            # Tạo một đối tượng hình ảnh từ mảng NumPy đã xử lý
            processed_image = Image.fromarray(processed_image_array)

            # Lưu hình ảnh đã xử lý vào trường image
            output = BytesIO()
            processed_image.save(output, format='JPEG')
            output.seek(0)
            self.image = InMemoryUploadedFile(
                output,
                'ImageField',
                f"{self.image.name.split('.')[0]}.jpg",
                'image/jpeg',
                sys.getsizeof(output),
                None,
            )

        super().save(*args, **kwargs)

