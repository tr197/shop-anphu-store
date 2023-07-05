import cv2
from app.constants import PHONE_NUMBER


def processing_image(image):
    """Chèn chữ vào ảnh trước khi lưu"""
    
    # image = cv2.imread(image)

    # Nội dung chữ
    text_content = PHONE_NUMBER
    font_scale = int(image.shape[0] // 250)
    thickness = int(image.shape[0] // 400)
    text_color = (255, 255, 255)
    font = cv2.FONT_HERSHEY_DUPLEX

    # Xác định kích thước của chữ
    (text_width, text_height), _ = cv2.getTextSize(text_content, font, font_scale, thickness=thickness)

    # Tính toán vị trí chữ để chèn vào trung tâm hình ảnh
    image_height, image_width, _ = image.shape
    text_x = (image_width - text_width) // 2
    text_y = (image_height + text_height) // 2

    cv2.putText(image, text_content, (text_x, text_y), font, font_scale, text_color, thickness=thickness, lineType=cv2.LINE_AA)

    return image