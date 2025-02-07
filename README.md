# PoliNLP 

PoliNLP is a data-driven project that leverages Natural Language Processing (NLP) and modern data engineering to analyze public datasets on social protection, and inequalities. Using open government data from the DREES, this project provides actionable insights into public perception of policies over time.
This project follows an ELT pipeline to retrieve data from the DREES API and store it in Parquet format for efficient processing. Advanced Natural Language Processing (NLP) techniques and modern data science frameworks are applied to analyze public opinion trends. The results are interpreted using policy evaluation methodologies to assess the impact of social policies.

## Technologies Used 

- **Data Engineering**: `requests`, `Polars`, `Onyxia`, `S3-like storage`  
- **DevOps & Code Quality**: `Poetry`, `pre-commit`, `Ruff`  
- **NLP & ML**: `CamemBERT`, `SpaCy`, `Scikit-learn`  

## Project Structure  

- `polinlp/` → Contains Python scripts for **data extraction, cleaning, and analysis**  
- `tests/` → Unit tests for **data integrity and model performance**  


## Orchestration 

I use a simple orchestrator, run `run.sh` in the terminal to execute all scripts. 
