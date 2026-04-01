# Datasets

## Kaggle dataset
The benchmark uses a 1-million-row CSV (`entry_1mil.csv`) derived from the full dataset.

Download link: https://www.kaggle.com/datasets/alnahian654/data-deduplication-algorithm-benchmarking-dataset

## Generating synthetic data locally
Run `generate_synthetic_data.py` to produce a fresh `synthetic_dataset.csv` (10 million rows, 70% unique).

```bash
pip install pandas numpy faker
python3 generate_synthetic_data.py
```
