import matplotlib.pyplot as plt
import numpy as np
import sys
import os
import subprocess

try:
    from moviepy.editor import VideoClip
    print("Successfully imported VideoClip from moviepy.editor!")
    
    # Custom mplfig_to_npimage function to handle newer matplotlib versions
    def mplfig_to_npimage(fig):
        """Convert a Matplotlib figure to a RGB frame."""
        # Draw the figure first to ensure it's rendered
        fig.canvas.draw()
        
        # Get the RGBA buffer from the figure
        w, h = fig.canvas.get_width_height()
        buf = np.frombuffer(fig.canvas.buffer_rgba(), np.uint8).reshape((h, w, 4))
        
        # Convert RGBA to RGB
        return buf[:,:,:3]
        
    print("Created custom mplfig_to_npimage function for matplotlib compatibility!")
except ImportError as e:
    print(f"Specific import error: {e}")
    print("Error: MoviePy import failed. Please check the MoviePy installation.")
    sys.exit(1)

# Function to check FFmpeg availability
def check_ffmpeg():
    """
    Check if FFmpeg is available in the system path.
    Returns True if FFmpeg is available, False otherwise.
    """
    try:
        # Run FFmpeg version command and capture output
        result = subprocess.run(['ffmpeg', '-version'], 
                              stdout=subprocess.PIPE, 
                              stderr=subprocess.PIPE,
                              text=True)
        return result.returncode == 0
    except FileNotFoundError:
        # FFmpeg executable not found in PATH
        return False

# Function to generate animation
def create_sine_wave_animation(output_filename="sine_wave_animation.mp4", duration=10, fps=20):
    """
    Create an animated sine wave and save it as an MP4 file.
    
    Args:
        output_filename (str): Path to save the output MP4 file
        duration (float): Duration of the animation in seconds
        fps (int): Frames per second for the output video
        
    Returns:
        bool: True if successful, False otherwise
    """
    try:
        # Check if FFmpeg is available
        if not check_ffmpeg():
            print("Error: FFmpeg is not found in your system PATH.")
            print("Please install FFmpeg and make sure it's in your PATH.")
            return False
            
        # Check if output directory exists, create if necessary
        output_dir = os.path.dirname(output_filename)
        if output_dir and not os.path.exists(output_dir):
            os.makedirs(output_dir)
            
        # Generate data points for the sine wave
        x = np.linspace(0, 2*np.pi, 100)  # Create 100 points from 0 to 2π
        y = np.sin(x)  # Calculate initial sine values
        
        # Create and set up the matplotlib figure and axis
        fig, ax = plt.subplots(figsize=(8, 4))  # Set a reasonable figure size
        ax.set_xlim(0, 2*np.pi)  # Set x-axis limits
        ax.set_ylim(-1.5, 1.5)   # Set y-axis limits with some padding
        ax.grid(True)  # Add grid for better visibility
        ax.set_title("Animated Sine Wave")  # Add a title
        ax.set_xlabel("x")  # Label x-axis
        ax.set_ylabel("sin(x)")  # Label y-axis
        
        # Create the initial line plot with enhanced styling
        line, = ax.plot(x, y, 'r-', linewidth=3)  # Thicker line for better visibility
        
        # Frame generation function - called by MoviePy for each frame
        def make_frame(t):
            # Update the y-data with a shifted sine wave based on time
            phase_shift = 2*np.pi*t/duration  # Calculate phase shift based on time
            line.set_ydata(np.sin(x + phase_shift))  # Update the line with new y values
            
            # Add a time indicator for reference
            ax.set_title(f"Animated Sine Wave - Time: {t:.1f}s")
            
            return mplfig_to_npimage(fig)  # Convert matplotlib figure to image array
        
        # Create video clip object
        print("Creating animation...")
        animation = VideoClip(make_frame, duration=duration)
        
        # Write to file with error handling for file operations
        try:
            print(f"Rendering and saving to {output_filename}...")
            # Explicitly specify codec and bitrate for better quality control
            animation.write_videofile(
                output_filename, 
                fps=fps,
                codec='libx264',  # Specify H.264 codec
                bitrate='5000k',  # Set a good quality bitrate
                logger=None  # Reduce console output verbosity
            )
            print(f"Animation saved successfully to {output_filename}")
        except Exception as e:
            # Handle MoviePy-specific exceptions during rendering
            if "FFMPEG encountered the following error" in str(e):
                print("FFmpeg error during encoding. Check if FFmpeg installation is correct.")
                print(f"Error details: {e}")
            elif "Permission denied" in str(e):
                print(f"Permission error when writing to {output_filename}.")
                print("Try running with administrator privileges or choose a different output location.")
            else:
                print(f"Error saving file: {e}")
            return False
        
        # Clean up matplotlib resources
        plt.close(fig)
        return True
        
    except KeyboardInterrupt:
        print("\nProcess interrupted by user.")
        return False
    except Exception as e:
        # Catch any other unexpected errors
        print(f"An unexpected error occurred: {e}")
        import traceback
        traceback.print_exc()  # Print the full traceback for better debugging
        return False

# Main execution block with error handling
if __name__ == "__main__":
    try:
        # Call the animation function with default parameters
        output_file = "sine_wave_animation.mp4"
        
        print(f"Starting sine wave animation creation...")
        success = create_sine_wave_animation(output_file)
        
        if success:
            print(f"Animation completed successfully.")
            print(f"Output saved to: {os.path.abspath(output_file)}")
        else:
            print("Animation creation failed.")
            sys.exit(1)
            
    except KeyboardInterrupt:
        print("\nProcess interrupted by user.")
        sys.exit(0)
    except Exception as e:
        print(f"Unhandled exception: {e}")
        sys.exit(1)