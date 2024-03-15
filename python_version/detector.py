import sys

def calculate_amplitude_and_offset(signal):
    if not signal:
        print("The signal is empty.", file=sys.stderr)
        return 0.0, 0.0

    max_val = float('-inf')
    min_val = float('inf')

    # Step 1: Finding the maximum and minimum values in the signal
    for val in signal:
        if val > max_val:
            max_val = val
        if val < min_val:
            min_val = val

    # Step 2: Calculating the difference between max and min values
    difference = max_val - min_val

    # Step 3: Calculating the amplitude based on the difference
    amplitude = abs(difference) / 2

    # Step 4: Calculating the offset
    offset = (max_val + min_val) / 2

    # Step 5: Returning the max amplitude and max offset
    return amplitude, offset

if __name__ == "__main__":
    # Example signal data (replace with the actual signal data)
    signal = [1.2, 3.5, 2.8, 4.1, 0.9, 3.7, 2.5, 1.0, 3.6]

    amplitude, offset = calculate_amplitude_and_offset(signal)

    print("Max Amplitude:", amplitude)
    print("Max Offset:", offset)