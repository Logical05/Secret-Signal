# Secret-Signal
#### Info
ต้องตั้งชื่อไฟล์เป็นชื่อเดียวกันกับชื่อฟังก์ชัน
```def secret_signal(signal)``` มี ```signal``` คือ List ถ้าไม่ตรงเงื่อนไขให้คืนค่า ```Error``` โดยที่ Element ของ ```signal``` ต้องมีแต่ ```'-'```, ```'.'``` เท่านั้นและต้องเปลี่ยนเป็น ```'0'``` และ ```'1'``` ตามลำดับ คำตอบมีรายละเอียดดังนี้
  
  1. ต้องตอบเป็น List ของ String
  2. String คำตอบไม่เอาที่ว่างหรือ ```' '``` หน้าหลัง

      - ```" A1 B2 "``` ต้องลบ ```' '``` หน้าหลังก่อนให้กลายเป็น ```"A1 B2"``` ถึงจะตอบได้

#### Hint
  - 1 Byte มี 8 Bit
  - เปลี่ยนค่า Byte แล้วหาเป็น Character

#### Example

- secret_signal(["-.--.----..--.-.-..-..---..-..---..-....--.------.-.-...-..-....-...--.--..-..---..--.--"]) >>
```
['Hello World']
```

- secret_signal(["-.-.-.---..-.----..----.-..-...--..-.-..", "-.-..--.-..-....-...-.-."]) >>
```
['Thank', 'You']
```

- secret_signal(["-.----.---..---.", "--.-----"]) >>
```
['B1']
```

```"--.-----"``` ได้ ```' '``` ทำให้ไม่เอามาเป็นคำตอบ

- secret_signal([1]) >>
```
[]
```
