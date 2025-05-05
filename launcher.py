#!/usr/bin/env python3
"""
SporeSight Application Launcher
This script handles Docker setup and launches the main application.
"""

import os
import sys
import subprocess
import time
import platform
import argparse
import webbrowser
import shutil
from pathlib import Path

# Docker container settings
CONTAINER_NAME = "sporesight_triton"
MODEL_REPO_PATH = "./model_repository"  # Path to your models directory
TRITON_PORTS = [8000, 8001, 8002]  # HTTP, GRPC, and Metrics ports

def get_application_path():
    """Get the base path of the application, works for both script and executable"""
    if getattr(sys, 'frozen', False):
        # If the application is run as a bundle (PyInstaller)
        return Path(sys.executable).parent
    else:
        # If the application is run as a script
        return Path(__file__).parent

def check_model_repository():
    """Check if model repository exists and has required files"""
    app_path = get_application_path()
    model_path = (app_path / MODEL_REPO_PATH).resolve()
    
    if not model_path.exists():
        print(f"Creating model repository at {model_path}")
        model_path.mkdir(parents=True, exist_ok=True)
    
    # Check if the YOLOv5 model directory exists with required files
    yolo_dir = model_path / "yolov5" / "1"
    if not yolo_dir.exists():
        yolo_dir.mkdir(parents=True, exist_ok=True)
        
    # Check if model.onnx exists
    model_file = yolo_dir / "model.onnx"
    if not model_file.exists():
        print("\nWARNING: YOLOv5 model not found!")
        print("Please download the model from https://drive.google.com/file/d/1sQwGXEBRTgwTPM9AR27Exm4nQ-WUKxmy/view?usp=drive_link")
        print(f"and place it in {yolo_dir} directory as 'model.onnx'\n")
        
        if input("Would you like to open the download link? (y/n): ").lower().startswith("y"):
            webbrowser.open("https://drive.google.com/file/d/1sQwGXEBRTgwTPM9AR27Exm4nQ-WUKxmy/view?usp=drive_link")
            
        input("Press Enter to continue after downloading the model...")
    
    return model_path

def is_docker_installed():
    """Check if Docker is installed and available"""
    try:
        subprocess.run(["docker", "--version"], 
                      check=True, 
                      stdout=subprocess.PIPE, 
                      stderr=subprocess.PIPE)
        return True
    except (subprocess.SubprocessError, FileNotFoundError):
        return False

def is_container_running():
    """Check if our Triton container is already running"""
    try:
        result = subprocess.run(
            ["docker", "ps", "-q", "-f", f"name={CONTAINER_NAME}"],
            check=True,
            capture_output=True,
            text=True
        )
        return bool(result.stdout.strip())
    except subprocess.SubprocessError:
        return False

def is_container_exists():
    """Check if our Triton container exists (running or stopped)"""
    try:
        result = subprocess.run(
            ["docker", "ps", "-a", "-q", "-f", f"name={CONTAINER_NAME}"],
            check=True,
            capture_output=True,
            text=True
        )
        return bool(result.stdout.strip())
    except subprocess.SubprocessError:
        return False

def stop_and_remove_container():
    """Stop and remove the container if it exists"""
    try:
        print(f"Stopping and removing existing container {CONTAINER_NAME}...")
        # Stop the container if it's running
        if is_container_running():
            subprocess.run(["docker", "stop", CONTAINER_NAME], check=True)
        
        # Remove the container
        if is_container_exists():
            subprocess.run(["docker", "rm", CONTAINER_NAME], check=True)
        
        return True
    except subprocess.SubprocessError as e:
        print(f"Error removing container: {e}")
        return False

def start_triton_container():
    """Start the Triton server container"""
    # Check and setup model repository
    model_path = check_model_repository()
    
    # Use official NVIDIA Triton image directly instead of building
    triton_image = "nvcr.io/nvidia/tritonserver:25.02-py3"
    print(f"Using pre-built Triton server image: {triton_image}")
    
    # Stop and remove the container if it already exists
    stop_and_remove_container()
    
    # Start the container
    print(f"Starting Triton server on ports {TRITON_PORTS}...")
    
    # Adjust volume mount for Windows paths if needed
    model_path_str = str(model_path)
    if platform.system() == "Windows":
        model_path_str = model_path_str.replace("\\", "/")
        if ":" in model_path_str:  # Handle Windows drive letter
            drive, path = model_path_str.split(":", 1)
            model_path_str = f"/{drive.lower()}{path}"
    
    # Construct the port mapping arguments
    port_args = []
    for port in TRITON_PORTS:
        port_args.extend(["-p", f"{port}:{port}"])
    
    cmd = [
        "docker", "run", "--rm",
        "--name", CONTAINER_NAME,
    ] + port_args + [
        "-v", f"{model_path_str}:/models",
        triton_image,
        "tritonserver", 
        "--model-repository=/models",
        "--log-verbose=1"
    ]
    
    print(f"Running command: {' '.join(cmd)}")
    
    # Use Popen to run in background instead of run to avoid blocking
    subprocess.Popen(cmd)
    
    # Wait for server to be ready
    print("Waiting for Triton server to initialize...")
    time.sleep(5)  # Give the server some time to start

def launch_main_application():
    """Launch the main SporeSight application"""
    app_path = get_application_path()
    main_path = app_path / "main.exe"
    if not main_path.exists():
        main_path = app_path / "main"
        if not main_path.exists():
            main_path = app_path / "main.py"
    
    if not main_path.exists():
        print("ERROR: Cannot find main application executable.")
        return False
    
    print("Launching SporeSight application...")
    if main_path.suffix == ".py":
        # Run with Python if it's a .py file
        subprocess.Popen([sys.executable, main_path, "--url", "localhost:8001"])
    else:
        # Run directly if it's an executable
        subprocess.Popen([main_path, "--url", "localhost:8001"])
    
    return True

def show_docker_instructions():
    """Show instructions for installing Docker"""
    print("\n===== Docker Installation Required =====")
    print("SporeSight requires Docker to run the backend server.")
    print("\nInstallation links:")
    print("- Windows: https://docs.docker.com/desktop/install/windows-install/")
    print("- macOS: https://docs.docker.com/desktop/install/mac-install/")
    print("- Linux: https://docs.docker.com/engine/install/")
    print("\nAfter installing Docker, please restart this launcher.")
    
    # Offer to open the installation page
    if input("\nWould you like to open the Docker installation page? (y/n): ").lower().startswith("y"):
        system = platform.system()
        if system == "Windows":
            webbrowser.open("https://docs.docker.com/desktop/install/windows-install/")
        elif system == "Darwin":  # macOS
            webbrowser.open("https://docs.docker.com/desktop/install/mac-install/")
        else:  # Linux
            webbrowser.open("https://docs.docker.com/engine/install/")
    
    input("\nPress Enter to exit...")

def main():
    """Main launcher function"""
    parser = argparse.ArgumentParser(description="SporeSight Application Launcher")
    parser.add_argument("--no-docker", action="store_true", 
                       help="Skip Docker setup and launch the application directly")
    parser.add_argument("--url", type=str, default="localhost:8001",
                       help="Inference server URL (only used with --no-docker)")
    parser.add_argument("--restart", action="store_true",
                       help="Force restart the Docker container even if it's already running")
    args = parser.parse_args()
    
    if args.no_docker:
        # Skip Docker setup and launch the app directly
        launch_main_application()
        return
    
    print("=== SporeSight Application Launcher ===")
    
    # Check if Docker is installed
    if not is_docker_installed():
        print("Docker is not installed or not available.")
        show_docker_instructions()
        return
    
    # Check if container is already running and restart option
    container_running = is_container_running()
    if args.restart and container_running:
        print("Restarting the Triton server container...")
        stop_and_remove_container()
        container_running = False
    
    if not container_running:
        try:
            start_triton_container()
        except subprocess.SubprocessError as e:
            print(f"ERROR: Failed to start Triton server container: {e}")
            print("Check that Docker is running and you have appropriate permissions.")
            input("Press Enter to exit...")
            return
    else:
        print("Triton server is already running.")
    
    # Launch the main application
    if not launch_main_application():
        input("Press Enter to exit...")

if __name__ == "__main__":
    main()