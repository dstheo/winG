from PIL import Image
import cairosvg
import os

# 경로와 파일명
data_path = 'data'
svg_image_name = 'seoul.svg'
jpg_image_name = 'seoul.jpg'

# 파일 경로 생성
svg_full_path = os.path.join(data_path, svg_image_name)
png_full_path = os.path.join(data_path, jpg_image_name.replace('.jpg', '.png'))
jpg_full_path = os.path.join(data_path, jpg_image_name)

# SVG를 PNG로 변환
cairosvg.svg2png(url=svg_full_path, write_to=png_full_path)

# PNG 파일을 열고 JPG로 저장
with Image.open(png_full_path) as png_image:
    png_image = png_image.convert('RGB')  # Ensure the image is in RGB mode before saving as JPG
    png_image.save(jpg_full_path)

# 임시 PNG 파일 삭제
os.remove(png_full_path)