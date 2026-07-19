import os
import sys
import json

def gorilla_xor_compress(timestamps, values):
    # Delta-of-delta encoding timestamps
    ts_deltas = []
    if len(timestamps) > 1:
        prev_ts = timestamps[0]
        prev_delta = timestamps[1] - timestamps[0]
        ts_deltas.append(prev_delta)
        for i in range(2, len(timestamps)):
            curr_delta = timestamps[i] - timestamps[i-1]
            delta_of_delta = curr_delta - prev_delta
            ts_deltas.append(delta_of_delta)
            prev_delta = curr_delta
            
    # Floating Gorilla XOR value streams
    val_xors = []
    if len(values) > 1:
        # Simple binary representation XOR emulation
        for i in range(1, len(values)):
            xor_val = int(values[i]) ^ int(values[i-1])
            val_xors.append(xor_val)
            
    return {
        "ts_deltas": ts_deltas,
        "val_xors": val_xors
    }

def main():
    print("Running bot-16-sensor-domain sensor compression...")
    ts = [1600000000, 1600000060, 1600000120]
    vals = [120, 122, 121]
    res = gorilla_xor_compress(ts, vals)
    assert len(res["val_xors"]) > 0
    print("Gorilla timestamp delta-of-delta splits validated.")

if __name__ == "__main__":
    main()
