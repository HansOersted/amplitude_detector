import rosbag2_py
from rosbag2_py import StorageFilter
from rclpy.serialization import deserialize_message
from rosidl_runtime_py.utilities import get_message
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


def get_rosbag_options(path, serialization_format="cdr"):
    storage_options = rosbag2_py.StorageOptions(uri=path, storage_id="sqlite3")

    converter_options = rosbag2_py.ConverterOptions(
        input_serialization_format=serialization_format,
        output_serialization_format=serialization_format,
    )

    return storage_options, converter_options

def open_reader(path: str):
    storage_options, converter_options = get_rosbag_options(path)
    reader = rosbag2_py.SequentialReader()
    reader.open(storage_options, converter_options)
    return reader



reader = open_reader("/home/shen/Desktop/J6_example")
lateral_error = "/control/trajectory_follower/lateral/diagnostic" 
topic_filter = StorageFilter(topics = [lateral_error])
reader.set_filter(topic_filter)

starting_seconds = 0  # set the desired starting time (unit: second)

(topic, data, stamp) = reader.read_next()
interested_starting_time = stamp + starting_seconds * 10**9
reader.seek(interested_starting_time)

topic_types = reader.get_all_topics_and_types()
type_map = {topic_types[i].name: topic_types[i].type for i in range(len(topic_types))}

print(type_map)

signal = []
while reader.has_next():
    (topic, data, stamp) = reader.read_next()
    msg_type = get_message(type_map[topic])
    msg = deserialize_message(data, msg_type)
    signal.append(msg.data[5])

amplitude, offset = calculate_amplitude_and_offset(signal)

print("Max Amplitude:", amplitude)
print("Max Offset:", offset)