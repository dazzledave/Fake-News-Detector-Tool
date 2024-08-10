import pandas as pd
from transformers import BertTokenizer, BertForSequenceClassification, AdamW
from torch.utils.data import DataLoader, Dataset
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import torch
import joblib

# Step 1: Load the dataset
data = pd.read_csv(r'C:\Users\HP\Documents\Fake_News_Detector_Tool\fake_news_detector\data\newsarticles.csv')

# Assuming the dataset has two columns: 'text' and 'label'
X = data['text'].fillna('')
y = data['label'].fillna('')

# Step 2: Load BERT tokenizer and model
tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')
model = BertForSequenceClassification.from_pretrained('bert-base-uncased')

# Step 3: Tokenize the text data
X = tokenizer(X.tolist(), padding=True, truncation=True, return_tensors="pt", max_length=512)

# Step 4: Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X['input_ids'], y, test_size=0.2, random_state=42)

# Create custom dataset for BERT
class FakeNewsDataset(Dataset):
    def __init__(self, inputs, labels):
        self.inputs = inputs
        self.labels = labels

    def __len__(self):
        return len(self.labels)

    def __getitem__(self, idx):
        return self.inputs[idx], self.labels[idx]

train_dataset = FakeNewsDataset(X_train, y_train)
test_dataset = FakeNewsDataset(X_test, y_test)

# Create DataLoader
train_loader = DataLoader(train_dataset, batch_size=16, shuffle=True)
test_loader = DataLoader(test_dataset, batch_size=16, shuffle=False)

# Step 5: Train the model
optimizer = AdamW(model.parameters(), lr=1e-5)
model.train()

for epoch in range(3):  # Run for more epochs if needed
    for inputs, labels in train_loader:
        outputs = model(inputs, labels=labels)
        loss = outputs.loss
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()

# Step 6: Evaluate the model
model.eval()
predictions = []
true_labels = []

with torch.no_grad():
    for inputs, labels in test_loader:
        outputs = model(inputs)
        logits = outputs.logits
        preds = torch.argmax(logits, dim=1).cpu().numpy()
        predictions.extend(preds)
        true_labels.extend(labels.cpu().numpy())

accuracy = accuracy_score(true_labels, predictions)
print(f'Accuracy: {accuracy}')

# Step 7: Save the trained model and tokenizer
model.save_pretrained('news/model/bert_fake_news_model')
tokenizer.save_pretrained('news/model/bert_tokenizer')
