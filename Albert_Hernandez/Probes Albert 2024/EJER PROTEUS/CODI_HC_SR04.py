import RPi.GPIO as GPIO
import time

# Set GPIO mode to BCM
GPIO.setmode(GPIO.BCM)

# Define GPIO pins for the sensor
TRIG_PIN = 23  # GPIO23 (change as needed)
ECHO_PIN = 24  # GPIO24 (change as needed)

# Set up the GPIO pins
GPIO.setup(TRIG_PIN, GPIO.OUT)
GPIO.setup(ECHO_PIN, GPIO.IN)

# Function to measure distance
def measure_distance():
    # Ensure the trigger pin is low
    GPIO.output(TRIG_PIN, False)
    time.sleep(0.1)  # Wait for sensor to settle

    # Generate a short trigger pulse
    GPIO.output(TRIG_PIN, True)
    time.sleep(0.00001)
    GPIO.output(TRIG_PIN, False)

    # Wait for the echo to start
    while GPIO.input(ECHO_PIN) == 0:
        pulse_start = time.time()

    # Wait for the echo to end
    while GPIO.input(ECHO_PIN) == 1:
        pulse_end = time.time()

    # Calculate the duration of the echo pulse
    pulse_duration = pulse_end - pulse_start

    # Calculate distance in centimeters
    distance = (pulse_duration * 34300) / 2

    return distance

try:
    while True:
        dist = measure_distance()
        print(f"Distance: {dist:.2f} cm")
        time.sleep(1)  # Wait for a moment before the next measurement

except KeyboardInterrupt:
    # Clean up GPIO on Ctrl+C
    GPIO.cleanup()

finally:
    # Clean up GPIO on script exit
    GPIO.cleanup()