import streamlit as st


# ตั้งค่าชื่อเว็บและแถบด้านข้าง (Sidebar)
st.sidebar.title("Menu")
page = st.sidebar.selectbox("เลือกหน้าที่ต้องการเข้าชม", ["Machine Learning", "Neural Network", "Machine Learning Graph", "Neural Network Graph"])

with st.sidebar:
    st.sidebar.empty()  # ช่องว่างด้านบ
    st.markdown("---")  # เส้นแบ่ง
    st.markdown(
        """
        <div style="text-align: left;">
            <h3>📊 โปรเจกต์ Data Visualization</h3>
            <h4>By นางสาวนภัสสร ฉิมวิเศษ</h4>
            <p style="font-size: 15px; color: #2C3E50;"><b>ID: 6504062663117</b></p>
        </div>
        """,
        unsafe_allow_html=True
    )

# Machine Learning
if page == "Machine Learning":
    st.markdown(
        """
        <div style="text-align: left;">
            <h3>แนวทางการพัฒนาระบบทำนายอาการหัวใจวาย</h3>
        </div>
        """,
         unsafe_allow_html=True
    )
    
    st.write(
        """
        <div style="text-align: left;">
            <p><b>1. การนำเข้าข้อมูล</b> 
            <p>ชุดข้อมูลที่ใช้มาจาก Kaggle: [Heart Attack Prediction](https://www.kaggle.com/datasets/imnikhilanand/heart-attack-prediction?resource=download)
            <p>แหล่งที่มา:
            <p>ผู้สร้าง:
            <p>1. สถาบันโรคหัวใจแห่งฮังการี บูดาเปสต์: Andras Janosi, MD
            <p>2. โรงพยาบาลมหาวิทยาลัย ซูริก สวิตเซอร์แลนด์: William Steinbrunn, MD
            <p>3. โรงพยาบาลมหาวิทยาลัย บาเซิล สวิตเซอร์แลนด์: Matthias Pfisterer, MD
            <p>4. ศูนย์การแพทย์ VA, มูลนิธิคลินิกลองบีชและคลีฟแลนด์:
            Robert Detrano, MD, Ph.D.
            <p>ผู้บริจาค: David W. Aha (aha@ics.uci.edu) (714) 856-8779

            เป็นฐานข้อมูลเดียวที่นักวิจัย ML ใช้มาจนถึง
            ปัจจุบัน ฟิลด์ "เป้าหมาย" หมายถึงการมีอยู่ของโรคหัวใจในผู้ป่วย

            <p><b>2. ทฤษฎีของอัลกอริทึมที่พัฒนา</b>
            <p>2.1 K-Nearest Neighbors (KNN)
            <p>ใช้ KNN เพื่อจัดกลุ่มข้อมูลและแบ่งกลุ่มข้อมูลที่ซับซ้อน โดยดูจากความใกล้เคียงและจำแนกว่าผู้ป่วยมีภาวะโรคหัวใจหรือไม่ (target = 1 or 0)
            เลือกฟีเจอร์ที่เกี่ยวข้อง เช่น อายุ (age), คอเลสเตอรอล (chol)
            แสดงผลการคาดการณ์และ Decision Boundary
            <p>2.2 Support Vector Machine (SVM)
            <p>ใช้ SVM ในการจำแนกข้อมูล โดยใช้ RBF Kernel เพื่อสร้างเส้นแบ่ง Decision Boundary
            ใช้ age และ chol เป็นตัวแปรสำคัญในการจำแนก

            <p><b>3. ขั้นตอนการพัฒนาโมเดล</b>
            <p>1.ริ่มต้นด้วยการนำเข้าไลบรารีต่างๆ ที่จำเป็นสำหรับการวิเคราะห์ข้อมูลและสร้างโมเดล เช่น `pandas`, `numpy`, `matplotlib`, `seaborn` 
            และไลบรารีที่เกี่ยวข้องกับ Machine Learning อย่าง `sklearn` และ `tensorflow` นอกจากนี้ยังมีการติดตั้ง `ydata-profiling` เพื่อช่วยในการสำรวจข้อมูลเบื้องต้น
            <p>โหลดข้อมูลจากไฟล์ CSV 
            <p>2.ตรวจสอบโครงสร้างข้อมูล (`df.info()`, `df.head()`, `df.describe()`) เพื่อทำความเข้าใจชุดข้อมูล 
            <p>3.และตรวจสอบข้อมูลที่หายไป และการจัดการค่าที่หายไป
            <p>4.การแปลงข้อมูลและการเลือก Features และการกำหนด Target Variable
            <p>5.การแบ่งชุดข้อมูล Train และ Test
            <p>6.การพัฒนาโมเดล K-Nearest Neighbors (KNN)
            <p>- ใช้ `KNeighborsClassifier()` กำหนดค่า `k = 5`
            <p>- ฝึกโมเดลด้วยชุดข้อมูล `X_train_scaled` และ `y_train`
            <p>- ทำนายผลลัพธ์ด้วย `X_test_scaled`
            <p>7.การทดสอบกับข้อมูลใหม่
            <p>- สร้างจุดข้อมูลใหม่ เช่น อายุ 57 ปี และระดับคอเลสเตอรอล 270
            <p>- ใช้โมเดล KNN ในการพยากรณ์ผลลัพธ์ของข้อมูลใหม่นี้
            <p>- แสดงผลลัพธ์ว่าข้อมูลใหม่มีแนวโน้มที่จะเป็นโรคหัวใจหรือไม่
            <p>8.การพัฒนาโมเดล Support Vector Machine (SVM)
            <p>- ใช้ `SVC(kernel='rbf')` ซึ่งเป็น Kernel ที่เหมาะกับข้อมูลที่ไม่เป็นเส้นตรง
            <p>- ฝึกโมเดลโดยใช้ Feature `age` และ `chol` เพื่อสร้าง Decision Boundary
            <p>- แสดงผลลัพธ์ของ Decision Boundary ด้วย `contourf()`
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )
  

# Neural Network          หน้า Graph Display (แสดงกราฟจากไฟล์ที่มีอยู่แล้ว)

if page == "Neural Network":
    st.markdown(
        """
        <div style="text-align: left;">
            <h3>แนวทางการพัฒนาระบบทำนายอาการหัวใจวาย</h3>
        </div>
        """,
         unsafe_allow_html=True
    )
    
    st.write(
        """
        <div style="text-align: left;">
            <p><b>1. การนำเข้าข้อมูล</b> 
            <p>ข้อมูลที่ใช้มาจาก Synthetic Circle Data Set(https://archive.ics.uci.edu/dataset/1013/synthetic+circle+data+set) ซึ่งเป็นชุดข้อมูลจำลองที่ประกอบด้วยจุดที่อยู่ภายในและภายนอกวงกลม โดยข้อมูลแต่ละแถวประกอบด้วยค่า (x, y) และคลาส (0 หรือ 1) ซึ่งเป็นปัญหาการจำแนกประเภท (Binary Classification)
            <p>แหล่งที่มา:
            <p>ชุดข้อมูลวงกลมสังเคราะห์ [ชุดข้อมูล] (2024) คลังเก็บข้อมูลการเรียนรู้ของเครื่อง UCI https://doi.org/10.24432/C51909
        
            <p><b>2. ทฤษฎีของอัลกอริทึมที่พัฒนา</b>
            <p>Multi-Layer Perceptron (MLP) ซึ่งเป็น Neural Network แบบฟีดฟอร์เวิร์ดที่ใช้ในการจำแนกข้อมูล
            <p>-ใช้โครงสร้าง Fully Connected Neural Network
            <p>-มี 2 Hidden Layers แต่ละเลเยอร์มี 64 นิวรอนและใช้ฟังก์ชันกระตุ้น ReLU
            <p>-เลเยอร์สุดท้าย (Output Layer) ใช้ฟังก์ชัน sigmoid เพื่อจำแนกข้อมูลเป็น 0 หรือ 1
            <p>-ใช้ฟังก์ชัน Binary Cross-Entropy เป็น Loss Function
        
            <p><b>3. ขั้นตอนการพัฒนาโมเดล</b>
            <p>1.กำหนดโครงสร้างของโมเดล ใช้ Sequential() เพื่อสร้างโมเดล เพิ่ม Hidden Layers และ Output Layer 
            <p>2.คอมไพล์โมเดล ใช้ model.compile() กำหนด Loss Function, Optimizer และ Metrics
            <p>3.ฝึกสอนโมเดล ใช้ model.fit() เพื่อ Train โมเดล โดยรันทั้งหมด 100 epochs ใช้ validation_data เพื่อดูผลลัพธ์ของโมเดลในชุด Test
            <p>4.ประเมินผลโมเดล ใช้ model.evaluate() วัดผลการทำงานของโมเดลในชุดข้อมูล Test แสดงผล accuracy
            <p>5.แสดงกราฟผลลัพธ์ ใช้ matplotlib เพื่อ Plot กราฟ Accuracy และ Loss ของโมเดล กราฟแสดงพัฒนาการของโมเดลในแต่ละ Epoch
            <p>6.ผลลัพธ์ที่ได้
            <p>-ค่า Test Accuracy ที่ได้จะบอกว่าโมเดลสามารถจำแนกจุดในวงกลมได้แม่นยำแค่ไหน
            <p>-กราฟ Loss และ Accuracy แสดงแนวโน้มของโมเดลว่าสามารถเรียนรู้ได้ดีขึ้นตามจำนวน Epoch หรือไม่
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )
  

elif page == "Machine Learning Graph":
    st.title("📊 Machine Learning Graph")
    st.write("นี่คือกราฟที่สร้างจาก Google Colab")
    st.image("img/knn.png", caption="กราฟจาก knn", use_container_width=True)
    st.image("img/knnPoint.png", caption="กราฟจาก PotPointknn", use_container_width=True)
    st.image("img/svm.png", caption="กราฟจาก svm", use_container_width=True)

# หน้า Neural Network Graph
elif page == "Neural Network Graph":
    st.title("📊 Neural Network Graph")
    st.write("นี่คือกราฟที่สร้างจาก Google Colab")
    st.image("img/accuracy.png", caption="กราฟจาก  Accuracy Model", width=300)
    st.image("img/loss.png", caption="กราฟจาก  Loss Model", width=300)

    
# หน้า About (เกี่ยวกับเว็บ)
elif page == "About":
    st.title("ℹ️ เกี่ยวกับเว็บนี้")
    st.write("เว็บนี้พัฒนาด้วย **Python + Streamlit**")
    st.write("สร้างโดย [Your Name] 😊")
