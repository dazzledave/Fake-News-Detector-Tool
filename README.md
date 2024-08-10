<h2>An AI powered tool that skeems through a news article and detects patterns of a news being fake or real.</h2>
To install & run, 
<h1>How to use</h1>

## Prerequisites

- **Python 3.x** installed on your computer

## Setup Instructions

1. **Clone the Repository**

   Open your terminal (or Command Prompt) and run the following command:

   ```bash
   git clone https://github.com/your-username/fake-news-detector-tool.git
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
   - Click the **Check** button.
   - The prediction result will display on the screen.

## Troubleshooting

- If you encounter any issues, make sure that all dependencies are correctly installed.
- Ensure your virtual environment is activated before running the project.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
