import argparse
import logging
import time
import numpy as np
from waggle import plugin


def process_frame(frame):
    # we assume frame shape is (H, W, 3) for an RGB image
    mean = np.mean(frame, (0, 1))
    min = np.min(frame, (0, 1))
    max = np.min(frame, (0, 1))
    return {
        "mean": mean,
        "min": min,
        "max": max,
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--rate", default=300, type=float, help="sampling interval in seconds")
    args = parser.parse_args()

    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s %(message)s',
        datefmt='%Y/%m/%d %H:%M:%S')

    logging.info("starting plugin. will process a frame every %ss", args.rate)
    
    plugin.init()

    while True:
        logging.info("getting camera snapshot")
        # TODO actually take a snapshot from the camera instead of using an empty image!
        fake_frame = np.zeros((640, 480, 3))

        logging.info("calling process_frame")
        results = process_frame(fake_frame)

        logging.info("results %s", results)

        plugin.publish("image.mean.red", results["mean"][0])
        plugin.publish("image.mean.green", results["mean"][1])
        plugin.publish("image.mean.blue", results["mean"][2])

        plugin.publish("image.min.red", results["min"][0])
        plugin.publish("image.min.green", results["min"][1])
        plugin.publish("image.min.blue", results["min"][2])

        plugin.publish("image.max.red", results["max"][0])
        plugin.publish("image.max.green", results["max"][1])
        plugin.publish("image.max.blue", results["max"][2])

        time.sleep(args.rate)


if __name__ == "__main__":
    main()
