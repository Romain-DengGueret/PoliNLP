#!/bin/bash

echo "🚀 Starting the PoliNLP pipeline"
start_time=$(date +%s)

# Ensure the script is run from the project root
if [ ! -d "polinlp" ]; then
  echo "❌ Error: 'polinlp' directory not found!"
  exit 1
fi

# Step 0: Ensure dependencies are installed
echo "🔍 Checking dependencies..."
if ! command -v poetry &> /dev/null; then
  echo "❌ Poetry is not installed! Install it first: curl -sSL https://install.python-poetry.org | python3 -"
  exit 1
fi

# Optional: Check Poetry version (optional suggestion)
echo "📦 Poetry version: $(poetry --version)"

echo "📦 Installing dependencies..."
poetry install --no-interaction --no-root

# Step 1: Activate the virtual environment
ENV_PATH=$(poetry env info --path)
if [ ! -d "$ENV_PATH" ]; then
  echo "❌ Error: Poetry virtual environment not found!"
  exit 1
fi
source "$ENV_PATH/bin/activate"

# Step 2: Fetch data
echo "📥 Calling API and transforming JSON into DataFrame..."
poetry run python polinlp/etl_api.py

if [ $? -ne 0 ]; then
  echo "❌ Error during API call!"
  exit 1
fi

# Step 3: Check data quality
echo "📊 Checking data quality..."
poetry run python polinlp/data_quality_check.py

if [ $? -ne 0 ]; then
  echo "❌ Error during data quality check!"
  exit 1
fi

# Step 4: Process the data
echo "🛠️ Processing the DataFrame..."
poetry run python polinlp/eda.py

if [ $? -ne 0 ]; then
  echo "❌ Error during data processing!"
  exit 1
fi

# Run tests (only if not skipped)
RUN_TESTS=${RUN_TESTS:-false}  # Default to false if not set
if [ "$RUN_TESTS" = true ]; then
  echo "🧪 Running tests..."
  poetry run pytest tests/ --tb=short | tee logs/test_results.log
  if [ $? -ne 0 ]; then
    echo "❌ Tests failed!"
    exit 1
  fi
fi

# Step 4: Final output
end_time=$(date +%s)
execution_time=$((end_time - start_time))

echo "✅ All steps completed successfully in $execution_time seconds!"
