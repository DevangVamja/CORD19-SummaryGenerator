# CORD-19 Summary Generator

## Overview
The CORD-19 Summary Generator is a Natural Language Processing (NLP) application designed to retrieve and summarize relevant articles from the COVID-19 Open Research Dataset (CORD-19). Given a user query, the system retrieves the top 5 most relevant documents and generates an abstractive summary of the retrieved articles. This project is particularly useful for researchers and healthcare professionals looking to quickly access summarized information from a large corpus of scientific literature.

## Methodology
The system operates in two main phases:

### 1. Retrieval of Top 5 Documents
This phase involves retrieving the most relevant articles from the CORD-19 dataset based on a user query. The steps include:

#### Data Collection and Cleaning
- Data is collected from the CORD-19 dataset, focusing on articles written in English.
- Preprocessing steps include:
  - Removing stop words, email addresses, and phone numbers.
  - Applying stemming and lemmatization to reduce word-based dependencies.

#### Named Entity Recognition (NER) and Knowledge Base
- NER is used to identify and categorize named entities in the text.
- A Knowledge Base (KB) is constructed using the extracted entities to improve search relevance.

#### Document Indexing
- An inverted indexing technique is used to index documents for efficient retrieval.
- This method ensures fast search rates and scalability for large document collections.

#### Document Scoring
- Documents are scored using TF-IDF (Term Frequency-Inverse Document Frequency) and cosine similarity.
- The relevance of documents to the query is determined by calculating the cosine similarity between the query vector and document vectors.

### 2. Abstractive Summary of Retrieved Articles
This phase generates an abstractive summary of the top 5 retrieved articles. The steps include:

#### Fine-Tuning of Pre-Trained Models
- The BART model is fine-tuned on the preprocessed data for the summarization task.
- The model is trained for 8 epochs and can generate summaries of up to 600 words.

#### Generate Summary
- The fine-tuned model generates a summary for each of the top 5 articles.
- The individual summaries are combined to produce a final, coherent summary.

## Features
- **Efficient Document Retrieval**: Uses TF-IDF and cosine similarity to retrieve the most relevant articles.
- **Abstractive Summarization**: Generates concise and coherent summaries using a fine-tuned BART model.
- **Scalable**: Handles large document collections efficiently using inverted indexing.
- **User-Friendly**: Provides a simple interface for users to input queries and receive summaries.

## Installation
### Prerequisites
- Python 3.8 or higher
- Libraries: `transformers`, `nltk`, `scikit-learn`, `pandas`, `numpy`

### Steps
Clone the repository:
```bash
git clone https://github.com/yourusername/cord19-summary-generator.git
cd cord19-summary-generator
```
Install the required libraries:
```bash
pip install -r requirements.txt
```
Download the CORD-19 dataset from Kaggle and place it in the `data` folder.

Follow through both the notebooks in **Notebooks** folder for data preprocessing and model training.
Once done running notebooks, update the locations for **covid19_Processed.csv** and **model.pkl** in **preprocess.py** and **queryProcessing.py** respectively.

Run the Flask application:
```bash
python app.py
```
Open your browser and navigate to `http://127.0.0.1:5000/` to access the application.

## Usage
1. Enter a query (e.g., "What are the symptoms of COVID-19?") in the input box.
2. Click **Search** to retrieve the top 5 relevant articles.
3. View the generated summary of the retrieved articles.

## Model Configuration
The BART model is fine-tuned with the following parameters:
```python
model_args = Seq2SeqArgs()
model_args.num_train_epochs = 8
model_args.no_save = False
model_args.evaluate_during_training = True
model_args.evaluate_during_training_verbose = True
model_args.overwrite_output_dir = True
model_args.max_length = 600

# Additional configurations
model_args.early_stopping = True
model_args.early_stopping_metric = "eval_loss"
model_args.early_stopping_patience = 3
model_args.learning_rate = 2e-5
model_args.gradient_accumulation_steps = 4
model_args.weight_decay = 0.01
model_args.save_steps = 500
model_args.save_total_limit = 2
model_args.evaluation_strategy = "steps"
model_args.eval_steps = 500
model_args.fp16 = True
model_args.warmup_ratio = 0.1
model_args.seed = 42

# Initialize model
model = Seq2SeqModel(
    encoder_decoder_type="bart",
    encoder_decoder_name="facebook/bart-large",
    args=model_args,
    use_cuda=True,
)
```

## File Structure
```
cord19-summary-generator/
├── app.py                  # Flask backend
├── requirements.txt        # List of dependencies
├── README.md               # Project documentation
├── Notebooks/
    ├── CORD-19 data extraction and preprocess.ipynb
    └── CORD-19 main.ipynb
├── src/
    ├── exception.py
    ├── logger.py
    ├── utils.py
    └── components/
        ├── preprocess.py
        └── queryProcessing.py                   
├── templates/              # HTML templates for the frontend
│   └── index.html
└── static/                 # Static files (CSS, JS)
    ├── styles.css
    └── script.js
```

## Technologies Used
- **Python**: Primary programming language.
- **Flask**: Backend framework for the web application.
- **Transformers**: Library for fine-tuning and using pre-trained NLP models (e.g., BART).
- **NLTK**: Library for text preprocessing (e.g., stemming, lemmatization).
- **Scikit-learn**: Library for TF-IDF and cosine similarity calculations.
- **HTML/CSS/JavaScript**: Frontend development.

## Future Improvements
- **In-built Training Routes**: Include flask app route to provide one-click data processing and model training.
- **Expand Dataset**: Include more datasets for broader coverage.
- **Improve Summarization**: Experiment with larger models (e.g., T5, PEGASUS) or ensemble methods.
- **User Authentication**: Add user accounts to save search history and preferences.
- **Deployment**: Deploy the application on a cloud platform (e.g., AWS, Heroku) for public access.

## Contributors
- Devang Vamja

## License
This project is licensed under the MIT License. See the `LICENSE` file for details.

## Acknowledgments
- **CORD-19 Dataset** by the Allen Institute for AI.

## 🤝 Contributing

Contributions are welcome! If you'd like to improve the project:

1. Fork the repo
2. Create a feature branch (`feature-xyz`)
3. Commit changes & open a PR


## 📬 Contact

👤 **Devang Vamja**  
📧 [devangvamja2000@gmail.com](mailto:devangvamja2000@gmail.com)  
🔗 [LinkedIn](https://linkedin.com/in/DevangVamja)  

---