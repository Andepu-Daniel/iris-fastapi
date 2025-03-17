---

# **🌸 Iris Flower Prediction API**  
🚀 **A FastAPI-powered machine learning API that predicts Iris flower species based on sepal and petal measurements.**  

![Iris API Banner](https://upload.wikimedia.org/wikipedia/commons/4/46/Iris_versicolor_3.jpg)  

## **📌 Project Overview**  
This API serves as a **ready-to-use machine learning model** that predicts the species of an Iris flower based on input measurements. The model is built using **Scikit-Learn** and deployed via **FastAPI on Render**, ensuring high performance and real-time accessibility.  

## **✨ Features**  
✅ **Accurate Predictions:** Utilizes a fine-tuned **RandomForestClassifier** for high accuracy.  
✅ **Fast & Scalable:** Built with **FastAPI** for low-latency predictions.  
✅ **Easy Integration:** Exposes a **JSON API endpoint** for use in web and mobile applications.  
✅ **Cloud Deployment:** Hosted on **Render**, eliminating local installation requirements.  

---

## **🔗 Live API Endpoint**  
🌍 **[Iris Prediction API](https://iris-fastapi-mvwa.onrender.com/predict)** (POST request)  

---

## **🚀 How to Use the API?**  

### **1️⃣ Send a `POST` request to:**  
```
https://iris-fastapi-mvwa.onrender.com/predict
```

### **2️⃣ JSON Input Format:**  
```json
{
  "sepal_length": 5.1,
  "sepal_width": 3.5,
  "petal_length": 1.4,
  "petal_width": 0.2
}
```

### **3️⃣ Expected JSON Response:**  
```json
{
  "prediction": "Setosa"
}
```

---

## **💻 Run Locally**  

### **1️⃣ Clone the Repository:**  
```bash
git clone https://github.com/yourusername/iris-fastapi.git
cd iris-fastapi
```

### **2️⃣ Install Dependencies:**  
```bash
pip install -r requirements.txt
```

### **3️⃣ Run the API Locally:**  
```bash
uvicorn app:app --host 0.0.0.0 --port 8000
```

### **4️⃣ Test the API:**  
Open **Postman** or run this `curl` command:  
```bash
curl -X POST http://127.0.0.1:8000/predict \
     -H "Content-Type: application/json" \
     -d '{"sepal_length": 5.1, "sepal_width": 3.5, "petal_length": 1.4, "petal_width": 0.2}'
```

---

## **📂 Project Structure**  
```
/iris_fastapi
├── app.py              # FastAPI application
├── model.pkl           # Trained Iris classification model
├── requirements.txt    # Dependencies
├── render.yaml         # Render deployment configuration
└── README.md           # Project documentation
```

---

## **🛠 Technologies Used**  
🔹 **Python** – Primary language  
🔹 **FastAPI** – Web framework for API development  
🔹 **Scikit-Learn** – Machine learning model training  
🔹 **Uvicorn** – ASGI server for running FastAPI  
🔹 **Render** – Cloud hosting and deployment  

---

## **📜 License**  
This project is open-source and available under the **MIT License**.  

---

## **🙌 Acknowledgments**  
Special thanks to the **FastAPI** and **Scikit-Learn** communities for their amazing tools and documentation.  

---

### **🚀 Connect & Contribute**  
Have suggestions or want to contribute? Open a **pull request** or connect with me on **LinkedIn**!  

📌 **GitHub Repository:** [https://github.com/Andepu-Daniel/]  
📌 **LinkedIn:** [https://www.linkedin.com/in/daniel-andepu-230167208/]  

---
