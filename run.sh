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

echo "✅ Pipeline completed successfully!"




