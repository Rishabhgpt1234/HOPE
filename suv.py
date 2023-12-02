import time
import picamera

def capture_images(output_directory, num_images, interval):
    with picamera.PiCamera() as camera:
        camera.resolution = (1024, 768)  # Set the resolution as needed
        
        for i in range(num_images):
            timestamp = time.strftime("%Y%m%d%H%M%S")
            filename = f"{output_directory}/image_{timestamp}.jpg"
            camera.capture(filename)
            print(f"Image captured: {filename}")
            time.sleep(interval)

if __name__ == "__main__":
    output_directory = "path/to/save/images"
    num_images = 10  # Number of images to capture
    capture_interval = 10  # Interval between captures in seconds

    capture_images(output_directory, num_images, capture_interval)
