import os
import time
import logging
from pathlib import Path
from shutil import copyfile, move

detect_dir = Path("/detect")
old_det_dir = detect_dir / "old"

def configure_logging():
    
    # Create a logger
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)

    # Create a formatter
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    # Create a file handler
    file_handler = logging.FileHandler('app.log')
    file_handler.setLevel(logging.INFO)
    file_handler.setFormatter(formatter)

    # Create a console handler
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.DEBUG)
    console_handler.setFormatter(formatter)

    # Add the handlers to the logger
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)

def get_latest_detection_name(detect_dir=detect_dir,old_det_dir=old_det_dir):
    
    latest_detection_name = sorted(
        [item
         for item in detect_dir.glob("*")
         if not os.path.samefile(item, old_det_dir)
         and not os.path.commonpath([item, old_det_dir]) == old_det_dir
         ],
        key=lambda x: x.stat().st_mtime,
        reverse=True,
    )[0].name
    
    return latest_detection_name

def main():

    while not [
        item
        for item in detect_dir.glob("*")
        if not os.path.samefile(item, old_det_dir)
        and not os.path.commonpath([item, old_det_dir]) == old_det_dir
    ]:
        
        time.sleep(0.5)

    latest_detection = get_latest_detection_name(detect_dir)
    frames_dir = detect_dir / latest_detection / "frames"
    stream_frames_dir = frames_dir / "frames_stream"
    renamed_frames_dir = frames_dir / "renamed_frames"
    os.makedirs(stream_frames_dir, exist_ok=True)
    os.makedirs(renamed_frames_dir, exist_ok=True)
    logging.warn("dsgoipjaspogjsa")

    # while not os.path.exists(stream_frames_dir):
        
    #     time.sleep(0.5)
        
    # frame_count=0
    
    # while True:
        
    #     try:
        
    #         for filename in sorted([os.path.join(frames_dir, file) for file in os.listdir(frames_dir) if os.path.isfile(os.path.join(frames_dir, file))]):
                
    #             copyfile(frames_dir / filename, stream_frames_dir / f"frame_{frame_count}.png")
    #             move(frames_dir / filename, renamed_frames_dir / filename)
    #             logging.info("movida a foto ",renamed_frames_dir / filename)
    #             frame_count += 1
                
    #         time.sleep(0.5)
        
    #     except:
            
    #         print("no more frames to rename.")
            
    #         break 
                                    
if __name__ == "__main__":
    
    time.sleep(5)
    main()
