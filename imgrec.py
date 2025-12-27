import cv2
import mediapipe as mp
from mediapipe.tasks import python
from mediapipe.tasks.python import vision


print(dir(mp)) 

model_path = 'blaze_face_short_range.tflite'

base_options = python.BaseOptions(model_asset_path=model_path)
options = vision.FaceDetectorOptions(base_options=base_options)
detector = vision.FaceDetector.create_from_options(options)

image_cv2 = cv2.imread('mu.jpg')
image_rgb = cv2.cvtColor(image_cv2, cv2.COLOR_BGR2RGB)
image_mp = mp.Image(image_format=mp.ImageFormat.SRGB, data=image_rgb)   


detection_result = detector.detect(image_mp)  



if detection_result.detections:
    print(f"تعداد چهره‌های شناسایی شده: {len(detection_result.detections)}")
else:
    print("چهره‌ای پیدا نشد.")



for detection in detection_result.detections:
    print('Detection score:', detection.categories[0].score)
    box = detection.bounding_box

            # رسم مستطیل با OpenCV (تبدیل مختصات به عدد صحیح)
    start_point = (int(box.origin_x), int(box.origin_y))
    end_point = (int(box.origin_x + box.width), int(box.origin_y + box.height))
    cv2.rectangle(image_cv2, start_point, end_point, (255, 0, 0), 2)

if detection.keypoints:
        for keypoint in detection.keypoints:
            # مختصات نقاط کلیدی به صورت درصدی (0 تا 1) هستند
            # باید آن‌ها را در عرض و ارتفاع تصویر ضرب کنیم
            x = int(keypoint.x * image_cv2.shape[1])
            y = int(keypoint.y * image_cv2.shape[0])
            
            # رسم یک دایره کوچک سبز رنگ روی هر نقطه
            cv2.circle(image_cv2, (x, y), 5, (0, 255, 0), -1)

# نمایش نتیجه
cv2.imshow('Face & Keypoints', image_cv2)
cv2.waitKey(0)