#!/bin/bash

echo "🚀 Starting the pipeline"

# Move into the 'polinlp' directory
cd polinlp || { echo "❌ Error: 'polinlp' directory not found!"; exit 1; }

# Step 1: Fetch data
echo "📥 Calling API and transforming JSON into DataFrame..."
python etl_api.py

# Check if the previous step was successful
if [ $? -ne 0 ]; then
  echo "❌ Error during API call!"
  exit 1
fi

# Step 2: Process the data
echo "🛠️ Processing the DataFrame..."
python eda.py

if [ $? -ne 0 ]; then
  echo "❌ Error during data processing!"
  exit 1
fi

# Move back to the project root directory
cd ..

# Step 3: Run tests with pytest
echo "🧪 Running tests..."
export PYTHONPATH="$(pwd)"
pytest tests/ --tb=short

# Check if tests passed
if [ $? -ne 0 ]; then
  echo "❌ Tests failed!"
  exit 1
fi

echo "✅ All steps completed successfully!"




