# Wine Quality Prediction Model with FastAPI

This project implements a wine quality prediction model using FastAPI. The model evaluates wine quality based on input features like alcohol content, acidity levels, and sulfur dioxide concentration.

## Requirements

To set up the environment, follow these steps:

### 1. Clone the Repository and Navigate to the Directory

```bash
git clone https://github.com/benedictdebrah/Predictive-Model-Deployment.git
```

```bash
cd Predictive-Model-Deployment
```

### 2. Create a Virtual Environment (Optional but Recommended)

Create a virtual environment to manage dependencies:

```bash
python3 -m venv venv
```

Activate the virtual environment:

- **Windows**: `venv\Scripts\activate`
- **Unix or MacOS**: `source venv/bin/activate`

### 3. Install Dependencies

Install the required Python packages using the provided `requirements.txt` file:

```bash
pip install -r requirements.txt
```

## Usage

To run the FastAPI server and make predictions:

### 1. Navigate to the `app` Directory

```bash
cd app
```

### 2. Start the FastAPI Server

```bash
uvicorn main:app --reload
```

### 3. Access the API Documentation

Once the server is running, access the API documentation at `http://localhost:8000/docs` in your web browser.

### 4. Make Predictions

Use the `/predict` endpoint to make predictions by sending a POST request with JSON data. Enter data in the following format:

```json
{
    "wine_type": "red",
    "alcohol": 10.2,
    "citric_acid": 0.08,
    "density": 0.99484,
    "ph": 3.5,
    "residual_sugar": 1.9,
    "total_sulfur_dioxide": 31.0,
    "fixed_acidity": 5.4
}
```

Replace the sample values with your desired inputs.

## Docker

Alternatively, you can run the application using Docker:

### 1. Build the Docker Image

```bash
docker build -t wine-quality-prediction .
```

### 2. Run the Docker Container

```bash
docker run -d -p 8000:8000 wine-quality-prediction
```

Access the application at `http://localhost:8000`.

## Notebook

For detailed insights into the model building process and analysis, refer to the notebook provided in this repository: [Notebook Link](https://github.com/benedictdebrah/Wine-Quality-Prediction).

