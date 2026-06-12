"""Project entry point for the sign language translator."""

import argparse

from src.camera.webcam import run_webcam_preview


def parse_args() -> argparse.Namespace:
    """Parse command-line options for the application."""
    parser = argparse.ArgumentParser(
        description="Run the sign language translator webcam preview."
    )
    parser.add_argument(
        "--camera-index",
        type=int,
        default=0,
        help="Camera index to open. Try 1 for an external Logitech webcam.",
    )
    return parser.parse_args()


def main() -> None:
    """Run the current application phase."""
    args = parse_args()
    run_webcam_preview(camera_index=args.camera_index)


if __name__ == "__main__":
    main()
