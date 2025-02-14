# Steps to run the application

1. Create a new virtual environment
```
python3 -m venv venv
```

2. Activate the virtual environment
```
source venv/bin/activate
```

3. Install the required packages
```
pip install -r requirements.txt
```

4. Run the application
```
python app.py
```

# Preparing for deployment
- requirements.txt: import aws-wsgi 
- app.py: import awsgi and add handler function

# Steps to deploy the application

1. Create a new directory for the deployment
```
mkdir -p deployment/package
```

2. [OPTIONAL] Append `deployment` directory to .gitignore

3. [OPTIONAL] Check the version of the installed packages & update requirements.txt
```
pip freeze | grep <packages>
```

4. Install dependencies to a package directory
```
pip install -r requirements.txt --target deployment/package
```

5. Copy application files
```
cp app.py deployment/package/
cp -r templates deployment/package/
```

6. Create deployment ZIP
```
cd deployment/package
zip -r ../deployment.zip .
```

7. Create AWS Lambda Function

8. Create a new API Gateway

9. Create a new ACM Certificate

10. Create a custom domain name in API Gateway

11. Configure API mappings

11. Create Route 53 record  with the new domain name

12. Test the API from the new domain name

