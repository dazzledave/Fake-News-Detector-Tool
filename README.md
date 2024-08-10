<h2>An AI powered tool that skeems through a news article and detects patterns of a news being fake or real.</h2>
<p>Used Google's Bert model to train a  real and fake news dataset I picked from kaggle. Accuracy rate is around **70%**. This is the first version of this tool so please do not expect operational excellence. I'll be updating this in the future so keep an eye out.</p>

## Prerequisites

- **Python 3.x** installed on your computer

## Setup Instructions

1. **Clone the Repository**

   Open your terminal (or Command Prompt) and run the following command:

   ```bash
   git clone https://github.com/dazzledave/Fake-News-Detector-Tool.git
   ```

   Then navigate into the project directory:

   ```bash
   cd fake-news-detector-tool
   ```

2. **Set Up a Virtual Environment (Optional but Recommended)**

   Create a virtual environment to manage dependencies:

   ```bash
   python -m venv venv
   ```

   Activate the virtual environment:

   - **On Windows:**
     ```bash
     .\venv\Scripts\activate
     ```
   - **On macOS/Linux:**
     ```bash
     source venv/bin/activate
     ```

3. **Install the Required Packages**

   Install the necessary Python packages using `pip`:

   ```bash
   pip install -r requirements.txt
   ```

4. **Run the Django Application**

   Migrate the database and start the Django development server:

   ```bash
   python manage.py migrate
   python manage.py runserver
   ```

5. **Access the Application**

   Open your web browser and go to:

   ```
   http://127.0.0.1:8000/
   ```

6. **Use the Fake News Detector**

   - Type the news text you want to check into the provided text box.
![FND2](https://github.com/user-attachments/assets/f5d3e44b-563a-45b7-b767-30e7ab6023f2)
   - Click the **Analyze Article** button.![FND3](https://github.com/user-attachments/assets/9c73da51-b402-4a18-a0e0-02fc0132f03f)
   - The prediction result will display on the screen.


## Troubleshooting

- If you encounter any issues, make sure that all dependencies are correctly installed.
- Ensure your virtual environment is activated before running the project.

