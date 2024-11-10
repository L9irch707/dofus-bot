import pyautogui as pg
import time

# دالة للتحقق من الصورة واللون
def checkImage(image_path, target_rgb=None(0, 255, 0)):
    try:
        # إضافة تأخير لتأكد من أن اللعبة أو التطبيق قد تم تحميله
        time.sleep(5)  # تأخير أكبر لضمان تحميل اللعبة بشكل كامل
        
        # تحديد موقع الصورة على الشاشة
        print(f"Looking for image: {image_path}")  # طباعة للمساعدة في التعرف على الصورة
        pos = pg.locateOnScreen(image_path, confidence=0.7)  # محاولة البحث عن الصورة مع الثقة 0.7
        
        if pos:
            print(f"Image found at position: {pos}")  # طباعة الموقع الذي تم العثور عليه

            # إذا تم توفير قيمة RGB، تحقق من اللون عند الموضع المحدد
            if target_rgb:
                # احصل على اللون في الموقع المحدد
                pixel_color = pg.pixel(pos[0], pos[1])
                print(f"Pixel color at position {pos}: {pixel_color}")  # طباعة اللون
                
                # تحقق من تطابق اللون (إذا كان اللون يطابق)
                if pixel_color == target_rgb:
                    print("RGB color match found!")
                    pg.moveTo(pos[0], pos[1])
                    pg.click()
                    print(f"Image {image_path} found and clicked.")
                else:
                    print("RGB color does not match. Skipping click.")
            else:
                # إذا لم يتم تحديد لون RGB، فقط انقر على الصورة
                pg.moveTo(pos[0], pos[1])
                pg.click()
                print(f"Image {image_path} found and clicked.")
        else:
            print(f"Image {image_path} not found on screen.")
    except Exception as e:
        print(f"An error occurred: {e}")  # طباعة الرسالة التي قد تحدث أثناء التنفيذ

# تحديد قيمة RGB المستهدفة (على سبيل المثال: RGB للون الأحمر)
target_rgb = (255, 0, 0)  # قيمة اللون الأحمر (أحمر، أخضر، أزرق)

# Checking each image one by one
checkImage(r"C:\Users\L9IRCH\OneDrive\Desktop\bot.py\nettels1.png", target_rgb)
checkImage(r"C:\Users\L9IRCH\OneDrive\Desktop\bot.py\nettels2.png", target_rgb)
checkImage(r"C:\Users\L9IRCH\OneDrive\Desktop\bot.py\nettels3.png", target_rgb)
checkImage(r"C:\Users\L9IRCH\OneDrive\Desktop\bot.py\nettels4.png", target_rgb)

