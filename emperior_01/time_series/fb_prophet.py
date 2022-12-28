import pandas as pd
from prophet import Prophet
from prophet.plot import plot_plotly


def main(csv_path: str):
    print(csv_path)

    # Load data and select only Date and Close columns
    df = pd.read_csv(csv_path)
    data = df[["Date", "Close"]]

    # Prophet requires specific column names
    data.columns = ["ds", "y"]

    # Split the data
    training_data = data.iloc[:, : round(0.8 * data.shape[1])]
    test_data = data.iloc[:, : round(0.2 * data.shape[1])]

    # Train the model
    model = Prophet(daily_seasonality=True)
    model.fit(training_data)

    # Save predictions plot
    future_dates = model.make_future_dataframe(periods=len(test_data.index))
    predictions = model.predict(future_dates)
    plot = plot_plotly(model, predictions)
    plot.write_image(csv_path.replace(".csv", ".p.png"))

    # Save seasonality plot
    model.plot_components(predictions).savefig(csv_path.replace(".csv", ".s.png"))


if __name__ == "__main__":
    main("TSLA_2012-01-01_2015-01-01.csv")
