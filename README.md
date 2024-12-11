## Multi-Class Classification of Mental Health Topics


### **Project Description**  
This project uses **Natural Language Processing (NLP)** techniques to analyze Reddit posts for detecting mental health concerns. It solves a **multi-class classification problem**, categorizing mental health-related text into three groups:  
1. **Disorders**  
2. **Improvements**  
3. **Distress**  

Using **Sentiment Analysis**, **Machine Learning**, and **Deep Learning models**, this study identifies patterns in mental health discussions to develop a scalable tool for mental health diagnostics.  

---
### **My code Repository Folders**
* DATA and reddit_data.py : It contains code too scrape data from reddit website
* EDA and Data Analysis: It contains code for data handling, preprocessing and analysis with visualization.
* Feature Engineering: It contains code related to added features such as vader sentiment analysis, processed text and title, their count. It includes text processing too.
* CNN,CNN2,CNN_edited: It contains code related to model training and their evaluation.
* Optimization: It contains code related to using distilBERT transformer and later training models with the final dataframe.

---
### Data Links:
- **Scraped data:** https://drive.google.com/file/d/1AhjlZZHivqAvq4q84IkZUNGpV6RrF9lY/view?usp=drive_link
- **Cleaned Data:** https://drive.google.com/file/d/1rXaAWK7PQQQYzkGEmOEsC5VTO8k3yKWW/view?usp=drive_link
- **Data with additional features:** https://drive.google.com/file/d/13daYpI0zlKocvVPE1aaLKJc864946We_/view?usp=drive_link


### **Features**  
- **Sentiment Analysis:**  
  - **VADER:** Rule-based sentiment analyzer.  
  - **DistilBERT:** Transformer-based model for contextual sentiment analysis.  

- **Machine Learning Models:**  
  - Logistic Regression  
  - Random Forest  

- **Deep Learning Models:**  
  - **CNNs:** For extracting local linguistic features.  
  - **RNN-LSTMs:** To capture long-term dependencies in text.  
  - **Hybrid Architectures:** Combining features for improved accuracy.  

---

### **Key Results**  
- **VADER Models:** Achieved ~70% accuracy with overfitting challenges.  
- **DistilBERT Models:** Achieved **over 90% accuracy**, demonstrating superior performance and generalization.
- Learning curves and validation metrics showcased the robustness of transformer-based approaches in mental health analysis.

#### Accuracy of Training, Testing, and Validation Accuracy Using Sentiment from VADER

| Models      | Training Accuracy | Testing Accuracy | Validation Accuracy |
|-------------|-------------------|------------------|---------------------|
| Hybrid CNN  | 77.5%            | 71.6%           | 70.6%              |
| KIM CNN     | 76.3%            | 71.1%           | 71.1%              |
| RNN CNN     | 75.9%            | 71.1%           | 72.1%              |

#### Accuracy of Training, Testing, and Validation Accuracy Using Sentiment from DistilBERT Transformer

| Models      | Training Accuracy | Testing Accuracy | Validation Accuracy |
|-------------|-------------------|------------------|---------------------|
| Hybrid CNN  | 97.6%            | 93.55%          | 95.21%             |
| KIM CNN     | 97.2%            | 94.5%           | 95.23%             |
| RNN CNN     | 96.5%            | 94.5%           | 94.1%              |


---

### **Methodology**  
1. **Data Collection:**  
   - Scraped data from 45 Reddit subreddits (~100,000 posts).  
   - Categories: Disorders, Improvements, Distress.  

2. **Data Preprocessing:**  
   - Stop word removal, lemmatization, punctuation elimination, text normalization.  
   - Features: Word counts, sentiment scores, post metadata.  

3. **Feature Engineering:**  
   - Combined linguistic and metadata features for model training.  

4. **Model Training & Evaluation:**  
   - Multiple models trained using TensorFlow’s Keras API.  
   - Metrics: Accuracy, F1-score, Precision, Recall.  
   - Optimization: Dropout layers, early stopping, checkpointing.  

---

### **Limitations**  
- Data bias from Reddit user demographics.  
- Lack of expert-validated categorization.  
- Challenges in interpreting complex emotional expressions (e.g., sarcasm).  
- Computational resource requirements for transformer-based models.  

---

### **Getting Started**  
1. **Prerequisites:**  
   - Python 3.8+
   - Jupyter notebook / Google collab 
   - TensorFlow, Hugging Face Transformers, NLTK, Matplotlib  

2. **Setup:**  
   Clone the repository and install dependencies:  
   ```bash
   git clone https://github.com/SriTheRocker/Mental_Health_Prediction.git
   cd Mental_Health_Prediction
   ```

3. **Run the Project:**  
   - You can run the ipynb files in google collab or jupyter notebook.

---

### **Contact**  
For any inquiries, feel free to reach out:  
**Srikanth Reddy Yeruva**  

---

