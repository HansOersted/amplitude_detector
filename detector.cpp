#include <iostream>
#include <vector>
#include <limits>

// Function to calculate the max amplitude and max offset
std::pair<double, double> calculateAmplitudeAndOffset(const std::vector<double>& signal) {
    if (signal.empty()) {
        std::cerr << "The signal is empty." << std::endl;
        return {0.0, 0.0};
    }

    double maxVal = std::numeric_limits<double>::lowest();
    double minVal = std::numeric_limits<double>::max();

    // Step 1: Finding the maximum and minimum values in the signal
    for (double val : signal) {
        if (val > maxVal) maxVal = val;
        if (val < minVal) minVal = val;
    }

    // Step 2: Calculating the difference between max and min values
    double difference = maxVal - minVal;

    // Step 3: Calculating the amplitude based on the difference
    double amplitude = std::abs(difference) / 2;

    // Step 4: Calculating the offset
    double offset = (maxVal + minVal) / 2;

    // Step 5: Returning the max amplitude and max offset
    return {amplitude, offset};
}

int main() {
    // Example signal data (replace with the actual signal data)
    std::vector<double> signal = {1.2, 3.5, 2.8, 4.1, 0.9, 3.7, 2.5, 1.0, 3.6};

    auto [amplitude, offset] = calculateAmplitudeAndOffset(signal);

    std::cout << "Max Amplitude: " << amplitude << std::endl;
    std::cout << "Max Offset: " << offset << std::endl;

    return 0;
}
