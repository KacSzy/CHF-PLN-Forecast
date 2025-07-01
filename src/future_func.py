import os
import numpy as np
import pandas as pd
from typing import Final
from keras.models import load_model

# Constants
SEQUENCE_LENGTH: Final[int] = 30


def create_sequences(data: np.ndarray, sequence_length: int = 10):
    """Create input sequences for the LSTM model."""
    X, y = [], []
    for i in range(sequence_length, len(data)):
        X.append(data[i - sequence_length:i])
        y.append(data[i])
    return np.array(X), np.array(y)


def predict_future_chf(day: int, month: int, year: int):
    """ Predict the CHF/PLN exchange rate for a given date."""

    script_dir = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.dirname(script_dir)

    model_path = os.path.join(project_root, 'models', 'chf_pln_forecast.keras')
    data_path = os.path.join(project_root, 'data', 'chfpln_d.csv')

    model = load_model(model_path)

    df = pd.read_csv(data_path, parse_dates=True)
    df['Data'] = pd.to_datetime(df['Data'])

    y = df['Zamkniecie']
    X, _ = create_sequences(data=y, sequence_length=SEQUENCE_LENGTH)

    # Last known sequence from the dataset
    last_known_sequence = X[-1:]

    # Last date in the dataset
    current_date = df['Data'].max()

    target_date = pd.to_datetime(f"{year}-{month}-{day}")

    days_to_predict = (target_date - current_date).days

    if days_to_predict <= 0:
        return "Target date must be in the future"

    future_predictions = []
    current_sequence = last_known_sequence.copy()

    for _ in range(days_to_predict):
        next_pred = model.predict(current_sequence, verbose=0)
        next_value = next_pred[0][0]  # Get the predicted value
        future_predictions.append(next_value)

        # Update the current sequence by rolling it and adding the new prediction
        current_sequence = np.roll(current_sequence, -1, axis=1)
        current_sequence[0, -1] = next_value

    return future_predictions[-1]


if __name__ == "__main__":
    predicted_value = predict_future_chf(day=1, month=8, year=2025)
    print(f"Predicted CHF/PLN rate: {predicted_value:.4f}")
