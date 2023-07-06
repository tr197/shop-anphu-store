import cv2
import uuid
import sys
import numpy as np
from io import BytesIO
from PIL import Image
from django.utils.text import slugify
from django.core.files.uploadedfile import InMemoryUploadedFile 
from django.db import models
from app.constants import PHONE_NUMBER
from django.urls import reverse

class BaseProduct(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=200, null=False, blank=False)
    slug = models.SlugField(max_length=200, unique=True, null=False, blank=True)
    image = models.ImageField(upload_to="product/images")
    create_date = models.DateField(auto_now_add=True)
    update_date = models.DateField(auto_now=True)
    
    class Meta:
        abstract = True
        db_table = 'base_product'

    def __str__(self) -> str:
        return self.name[:200]


    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)

        if self.image:
            processed_image_array = self.__processing_image()

            # Tạo một đối tượng hình ảnh từ mảng NumPy đã xử lý
            processed_image = Image.fromarray(processed_image_array)

            # Lưu hình ảnh đã xử lý vào trường image
            output = BytesIO()
            try:
                processed_image.save(output, format='PNG')
            except Exception as e:
                try:
                    processed_image.save(output, format='JPEG')
                except Exception as e:
                    print(f'JPEG error: {e}')
                    return

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

    def __processing_image(self):
        """Chèn chữ vào ảnh trước khi lưu"""
        
        image_cv = Image.open(self.image)
        image_cv = np.array(image_cv)

        # Nội dung chữ
        text_content = PHONE_NUMBER
        font_scale = int(image_cv.shape[0] // 250)
        thickness = int(image_cv.shape[0] // 400)
        text_color = (255, 255, 255)
        font = cv2.FONT_HERSHEY_DUPLEX

        # Xác định kích thước của chữ
        (text_width, text_height), _ = cv2.getTextSize(text_content, font, font_scale, thickness=thickness)

        # Tính toán vị trí chữ để chèn vào trung tâm hình ảnh
        image_height, image_width, _ = image_cv.shape
        text_x = (image_width - text_width) // 2
        text_y = (image_height + text_height) // 2

        cv2.putText(image_cv, text_content, (text_x, text_y), 
                    font, font_scale, text_color, 
                    thickness=thickness, lineType=cv2.LINE_AA)

        return image_cv


class BaseCategory(BaseProduct):

    class Meta:
        db_table = 'base_category'

    def __str__(self) -> str:
        try:
            sub_category = SubCategory.objects.get(id=self.id)
            return f'{sub_category.parent_category.name[:70]} > {sub_category.name[:200]}'
        except Exception:
            return self.name[:100]


class Category(BaseCategory):

    class Meta:
        db_table = 'category'


    def get_link_to(self):
        return reverse(
            'product:list-category',
            kwargs={'slug': self.slug, 'category_id': self.id}
            )


class SubCategory(BaseCategory):
    parent_category = models.ForeignKey(Category, related_name='children',
                                        on_delete=models.CASCADE,
                                        null=False, blank=False,)

    class Meta:
        db_table = 'sub_category'

    def __str__(self) -> str:
        return f'{self.parent_category.name[:70]} > {self.name[:200]}'
    
    def get_link_to(self):
        return reverse(
            'product:list-products',
            kwargs={'slug': self.parent_category.slug, 'sub_slug': self.slug, 'sub_category_id': self.id}
            )
    

class Product(BaseProduct):
    category = models.ForeignKey(BaseCategory, related_name='products',
                                 on_delete=models.CASCADE,
                                 null=False, blank=False)
    
    class Meta:
        db_table = 'product'



