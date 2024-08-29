import pandas as pd
from sentence_transformers import SentenceTransformer
from transformers import T5ForConditionalGeneration, T5Tokenizer
import faiss

# CSV dosyasını yükleyerek log verilerini okudum
file_path = 'E-commerce_Website_Logs.csv'
logs_df = pd.read_csv(file_path)

# 'accessed_date' sütununu datetime formatına dönüştürdüm
logs_df['accessed_date'] = pd.to_datetime(logs_df['accessed_date'], errors='coerce')

# Eksik değerleri "Unknown" olarak doldurdum
logs_df = logs_df.fillna('Unknown')

# İlgili sütunları kategorik veri tipine dönüştürdüm
logs_df['network_protocol'] = logs_df['network_protocol'].astype('category')
logs_df['accessed_From'] = logs_df['accessed_From'].astype('category')
logs_df['gender'] = logs_df['gender'].astype('category')
logs_df['country'] = logs_df['country'].astype('category')
logs_df['membership'] = logs_df['membership'].astype('category')
logs_df['language'] = logs_df['language'].astype('category')
logs_df['pay_method'] = logs_df['pay_method'].astype('category')

# Metin verisini oluşturmak için log verilerinin ilgili sütunlarını birleştirdim
logs_df['text_data'] = logs_df[['ip', 'accessed_From', 'network_protocol', 'country', 'language',
                                'pay_method', 'membership', 'gender']].astype(str).agg(' '.join, axis=1)

# Daha iyi sonuçlar almak için bir sentence transformer modeli başlattım
model = SentenceTransformer('msmarco-distilbert-base-tas-b')

# Metin verilerini vektörlere dönüştürdüm, işlemi hızlandırmak için batch boyutunu ayarladım
batch_size = 128
vectors = model.encode(logs_df['text_data'].tolist(), batch_size=batch_size, show_progress_bar=True)

# Vektörlerin boyutlarını kontrol ettim
print("Vektörlerin Şekli:", vectors.shape)

# FAISS kütüphanesi kullanarak bir indeks oluşturdum ve vektörleri bu indekse ekledim
dimension = vectors.shape[1]
index = faiss.IndexFlatL2(dimension)  # Benzerlik araması için L2 mesafesi kullandım
index.add(vectors)  # Vektörleri indekse ekledim

# Belirli bir sorguya göre en alakalı log girişlerini getiren bir fonksiyon yazdım
def retrieve_logs(query, index, model, top_k=5):
    # Sorguyu bir vektöre dönüştürdüm
    query_vector = model.encode([query])

    # FAISS indeksi kullanarak en benzer vektörleri aradım
    distances, indices = index.search(query_vector, top_k)

    # En benzer log girişlerini aldım
    retrieved_logs = logs_df.iloc[indices[0]]

    return retrieved_logs

# T5-base modelini ve tokenizer'ını yükledim
t5_model = T5ForConditionalGeneration.from_pretrained('t5-base')  # Daha güçlü bir model kullanıyorum
t5_tokenizer = T5Tokenizer.from_pretrained('t5-base')

# Log verilerini kullanarak bir yanıt oluşturmak için bir fonksiyon yazdım
def generate_response(retrieved_logs, query):
    # Loglardan anlamlı bir bağlam oluşturdum
    context = ". ".join([f"Device: {row['accessed_From']}, Membership: {row['membership']}, Network Protocol: {row['network_protocol']}, Country: {row['country']}" for _, row in retrieved_logs.iterrows()])

    # Model için uygun formatta giriş metnini hazırladım
    input_text = f"question: {query} context: {context}"
    input_ids = t5_tokenizer.encode(input_text, return_tensors='pt')

    # T5 modeli kullanarak yanıtı oluşturdum
    outputs = t5_model.generate(input_ids, max_length=150, num_beams=5, early_stopping=True)
    answer = t5_tokenizer.decode(outputs[0], skip_special_tokens=True)

    return answer

# Sistemi entegre etmek için bir fonksiyon yazdım, bu fonksiyon hem bilgi almayı hem de yanıt oluşturmayı içeriyor
def rag_qa_system(query):
    # Sorguya göre en alakalı log girişlerini getirdim
    retrieved_logs = retrieve_logs(query, index, model)

    # Alınan loglar üzerinden bir yanıt oluşturdum
    response = generate_response(retrieved_logs, query)

    return response

# Sistemi test etmek için örnek sorgular hazırladım
query1 = "What type of device do most visitors use?"
query2 = "Which membership type is most frequently seen in the logs?"
query3 = "What is the most common network protocol used by visitors?"
query4 = "What are the different countries from which visitors access the website?"

# Hazırlanan sorgularla sistemi test ettim ve yanıtları aldım
answer1 = rag_qa_system(query1)
answer2 = rag_qa_system(query2)
answer3 = rag_qa_system(query3)
answer4 = rag_qa_system(query4)

# Yanıtları ekrana yazdırdım
print(f"Query: {query1}")
print(f"Answer: {answer1}\n")

print(f"Query: {query2}")
print(f"Answer: {answer2}\n")

print(f"Query: {query3}")
print(f"Answer: {answer3}\n")

print(f"Query: {query4}")
print(f"Answer: {answer4}\n")
