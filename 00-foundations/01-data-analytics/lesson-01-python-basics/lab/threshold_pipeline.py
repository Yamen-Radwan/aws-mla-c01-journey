"""Lesson 1 lab: a tiny ML-style pipeline using only Python basics."""


class SimpleThresholdModel:
    """Predicts 1 if a value is above the average seen during training."""

    def fit(self, values):
        self.threshold = sum(values) / len(values)
        return self

    def predict(self, value):
        return 1 if value > self.threshold else 0


def read_numbers(path):
    """Read one number per line from a text file and return a list."""
    numbers = []
    with open(path, "r") as file:
        for line in file:
            if line.strip():
                numbers.append(float(line))
    return numbers


def write_results(path, values, predictions):
    """Write one 'value,prediction' line per input."""
    with open(path, "w") as file:
        for i in range(len(values)):
            file.write(f"{values[i]},{predictions[i]}\n")


def main():
    try:
        training = read_numbers("training_data.txt")
        model = SimpleThresholdModel().fit(training)

        new_values = [12, 25, 31, 18]
        predictions = []
        for value in new_values:
            predictions.append(model.predict(value))

        write_results("results.txt", new_values, predictions)
        print(f"Threshold learned: {model.threshold}")
        print("Wrote results.txt")
    except FileNotFoundError:
        print("training_data.txt not found - create it first.")
    except ZeroDivisionError:
        print("training_data.txt is empty - add some numbers.")
    finally:
        print("Done.")


main()