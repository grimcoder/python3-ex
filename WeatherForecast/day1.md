### **Day 1: Setting Up and Basic Infrastructure**

#### **1. Project Initialization**:

**a. Virtual Environment Setup**:

To isolate our project's dependencies, we use a virtual environment.

```bash
# Navigate to your project directory
cd path/to/your/project

# Set up a virtual environment
python -m venv weatherly_env

# Activate the virtual environment
# On Windows
weatherly_env\Scripts\activate

# On MacOS/Linux
source weatherly_env/bin/activate

# Once activated, you'll notice the environment name 'weatherly_env' on the terminal.
```

**b. Install Necessary Packages**:

Now that we're inside our virtual environment, let's install the necessary packages.

```bash
pip install Flask requests
```

#### **2. Basic Flask Application**:

Let's start by creating a simple Flask application:

**`app.py`**:

```python
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({"message": "Welcome to Weatherly!"}), 200

if __name__ == '__main__':
    app.run(debug=True, port=5001)  # Using port 5001 as per your request.
```

To run the Flask application, use:

```bash
python app.py
```

Visit `http://127.0.0.1:5001/` in your browser, and you should see the welcome message.

#### **3. Amazon Cognito Setup**:

Amazon Cognito is a service that helps you create a secure user directory that scales. It also offers user sign-up, sign-in, and access control.

**a. Create a User Pool**:

1. Go to the AWS Management Console.
2. Navigate to Amazon Cognito.
3. Click on "Manage User Pools" and then "Create a User Pool".
4. Provide a name for the user pool, e.g., `WeatherlyUserPool`.
5. You can go with the default settings or customize them as needed. For this exercise, default settings should be fine for the most part.
6. Once you've reviewed the settings, click "Create Pool".

**b. App Client Setup**:

1. Inside `WeatherlyUserPool`, click on "App clients".
2. Click on "Add an app client".
3. Provide a name, e.g., `WeatherlyWebClient`.
4. Uncheck "Generate client secret" because JavaScript-based applications can't keep secrets hidden.
5. Adjust other settings as needed, but defaults should work for our case.
6. Click on "Create app client".

**c. Configure Signup and Login UI**:

Amazon Cognito provides a hosted UI that you can use, or you can build your own UI and integrate using the Amazon Cognito SDK.

1. Within `WeatherlyUserPool`, click on "Domain name".
2. Provide a domain prefix, e.g., `weatherly-domain`.
3. Once the domain is available, click "Save changes".
4. Under "App integration" -> "App client settings", set the callback URL(s) for your application. For now, you can use `http://localhost:5001/`, which will be our Flask server's address.
5. Enable the Cognito User Pool as an Identity Provider (IdP).
6. Click "Save changes".

At this point, you have a user pool ready, and you can integrate it into your Flask application or frontend for user signup and authentication. You'll use the user pool ID, app client ID, and the domain URL for integration.

---

With the Flask application running and the user pool set up in Cognito, you've laid the foundation for your weather forecasting app. The next days will involve building on this foundation by adding more features and integrations.