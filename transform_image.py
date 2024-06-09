import requests

# مفتاح API الخاص بك من DeepAI
api_key = '056f18fc-0420-40b7-85bf-91624b4c0782'

# عنوان API لمحرر الصور من DeepAI
url = 'https://api.deepai.org/api/image-editor'

# المسار إلى الصورة التي تريد تحويلها
image_path = 'C:/Users/ELmohands/Downloads/ft1.jpg'  # تأكد من تحديث المسار حسب الحاجة

# فتح ملف الصورة
with open(image_path, 'rb') as image_file:
    response = requests.post(
        url,
        files={'image': image_file},
        headers={'api-key': api_key},
        data={'prompt': 'make the body look slimmer'}
    )

# التحقق من نجاح الطلب
if response.status_code == 200:
    result = response.json()
    # تحميل الصورة المعدلة
    transformed_image_url = result['output_url']
    transformed_image = requests.get(transformed_image_url)

    # حفظ الصورة المعدلة
    with open('transformed_image.jpg', 'wb') as out_file:
        out_file.write(transformed_image.content)
    print('تم التحويل بنجاح! الصورة المعدلة تم حفظها باسم transformed_image.jpg')
else:
    print('خطأ:', response.status_code, response.text)
