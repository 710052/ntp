import ntplib  # Install this library with "pip install ntplib" to get the atomic time from an NTP server 
from time import ctime, sleep  # Import the ctime and sleep functions from the time module to work with the atomic time and sleep the program
import sys  # Import the sys module to exit the program cleanly if needed.

# Import the Waveshare e-Paper library and the PIL library (Python Imaging Library) to work with the e-Paper display 
from waveshare_epd import epd2in7  # Change this to match your specific e-Paper model (e.g., epd2in7, epd7in5, etc.)
from PIL import Image, ImageDraw, ImageFont  # Import the Image, ImageDraw, and ImageFont classes from the Python Imaging Library (PIL) to work with images and text on the e-Paper display.

def get_atomic_time(): # Define a function to get the atomic time from an NTP server
    """Function to get the atomic time from an NTP server""" # Docstring for the function to get the atomic time from an NTP server.
    try: # Try to get the atomic time from an NTP server, catch exceptions if they occur
        ntp_client = ntplib.NTPClient() # Create a new NTPClient object to request the atomic time from an NTP server 
        response = ntp_client.request('pool.ntp.org', version=3) # Get the atomic time from an NTP server (e.g., pool.ntp.org) using NTP version 3
        atomic_time = ctime(response.tx_time) # Convert the NTP timestamp to a human-readable date and time string using ctime and the response.tx_time attribute 
    except Exception as e: # Catch any exceptions that occur when trying to get the atomic time.
        atomic_time = f"Could not get atomic time: {e}" # Display an error message if the atomic time cannot be retrieved
    return atomic_time # Return the atomic time as a string (or an error message)

def main(): # Define the main function to run the program
    """Main function to display the atomic time on an e-Paper display using the Waveshare e-Paper library and the PIL library."""
    epd = epd2in7.EPD()  # Initialize your specific e-Paper display model here (e.g., epd2in7.EPD(), epd7in5.EPD(), etc.)
    try: # Try to run the main code, catch exceptions and exit cleanly if needed.
        epd.init()  # Initialize the display (turn it on and clear the buffer).
        font = ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf', 24)  # Load a font for the text (change the path to the font file as needed) 
        while True: # Run an infinite loop to continuously update the display with the atomic time 
            atomic_time = get_atomic_time()  # Get the atomic time from an NTP server (e.g., pool.ntp.org)
            epd.clear(0xFF)  # Clear the display to white (0xFF is white, 0x00 is black)

            # Create an image to display the atomic time on the e-Paper display (black text on a white background)
            image = Image.new('1', (epd.height, epd.width), 255)  # 1: black and white mode (1-bit per pixel), (width, height), white background (255)
            draw = ImageDraw.Draw(image) # Create an ImageDraw object to draw on the image.
            draw.text((10, 10), atomic_time, font=font, fill=0)  # Draw the atomic time text on the image at position (10, 10) in black (0) colour using the font .ttf file loaded above.

            epd.display(epd.getbuffer(image))  # Display the image on the e-Paper display (send the image buffer to the display)
            sleep(60)  # Update every minute (60 seconds) to avoid excessive requests to the NTP server
    except KeyboardInterrupt: # Catch a Ctrl+C keyboard interrupt and exit the program cleanly 
        epd.sleep()  # Put the e-Paper display to sleep if Ctrl+C is pressed 
        sys.exit("Program exited cleanly") # Exit the program cleanly if Ctrl+C is pressed 
    except Exception as e: # Catch any exceptions that occur during execution of the main function 
        epd.sleep()  # Put the e-Paper display to sleep if an exception occurs 
        sys.exit(f"An error occurred: {e}") # Exit the program with an error message if an exception occurs 

if __name__ == "__main__": # If the script is run directly (not imported as a module)
    main() # Run the main function to display the atomic time on the e-Paper display
    
    # Note: The main function will run an infinite loop to continuously update the display with the atomic time. Press Ctrl+C to exit the program.
