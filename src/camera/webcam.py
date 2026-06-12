"""Webcam utilities for reading and displaying live video."""

from __future__ import annotations

import cv2


def run_webcam_preview(camera_index: int = 0) -> None:
    """Open the webcam and display frames until the user presses q.

    Args:
        camera_index: The camera number OpenCV should open.
            Most laptops use camera index 0 for the built-in webcam.
    """
    camera = cv2.VideoCapture(camera_index)

    if not camera.isOpened():
        raise RuntimeError(
            "Could not open webcam. Check that your camera is connected "
            "and not being used by another app."
        )

    window_name = "Sign Language Translator - Webcam Preview"

    try:
        while True:
            success, frame = camera.read()

            if not success:
                raise RuntimeError("Could not read a frame from the webcam.")

            cv2.imshow(window_name, frame)

            # waitKey checks for keyboard input.
            # The bitmask keeps behavior consistent across platforms.
            key = cv2.waitKey(1) & 0xFF
            if key == ord("q"):
                break
    finally:
        camera.release()
        cv2.destroyAllWindows()

