# GSV-BKK-Tree-Detection

## Introduction
ต้นไม้ในกรุงเทพมีกี่ต้น? เป็นคำถามที่ตอบได้ยาก เนื่องจากข้อมูลปัจจุบันยังไม่มีหน่วยงานใดเป็นผู้รวบรวม และเป็นงานที่ใหญ่มากหากใช้กำลังคนในการเก็บ  
ในเบื้องต้นเราแบ่งต้นไม้ออกเป็น 2 กลุ่ม กลุ่มแรกคือต้นไม้ส่วนกลาง(กทม.) อีกกลุ่มคือต้นไม้ส่วนตัว (เอกชน,ประชาชน) เฉพาะส่วนของ กทมนั้นเราสามารถแบ่งได้อีก 2 กลุ่มคือ
1.ต้นไม้ในสวนสาธารณะ (อยู๋ในความดูแลของกองงานสวนสาธารณะ๗
2.ต้นไม้ริมฟุตบาธ,เกาะกลาง (อยู่ในความดูแลของแต่ละเขต)

โปรเจกต์นี้โฟกัสที่ต้นไม้ริมฟุตบาธ,เกาะกลางโดยการ detect รูปต้นไม้จาก google street view โดยใช้ AI


# need help for each task

### Part-0 : เตรียมข้อมูล
1.หาข้อมูลถนนทุกเส้นในแต่ละเขตกทม.ในลักษณะ (way-id) หรือ shapfile - ตอนนี้มีข้อมูลเขตวัฒนา. 
2.แปลงข้อมูลเป็น list ของ way_id เพื่อเอาไปใช้ต่อ

### Part-1 : ดึงข้อมูลในแต่ละ way-id
1. ดึงข้อมูลจาก openstreetmap ในแต่ละเขตโดยเอาเฉพาะข้อมูลถนน (ways). 
2. นำ way_id ออกมา. 
3. นำข้อมูลจากแต่ละถนนมาดึงภาพจาก google street map. จาก way_id  โดย.   
  3.1 ใช้ way_id ดึง node_list ของถนนออกมา.    
  3.2 คำนวณ direction ของถนนว่าควรหันหน้าไปทางไหน (ใช้ปรับ head ในการดึงภาพจาก GSM).      
  3.3 ดึงภาพจาก GSM จุดนั้น โดยหันหน้าตรง และมุมเงย 20 องศา (มุมที่คาดว่าเห็นพ้นยอดต้นไม้).    
  3.4 เซฟภาพลงใน folder ของแต่ละถนน (way_id).    
  3.5 กระโดดไปยังจุดถัดไปของ node (หรือสามารถปรับระยะ shift ได้ เช่นทุกๆ 20m) แล้วทำซ้ำจนจบถนน

**MINIMUM FEATURE** : ดูดภาพจาก GSM ของถนนแต่ละเส้นได้   
** ปัญหาที่คิดว่าน่าจะเกิด - มีต้นไม้ต้นเดียวกันใน 2 รูป (ไม่แน่ใจว่ามีวิธีที่ทำให้ภาพซ้อนกันน้อยที่สุดหรือไม่).   
** หรืออาจต้องใช้วิธีการเดินไปทีละ node, get forward direction แล้วหันซ้าย,ขวา เพื่อเอาแนวตั้งฉาก (ถ้ามองตรงจะเป็น perspective)


### Part-2 : Train model
1.นำภาพที่ได้จากถนนแต่ละเส้นมา label ต้นไม้.  
2.Train model เพื่อตรวจจับต้นไม้โดยใช้ yolo.  
3.ทดสอบ model ว่าสามารถตรวจจับต้นไม้ได้

### Part-3 : Convert to lat-long
1.นำภาพที่จับต้นไม้ได้มาหาระยะทางจาก lat-long ที่ใช้ดึงภาพจาก GSM.  
2.ฟังก์ชันคำนวณตำแหน่งต้นไม้ที่แท้จริง (เพื่อนำไปบันทึกข้อมูล) 

# Current-Status
- มี code ส่วนที่ดึงภาพ GSM จาก roads แบบปรับระยะได้ เช่นทุกๆ 20 เมตร (นำ opensource อื่นมาต่อยอด)
- มี code คำนวณองศาของถนนว่ามุ่งตรงไปยังทิศได้ (0-360) อิงจากทิศเหนือ โดยคำนวณจาก node ต่อ node บนถนนเส้นเดียวกัน
- มีข้อมูลส่วนของเขตวัฒนาในลักษณะ shapefile
