Question-Answer System Based on E-Commerce Website Logs
1. Project Definition and Purpose
This project aims to develop a Question-Answer (Q&A) system that can automatically answer users' specific questions using log data from an e-commerce website.
The RAG (Retrieval-Augmented Generation) model, which combines the stages of information retrieval and response generation, was used in the project. The RAG model first retrieves the relevant information from the dataset to generate an answer to a given question and uses this information to generate an answer through a language model.
2. Methods and Tools Used
The basic steps followed throughout the project are summarized below:
● Data Loading and Preprocessing:
○ E-commerce website logs were loaded using pandas and columns in date format such as accessed_date were converted to datetime format.
○ Missing values ​​were filled as "Unknown" and appropriate columns were converted to categorical
data.
○ The dataset was taken from Kaggle and was reduced by 70% for shorter compile time.

● Preparation of Text Data:
○ Various columns in the log data (ip, accessed_From, network_protocol,
country, language, pay_method, membership, gender) were combined to create a single text data point for each log. These texts were used to create meaningful vectors representing the data.

● Model Selection and Vectorization:
○ Text data was transformed into vectors using the sentence-transformers library with the msmarco-distilbert-base-tas-b model. This model was used for the information retrieval phase in the RAG system.

○ Vectors were indexed in a high-dimensional space using the FAISS library and the nearest neighbors were searched.

● Response Generation:
○ After the most appropriate log entries for the question were obtained, this information was given to the T5-base language model to produce the answer. This model is a transformer model trained to ensure that the response is context-compatible.

3. Challenges and Solutions

The biggest challenge encountered throughout the project was the limited options in language model selection. Since my computer system was not equipped enough to run more powerful models, I had to use relatively simpler and lighter models. This limited the quality of the answers obtained. If I could have used a more powerful language model, the accuracy and contextual compatibility of the results obtained could have been higher.

In addition, preparing the text data and organizing the context provided to the model were also important steps in order to increase the quality of the answers. In order to increase the accuracy of the answers, I tried to ensure that the model made more accurate predictions by extracting more summary and target-oriented information from the log data.

Finally, I can admit that I had technical difficulties because I had no experience with RAG.

4. System Performance and Accuracy Assessment
● Performance: The models and methods used gave results quite quickly within the limits of the available hardware. In particular, the msmarco-distilbert-base-tas-b
model was a suitable choice for obtaining fast and relevant information from log data.

● Accuracy: Although the system was able to provide correct and context-compatible answers to some questions,
it could not provide the expected level of accuracy for some questions. More sophisticated models or fine-tuned language models
could be used to improve the quality of the answers. I tried to explain every code I wrote with a comment line. Since NLP is a field that I have tried for the first time, it is highly probable that there were technical errors.

5. Conclusion and Future Work
This project provides a basic approach and a workable solution in the process of developing a data-based Question-Answer system. In the future, it will be possible to improve the accuracy and contextual meaning of the system by using more powerful language models and more advanced hardware.
In addition, it is possible to develop a more advanced Question-Answer platform that can be customized according to the needs of users and can respond to a wider variety of queries. Here are some questions and the answers produced by the model;
As a result, the current system integrates the data acquisition and response generation stages, allowing users to obtain meaningful information from e-commerce site logs. However, the performance of this system can be further improved with the integration of more advanced models and a larger dataset. As can be seen, while the system gives accurate answers to some questions, it has difficulty understanding the context of some questions. To improve this situation, more powerful language models (such as T5-Base, GPT3.5) could be used and perhaps better vector optimization could be done.
