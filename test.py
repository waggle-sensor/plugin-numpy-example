from main import process_frame
import numpy as np
import cv2


def main():
    frame = cv2.imread("test.jpg")
    results = process_frame(frame)
    for k, v in results.items():
        print(k, v)


if __name__ == "__main__":
    main()
